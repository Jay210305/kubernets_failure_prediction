"""Convert bibliography PDFs to Markdown with the markitdown CLI."""

from __future__ import annotations

import argparse
import shutil
import subprocess
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ConversionResult:
    converted: int = 0
    skipped: int = 0
    failed: int = 0
    errors: list[tuple[Path, str]] = field(default_factory=list)


def convert_pdfs(folder: Path, executable: str = "markitdown") -> ConversionResult:
    """Convert PDFs below *folder*, preserving subfolders and existing Markdown."""
    root = Path(folder)
    result = ConversionResult()
    if not root.is_dir():
        result.failed = 1
        result.errors.append((root, "La carpeta indicada no existe o no es un directorio."))
        return result

    for pdf_path in sorted(root.rglob("*.pdf")):
        markdown_path = pdf_path.with_suffix(".md")
        if markdown_path.exists():
            result.skipped += 1
            print(f"Omitido (ya existe): {markdown_path}")
            continue
        try:
            subprocess.run(
                [executable, str(pdf_path), "-o", str(markdown_path)],
                check=True,
            )
            result.converted += 1
            print(f"Convertido: {pdf_path}")
        except (subprocess.CalledProcessError, OSError) as error:
            result.failed += 1
            result.errors.append((pdf_path, str(error)))
            print(f"Error al convertir {pdf_path}: {error}")

    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "folder",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "Bibliografia_Micro",
        help="Carpeta de bibliografía (por defecto: Bibliografia_Micro del proyecto).",
    )
    args = parser.parse_args()

    executable = shutil.which("markitdown")
    if executable is None:
        parser.error("No se encontró 'markitdown' en PATH. Instala/configura la CLI antes de ejecutar.")

    result = convert_pdfs(args.folder, executable)
    print(
        f"Resumen: {result.converted} convertidos, "
        f"{result.skipped} omitidos, {result.failed} con error."
    )
    return 1 if result.failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
