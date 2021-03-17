from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from .serializers import *
from datetime import timedelta
import datetime
from .models import *


def save_role(request):
    msg = 'not able to save role'
    success = False
    try:
        post_data = request.data
        create_list = []

        role_count = Role.objects.filter(name__in= post_data).count()
        if role_count== 0:
            for role_name in post_data:
                role = Role()
                role.name = role_name
                create_list.append(role)
            Role.objects.bulk_create(create_list)
            msg = 'Data saved successfully'
            success = True
        else:
            msg = 'Duplicate data'
    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg}


def save_user(request):
    msg = 'not able to save data'
    success = False
    try:
        post_data = request.POST

        if post_data['password'] == post_data['confirm_password']:
            if post_data.get('id'):
                user_data = User.objects.get(id = post_data.get('id'))
                user_data.first_name = post_data.get('firstName')
                user_data.last_name = post_data.get('lastName')
                profile = Profile.objects.get(user_id = post_data.get('id'))
            else:
                user_data = User()
                user_data.email = post_data.get('email')
                user_data.username = post_data.get('email')
                user_data.set_password(post_data.get('password'))
                profile = Profile()
                msg = 'Data saved successfully'
                success = True
            user_data.first_name = post_data.get('firstName')
            user_data.last_name = post_data.get('lastName')
            user_data.save()
            if not post_data.get('id'):
                profile.user_id = user_data.id
                profile.role_id = post_data['role_id']
            profile.phone = post_data.get('phone_no')
            profile.save()
    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg}


def get_user_details(request):
    msg = 'not able to save data'
    success = False
    user_data = []
    try:
        user_obj = Profile.objects.filter()
        serializer = GetUserDataSerializers(user_obj, many=True)
        user_data = serializer.data
        success = True
        msg = 'Success in getting user details.'
    except Exception as e:
        print(e.args)
    return success, msg, user_data


def get_role(request):
    msg = 'not able to save data'
    success = False
    role_data = []
    try:
        role_obj = Role.objects.filter()
        serializer = GetRoleDataSerializers(role_obj, many=True)
        role_data = serializer.data
        success = True
        msg = 'Success in getting user details.'
    except Exception as e:
        print(e.args)
    return success, msg, role_data


def save_book(request):
    msg = 'not able to save book'
    success = False
    try:
        post_data = request.data
        book_obj = Books()
        book_obj.title = post_data.get('title')
        book_obj.description = post_data.get('description')
        book_obj.author_id = save_get_author(post_data.get('author'))
        book_obj.save()
        success = True
        msg = 'data saved'
    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg}


def save_get_author(author_name):
    author_id = None
    try:
        author = Author.objects.filter(name__iexact=author_name)
        if not author:
            author = Author()
            author.name = author_name
            author.save()
        else:
            author = author[0]
        author_id = author.id
    except Exception as e:
        print(e.args)
    return author_id


def get_book_details(request):
    data = []
    success = False
    msg = 'data not able to fetched'
    try:
        book_obj = Books.objects.filter()
        serialise = GetBookDetailsSerializer(book_obj, many=True)
        data = serialise.data
        success = True
        msg = 'data fetched'

    except Exception as e:
        print(e.args)
    return {'success':success,'msg':msg,'data':data}


def issue_book(request):
    success = False
    msg = 'data not saved'
    try:
        post_data = request.data
        issue_obj = BookIssue()
        issue_obj.user_id = post_data.get('user_id')
        issue_obj.book_id = post_data.get('book_id')

        issue_obj.return_date = datetime.date.today() + timedelta(days=7)
        issue_obj.save()
        success = True
        msg = 'data saved successfully'

    except Exception as e:
        print(e.args)
    return {'success':success, 'msg':msg}


def get_issued_books(request):
    success = False
    msg = 'data not saved'
    data =[]
    try:
        # way 1
        # if request.GET.get('id'):
        #     issued_obj = BookIssue.objects.filter(user_id = request.GET.get('id'))
        # else:
        #     issued_obj = BookIssue.objects.filter()

        # way 2
        search_filter = Q()
        if request.GET.get('id'):
            search_filter = Q(user_id = request.GET.get('id'))
        issued_obj = BookIssue.objects.filter(search_filter)

        serializer = GetIssuedBookSerializer(issued_obj, many=True)
        data = serializer.data
        success = True
        msg = 'data fetched'

    except Exception as e:
        print(e.args)
    return success,msg,data


def activity_start(request):
    success = False
    msg = 'activity not saved'
    try:
        post_data = request.POST
        username = post_data.get('username')
        password = post_data.get('password')
        tz = post_data.get('tz')
        user = authenticate(username=username, password=password)
        activity_obj = ActivityPeriod.objects.filter(user_id=user.id, end_time__isnull = True)
        if user and not activity_obj:
            activity = ActivityPeriod()
            activity.user_id = user.id
            activity.tz = tz
            activity.start_time = datetime.datetime.now()
            activity.save()
            msg = 'data saved successfully'
        else:
            msg = 'user is already logged in !!'
        success = True

    except Exception as e:
        print(e.args)
    return {'success':success, 'msg':msg}


def activity_end(request):
    success = False
    msg = 'activity not ended'
    try:
        post_date = request.POST
        user_id = post_date.get('id')
        activity_obj = ActivityPeriod.objects.filter(user_id=user_id, start_time__isnull=False, end_time__isnull = True)

        if activity_obj:
            activity_obj = activity_obj[0]
            activity_obj.end_time = datetime.datetime.now()
            activity_obj.save()
            msg = 'User logged out'
        else:
            msg = 'user is not logged in'
        success = True
    except Exception as e:
        print(e.args)
    return {'success': success, 'msg': msg}


def get_user_activity_details(request):
    ok = False
    members = []
    try:
        get_data = request.GET
        if get_data.get('id'):
            search_filter = Q(id = get_data.get('id'))
            user_obj = User.objects.filter(search_filter)
        else:
            user_obj = User.objects.filter()
        serializer = GetUserActivityDetailsSerializer(user_obj, many=True)
        members = serializer.data
        ok = True

    except Exception as e:
        print(e.args)
    return {'ok':ok, 'members': members}