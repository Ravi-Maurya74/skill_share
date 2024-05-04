from django.urls import path
from chat import views

urlpatterns = [
    path("",views.ChatCreateView.as_view(),name="chat-user-view")
]