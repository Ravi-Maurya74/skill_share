from user.models import User 
from community.models import Skill,Community,Badge,Session,Membership

class CommunityRepository:
    def create_new_community(self,name,skill):
        return Community.objects.create(name = name,skill = skill)
    
    # here is_admin data can also be passed
    def add_members_to_community(self,name,members):
        community = Community.objects.get(pk = name)
        community.members.add(*members)
        return community
    
    def make_admin(self,community,user):
        membership = Membership.objects.get(user = user,community = community)
        membership.is_admin = True
        membership.save()
        return membership
    
    def create_new_badge(self,data):
        return Badge.objects.create(**data)
    
    def update_badge_level(self,user,skill,dec = False):
        if Badge.objects.get(user = user,skill = skill) is not None:
            badge = Badge.objects.get(user = user,skill = skill)
            if dec:
                badge.level = max(0,badge.level-1)
            else:
                badge.level = badge.level+1
            badge.save()
            return badge
      
    def create_new_session_for_community(self,data):
        return Session.objects.create(**data)
    
    def get_all_communities(self):
        return Community.objects.all()
    
    # def plan_sessions(self,community,date,description):
    #     session = Session.objects.get(community = community)




    
    
    