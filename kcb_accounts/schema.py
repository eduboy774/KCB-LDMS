import graphene
from graphene import ObjectType
from kcb_accounts.models import  *
from kcb_backend.decorators.Permission import has_query_access
from kcb_builders.UserAccountsBuilders import UserAccountBuilder
from kcb_dto.Response import PageObject, ResponseObject
from kcb_dto.UserAccounts import  *

from django.core.paginator import Paginator
from kcb_utils.UserUtils import UserUtils


class Query(ObjectType): 
    get_users = graphene.Field(UsersResponseObject,filtering=UserFilteringInputObject())
    get_user_profile_and_role = graphene.Field(UserProfileAndRoleResponseObject)



    # @has_query_access(permissions=['can_manage_settings','can_view_settings'])
    def resolve_get_users(self, info,filtering=None,**kwargs):
        try:
            all_users =UsersProfiles.objects.filter(profile_is_active=True).values('profile_unique_id','profile_type')

            if filtering.profile_type is not None:
                all_users = all_users.filter(profile_type=filtering.profile_type.value)
                
            if filtering.profile_unique_id is not None:
                all_users = all_users.filter(profile_unique_id=filtering.profile_unique_id)
                
                    

            paginated_users=Paginator(all_users,20)
            all_users=paginated_users.page(filtering.page_number)
            page_object=PageObject.get_page(all_users)
                
            all_users_list = list(map(lambda x: UserAccountBuilder.get_user_profile_and_role_data(str(x['profile_unique_id'])), all_users))
            
            return info.return_type.graphene_type(response=ResponseObject.get_response(id="1"),data=all_users_list , page = page_object)
        except Exception as e:
            return info.return_type.graphene_type(response=ResponseObject.get_response(id="4"))

    def resolve_get_user_profile_and_role(self, info,**kwargs):
        profile_unique_id = UserUtils.__profile__(info.context.headers)
        print('profile_unique_id',profile_unique_id)
        if profile_unique_id is None:
            return info.return_type.graphene_type(response=ResponseObject.get_response(id="6"))

        profile=UsersProfiles.objects.filter(profile_unique_id=profile_unique_id).first()
        
        if profile is None:
            return info.return_type.graphene_type(response=ResponseObject.get_response(id="7"))

        user_object=UserAccountBuilder.get_user_profile_and_role_data(profile.profile_unique_id)
        
        return info.return_type.graphene_type(response=ResponseObject.get_response(id="1"),data=user_object)
