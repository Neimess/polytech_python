import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []
    with open(INPUT_FILENAME, encoding="utf-8") as input_file:
        # Класс для записи данных из таблицы сразу в словарь
        reader = csv.DictReader(input_file)
        # Чтение данных
        for row in reader:
            data.append(row)
        with open(OUTPUT_FILENAME, "w", encoding="utf-8") as output_file:
            # Сериализация data в JSON
            output_file.write(json.dumps(data, indent=4))


    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
