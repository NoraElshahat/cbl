from rest_framework import serializers
from .models import CblUser

class StudenSerialiezer(serializers.ModelSerializer):
    class Meta:
        model = CblUser
        depth = 1      
        fields = ('user_name' , 'email', 'phone', 'gender', 'country', 'address','last_login')
        
        