from rest_framework.permissions import IsAuthenticated
from kcb_settings.models import LocationScanUsers
from kcb_uaa.models import UsersWithRoles
from kcb_accounts.models import UsersProfiles
from .BearerTokenAuthentication import BearerTokenAuthentication
from kcb_builders.UAABuilder import UAABuilder 
import uuid


class UserUtils:
    def __profile__(request):

        user_data = UserUtils.get_user(request)
        return user_data['profile_unique_id']
    
    def __location__(request):

        user_data = UserUtils.get_user_location_scan(request)
        return user_data['location']
    
    
    def get_user_permissions(user):
        user_with_role= UsersWithRoles.objects.filter(user_with_role_user=user).first()
        if not user_with_role:
            return []
        user_roles = UAABuilder.get_role_data(id=user_with_role.user_with_role_role.role_unique_id)
        user_permissions =[]
        for permission in user_roles.role_permissions:
            user_permissions.append(permission.permission_code)
        return user_permissions
    
    
    def get_user(user = None, request = None):
        
        is_authenticated, user = BearerTokenAuthentication.authenticate(None,user)
        
        profile=UsersProfiles.objects.filter(profile_user=user).first()
        
        user_data={
            'profile_unique_id':str(profile.profile_unique_id),
            'first_name':user.first_name,
            'last_name':user.last_name,
            'username':user.username,
            'email':user.email,
            'user_permissions':UserUtils.get_user_permissions(user),
            'user_type':profile.profile_type,
            "profile_phone":profile.profile_phone
        }      
        

        return user_data
    
    def get_user_location_scan(user):

        is_authenticated, user = BearerTokenAuthentication.authenticate(None,user)
        
        profile=UsersProfiles.objects.filter(profile_user=user).first()
        location = LocationScanUsers.objects.filter(user_profile=profile).first()
        user_data={
            'location': location.location_scan.location_unique_id,
            
        }

        return user_data

    
    def get_forgot_password_token():
        token =  str(uuid.uuid4())
        return token
    
    