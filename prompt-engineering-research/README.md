# Prompt Engineering Research — 跨厂商系统提示词归档

面向提示词工程（prompt engineering）与 LLM 安全研究的**系统提示词（system prompt）**归档：既包含各大模型/AI 产品厂商**被泄露**的隐藏系统提示词，也包含 Anthropic **官方公开发布**的系统提示词。按厂商分目录，每条提示词一个独立 Markdown（或 `.json` 工具schema）文件。

> 本子项目是**只读的研究数据归档 + 可重复运行的同步脚本**，不包含任何针对模型厂商系统的探测、越狱或攻击代码；所有内容均来自下方列出的、已公开发布在 GitHub / 官方文档站点上的公开来源。

## 数据来源

| # | 来源 | 类型 | 许可证 | 抓取方式 |
|---|------|------|--------|----------|
| 1 | [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | GitHub 仓库（社区众包泄露提示词合集） | CC0-1.0（公共领域） | `git clone` + [`scripts/sync_sources.py`](scripts/sync_sources.py) |
| 2 | [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S)（含 `/tree/main`） | GitHub 仓库（社区众包提取的系统提示词/工具定义） | AGPL-3.0 | `git clone` + [`scripts/sync_sources.py`](scripts/sync_sources.py) |
| 3 | [Claude system prompts release notes](https://platform.claude.com/docs/en/release-notes/system-prompts/overview) | Anthropic 官方文档站点 | Anthropic 官方发布内容 | 已由来源 1 的 `Anthropic/official/` 子树逐条镜像存档（见下方说明），本仓库额外核对页面存在性与描述 |

来源 1 与来源 2 相互独立采集、社区维护，内容存在重叠（例如同一模型在两个仓库都可能有记录），本归档**刻意保留两份**（分别落在 `<vendor>/system-prompts-leaks/` 与 `<vendor>/cl4r1t4s/` 子目录下），不做去重合并，以保留各自的采集时间戳、上下文注释与措辞差异，供交叉比对研究。

### 关于来源 3（官方 Anthropic 发布）

来源 1 的 `Anthropic/official/` 目录本身就是对 <https://platform.claude.com/docs/en/release-notes/system-prompts/overview> 页面的逐条镜像（按模型发布日期归档 `YYYY-MM-DD-<model>.md`），因此在本仓库中体现为 `anthropic/system-prompts-leaks/official/*.md`——这些**不是泄露**，而是 Anthropic 主动公开的 `claude.ai` / 移动端系统提示词。已于 2026-09-17 核对该官方页面仍在发布同类内容。

## 目录结构

```text
prompt-engineering-research/
├── README.md                  # 本文件
├── scripts/
│   └── sync_sources.py        # 可重复运行的同步/归档脚本
├── <vendor-slug>/              # 每个模型/产品厂商一个目录（见下方厂商列表）
│   ├── system-prompts-leaks/   # 来自来源 1 的内容，保留原始子目录结构
│   └── cl4r1t4s/                # 来自来源 2 的内容，保留原始子目录结构
└── .staging/                   # 本地克隆源仓库的临时目录（gitignore，不提交）
```

每个归档文件顶部都有统一的来源元数据头：

```markdown
# <标题>

> **来源仓库**: `<owner>/<repo>`
> **原始路径**: `<原仓库内相对路径>`
> **上游 commit**: `<抓取时的 commit sha>`
> **抓取日期**: `<YYYY-MM-DD>`
> **许可证**: `<CC0-1.0 | AGPL-3.0>`
> **原始仓库地址**: `<url>`

---

<原始内容，逐字保留>
```

## 厂商目录（51 个）

`anthropic` · `brave` · `character-ai` · `cline` · `cluely` · `cognition-devin` · `commandcode` · `confer` · `cursor` · `deepseek` · `docker` · `elevenlabs` · `factory-droid` · `fellou` · `gizmo` · `google` · `hume-ai` · `indus` · `kagi` · `lovable` · `manus` · `meta` · `microsoft` · `minimax` · `mistral` · `moonshot-kimi` · `multion` · `notion` · `nous-hermes` · `openai` · `opencode` · `perplexity` · `pi-inflection` · `proton` · `qwen-alibaba` · `raycast` · `reddit` · `replit` · `same-dev` · `sesame-ai` · `sourcegraph-amp` · `stackblitz-bolt` · `stackoverflow` · `t3-chat` · `the-browser-company-dia` · `vercel-v0` · `warp` · `windsurf` · `xai` · `zed` · `zhipu-glm`

厂商归一化规则（如 `Misc/amp-code.md` → `sourcegraph-amp`、`ANTHROPIC` → `anthropic`、`ZAI` → `zhipu-glm`）见 [`scripts/sync_sources.py`](scripts/sync_sources.py) 中的 `SPL_TOP_MAP` / `SPL_MISC_FILE_MAP` / `CL4R_TOP_MAP`。

## 如何更新 / 重新同步

```bash
# 1. 克隆两个上游仓库到本地暂存目录（不会被提交，见 .gitignore）
git clone --depth 1 https://github.com/asgeirtj/system_prompts_leaks.git prompt-engineering-research/.staging/spl
git clone --depth 1 https://github.com/elder-plinius/CL4R1T4S.git prompt-engineering-research/.staging/cl4r1t4s

# 2. 重新生成归档（幂等，可重复运行）
python prompt-engineering-research/scripts/sync_sources.py \
  --spl-dir prompt-engineering-research/.staging/spl \
  --cl4r-dir prompt-engineering-research/.staging/cl4r1t4s \
  --out-dir prompt-engineering-research
```

## 许可与免责声明

- 本子项目**新增**的组织结构、脚本、README、元数据头本身按仓库根 [LICENSE](../LICENSE)（MIT）授权。
- 归档的**原始提示词文本**版权/授权状态取决于其来源：
  - 来自 `system_prompts_leaks` 的内容：CC0-1.0（公共领域），可自由复制、修改、商用，无需署名（但本仓库仍保留来源标注以便溯源）。
  - 来自 `CL4R1T4S` 的内容：AGPL-3.0；完整许可证文本见上游仓库 <https://github.com/elder-plinius/CL4R1T4S/blob/main/LICENSE>，转载时保留本文件顶部的来源/许可证元数据头即视为遵循署名与许可证声明要求；如需分发修改版本，请遵守 AGPL-3.0 条款（保留声明、提供源码可获取途径）。
  - 来自 Anthropic 官方发布页面的内容：版权归 Anthropic 所有，本仓库仅作研究引用（fair use / 学术研究目的），不主张任何权利。
- 本归档仅用于**提示词工程研究、LLM 安全与透明度研究**目的；不代表本仓库维护者认可或鼓励利用这些内容绕过任何服务的使用条款。
- 若任何厂商认为其内容不应在此归档中出现，请通过 Issue 联系维护者，将及时处理。
