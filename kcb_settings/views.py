import graphene
from graphql import build_schema
from kcb_builders.KcbBuilders import KcbBuilders

from kcb_dto.Kcb import *
from kcb_settings.models import *
# Kcb Category
class CreateKcbCategoryMutation(graphene.Mutation):
    class Arguments:
        input = KcbCategoryInputObject()

    response = graphene.Field(ResponseObject)
    data = graphene.Field(KcbCategoryObject)

    @classmethod
    def mutate(self, root, info, input):
        
        category, success = KcbCategory.objects.update_or_create(
            category_name = input.category_name,
            defaults={
                'is_active': True
            }
        )

        data = KcbBuilders.get_category_data(id=category.uuid)
        return self(ResponseObject.get_response(id='1'), data=data)

class UpdateKcbCategoryMutation(graphene.Mutation):
    class Arguments:
        input = KcbCategoryInputObject()

    response = graphene.Field(ResponseObject)
    data = graphene.Field(KcbCategoryObject)

    @classmethod
    def mutate(self, root, info, input):
        
        category, success = KcbCategory.objects.update_or_create(
            uuid = input.uuid,
            defaults={
                'category_name' : input.category_name,
                'is_active': True
            }
        )

        data = KcbBuilders.get_category_data(id=category.uuid)
        return self(ResponseObject.get_response(id='1'), data=data)

class DeleteKcbCategoryMutation(graphene.Mutation):
    class Arguments:
        uuid = graphene.String()

    response = graphene.Field(ResponseObject)

    @classmethod
    def mutate(self, root, info, uuid):
        
        category = KcbCategory.objects.filter(uuid=uuid).first()
        category.is_active = False
        category.save()

        return self(ResponseObject.get_response(id='1'))
    
# Kcb Regional Zonal
class CreateKcbRegionalZonalMutation(graphene.Mutation):
    class Arguments:
        input = KcbRegionalZonalFilteringInputObject()

    response = graphene.Field(ResponseObject)
    data = graphene.Field(KcbRegionalZonalObject)

    @classmethod
    def mutate(self, root, info, input):
        
        regional_zone, success = KcbRegionalZonal.objects.update_or_create(
            zone_name = input.zone_name,
            zone_code = input.zone_code,
            zone_description = input.zone_description,
            defaults={
                'is_active': True
            }
        )

        data = KcbBuilders.get_regional_zone_data(id=regional_zone.uuid)
        return self(ResponseObject.get_response(id='1'), data=data)

class UpdateKcbRegionalZoneMutation(graphene.Mutation):
    class Arguments:
        input = KcbRegionalZonalInputObject()

    response = graphene.Field(ResponseObject)
    data = graphene.Field(KcbRegionalZonalObject)

    @classmethod
    def mutate(self, root, info, input):
        
        category, success = KcbRegionalZonal.objects.update_or_create(
            uuid = input.uuid,
            defaults={
                'zone_name' : input.zone_name,
                'zone_code' : input.zone_code,
                'zone_description' : input.zone_description,
                'is_active': True
            }
        )

        data = KcbBuilders.get_regional_zone_data(id=category.uuid)
        return self(ResponseObject.get_response(id='1'), data=data)

class DeleteKcbRegionalZoneMutation(graphene.Mutation):
    class Arguments:
        uuid = graphene.String()

    response = graphene.Field(ResponseObject)

    @classmethod
    def mutate(self, root, info, uuid):
        
        category = KcbRegionalZonal.objects.filter(uuid=uuid).first()
        category.is_active = False
        category.save()

        return self(ResponseObject.get_response(id='1'))
# Kcb Department
class CreateKcbDepartmentMutation(graphene.Mutation):
    class Arguments:
        input = KcbDepartmentInputObject()

    response = graphene.Field(ResponseObject)
    data = graphene.Field(KcbDepartmentObject)

    @classmethod
    def mutate(self, root, info, input):
        
        regional_zone, success = KcbDepartments.objects.update_or_create(
            department_name = input.department_name,
            department_code = input.department_code,
            department_description = input.department_description,
            defaults={
                'is_active': True
            }
        )

        data = KcbBuilders.get_departments_data(id=regional_zone.uuid)
        return self(ResponseObject.get_response(id='1'), data=data)

class UpdateKcbDepartmentMutation(graphene.Mutation):
    class Arguments:
        input = KcbDepartmentInputObject()

    response = graphene.Field(ResponseObject)
    data = graphene.Field(KcbDepartmentObject)

    @classmethod
    def mutate(self, root, info, input):
        
        category, success = KcbDepartments.objects.update_or_create(
            uuid = input.uuid,
            defaults={
                'department_name' : input.department_name,
                'department_code' : input.department_code,
                'department_description' : input.department_description,
                'is_active': True
            }
        )

        data = KcbBuilders.get_departments_data(id=category.uuid)
        return self(ResponseObject.get_response(id='1'), data=data)

class DeleteKcbDepartmentMutation(graphene.Mutation):
    class Arguments:
        uuid = graphene.String()

    response = graphene.Field(ResponseObject)

    @classmethod
    def mutate(self, root, info, uuid):
        
        category = KcbDepartments.objects.filter(uuid=uuid).first()
        category.is_active = False
        category.save()

        return self(ResponseObject.get_response(id='1'))


class Mutation(graphene.ObjectType):

    create_kcb_category_mutation = CreateKcbCategoryMutation.Field()
    update_kcb_category_mutation = UpdateKcbCategoryMutation.Field()
    delete_kcb_category_mutation = DeleteKcbCategoryMutation.Field()

    create_kcb_regional_zonal_mutation = CreateKcbRegionalZonalMutation.Field()
    update_kcb_regional_zonal_mutation = UpdateKcbRegionalZoneMutation.Field()
    delete_kcb_regional_zonal_mutation = DeleteKcbRegionalZoneMutation.Field()

    create_department_mutation = CreateKcbDepartmentMutation.Field()
    update_department_mutation = UpdateKcbDepartmentMutation.Field()
    delete_department_mutation = DeleteKcbDepartmentMutation.Field()

    