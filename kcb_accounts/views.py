import graphene
from graphene_federation import build_schema
from kcb_backend.decorators.Permission import has_mutation_access

from  kcb_dto.UserAccounts import  *
from kcb_dto.Response import ResponseObject
from django.contrib.auth.models import User
from kcb_accounts.models import *
from kcb_builders.UserAccountsBuilders import UserAccountBuilder
from kcb_uaa.models import *
from kcb_utils.EmailUtils import EmailNotifications
from kcb_utils.UserUtils import UserUtils
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

from dotenv import dotenv_values

config = dotenv_values(".env")


class CreateUsersMutation(graphene.Mutation):
    class Arguments:
        input = UserInputObject(required=True)
        

    response = graphene.Field(ResponseObject)
    data = graphene.Field(UserProfileAndRoleObjects) 

    @classmethod
    # @has_mutation_access(permissions=['can_manage_settings'])
    def mutate(self, root, info,  input):

        user = User.objects.create(
            first_name=input.user_first_name,
            last_name=input.user_last_name,
            username=input.user_email,
            email=input.user_email,
        )


        user_profile = UsersProfiles.objects.create(
            profile_type=input.profile_type.value,
            profile_phone=input.profile_phone,
            profile_title=input.profile_title,
            profile_user=user
        )

        UsersWithRoles.objects.create(
            user_with_role_role = UserRoles.objects.filter(role_unique_id=input.role_unique_id).first(),
            user_with_role_user=user
        )


        response_body = UserAccountBuilder.get_user_profile_and_role_data(id=user_profile.profile_unique_id)

        return self(response=ResponseObject.get_response(id="1"), data=response_body)

class UpdateUsersMutation(graphene.Mutation):
    class Arguments:
        input = UserInputObject(required=True)

    response = graphene.Field(ResponseObject)
    data = graphene.Field(UserProfileAndRoleObjects)

    @classmethod
    # @has_mutation_access(permissions=['can_manage_settings'])
    def mutate(self, root, info,  input):

        profile = UsersProfiles.objects.filter(profile_is_active=True, profile_unique_id=input.profile_unique_id).first()

        if profile is None:
            return self(response=ResponseObject.get_response(id="6"), data=None)

        profile.profile_phone = input.profile_phone
        profile.profile_title = input.profile_title
        profile.profile_type=input.profile_type.value
        profile.profile_photo = input.profile_photo
        profile.profile_gender = input.profile_gender.value if input.profile_gender else None,
        profile.save()

        profile.profile_user.first_name = input.user_first_name
        profile.profile_user.last_name = input.user_last_name
        profile.profile_user.email = input.user_email
        profile.profile_user.save()

        user_with_role = UsersWithRoles.objects.filter(user_with_role_role__role_unique_id=input.role_unique_id).first()
        user_with_role.user_with_role_role = UserRoles.objects.filter(role_unique_id=input.role_unique_id).first()
        user_with_role.save()
        
        response_body = UserAccountBuilder.get_user_profile_and_role_data(id=profile.profile_unique_id)

        return self(response=ResponseObject.get_response(id="1"), data=response_body)
    
class DeleteUsersMutation(graphene.Mutation):
    class Arguments:
        profile_unique_id = graphene.String(required=True)

    response = graphene.Field(ResponseObject)

    @classmethod
    # @has_mutation_access(permissions=['can_manage_settings'])
    def mutate(self, root, info,  profile_unique_id):

        admin_profile = UsersProfiles.objects.filter(profile_unique_id=profile_unique_id).first()
        admin_profile.profile_type = ""
        admin_profile.profile_is_active = False
        admin_profile.save()
        admin_profile.profile_user.is_active = False
        admin_profile.profile_user.save()

        return self(response=ResponseObject.get_response(id="1"))

class UpdateMyProfileMutation(graphene.Mutation):
    class Arguments:
        input = UserInputObject(required=True)

    response = graphene.Field(ResponseObject)
    data = graphene.Field(UserProfileObject)

    @classmethod
    def mutate(self, root, info,  input):

        profile = UsersProfiles.objects.filter(profile_unique_id=input.profile_unique_id, profile_is_active=True).first()

        if profile is None:
            return self(response=ResponseObject.get_response(id="6"), data=None)

        profile.profile_phone = input.profile_phone
        profile.profile_title = input.profile_title
        profile.profile_photo = input.profile_photo
        profile.profile_gender = input.profile_gender
        profile.save()

        profile.profile_user.first_name = input.user_first_name
        profile.profile_user.last_name = input.user_last_name
        profile.profile_user.email = input.user_email
        profile.profile_user.save()

        response_body = UserAccountBuilder.get_user_profile_data(id=profile.profile_unique_id)

        return self(response=ResponseObject.get_response(id="1"), data=response_body)


class ForgotPasswordMutation(graphene.Mutation):
    class Arguments:
        user_email = graphene.String(required=True)
    
    response = graphene.Field(ResponseObject)
    
    @classmethod
    # @has_mutation_access(permissions=['can_manage_settings'])
    def mutate(self, root, info,  user_email):
        try:
            user = User.objects.filter(username = user_email ).first()
            if user is None:
                return self(response=ResponseObject.get_response(id="3"))
            
            request_token = UserUtils.get_forgot_password_token()
           
            ForgotPasswordRequestUsers.objects.create(
                request_user = user,
                request_token = request_token
            )

            url = config['FRONTEND_DOMAIN'] + f"password-reset/{request_token}/"

            body = {
                'receiver_details': user.email,
                'user': user,
                'url': url,
                'subject': "Kcb Password Reset"
            }

            EmailNotifications.send_email_notification(body, 'password_reset.html')


            return self(response=ResponseObject.get_response(id="1"))
        except Exception as e:
            return self(response=ResponseObject.get_response(id="5"))

class ChangeUserPasswordMutation(graphene.Mutation):
    class Arguments:
        input = ForgortPasswordFilteringInputObject(required=True)

    response = graphene.Field(ResponseObject)
    @classmethod
    def mutate(self, root, info,  input):

        profile_unique_id = UserUtils.__profile__(info.context.headers)

        user = UsersProfiles.objects.filter(profile_unique_id=profile_unique_id, profile_is_active=True).first()

        if not authenticate(username=user.profile_user.username, password=input.old_password):
            return self(response=ResponseObject.get_response(id="16"))

        user.profile_user.set_password(input.new_password)
        user.profile_user.save()

        return self(response=ResponseObject.get_response(id="1"))




class Mutation(graphene.ObjectType):
    create_users_mutation = CreateUsersMutation.Field()
    update_users_mutation = UpdateUsersMutation.Field()
    delete_users_mutation = DeleteUsersMutation.Field()
    
    update_user_profile_mutation = UpdateMyProfileMutation.Field()
    forgot_password_mutation = ForgotPasswordMutation.Field()
    change_user_password_mutation = ChangeUserPasswordMutation.Field()


schema = build_schema(Mutation, types=[])

