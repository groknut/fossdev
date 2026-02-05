
from pathlib import Path

src_path = Path(__file__).parent / "src"

if not src_path.exists():
    src_path.mkdir()

print(src_path)
