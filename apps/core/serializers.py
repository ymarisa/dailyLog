from django.contrib.auth.models import User
from rest_framework import serializers
from apps.core.models import Habit, Log


class LogSerializer(serializers.HyperlinkedModelSerializer):
    # habit = serializers.ReadOnlyField(source="habit.title")

    class Meta:
        model = Log
        fields = ['url', 'id', 'date', 'score', 'habit']


class HabitSerializer(serializers.HyperlinkedModelSerializer):
    logs = serializers.HyperlinkedRelatedField(many=True, view_name='log-detail', read_only=True)
    owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Habit
        fields = ['url', 'id', 'owner', 'title', 'display_type', 'weekly_goal', 'logs']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # habits = serializers.HyperlinkedRelatedField(many=True, view_name='habit-detail', read_only=True)
    # habits = serializers.ReadOnlyField(source='habit.title')

    class Meta:
        model = User
        fields = ['url', 'id', 'habits']
        # fields = ['url', 'id']

