""""
В этой миссии Вам надо определить, все ли элементы массива равны.
Входные: List.
Выходные: Bool.
"""
from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    #    temp = 1
    #    if len(elements) <= 1:
    #        return True
    #    for each in elements:
    #        if each != elements[0]:
    #            temp = 0
    #            break
    #        else:
    #            pass
    #    return False if temp == 0 else True
    return elements[1:] == elements[:-1]


if __name__ == '__main__':
    print("Example:")
    print(all_the_same([1, 1, 1]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
