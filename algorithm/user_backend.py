from algorithm.models import CustomUser
from django.contrib.auth.backends import ModelBackend

class ProxiedUserBackend(ModelBackend):
    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None