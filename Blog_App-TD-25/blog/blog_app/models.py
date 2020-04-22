from django.db import models
from django.shortcuts import reverse

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts:post_details', kwargs={'pk':self.pk}) #3rd method first two mentioned in html page
        # return "post/details/%s/" %(self.pk)

    

