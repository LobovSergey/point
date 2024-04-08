def sort_strings(data: list, reverse=False) -> list:
    if len(data) > 1:
        len_string = len(data[0])
        great = [x for x in data if len(x) > len_string]
        same = [x for x in data if len(x) == len_string]
        low = [x for x in data if len(x) < len_string]
        if not reverse:
            result = sort_strings(low, reverse=reverse) + \
                same + sort_strings(great, reverse=reverse)
        else:
            result = sort_strings(great, reverse=reverse) + \
                same + sort_strings(low, reverse=reverse)
        return result
    return data


str_list = ['fwefewf', 'qwefwefewfasv wvqvq', 'f wqefqw', 'efw', 'ddd']
res_1 = sort_strings(data=str_list)
res_2 = sort_strings(data=str_list, reverse=True)
print(res_1)
print(res_2)
