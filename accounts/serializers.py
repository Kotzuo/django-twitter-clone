
from rest_framework import serializers

from .models import User


class AccountSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'confirm_password']
        extra_kwargs = {'password': {'write_only': True},
                        'id': {'read_only': True}}

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'confirm_password':
                continue
            setattr(instance, attr, value)

        if 'password' in validated_data:
            instance.set_password(validated_data['password'])

        instance.save()
        return instance

    def validate(self, attrs):
        data = {
            'password': attrs.get('password', None),
            'confirm_password': attrs.get('confirm_password', None)
        }

        if attrs.get('password', False) or attrs.get('confirm_password', False):
            password_serializer = PasswordSerializer(data=data)
            password_serializer.is_valid(raise_exception=True)

        return attrs


class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, max_length=128)
    confirm_password = serializers.CharField(write_only=True, max_length=128)

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Passwords don't match.")

        return attrs
