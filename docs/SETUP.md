# Setup

## Local quick start
1. Clone the repository or download the starter ZIP.
2. Install Python 3.11+.
3. Run `python -m unittest discover -s tests -v` to verify the offline planning logic.
4. Run `python -m src.pipeline --idea "My AI Assistant Took Everything Literally" --output output/episode.json`.
5. Import `workflows/idea-to-manifest.json` into n8n and run the manual trigger.

This starter generates a **planning manifest only**; video creation, live API calls, and public posting are not implemented.

## Milestones
- M1: original script generation and schema validation
- M2: stable character media and voice generation
- M3: video assembly and QA with test fixtures
- M4: OAuth and private/unlisted test uploads
- M5: scheduled cross-posting and monitoring

Never commit credentials, OAuth refresh tokens or private media. Keep dry-run enabled until integrations are reviewed.
