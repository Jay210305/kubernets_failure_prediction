import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import convert_bibliography as converter


class ConvertBibliographyTests(unittest.TestCase):
    def test_converts_nested_pdfs_preserving_tree_and_existing_markdown(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory) / "Bibliografia_Micro"
            nested = root / "subcarpeta"
            nested.mkdir(parents=True)
            first_pdf = root / "paper.pdf"
            second_pdf = nested / "paper.pdf"
            first_pdf.touch()
            second_pdf.touch()
            (root / "paper.md").write_text("nota existente", encoding="utf-8")

            with patch.object(converter.subprocess, "run") as run:
                run.return_value = subprocess.CompletedProcess([], 0)
                result = converter.convert_pdfs(root)

            self.assertEqual(result.converted, 1)
            self.assertEqual(result.skipped, 1)
            self.assertEqual(run.call_count, 1)
            self.assertEqual(run.call_args.args[0], ["markitdown", str(second_pdf), "-o", str(second_pdf.with_suffix(".md"))])
            self.assertEqual((root / "paper.md").read_text(encoding="utf-8"), "nota existente")

    def test_continues_after_cli_failure_and_reports_failed_file(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            root = Path(temporary_directory)
            (root / "a.pdf").touch()
            (root / "b.pdf").touch()

            with patch.object(converter.subprocess, "run", side_effect=[subprocess.CalledProcessError(1, "markitdown"), subprocess.CompletedProcess([], 0)]):
                result = converter.convert_pdfs(root)

            self.assertEqual(result.converted, 1)
            self.assertEqual(result.failed, 1)
            self.assertEqual(result.errors[0][0], root / "a.pdf")


if __name__ == "__main__":
    unittest.main()
