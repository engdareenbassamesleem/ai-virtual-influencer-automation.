# AI Virtual Influencer Automation 🎬

**Status: MVP scaffold / dry-run only. No automatic video generation or public posting is enabled.**

A Python + n8n starter for an original, disclosed virtual influencer publishing English-language comedy Shorts to YouTube, TikTok and Instagram. Inspired by a prior YouTube automation codebase, but intentionally isolated until integrations are reviewed and tested.

## Pipeline
`Ideas → Script → Scene manifest → Video renderer (TODO) → QA → Approval → Platform publishers (TODO) → Analytics`

## Quick start
```bash
python -m src.pipeline --idea "My AI Assistant Took Everything Literally" --output output/episode.json
python -m unittest discover -s tests -v
```
No dependencies are required for the local dry run. It generates a **planning manifest, not a video**.

## n8n
Import `workflows/idea-to-manifest.json` into n8n. It uses a manual trigger and a Code node to demonstrate the content structure. It does **not** call an LLM, generate media or publish.

## Production integrations (not yet implemented)
- Research: vidIQ (approved API / connected app)
- Script: approved LLM provider
- Media: video generation provider, voice provider and FFmpeg assembly
- Storage: local disk or approved object storage
- Distribution: authorized YouTube, Instagram and TikTok publishing APIs
- Observability: structured logs, idempotency keys, retries, per-platform status

Before enabling automated public publishing, verify credentials, rights to generated assets, platform permissions, disclosure requirements, quality gates and budget limits. Never commit API keys or OAuth tokens.

See `docs/ARCHITECTURE.md`, `docs/SETUP.md`, and `docs/CHARACTER_BIBLE.md`.

## Originality
All story scripts and characters must be original; no copying competitor footage or impersonating real people. Disclose synthetic or AI-generated content where required by each platform.

## License
MIT.
