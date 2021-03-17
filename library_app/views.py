from django.http import JsonResponse
from django.shortcuts import render
from .controllers import *
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def save_role_api(request):
    data = {
        'msg': 'Entered invalid data',
        'success': 'False'
    }
    try:
        data = save_role(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
def save_user_api(request):
    data = {
        'msg': 'Entered invalid data',
        'success': 'False'
    }
    try:
        data = save_user(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_details_api(request):
    ret_dict = {
        'msg': '',
        'success': False,
        'data': []
    }
    try:
        success, msg, data = get_user_details(request)
        ret_dict = {
            'msg': msg,
            'success': success,
            'data': data
        }
    except Exception as e:
        print(e.args)
    return Response(ret_dict, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_role_api(request):
    ret_dict = {
        'msg': 'Entered invalid data',
        'success': 'False',
        'data' : 'no data'
    }
    try:
        success,msg,data = get_role(request)
        ret_dict = {
            'msg': msg,
            'success': success,
            'data': data
        }
    except Exception as e:
        print(e.args)
    return Response(data=ret_dict, status=status.HTTP_200_OK)


@api_view(['POST'])
def save_book_api(request):
    data = {
        'msg': 'Entered invalid data',
        'success': 'False'
    }
    try:
        data = save_book(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_book_details_api(request):
    data = {
        'msg': 'Entered invalid data',
        'success': 'False',
        'data' : []
    }
    try:
        data = get_book_details(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
def issue_book_api(request):
    data = {
        'success': False,
        'msg': 'Book not issues',
        'data': []
    }
    try:
        data = issue_book(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_issued_books_api(request):
    ret_dict = {
        'msg': 'Entered invalid data',
        'success': 'False',
        'data': []
    }
    try:
        success,msg,data = get_issued_books(request)
        ret_dict = {
            'msg': msg,
            'success': success,
            'data': data
        }
    except Exception as e:
        print(e.args)
    return Response(data=ret_dict, status=status.HTTP_200_OK)


@api_view(['POST'])
def activity_start_api(request):
    data = {
        'success': False,
        'msg': 'No start activity logged',
    }
    try:
        data = activity_start(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
def activity_end_api(request):
    data = {
        'success': False,
        'msg': 'No end activity logged',
    }
    try:
        data = activity_end(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_activity_details_api(request):
    data = {
        'ok': False,
        'members': []
    }
    try:
        data = get_user_activity_details(request)
    except Exception as e:
        print(e.args)
    return Response(data=data, status=status.HTTP_200_OK)