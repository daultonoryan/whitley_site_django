from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=150, default="")
    slug = models.SlugField(max_length=150)
    body = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True, blank=True)
    modified = models.DateField(db_index=True, auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_blog_post', args=(self.slug,))
