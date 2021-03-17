from rest_framework import serializers
from django.contrib.auth.models import User
from.models import *


class GetUserDataSerializers(serializers.ModelSerializer):
    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')
    email = serializers.CharField(source='user.email')
    role = serializers.CharField(source='role.name')

    class Meta:
        model = Profile
        fields = ('id','phone','first_name','last_name','email','role')


class GetRoleDataSerializers(serializers.ModelSerializer):

    class Meta:
        model = Role
        fields = ('__all__')


class GetBookDetailsSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name')

    class Meta:
        model = Books
        fields = ('__all__')


class GetIssuedBookSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username')
    book_title = serializers.CharField(source='book.title')
    book_author = serializers.CharField(source='book.author.name')

    class Meta:
        model = BookIssue
        fields = ('id','user_name','book_title','book_author','issue_date','return_date')


class GetUserActivityDetailsSerializer(serializers.ModelSerializer):
    activity_period = serializers.SerializerMethodField()
    tz = serializers.SerializerMethodField()

    def get_activity_period(self, obj):
        activity_obj = ActivityPeriod.objects.filter(user_id = obj.id)
        return GetActivitySerializer(activity_obj,many=True).data

    def get_tz(self, obj):
        activity_obj = ActivityPeriod.objects.filter(user_id = obj.id)
        if activity_obj:
            return activity_obj[0].tz
        else:
            return "NA"

    class Meta:
        model = User
        fields = ('id', 'username', 'tz', 'activity_period')


class GetActivitySerializer(serializers.ModelSerializer):
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    # way 1
    def get_start_time(self, obj):

        h = int(obj.start_time.strftime("%H"))
        if h>12:
            H = h-12
            return obj.start_time.strftime("%b %d,%Y "+str(H)+":%M:%S PM")
        else:
            return obj.start_time.strftime("%b %d,%Y %H:%M:%S AM")

    # way 2
    def get_end_time(self, obj):
        return obj.end_time.strftime("%b %d,%Y %H:%M:%S")

    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')
