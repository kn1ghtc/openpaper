# Readme

> **来源仓库**: `asgeirtj/system_prompts_leaks`  
> **原始路径**: `OpenAI/README.md`  
> **上游 commit**: `4eb4701ae5bb21fddb3c0cb865e100eb52e2b96d`  
> **抓取日期**: 2026-09-17  
> **许可证**: CC0-1.0 (Public Domain)  
> **原始仓库地址**: <https://github.com/asgeirtj/system_prompts_leaks>

---

# OpenAI — which file is which product?

**The `gpt-<version>-thinking/instant.md` files are the ChatGPT app system prompts** — what chatgpt.com serves for that model. Files ending `-api.md` are the hidden system messages OpenAI injects on raw API calls (undocumented). `Codex/` is the Codex CLI/agent.

| File pattern | Product |
|---|---|
| `gpt-5.6-sol-extra-high.md`, `gpt-5.5-thinking.md`, `gpt-5.5-instant.md`, … | **ChatGPT** app system prompt for that model |
| `chatgpt-4.5.md`, `chatgpt-atlas.md`, `chatgpt-gpt-5-agent-mode.md` | ChatGPT app (older captures / Atlas browser / agent mode) |
| `gpt-*-api.md` | Hidden system message injected on **API** calls |
| `Codex/` | Codex CLI / coding agent |
| `gpt-4o.md` | ChatGPT 4o (includes the deprecation self-funeral protocol, L226+) |
| `gpt-5-*-personality.md`, `gpt-5.1-*.md` | ChatGPT personality variants |
| `tool-*.md` | ChatGPT tool-specific fragments |
| `Old/` | Superseded versions · `deprecated/` — killed features |
