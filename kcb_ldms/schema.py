from graphene import ObjectType
import graphene
from kcb_builders.KcbBuilders import KcbBuilders

from kcb_dto.Kcb import *
from kcb_settings.models import *


class Query(ObjectType): 
    get_all_kcb_categories = graphene.Field(KcbCategoryResponseObject,filtering=KcbCategoryFilteringInputObject())


    @staticmethod
    def resolve_get_all_kcb_categories(self, info,filtering=None,**kwargs):

        if filtering is None:
            return info.return_type.graphene_type(response=ResponseObject.get_response(id="2"), data = [])
        
        categories = KcbCategory.objects.filter(is_active=True).values('uuid')

        if filtering.uuid is not None:
            categories = categories.filter(uuid=filtering.uuid).values('uuid')
        if filtering.category_name is not None:
            categories = categories.filter(name=filtering.category_name).values('category_name')

        category_list = list(map(lambda x: KcbBuilders.get_category_data(str(x['uuid'])),categories))
        return info.return_type.graphene_type(response=ResponseObject.get_response(id="1"), data = category_list)
    
