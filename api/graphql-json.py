from graphene import Schema, ObjectType, JSONString, String

class Query(ObjectType):
   
    update_json_key = JSONString(
        required=True,
        json_input=JSONString(required=True),
        key=String(required=True),
        value=String(required=True)
    )

    def resolve_update_json_key(root, info, json_input, key, value):
        #assert json_input == {"name": "John"}
        json_input[key] = value
        return json_input

schema = Schema(query=Query)

results = schema.execute("""
    query {
        updateJsonKey(jsonInput: "{\\"name\\": \\"John\\"}", key: "name", value: "Jack")
    }
""")

print(results)
