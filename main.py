
from pathlib import Path

src_path = Path(__file__).parent / "src"

src_path.mkdir(exist_ok=True)
print(src_path)
