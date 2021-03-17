from django.urls import path
from . import views

urlpatterns = [
    path(r'save_user/', views.save_user_api, name='save_user'),
    path(r'save_role/', views.save_role_api, name='save_user'),
    path(r'get_user_details/', views.get_user_details_api, name='save_user'),
    path(r'get_role/', views.get_role_api, name='get_role'),
    path(r'save_book/', views.save_book_api, name='save_book'),
    path(r'get_book_details/', views.get_book_details_api, name='get_book_details'),
    path(r'issue_book/', views.issue_book_api, name='issue_book'),
    path(r'get_issued_books/', views.get_issued_books_api, name='get_issues_book'),
    path(r'activity_start/', views.activity_start_api, name='activity_start'),
    path(r'activity_end/', views.activity_end_api, name='activity_end'),
    path(r'get_user_activity_details/', views.get_user_activity_details_api, name='get_user_activity_details'),
]