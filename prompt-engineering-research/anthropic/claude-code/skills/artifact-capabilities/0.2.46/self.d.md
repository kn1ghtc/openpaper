# Self.D

> **来源仓库**: `asgeirtj/system_prompts_leaks`  
> **原始路径**: `Anthropic/claude-code/skills/artifact-capabilities/0.2.46/self.d.ts`  
> **上游 commit**: `4eb4701ae5bb21fddb3c0cb865e100eb52e2b96d`  
> **抓取日期**: 2026-09-17  
> **许可证**: CC0-1.0 (Public Domain)  
> **原始仓库地址**: <https://github.com/asgeirtj/system_prompts_leaks>

---

/**
 * `self` is the FORMER NAME of the `artifact` capability — renamed at
 * 0.2.0; this roster entry remains so the name published pages and
 * shipped clients know keeps resolving. Both spellings resolve
 * permanently: `claude.use("self")` and `claude.use("artifact")`
 * answer the same capability on every page that serves it (older pages
 * may also carry a `window.claude.self` member; this contract promises
 * none). New pages declare `capabilities: {artifact: {}}` and call
 * `claude.use("artifact")`; see artifact's type definitions for the
 * full surface.
 */

interface ClaudeCapabilityMap {
  self: typeof Claude.artifact;
}
