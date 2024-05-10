from django.db import models


class CommunityPost(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    community = models.ForeignKey("community.Community", on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__original_image = self.image

    def save(self, *args, **kwargs):
        old_image = self.__original_image
        super().save(*args, **kwargs)
        if old_image != self.image:
            old_image.delete(save=False)
        self.__original_image = self.image

    def delete(self, *args, **kwargs):
        self.image.delete(save=False)  # delete image file from S3
        super().delete(*args, **kwargs)  # delete Post object
