from rest_framework import serializers
from .models import Article

#serializer class
# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     descripition = serializers.CharField(max_length=400)

#     def create(self, validated_data):
#         return Article.objects.create(validated_data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.descripition = validated_data.get('descripition', instance.descripition)

#Model Serializer
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'descripition']