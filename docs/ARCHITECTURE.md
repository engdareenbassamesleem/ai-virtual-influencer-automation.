# Architecture and safety gates

1. Trend scout: collect sourced examples and record timestamp, source URL, and confidence.
2. Creative agent: produce original concept, script, shots, CTA and platform-specific copy.
3. Character engine: enforce a consistent character bible and synthetic-person disclosure.
4. Renderer: generate licensed scenes, voice and captions; assemble 9:16 video.
5. QA: validate duration, audio, subtitles, rights, originality and synthetic-media labels.
6. Approval: explicit owner approval for initial public launch and any changes in posting scope; configure ongoing automation only after successful tests.
7. Publisher: platform OAuth, rate limits, idempotent upload, retry with bounded backoff.
8. Analytics: read impressions, views, retention where permitted; evaluate without promising virality.

## Security
Use environment secrets or a secrets manager; never store access tokens in workflow JSON. Keep budget cap and dry-run default. Stop rather than publish on any failed QA gate.

## Migration from original ZIP
Prior `YoutubeAutomationPorject-main.zip` includes FastAPI backend, platform publishers and scheduler. Review its license, credential handling, dependencies, API compatibility and tests before porting any module. No original code is copied into this public starter.
