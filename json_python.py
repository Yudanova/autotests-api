import json

json_data = '{"name": "Иван", "age": 30, "is_student": false}'
parsed_data = json.loads(json_data)  # transform JSON row в Python-object (dict)

print(parsed_data["name"],type(parsed_data))  # output Иван