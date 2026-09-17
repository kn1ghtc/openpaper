# Files Api

> **来源仓库**: `asgeirtj/system_prompts_leaks`  
> **原始路径**: `Anthropic/claude-code/skills/claude-api/csharp/claude-api/files-api.md`  
> **上游 commit**: `4eb4701ae5bb21fddb3c0cb865e100eb52e2b96d`  
> **抓取日期**: 2026-09-17  
> **许可证**: CC0-1.0 (Public Domain)  
> **原始仓库地址**: <https://github.com/asgeirtj/system_prompts_leaks>

---

# Files API - C#

## Files API

> **Out of beta.** In current SDKs `client.Beta.Files` has breaking shape changes from previous versions, matching the stable `client.Files` - migrate per the Files API row in `shared/live-sources.md`. Examples below predate this.

Files live under `client.Beta.Files` (namespace `Anthropic.Models.Beta.Files`). `BinaryContent` implicit-converts from `Stream` and `byte[]`.

```csharp
using Anthropic.Models.Beta.Files;
using Anthropic.Models.Beta.Messages;

FileMetadata meta = await client.Beta.Files.Upload(
    new FileUploadParams { File = File.OpenRead("doc.pdf") });

// Referencing the uploaded file requires Beta message types:
new BetaRequestDocumentBlock {
    Source = new BetaFileDocumentSource { FileID = meta.ID },
}
```

The non-beta `DocumentBlockParamSource` union has no file-ID variant - file references need `client.Beta.Messages.Create()`.

---

