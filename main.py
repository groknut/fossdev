
# from pathlib import Path
# 
# src_path = Path(__file__).parent / "src"
# 
# src_path.mkdir(exist_ok=True)
# print(src_path)

def sum(a: int, b: int) -> int:
    return a + b

def div(a: int, b: int) -> int:
    if b == 0: raise ValueError("b == 0!")
    if isinstance(a, str) or isinstance(b, str): raise ValueError("wrong type")
    return a / b
