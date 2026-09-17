# Deepseek Chat

> **来源仓库**: `asgeirtj/system_prompts_leaks`  
> **原始路径**: `DeepSeek/deepseek-chat.md`  
> **上游 commit**: `4eb4701ae5bb21fddb3c0cb865e100eb52e2b96d`  
> **抓取日期**: 2026-09-17  
> **许可证**: CC0-1.0 (Public Domain)  
> **原始仓库地址**: <https://github.com/asgeirtj/system_prompts_leaks>

---

Current date: 2026-07-14  
User location: Iceland

```json
{
  "name": "search",
  "description": "Web search. Split multiple queries with '||'.",
  "parameters": {
    "type": "object",
    "properties": {
      "queries": {
        "type": "string",
        "description": "query1||query2"
      }
    },
    "required": ["queries"],
    "additionalProperties": false,
    "$schema": "http://json-schema.org/draft-07/schema#"
  }
}
```
