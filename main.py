def bubble_sort(arr):
    n = len(arr)
    # Проходим по всем элементам массива
    for i in range(n):
        # Последние i элементов уже отсортированы, поэтому не рассматриваем их
        for j in range(0, n-i-1):
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Выбираем опорный элемент (можно выбирать другие способы)
    left = [x for x in arr if x < pivot]  # Элементы меньше опорного
    middle = [x for x in arr if x == pivot]  # Элементы равные опорному
    right = [x for x in arr if x > pivot]  # Элементы больше опорного

    # Рекурсивно сортируем подмассивы слева и справа
    return quick_sort(left) + middle + quick_sort(right)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # Текущий элемент, который нужно вставить в правильное место
        j = i - 1  # Индекс предыдущего элемента

        # Перемещаем элементы больше key на одну позицию вперед
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Вставляем key в правильное место
        arr[j + 1] = key
