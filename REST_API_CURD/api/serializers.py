from rest_framework import serializers

class Studentserializers(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length=30)
    subject = serializers.CharField(max_length=30)
    city = serializers.CharField(max_length=30)



class Userserializers(serializers.Serializer):
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(max_length=50)

   


   