def simple_search(num: int) -> bool:
    i = 2
    while i < num:
        if num % i == 0 and i != 1:
            return False
        i += 1
    return True


def simple_list(min: int, max: int) -> list:
    return [i for i in range(min, max + 1) if simple_search(num=i) and i not in [-1, 0, 1]]


case_1 = [1, 100]
case_2 = [-2, 0]
case_3 = [-999, 999]

print(simple_list(*case_1))
print(simple_list(*case_2))
print(simple_list(*case_3))
