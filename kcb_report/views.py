import graphene
from graphql import build_schema
from kcb_builders.KcbBuilders import KcbBuilders

from kcb_dto.Kcb import *
from kcb_settings.models import *

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


class Mutation(graphene.ObjectType):
    create_kcb_category_mutation = CreateKcbCategoryMutation.Field()
    update_kcb_category_mutation = UpdateKcbCategoryMutation.Field()
    delete_kcb_category_mutation = DeleteKcbCategoryMutation.Field()

    