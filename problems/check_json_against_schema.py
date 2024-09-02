import requests
import json
import jsonschema
from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "ALIAS": {"type": "string"},
        "EXTERNAL_PUBLIC_KEY": {"type": "string"},
        "KEYSTORE_TYPE": {"type": "string"},
        "PRIVATE_KEY": {"type": "string"}
    },
    "required": ["ALIAS", "EXTERNAL_PUBLIC_KEY", "KEYSTORE_TYPE", "PRIVATE_KEY"]
}

# response = requests.get('path')
# json_object = json.load(response.text)

json_object = {
    "ALIAS": "John Doe",
    "EXTERNAL_PUBLIC_KEY": "John Doe",
    "KEYSTORE_TYPE": "john.doe@example.com",
    "PRIVATE_KEY": "John Doe",
    "NEW_KEY": "Value"
}

# json_object = {
#     "EXTERNAL_PUBLIC_KEY": "John Doe",
#     "KEYSTORE_TYPE": "john.doe@example.com",
#     "PRIVATE_KEY": "John Doe"
# }

try:
    validate(instance=json_object, schema=schema)
    print("JSON is valid.")
except ValidationError as e:
    print(f"JSON is invalid: {e.message}")
