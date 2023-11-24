import json

INPUT_FILE = "input.json"

def task() -> float:
    try:
        with open(INPUT_FILE, "r", encoding="utf-8") as input_file:
            data = json.load(input_file)

        product_sum = 0.0

        for entry in data:
            score = entry.get("score", 0)
            weight = entry.get("weight", 0)
            product_sum += score * weight

        return round(product_sum, 3)
    except Exception as e:
        print(f"Ошибка: {str(e)}")
        return None


print(task())
