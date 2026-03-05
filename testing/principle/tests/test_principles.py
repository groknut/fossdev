
# костыль (так делать не надо)
# ищет по относительному пути
# запуск возможен только из директории с файлом тестов
# import sys
# sys.path.append('../src')
# from math_demo import add

#TODO make if with pip install -e .

from math_demo import add

def test_addition():
    assert 2 + 2 == 4

if __name__ == '__main__':
    test_addition()
