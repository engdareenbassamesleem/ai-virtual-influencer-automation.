"""Safe offline planning pipeline. Does not call APIs or publish."""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


def create_manifest(idea: str) -> dict:
    idea = idea.strip()
    if not idea:
        raise ValueError("An idea is required")
    return {
        "episode_id": str(uuid4()),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "draft",
        "idea": idea,
        "character": "NOVA AI (provisional)",
        "language": "en",
        "format": {"width": 1080, "height": 1920, "target_seconds": 30},
        "script": None,
        "scenes": [],
        "rendered_video_path": None,
        "qa": {"originality_checked": False, "rights_checked": False,
               "audio_checked": False, "captions_checked": False,
               "ai_disclosure_checked": False},
        "approval": {"approved": False, "approved_by": None},
        "publishing": {"youtube": "not_configured", "instagram": "not_configured",
                       "tiktok": "not_configured"},
    }


def main():
    parser = argparse.ArgumentParser(description="Generate an episode planning manifest (dry-run)")
    parser.add_argument("--idea", required=True)
    parser.add_argument("--output", default="output/episode.json")
    args = parser.parse_args()
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(create_manifest(args.idea), indent=2), encoding="utf-8")
    print(f"Dry-run manifest written: {path}")

if __name__ == "__main__":
    main()
