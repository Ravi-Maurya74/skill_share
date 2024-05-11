from django.urls import path
from community_post import views

urlpatterns = [
    path("", views.CommunityPostView.as_view(), name="community-post-view"),
    path("<int:pk>/", views.CommunityPostDetailView.as_view(), name="community-detail-view"),
    path("<int:pk>/comments/", views.CommunityPostCommentView.as_view(), name="community-comment-view"),
]
