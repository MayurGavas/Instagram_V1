from django.db import models
from users.models import TimeStamp, UserProfile


# Create your models here.


class UserPost(TimeStamp):
    caption_text = models.CharField(max_length=255, null = True)
    # tODO: Store lat long instead of string
    location = models.CharField(max_length=255,null = True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='post')

    is_published = models.BooleanField(default=False)


class PostMedia(TimeStamp):

    def media_name(instance, filename):
        ext = filename.split(".")[-1]
        # TODO : Implement a UUID instead of integer post_id
        return f'post_media/{instance.post.id}_{instance.sequence_index}.{ext}'


    # TODO :Limit this field to accept files of a certain type and size : Hint- Validator attribute
    media_file = models.FileField(upload_to='post_media/')
    sequence_index = models.PositiveSmallIntegerField(default=0)
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name='media')

    class Meta:
        unique_together = ('sequence_index', 'post',)
