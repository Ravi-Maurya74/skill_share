from community.repositories.community_repository import CommunityRepository


class CommunityService:
    def __init__(self):
        self.community_repository = CommunityRepository()

    def create_new_community(self, community_name, skill, user):
        community = self.community_repository.create_new_community(community_name, skill)
        self.community_repository.add_members_to_community(community.name, [user])
        self.community_repository.make_admin(community, user)
        return community
    
    def add_members_to_community(self, community_name, members):
        return self.community_repository.add_members_to_community(community_name, members)
    
    def make_admin(self, community_name, user):
        return self.community_repository.make_admin(community_name, user)
    
    def get_all_communities(self):
        return self.community_repository.get_all_communities()
    
