from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    class Meta:
        permissions = [
            # Define tus permisos aquí si es necesario
        ]

User._meta.get_field('groups').remote_field.related_name = 'user_set_custom'
User._meta.get_field('user_permissions').remote_field.related_name = 'user_set_custom'
