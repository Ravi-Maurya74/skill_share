from rest_framework import generics, permissions, authentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from skill_share.authentication import FirebaseAuthentication
from community.models import Skill
from community.serializers import (
    SkillSerializer,
    CommunitySerializer,
    CommunityListSerializer,
)

from community.services.community_service import CommunityService

community_service = CommunityService()


class SkillListCreateView(generics.ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    authentication_classes = [FirebaseAuthentication]


class CommunityListCreateView(APIView):
    authentication_classes = [FirebaseAuthentication]

    def post(self, request):
        data = request.data
        skill = Skill.objects.get(pk=data["skill"])
        community = community_service.create_new_community(
            community_name=data["community_name"], skill=skill, user=request.user
        )
        return Response(
            CommunitySerializer(community).data, status=status.HTTP_201_CREATED
        )

    def get(self, request):
        communities = community_service.get_all_communities()
        return Response(
            CommunityListSerializer(
                communities, many=True, context={"request": request}
            ).data,
            status=status.HTTP_200_OK,
        )
