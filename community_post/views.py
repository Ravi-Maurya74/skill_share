from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from skill_share.authentication import FirebaseAuthentication
from community_post.services.community_post_service import CommunityPostService
from community_post.repositories.community_post_repository import (
    CommunityPostRepository,
)

from user.models import User

communityPostService = CommunityPostService(repository=CommunityPostRepository())


class CommunityPostView(APIView):
    authentication_classes = [FirebaseAuthentication]

    def post(self, request):
        data = request.data
        data["user"] = request.user.pk
        return Response(
            communityPostService.create_new_community_post(data=data),
            status=status.HTTP_201_CREATED,
        )

    def get(self, request):
        return Response(
            communityPostService.get_all_community_posts(request=request),
            status=status.HTTP_200_OK,
        )


class CommunityPostDetailView(APIView):
    authentication_classes = [FirebaseAuthentication]

    def get(self, request, pk):
        return Response(communityPostService.get_community_post(pk=pk, request=request))
