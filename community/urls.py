from django.urls import path
from community import views

urlpatterns = [
    path("skills/", views.SkillListCreateView.as_view(), name="skill-list-create"),
    path("", views.CommunityListCreateView.as_view(), name="community-list-create"),
]
