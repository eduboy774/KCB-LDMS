from graphene_federation import build_schema

from kcb_settings.views import Mutation as kcb_settings_mutation
from kcb_settings.schema import Query as   kcb_settings_query
from kcb_accounts.views import Mutation as kcb_accounts_mutation
from kcb_accounts.schema import Query as   kcb_accounts_query


class Query(kcb_settings_query,kcb_accounts_query):
    pass

class Mutation(kcb_settings_mutation,kcb_accounts_mutation):
    pass


schema = build_schema(query=Query, mutation=Mutation) 