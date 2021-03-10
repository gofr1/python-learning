#!/usr/bin/env python3
# Graphene-Python is a library for building GraphQL APIs in Python
# sudo pip3 install graphene

import graphene

class Query(graphene.ObjectType):
    hello = graphene.String()
    
    def resolve_hello(self, info):
        return 'World'


schema = graphene.Schema(query=Query)

result = schema.execute('''
  query {
    hello
  }
''')

print(result)
#* {'data': {'hello': 'World'}}
