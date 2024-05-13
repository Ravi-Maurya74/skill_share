from django.db import models


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


# can a community have many skills ?
class Community(models.Model):
    name = models.CharField(max_length=255, primary_key=True)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    members = models.ManyToManyField("user.User", through="Membership")

    def __str__(self) -> str:
        return f"{self.name} - {self.skill}"


class Membership(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)


class Badge(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.IntegerField()


# date can be scheduled so not auto_now
class Session(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True)
    description = models.TextField(blank=True)


class Feedback(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comments = models.TextField()


# not for specific skill
class TimeBank(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    hours_spent = models.IntegerField()
    # can add skill if specific


# why is community not many to many here
class Project(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    members = models.ManyToManyField("user.User")
    description = models.TextField()
