from apps.accounts.models import User
from rest_framework import serializers
from apps.core.models import Habit, Log


class LogSerializer(serializers.ModelSerializer):
    # date = serializers.DateTimeField()
    # score = serializers.IntegerField()
    class Meta:
        model = Log
        fields = ['date', 'score']


class HabitSerializer(serializers.ModelSerializer):
    logs = LogSerializer(many=True)

    class Meta:
        model = Habit
        fields = ["title", "display_type", "weekly_goal", "daily_goal", "logs"]


class UserSerializer(serializers.ModelSerializer):
    habits = HabitSerializer(many=True)

    class Meta:
        model = User
        fields = ["habits"]

# class LogSerializer(serializers.HyperlinkedModelSerializer):
#     # habit = serializers.ReadOnlyField(source="habit.title")
#
#     class Meta:
#         model = Log
#         fields = ['url', 'id', 'date', 'score', 'habit']


# class HabitSerializer(serializers.HyperlinkedModelSerializer):
#     logs = serializers.HyperlinkedRelatedField(many=True, view_name='log-detail', read_only=True)
#     owner = serializers.HyperlinkedRelatedField(view_name='user-detail', read_only=True)
#     # owner = serializers.ReadOnlyField(source='owner.username')
#
#     class Meta:
#         model = Habit
#         fields = ['url', 'id', 'owner', 'title', 'display_type', 'weekly_goal', 'logs']


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     habits = serializers.HyperlinkedRelatedField(many=True, view_name='habit-detail', read_only=True)
#     # logs = LogSerializer()
#     # habits = serializers.ReadOnlyField(source='habit.title')
#
#     class Meta:
#         model = User
#         fields = ['habits']
#         # fields = ['url', 'id']

