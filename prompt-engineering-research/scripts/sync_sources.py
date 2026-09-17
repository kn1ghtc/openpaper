#!/usr/bin/env python3
"""Sync leaked/official system-prompt sources into vendor-organized Markdown.

Reproduces the `prompt-engineering-research/<vendor>/...` tree from two
upstream public repositories:

  - asgeirtj/system_prompts_leaks  (CC0-1.0, public domain)
  - elder-plinius/CL4R1T4S          (AGPL-3.0)

Usage (from repo root, after cloning both sources into a staging dir):

    py -3.12 prompt-engineering-research/scripts/sync_sources.py \
        --spl-dir prompt-engineering-research/.staging/spl \
        --cl4r-dir prompt-engineering-research/.staging/cl4r1t4s \
        --out-dir prompt-engineering-research

This script only reorganizes/annotates already-public text content; it does
not scrape or reverse-engineer anything itself. See README.md for policy.
"""
from __future__ import annotations

import argparse
import datetime
import subprocess
from pathlib import Path

TODAY = datetime.date.today().isoformat()

# --- Vendor normalization -------------------------------------------------

SPL_TOP_MAP = {
    "Anthropic": "anthropic",
    "Cursor": "cursor",
    "DeepSeek": "deepseek",
    "GLM": "zhipu-glm",
    "Google": "google",
    "Kimi": "moonshot-kimi",
    "Meta": "meta",
    "Microsoft": "microsoft",
    "Mistral": "mistral",
    "Notion": "notion",
    "OpenAI": "openai",
    "OpenCode": "opencode",
    "Perplexity": "perplexity",
    "Pi": "pi-inflection",
    "Qwen": "qwen-alibaba",
    "xAI": "xai",
}

# `Misc/<file>` in system_prompts_leaks holds one product per file; map each
# stem (filename without extension) to its own vendor slug.
SPL_MISC_FILE_MAP = {
    "amp-code": "sourcegraph-amp",
    "brave-search": "brave",
    "character-ai": "character-ai",
    "commandcode-cli": "commandcode",
    "confer": "confer",
    "devin-cli": "cognition-devin",
    "docker-gordon-ai": "docker",
    "elevenlabs-voice-agent": "elevenlabs",
    "fellou-browser": "fellou",
    "gizmo-ai": "gizmo",
    "hermes": "nous-hermes",
    "indus-ai": "indus",
    "kagi-assistant": "kagi",
    "minimax-m2.5": "minimax",
    "opencode": "opencode",
    "proton-lumo-ai": "proton",
    "raycast-ai": "raycast",
    "reddit-answers": "reddit",
    "sesame-ai-maya": "sesame-ai",
    "stack-overflow-ai-assist": "stackoverflow",
    "t3-code": "t3-chat",
    "t3.chat": "t3-chat",
    "warp-2.0-agent": "warp",
    "zed": "zed",
}

CL4R_TOP_MAP = {
    "ANTHROPIC": "anthropic",
    "BOLT": "stackblitz-bolt",
    "BRAVE": "brave",
    "CLINE": "cline",
    "CLUELY": "cluely",
    "CURSOR": "cursor",
    "DEVIN": "cognition-devin",
    "DIA": "the-browser-company-dia",
    "FACTORY": "factory-droid",
    "GOOGLE": "google",
    "HUME": "hume-ai",
    "LOVABLE": "lovable",
    "MANUS": "manus",
    "META": "meta",
    "MINIMAX": "minimax",
    "MISTRAL": "mistral",
    "MOONSHOT": "moonshot-kimi",
    "MULTION": "multion",
    "OPENAI": "openai",
    "PERPLEXITY": "perplexity",
    "REPLIT": "replit",
    "SAMEDEV": "same-dev",
    "VERCEL V0": "vercel-v0",
    "WINDSURF": "windsurf",
    "XAI": "xai",
    "ZAI": "zhipu-glm",
}

SPL_TOP_SKIP = {".git", ".gitattributes", ".github", "assets", "LICENSE", "README.md"}
CL4R_TOP_SKIP = {".git", "LICENSE", "README.md"}

BINARY_SKIP_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".xml"}
KEEP_EXT_AS_IS = {".json", ".md"}


def to_md_name(name: str) -> str:
    """Normalize a filename so every archived prompt lands as .md, except
    structured tool schemas (.json) which keep their extension."""
    p = Path(name)
    if p.suffix.lower() == ".json":
        return name
    if p.suffix.lower() == ".md":
        return name
    # .txt, .mkd, or no extension at all -> .md
    return p.stem + ".md" if p.suffix else name + ".md"


def header(title: str, repo: str, repo_url: str, rel_path: str, license_: str, commit: str) -> str:
    return (
        f"# {title}\n\n"
        f"> **来源仓库**: `{repo}`  \n"
        f"> **原始路径**: `{rel_path}`  \n"
        f"> **上游 commit**: `{commit}`  \n"
        f"> **抓取日期**: {TODAY}  \n"
        f"> **许可证**: {license_}  \n"
        f"> **原始仓库地址**: <{repo_url}>\n\n"
        "---\n\n"
    )


def copy_tree(src_root: Path, vendor_root: Path, tag: str, repo: str, repo_url: str,
              license_: str, commit: str, top_map: dict[str, str], top_skip: set[str],
              misc_file_map: dict[str, str] | None = None) -> int:
    count = 0
    for top in sorted(src_root.iterdir()):
        name = top.name
        if name in top_skip:
            continue
        is_misc_special = misc_file_map is not None and name == "Misc"
        if name not in top_map and not is_misc_special:
            print(f"  [skip: unmapped top-level entry] {name}")
            continue
        vendor = top_map.get(name, "")
        if not top.is_dir():
            continue
        for f in sorted(top.rglob("*")):
            if f.is_dir():
                continue
            if f.suffix.lower() in BINARY_SKIP_EXT:
                continue
            rel = f.relative_to(src_root)
            stem = f.stem
            # Misc/<file> per-file vendor override (system_prompts_leaks only)
            if is_misc_special:
                if stem not in misc_file_map:
                    print(f"  [skip: unmapped Misc file] {rel}")
                    continue
                vendor_for_file = misc_file_map[stem]
                out_rel = Path(f.name)
            else:
                vendor_for_file = vendor
                out_rel = f.relative_to(top)
            out_name = to_md_name(out_rel.name)
            out_path = vendor_root / vendor_for_file / tag / out_rel.parent / out_name
            out_path.parent.mkdir(parents=True, exist_ok=True)

            text = f.read_text(encoding="utf-8", errors="replace")
            if out_path.suffix.lower() == ".json":
                out_path.write_text(text, encoding="utf-8")
            else:
                title = f.stem.replace("-", " ").replace("_", " ").title()
                out_path.write_text(
                    header(title, repo, repo_url, str(rel).replace("\\", "/"), license_, commit) + text,
                    encoding="utf-8",
                )
            count += 1
    return count


def git_head(repo_dir: Path) -> str:
    try:
        return subprocess.check_output(["git", "-C", str(repo_dir), "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--spl-dir", required=True)
    ap.add_argument("--cl4r-dir", required=True)
    ap.add_argument("--out-dir", required=True)
    args = ap.parse_args()

    spl_dir = Path(args.spl_dir)
    cl4r_dir = Path(args.cl4r_dir)
    out_dir = Path(args.out_dir)

    spl_commit = git_head(spl_dir)
    cl4r_commit = git_head(cl4r_dir)

    n1 = copy_tree(
        spl_dir, out_dir, tag="system-prompts-leaks",
        repo="asgeirtj/system_prompts_leaks",
        repo_url="https://github.com/asgeirtj/system_prompts_leaks",
        license_="CC0-1.0 (Public Domain)",
        commit=spl_commit,
        top_map=SPL_TOP_MAP, top_skip=SPL_TOP_SKIP,
        misc_file_map=SPL_MISC_FILE_MAP,
    )
    print(f"system_prompts_leaks: wrote {n1} files (commit {spl_commit[:12]})")

    n2 = copy_tree(
        cl4r_dir, out_dir, tag="cl4r1t4s",
        repo="elder-plinius/CL4R1T4S",
        repo_url="https://github.com/elder-plinius/CL4R1T4S",
        license_="AGPL-3.0",
        commit=cl4r_commit,
        top_map=CL4R_TOP_MAP, top_skip=CL4R_TOP_SKIP,
    )
    print(f"CL4R1T4S: wrote {n2} files (commit {cl4r_commit[:12]})")

    print(f"Total: {n1 + n2} files across "
          f"{len(set(SPL_TOP_MAP.values()) | set(SPL_MISC_FILE_MAP.values()) | set(CL4R_TOP_MAP.values()))} vendor dirs")


if __name__ == "__main__":
    main()
