# import sys
# sys.path.append("../src")
#TODO make it with pip install math_demo

# Ранее тестирование позволяет съэкономить время позднее
# Тесты показывают наличие ошибок, а не их отствие
# Тесты не должны использовать ВСЕ наборы входных параметров
# Тесты не должны дублировать логику тестируемого кода
# тесты должны покрывать "класстеры" входных параметров
# Тесты должны обнаруживать новые ошибки
# тесты покрывают как успешные так и ошибочные кейсы

from math_demo import add, add_with_bug

def test_addition():
    assert add(2,2)==4
    print("Test ADDITION PASSED")

def test_addition_with_bug():
    # Тесты показывают наличие ошибок, а не их отсутстиве 
    assert add_with_bug(2,2) == 4
    assert add_with_bug(0,0) == 0
    print("Test ADDITION PASSED")
    # finally we found error 
    # assert add_with_bug(7,6) == 13

def test_addition_duplicate():
    assert add(6,7) == 6 + 7
    print("Test DUPLICATION ADDITION PASSED")

def test_addition_overkill():
    for i in range(0, 2**32):
        for j in range(0, 2**32):
            assert add(i,j) == i +j
            assert add(-i,j) == -i + j
            assert add(-i, -j) == -i-j
            assert add(i, -j) == i -j

def test_addition_clusters():
    assert add(7, 6) == 13
    assert add(10, -11) == -1
    assert add(6, -2) == 4
    assert add(5, 9) == 14
    assert add(9, 5) == 14
    print("Test ADDITION CLUSTERS PASSED")

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicate()
    # test_addition_overkill()
    test_addition_clusters()
