from jsonschema import validate, ValidationError

# Example schema
schema = {
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "age": { "type": "number" }
  },
  "required": ["name"]
}

# Example data
data = {
  "name": "John Doe",
  "age": 30
}

validate(instance=data, schema=schema)

# try:
#     validate(instance=data, schema=schema)
#     print("Data conforms to the schema.")
# except ValidationError as e:
#     print(f"Validation error: {e.message}")