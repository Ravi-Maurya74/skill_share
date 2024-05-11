from django.urls import path
from community_post import views

urlpatterns = [path("", views.CommunityPostView.as_view(), name="community-post-view")]
urlpatterns = [path("<int:pk>/", views.CommunityPostDetailView.as_view(), name="community-detail-view")]