"""
Extract source code context around a Semgrep finding.
"""

from pathlib import Path

from src.models import CodeContext


def extract_code_context(
    file_path: str,
    start_line: int,
    end_line: int,
    lines_before: int = 3,
    lines_after: int = 3,
) -> CodeContext:
    """
    Extract source code surrounding a vulnerability.

    Returns a CodeContext object containing:
    - code before the finding
    - vulnerable code
    - code after the finding
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"Source file not found: {file_path}")

    with open(path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    start_index = max(0, start_line - lines_before - 1)
    end_index = min(len(lines), end_line + lines_after)

    before = "".join(lines[start_index:start_line - 1])

    target = "".join(lines[start_line - 1:end_line])

    after = "".join(lines[end_line:end_index])

    return CodeContext(
        before=before,
        target=target,
        after=after,
    )
