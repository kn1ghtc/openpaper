# Batches

> **来源仓库**: `asgeirtj/system_prompts_leaks`  
> **原始路径**: `Anthropic/claude-code/skills/claude-api/typescript/claude-api/batches.md`  
> **上游 commit**: `4eb4701ae5bb21fddb3c0cb865e100eb52e2b96d`  
> **抓取日期**: 2026-09-17  
> **许可证**: CC0-1.0 (Public Domain)  
> **原始仓库地址**: <https://github.com/asgeirtj/system_prompts_leaks>

---

# Message Batches API - TypeScript

The Batches API (`POST /v1/messages/batches`) processes Messages API requests asynchronously at 50% of standard prices.

## Key Facts

- Up to 100,000 requests or 256 MB per batch
- Most batches complete within 1 hour; maximum 24 hours
- Results available for 29 days after creation
- 50% cost reduction on all token usage
- All Messages API features supported (vision, tools, caching, etc.)

---

## Create a Batch

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

const messageBatch = await client.messages.batches.create({
  requests: [
    {
      custom_id: "request-1",
      params: {
        model: "claude-opus-5",
        max_tokens: 16000,
        messages: [
          { role: "user", content: "Summarize climate change impacts" },
        ],
      },
    },
    {
      custom_id: "request-2",
      params: {
        model: "claude-opus-5",
        max_tokens: 16000,
        messages: [
          { role: "user", content: "Explain quantum computing basics" },
        ],
      },
    },
  ],
});

console.log(`Batch ID: ${messageBatch.id}`);
console.log(`Status: ${messageBatch.processing_status}`);
```

---

## Poll for Completion

```typescript
let batch;
while (true) {
  batch = await client.messages.batches.retrieve(messageBatch.id);
  if (batch.processing_status === "ended") break;
  console.log(
    `Status: ${batch.processing_status}, processing: ${batch.request_counts.processing}`,
  );
  await new Promise((resolve) => setTimeout(resolve, 60_000));
}

console.log("Batch complete!");
console.log(`Succeeded: ${batch.request_counts.succeeded}`);
console.log(`Errored: ${batch.request_counts.errored}`);
```

---

## Retrieve Results

```typescript
for await (const result of await client.messages.batches.results(
  messageBatch.id,
)) {
  switch (result.result.type) {
    case "succeeded":
      console.log(
        `[${result.custom_id}] ${result.result.message.content[0].text.slice(0, 100)}`,
      );
      break;
    case "errored":
      if (result.result.error.type === "invalid_request") {
        console.log(`[${result.custom_id}] Validation error - fix and retry`);
      } else {
        console.log(`[${result.custom_id}] Server error - safe to retry`);
      }
      break;
    case "expired":
      console.log(`[${result.custom_id}] Expired - resubmit`);
      break;
  }
}
```

---

## Cancel a Batch

```typescript
const cancelled = await client.messages.batches.cancel(messageBatch.id);
console.log(`Status: ${cancelled.processing_status}`); // "canceling"
```
