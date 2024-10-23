from graphene import ObjectType
import graphene
from kcb_builders.KcbBuilders import KcbBuilders

from kcb_dto.Kcb import *
from kcb_settings.models import *


class Query(ObjectType): 
    get_all_kcb_categories = graphene.Field(KcbCategoryResponseObject,filtering=KcbCategoryFilteringInputObject())
    get_all_kcb_regional_zone = graphene.Field(KcbRegionalZonalResponseObject,filtering=KcbRegionalZonalFilteringInputObject())
    get_all_kcb_departments = graphene.Field(KcbDepartmentResponseObject,filtering=KcbDepartmentFilteringInputObject())



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
    
    def resolve_get_all_kcb_regional_zone(self, info,filtering=None,**kwargs):

        if filtering is None:
            return info.return_type.graphene_type(response=ResponseObject.get_response(id="2"), data = [])
        
        regional_zone = KcbRegionalZonal.objects.filter(is_active=True).values('uuid')

        if filtering.uuid is not None:
            regional_zone = regional_zone.filter(uuid=filtering.uuid).values('uuid')
        if filtering.zone_name is not None:
            regional_zone = regional_zone.filter(name=filtering.zone_name).values('zone_name')
        if filtering.zone_code is not None:
            regional_zone = regional_zone.filter(name=filtering.zone_code).values('zone_code')

        zone_list = list(map(lambda x: KcbBuilders.get_regional_zone_data(str(x['uuid'])),regional_zone))
        return info.return_type.graphene_type(response=ResponseObject.get_response(id="1"), data = zone_list)
    

    def resolve_get_all_kcb_departments(self, info,filtering=None,**kwargs):

        if filtering is None:
            return info.return_type.graphene_type(response=ResponseObject.get_response(id="2"), data = [])
        
        department = KcbDepartments.objects.filter(is_active=True).values('uuid')

        if filtering.uuid is not None:
            department = department.filter(uuid=filtering.uuid).values('uuid')
        if filtering.department_name is not None:
            department = department.filter(name=filtering.department_name).values('department_name')
        if filtering.department_code is not None:
            department = department.filter(name=filtering.department_code).values('department_code')
    

        department_list = list(map(lambda x: KcbBuilders.get_departments_data(str(x['uuid'])),department))
        return info.return_type.graphene_type(response=ResponseObject.get_response(id="1"), data = department_list)
    

    
