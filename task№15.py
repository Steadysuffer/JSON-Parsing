import json
from statistics import mean

json_string = [
    {
        "name": "Петр",
        "surname": "Петров",
        "patronymic": "Васильевич",
        "age": 23,
        "occupation": "ойтишнек"
    },
    {
        "name": "Василий",
        "surname": "Васильев",
        "patronymic": "Петрович",
        "age": 24,
        "occupation": "дворник"
    }
]
json_string = json.dumps(json_string)


def mean_age(json_string):
    list_age = []
    json_to_str = json.loads(json_string)
    for i in json_to_str:
        list_age.append(i.get("age"))
    json_dict = {"mean_age": mean(list_age)}
    str_to_json = json.dumps(json_dict)
    return str_to_json

print(mean_age(json_string))
