from graphene_federation import build_schema

from kcb_settings.views import Mutation as kcb_settings_mutation
from kcb_settings.schema import Query as   kcb_settings_query


class Query(kcb_settings_query):
    pass

class Mutation(kcb_settings_mutation):
    pass


schema = build_schema(query=Query, mutation=Mutation) 