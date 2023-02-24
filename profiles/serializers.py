from rest_framework import serializers
from .models import UserNet


class GetUserNetSerializer(serializers.ModelSerializer):
    """Displaying user information"""

    class Meta:
        model = UserNet
        exclude = (
            'password',
            'last_login',
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions'
        )


class GetUserPublicNetSerializer(serializers.ModelSerializer):
    """Displaying public user information"""

    class Meta:
        model = UserNet
        exclude = (
            'password',
            'last_login',
            'is_active',
            'is_staff',
            'is_superuser',
            'email',
            'groups',
            'user_permissions',
            'phone',
        )
