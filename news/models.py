from email.mime import image
from email.policy import default
from django.db import models
from django.conf import settings
from datetime import datetime
from django.core.files.base import ContentFile
import os
from PIL import Image
from io import BytesIO
# Create your models here.
User = settings.AUTH_USER_MODEL
class UserInformation(models.Model):
    profile = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    bio = models.CharField(max_length=250)
    profile_image = models.ImageField(upload_to="profile_images/", null=True, blank=True)
class Likes(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    like = models.BooleanField(default=False)
class Commentaries(models.Model):
    class Meta:
        ordering = ['-date']

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    date = models.DateTimeField(datetime.now(), null=True)
    text = models.TextField(blank=False, null=True)

class News(models.Model) :
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    article = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    commentary = models.ManyToManyField(Commentaries)
    likes = models.ManyToManyField(Likes)
    image = models.ImageField(upload_to="news_images/", default="news_images/default.webp", null=True, blank=True)
    image_thumbnail = models.ImageField(upload_to="news_images/", default="news_images/news_images_thumb.webp",  null=True, blank=True)
    def __str__(self) :
        return self.article
    def get_likes(self):
        print(self.likes.count())
        return self.likes.count()
    def get_image_name(self) :
        return self.image.name if self.image else False
    def save(self, *args, **kwargs):
        self.make_thumbnail()
        super(News, self).save(*args, **kwargs)
    def make_thumbnail(self):
        image = Image.open(self.image)
        image.thumbnail((400, 400), Image.ANTIALIAS)
        print(self.image.name)
        thumb_name, thumb_extension = os.path.splitext(self.image.name)
        thumb_extension = thumb_extension.lower()
        thumb_filename = thumb_name.split("/")[0] + "_thumb" + thumb_extension
        if "default" in thumb_name :
            return
        if thumb_extension in [".jpg", ".jpeg"]:
            FILE_TYPE = "JPEG"
        elif thumb_extension == ".gif" :
            FILE_TYPE = "GIF"
        elif thumb_extension == ".png" :
            FILE_TYPE = "PNG"
        elif thumb_extension == ".webp" :
            FILE_TYPE = "WEBP"
        temp_thumb = BytesIO()
        image.save(temp_thumb, FILE_TYPE)
        temp_thumb.seek(0)
        self.image_thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()
    
