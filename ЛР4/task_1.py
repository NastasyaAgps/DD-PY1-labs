import json
def task() -> float:
    with open('input.json','r') as file:
        i = json.load(file)

    s = 0
    for item in i:
        s += item['score'] * item['weight']
    return round(s, 3)

print(task())
