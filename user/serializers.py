from rest_framework import serializers

from .models import User



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        request = self.context['request']
        last_name = request._request.path
        return User.objects.create_user(**validated_data)
