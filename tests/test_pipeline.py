import unittest
from src.pipeline import create_manifest

class PipelineTests(unittest.TestCase):
    def test_draft_is_not_approved_or_published(self):
        data = create_manifest("A robot learns sarcasm")
        self.assertEqual(data["status"], "draft")
        self.assertFalse(data["approval"]["approved"])
        self.assertIsNone(data["rendered_video_path"])
        self.assertEqual(set(data["publishing"].values()), {"not_configured"})

    def test_blank_idea_rejected(self):
        with self.assertRaises(ValueError):
            create_manifest("  ")
