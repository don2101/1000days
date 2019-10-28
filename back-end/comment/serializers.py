from rest_framework import serializers
from account.serializers import UserSerializer
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
	writer = serializers.StringRelatedField()
	diary = serializers.StringRelatedField()
	created_at = serializers.DateTimeField(read_only=True)
	updated_at = serializers.DateTimeField(read_only=True)
	id = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = Comment
		fields = ['id', 'writer', 'diary', 'content', 'created_at', 'updated_at']