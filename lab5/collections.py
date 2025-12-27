import random


def reverse_list(lst):
    reversed_list = []
    i = len(lst) - 1
    while i >= 0:
        reversed_list.append(lst[i])
        i = i - 1
    return reversed_list


def modify_list(lst):
    new_list = []
    for item in lst:
        new_item = item * 2
        new_list.append(new_item)
    return new_list


def compare_lists(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            return False
    return True


def range_with_step(lst):
    result = []
    for i in range(0, len(lst), 2):
        result.append(lst[i])
    return result


def create_list():
    new_list = []
    for i in range(1, 6):
        new_list.append(i * 10)
    return new_list


def insert_element(lst, pos, val):
    new_list = []
    for i in range(len(lst)):
        if i == pos:
            new_list.append(val)
        new_list.append(lst[i])
    return new_list


def merge_sort_lists(lst1, lst2):
    merged = []
    for item in lst1:
        merged.append(item)
    for item in lst2:
        merged.append(item)
    for i in range(len(merged)):
        for j in range(i + 1, len(merged)):
            if merged[i] > merged[j]:
                temp = merged[i]
                merged[i] = merged[j]
                merged[j] = temp
    return merged


def random_list_center():
    random_list = []
    for i in range(8):
        random_list.append(random.randint(1, 100))
    length = len(random_list)
    is_even = length % 2 == 0
    center = length // 2
    return random_list, is_even, center


def add_lists_threshold(lst1, lst2, threshold):
    if len(lst1) >= threshold and len(lst2) >= threshold:
        result = []
        for item in lst1:
            result.append(item)
        for item in lst2:
            result.append(item)
        return result
    return None


def sort1(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
    for i in range(len(new_list)):
        for j in range(i + 1, len(new_list)):
            if new_list[i] > new_list[j]:
                temp = new_list[i]
                new_list[i] = new_list[j]
                new_list[j] = temp
    return new_list


def sort2_with_map(lst):
    strings = []
    for item in lst:
        strings.append(str(item))
    strings_list = list(map(str, lst))
    sorted_list = []
    for s in strings_list:
        sorted_list.append(int(s))
    for i in range(len(sorted_list)):
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[i] > sorted_list[j]:
                temp = sorted_list[i]
                sorted_list[i] = sorted_list[j]
                sorted_list[j] = temp
    return sorted_list


def sort3_with_map(lst):
    lengths = list(map(len, [str(x) for x in lst]))
    result = []
    for item in lst:
        result.append(item)
    return result


def sort4(lst):
    new_list = []
    for item in lst:
        new_list.append(item)
    n = len(new_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if new_list[j] < new_list[j + 1]:
                temp = new_list[j]
                new_list[j] = new_list[j + 1]
                new_list[j + 1] = temp
    return new_list


def sort5_with_map(lst):
    doubled = list(map(lambda x: x * 2, lst))
    result = []
    for d in doubled:
        result.append(d // 2)
    return result


def sort6_with_map(lst):
    processed = list(map(abs, lst))
    sorted_list = []
    for item in processed:
        sorted_list.append(item)
    return sorted_list


def find_min(lst):
    min_val = lst[0]
    for item in lst:
        if item < min_val:
            min_val = item
    return min_val


def tuple_work1(tpl):
    length = len(tpl)
    return length


def tuple_work2(tpl):
    result = ()
    for item in tpl:
        result = result + (item * 2,)
    return result


def tuple_types(tpl):
    types_list = []
    for item in tpl:
        types_list.append(type(item).__name__)
    return types_list


def tuple_contains(tpl, val):
    for item in tpl:
        if item == val:
            return True
    return False


def create_2d_list():
    matrix = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(i * 3 + j)
        matrix.append(row)
    return matrix


def dict_work1(d):
    return len(d)


def dict_work2(d):
    keys = []
    for key in d:
        keys.append(key)
    return keys


def dict_work3(d):
    values = []
    for key in d:
        values.append(d[key])
    return values


def count_dict_keys(dicts_list):
    total = 0
    for d in dicts_list:
        total = total + len(d)
    return total


def find_nested_element(nested_dict, keys_path):
    current = nested_dict
    for key in keys_path:
        if key in current:
            current = current[key]
        else:
            return None
    return current


def call_all():
    print("1. Reverse list:", reverse_list([1, 2, 3, 4, 5]))
    print("2. Modify list:", modify_list([1, 2, 3]))
    print("3. Compare lists:", compare_lists([1, 2, 3], [1, 2, 3]))
    print("4. Range with step:", range_with_step([0, 1, 2, 3, 4, 5]))
    print("5. Create list:", create_list())
    print("6. Insert element:", insert_element([1, 2, 4, 5], 2, 3))
    print("7. Merge sort:", merge_sort_lists([3, 1], [4, 2]))
    print("8. Random list center:", random_list_center())
    print("9. Add with threshold:", add_lists_threshold([1, 2], [3, 4], 2))
    print("10.1 Sort:", sort1([5, 2, 8, 1]))
    print("10.2 Sort with map:", sort2_with_map([5, 2, 8]))
    print("10.3 Sort with map:", sort3_with_map([1, 2, 3]))
    print("10.4 Sort:", sort4([3, 1, 4, 1, 5]))
    print("10.5 Sort with map:", sort5_with_map([1, 2, 3]))
    print("10.6 Sort with map:", sort6_with_map([-3, -1, 2]))
    print("11. Find min:", find_min([5, 2, 8, 1]))
    print("12.1 Tuple work:", tuple_work1((1, 2, 3)))
    print("12.2 Tuple work:", tuple_work2((1, 2, 3)))
    print("13. Tuple types:", tuple_types((1, "hello", 3.14)))
    print("14. Tuple contains:", tuple_contains((1, 2, 3), 2))
    print("15. Create 2D list:", create_2d_list())
    print("16.1 Dict work:", dict_work1({"a": 1, "b": 2}))
    print("16.2 Dict work:", dict_work2({"x": 10, "y": 20}))
    print("16.3 Dict work:", dict_work3({"p": 100, "q": 200}))
    print("17. Count dict keys:", count_dict_keys([{"a": 1}, {"b": 2, "c": 3}]))
    nested = {"level1": {"level2": {"level3": "value"}}}
    print("18. Find nested:", find_nested_element(nested, ["level1", "level2", "level3"]))
