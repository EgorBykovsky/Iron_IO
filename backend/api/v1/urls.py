from django.urls import path
from .views import Session_Api, Chat_API, Add_user_to_session_api

urlpatterns = [
    path('session/', Session_Api.as_view()),
    path('chat/', Chat_API.as_view()),
    path('users/', Add_user_to_session_api.as_view()),
]