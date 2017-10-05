from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models
from django.template.defaultfilters import slugify


class BlogPost(models.Model):
    post_title = models.CharField(max_length=150)
    publish_date = models.DateTimeField(verbose_name=None, name=None, auto_now_add=True)
    content = models.TextField()
    feature_image = models.CharField(max_length=200, default='none')
    hooker = models.TextField()
    #slug = models.SlugField(unique=True, default=None)

    def __str__(self):
        return self.post_title

    @models.permalink
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    #def save(self, *args, **kwargs):
    #    if not self.slug:
    #        self.slug = slugify(self.title)
    #    super(BlogPost, self).save(*args, **kwargs)


    def get_comment_count(self):
        return self.comments.filter(post=self).count()


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments')
    commenter = models.CharField(max_length=80)
    comment_content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content





