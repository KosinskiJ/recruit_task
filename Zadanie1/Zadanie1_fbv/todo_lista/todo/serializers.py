from rest_framework import serializers

from todo.models import TodoList


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ('id', 'title', 'done', 'author_ip', 'created_date', 'done_date')
        extra_kwargs = {
            'author_ip': {'read_only': True},
            'created_date': {'read_only': True}
        }

    def validate(self, attrs):

        try:
            if attrs['done'] is False and attrs['done_date'] is not None:
                raise serializers.ValidationError()
            return attrs

        except KeyError:
            return attrs
