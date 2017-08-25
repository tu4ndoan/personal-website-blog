from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


class BlogPost(models.Model):
    post_title = models.CharField(max_length=150)
    publish_date = models.DateTimeField(verbose_name=None, name=None, auto_now_add=True)
    content = models.TextField()
    feature_image = models.ImageField(upload_to='./static/blog/images/')
    hooker = models.TextField()

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.post_title + ' - ' + self.content


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments')
    name = models.CharField(max_length=80)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text




