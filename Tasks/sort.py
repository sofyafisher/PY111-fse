import random
import time

array = [random.randint(13, 25) for _ in range(10**2)]

def get_key(d, value):

    for k, v in d.items():
        if v == value:
            return k

def quick_sort(container):
    """
    Sort input container with quick sort
    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) > 1:
        pivot = container[len(container) // 2]

        less = []
        greater = []
        equal = []

        for i in container:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                greater.append(i)
            else:
                equal.append(i)
        return quick_sort(less) + equal + quick_sort(greater)
    else: return container

def merge_sort(container):
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    if len(container) > 1:
        mid = len(container) // 2
        L = container[:mid]
        R = container[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                container[k] = L[i]
                i += 1
            else:
                container[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            container[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            container[k] = R[j]
            j += 1
            k += 1

    return container

def bubble_sort(container):
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    for _ in range(len(container)):
        for i in range(len(container) - 1):
             if container[i] > container[i + 1]:
                 container[i], container[i + 1] = container[i + 1], container[i]

    return container

def time_measure(sort_type):

    time_list = []
    for i in range(11):
        start = time.perf_counter()
        if sort_type == "quick_sort":
            quick_sort(array)
        if bubble_sort == "bubble_sort":
            quick_sort(array)
        if sort_type == "merge_sort":
            merge_sort(array)
        time_list.append(time.perf_counter() - start)

    return sum(time_list) / 10


dict_of_measurements = {"quick_sort": time_measure(quick_sort),
                        "bubble_sort": time_measure(bubble_sort),
                        "merge_sort": time_measure(merge_sort)}

print("Лучшее время", min(dict_of_measurements.values()))
print("Самая эффективная сортировка", get_key(dict_of_measurements, min(dict_of_measurements.values())))