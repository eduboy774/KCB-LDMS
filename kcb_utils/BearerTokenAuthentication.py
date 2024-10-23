from django.contrib.auth.backends import BaseBackend
from provider.oauth2.models import AccessToken 
from provider.utils import now

class BearerTokenAuthentication(BaseBackend):
    def authenticate_header(self, request):
        return 'Bearer'

    def authenticate(self, headers):
        try:
            bearer_token=headers['Authorization'].split(' ')[1]
            token=AccessToken.objects.filter(token=bearer_token,expires__gt=now(), client__client_id='840dc4b19b2bc82a55e5').first()

            return True, token.user
        except AccessToken.DoesNotExist:
            return False, None
        #TODO: remove this when in production
        except Exception as e:
            return False, None
# 


# npx diagnose-endpoint@1.1.0 --endpoint="http://127.0.0.1:8000/" --method="POST" --headers="Content-Type: application/json,Authorization: Bearer c86b0f6e63a8aecb6d0e7f5cffce4c2a66ee2a62"