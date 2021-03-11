#!/usr/bin/env python3

from graphene import ObjectType, String, Schema

#! Creating a basic Schema
class Query(ObjectType):
    # this defines a Field `hello` in our Schema with a single Argument `name`
    # with default value 'stranger'
    hello = String(name=String(default_value="stranger"))
    goodbye = String()

    # our Resolver method takes the GraphQL context (root, info) as well as
    # Argument (name) for the Field and returns data for the query Response
    def resolve_hello(root, info, name):
        return f'Hello {name}!'

    def resolve_goodbye(root, info):
        return 'See ya!'

schema = Schema(query=Query)

#! Schema Definition Language (SDL)
# In the GraphQL Schema Definition Language, we could describe the fields defined by our example code as shown below.
# 
# type Query {
#   hello(name: String = "stranger"): String
#   goodbye: String
# }

#! Querying

# we can query for our field (with the default argument)
query_string = '{ hello }'
result = schema.execute(query_string)
print(result.data['hello'])
#* Hello stranger!

# or passing the argument in the query
query_with_argument = '{ hello(name: "GraphQL") }'
result = schema.execute(query_with_argument)
print(result.data['hello'])
#* Hello GraphQL!

print(result)
#* {'data': {'hello': 'Hello GraphQL!'}}

query_string = '{ goodbye }'
result = schema.execute(query_string)
print(result.data['goodbye'])
#* See ya!