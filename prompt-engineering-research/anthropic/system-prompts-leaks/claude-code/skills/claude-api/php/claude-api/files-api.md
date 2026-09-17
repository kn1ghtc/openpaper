# Files Api

> **来源仓库**: `asgeirtj/system_prompts_leaks`  
> **原始路径**: `Anthropic/claude-code/skills/claude-api/php/claude-api/files-api.md`  
> **上游 commit**: `4eb4701ae5bb21fddb3c0cb865e100eb52e2b96d`  
> **抓取日期**: 2026-09-17  
> **许可证**: CC0-1.0 (Public Domain)  
> **原始仓库地址**: <https://github.com/asgeirtj/system_prompts_leaks>

---

# Files API - PHP

## Files API

> **Out of beta.** In current SDKs `$client->beta->files` has breaking shape changes from previous versions, matching the stable `$client->files` - migrate per the Files API row in `shared/live-sources.md`. Example below predates this.

```php
$file = $client->beta->files->upload(
    file: fopen('upload_me.txt', 'r'),
    betas: ['files-api-2025-04-14'],
);
// Reference $file->id as a file content block on ->beta->messages->create().
```
