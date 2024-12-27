# Алгоритм взял в интернете

def merge(left_list, right_list):  
    sorted_list = []
    left_list_index = right_list_index = 0

    # Т. к. длина списков применяется часто, создадим для удобства переменные
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если 1-й элемент левого подсписка меньше, добавляем его
            # в сортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если 1-й элемент правого подсписка меньше, добавляем его
            # в сортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Когда достигнут конец левого списка, добавляем элементы правого списка
        # в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Когда достигнут конец правого списка, добавляем элементы левого списка
        # в сортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(nums):  
    # Возвращаем список, когда он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Чтобы найти середину списка, применяем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем сортированные списки в результирующий
    return merge(left_list, right_list)




# Проверяем, что всё работает
# random_list_of_nums = [120, 45, 68, 250, 176]  
# random_list_of_nums = merge_sort(random_list_of_nums)  
# print(random_list_of_nums)