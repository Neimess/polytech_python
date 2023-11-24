# TODO Напишите функцию find_common_participants
def find_common_participants(str1:str, str2:str, separator=","):
    # Разделяем строки на списки участников, используя заданный разделитель
    participants1 = str1.split(separator)
    participants2 = str2.split(separator)

    # Преобразуем списки в множества для выполнения операции пересечения
    set1 = set(participants1)
    set2 = set(participants2)

    # Находим общих участников среди двух групп
    common_participants = set1.intersection(set2)

    # Возвращаем отсортированный список общих участников
    return sorted(list(common_participants))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, "|"))
# TODO Провеьте работу функции с разделителем отличным от запятой
