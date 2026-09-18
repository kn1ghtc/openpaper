# Skill

> **来源仓库**: `asgeirtj/system_prompts_leaks`  
> **原始路径**: `Anthropic/claude-design/skills/claude-api-in-prototypes/SKILL.md`  
> **上游 commit**: `4eb4701ae5bb21fddb3c0cb865e100eb52e2b96d`  
> **抓取日期**: 2026-09-17  
> **许可证**: CC0-1.0 (Public Domain)  
> **原始仓库地址**: <https://github.com/asgeirtj/system_prompts_leaks>

---

---
name: claude-api-in-prototypes
description: "Call Claude from your HTML artifacts via window.claude.complete"
user-invocable: true
---

# Claude API in prototypes

Your HTML artifacts can call Claude via a built-in helper. No SDK or API key needed.

```html
<script>
(async () => {
  const text = await window.claude.complete("Summarize this: ...");
  // or with a messages array:
  const text2 = await window.claude.complete({
    messages: [{ role: 'user', content: '...' }],
  });
})();
</script>
```

Calls default to `claude-haiku-4-5` with a 1024-token output cap. The body may also set `model` (haiku/sonnet families only), `max_tokens` (up to 32000), `system`, `tool_choice`, and client `tools` — standard Messages API shapes, except each tool also carries `run: async (input) => string` and the helper executes tool calls in-page and loops (max 8 model calls), resolving with the final text. Handler throws become is_error tool_results. Server tools (web search etc.) are rejected; no streaming; rate-limited 15 calls/minute per user, loop iterations included. Shared artifacts run under the viewer's quota.
