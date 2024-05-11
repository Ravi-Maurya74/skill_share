from community_post.models import CommunityPost

from community_post.repositories.community_post_repository import (
    CommunityPostRepository,
)


class CommunityPostService:
    def __init__(self, repository: CommunityPostRepository) -> None:
        self.repository = repository

    def create_new_community_post(self, data):
        return self.repository.create_new_community_post(data=data)

    def get_all_community_posts(self, request):
        return self.repository.get_all_community_posts(request=request)

    def get_community_post(self, pk, request):
        return self.repository.get_community_post(pk=pk, request=request)

    def get_community_post_comments(self, post_pk, request):
        return self.repository.get_community_post_comments(
            post_pk=post_pk, request=request
        )
