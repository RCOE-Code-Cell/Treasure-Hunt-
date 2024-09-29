from rest_framework import serializers
from .models import Groups

class TotalGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['group_name']

class Round1SelectedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['group_name']

class Round1EliminatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['group_name']

class Round2SelectedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['group_name']

class Round2EliminatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['group_name']

class Round3SelectedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['group_name']

class Round3EliminatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['group_name']

class Round4SelectedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['group_name']

class Round4EliminatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['group_name']

class WinnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['group_name']
