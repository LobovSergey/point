def unique_list(data: list) -> list:
    unique = []
    for i in data:
        if i not in unique:
            unique.append(i)
    return unique


case_1 = [1, 2, 4, 5, 1, 2313, 45, 123, 4, 5, 2]
case_2 = [123123, 1241412, 0]
case_3 = [0]

print(unique_list(data=case_1))
print(unique_list(data=case_2))
print(unique_list(data=case_3))
