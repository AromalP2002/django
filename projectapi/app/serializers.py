from rest_framework import serializers

class user_serializer(serializers.Serializer):
    roll_no=serializers.IntegerField()
    age=serializers.CharField()
    age=serializers.IntegerField()
    email=serializers.EmailField()