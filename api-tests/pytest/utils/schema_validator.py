import json
from jsonschema import validate

def validate_schema(response_json, schema_path):
    with open(schema_path) as f:
        schema = json.load(f)
    validate(instance=response_json, schema=schema)