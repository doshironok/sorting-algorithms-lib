def sort_matrix_by_row_sum(matrix):
    """
    Сортирует строки матрицы по возрастанию суммы элементов в строке.
    
    Аргументы:
        matrix (list of list of numbers): входная матрица NxM
    
    Возвращает:
        list of list of numbers: новая матрица с отсортированными строками
    
    Пример:
        >>> sort_matrix_by_row_sum([[3, 1], [1, 2], [4, 0]])
        [[1, 2], [3, 1], [4, 0]]  # суммы: 3, 4, 4 → стабильная сортировка
    """
    if not matrix:
        return []
    
    # Проверка на корректность: все строки одинаковой длины
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise ValueError("Все строки матрицы должны иметь одинаковую длину")
    
    # Сортировка с использованием суммы строки как ключа
    # sorted() гарантирует стабильность (сохраняет порядок при равных суммах)
    sorted_matrix = sorted(matrix, key=lambda row: sum(row))
    return sorted_matrix


def sort_matrix_by_column_sum(matrix):
    """
    Транспонирует матрицу, сортирует столбцы как строки по сумме,
    затем возвращает обратно транспонированную матрицу.
    Эквивалентно сортировке столбцов по возрастанию их суммы.
    """
    if not matrix:
        return []
    
    # Транспонирование
    transposed = list(zip(*matrix))
    # Сортировка "столбцов" (теперь это строки)
    sorted_transposed = sorted(transposed, key=lambda col: sum(col))
    # Обратное транспонирование
    result = list(zip(*sorted_transposed))
    # Преобразуем кортежи обратно в списки
    return [list(row) for row in result]
