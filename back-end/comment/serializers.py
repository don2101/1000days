from rest_framework import serializers
from account.serializers import UserSerializer
from .model import Comment

class CommentSerializer(serializers.ModelSerializer)
	writer = serializers.StringRelatedField()
	created_at = serializers.DateTimeField(read_only=True)
	updated_at = serializers.DateTimeField(read_only=True)

	class Meta:
		model = Comment
		fields = ['writer', 'content', 'created_at', 'updated_at']