from user.models import User
from community_post.models import CommunityPost
from community_post.serializers import (CommunityPostSerializer,CommunityPostListSerializer, CommunityPostDetailSerializer)

class CommunityPostRepository:
    def create_new_community_post(self,data):
        serializer = CommunityPostSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data
    
    def get_all_community_posts(self,request):
        posts = CommunityPost.objects.all()
        serializer = CommunityPostListSerializer(posts,many=True,context={"request":request})
        return serializer.data
    
    def get_community_post(self,pk,request):
        post = CommunityPost.objects.get(pk=pk)
        serializer = CommunityPostDetailSerializer(post,context={"request":request})
        return serializer.data
    
    
