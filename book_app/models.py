from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length=200, unique=True)
  intro = models.TextField()
  body = models.TextField()
  posted = models.DateField(db_index=True, auto_now_add=True)
  author = models.ForeignKey(
          get_user_model(),
          on_delete=models.CASCADE,
          default=1,
          )

  def get_absolute_url(self):
    return reverse("book_app:blog_detail",kwargs={'pk':self.pk})

  def __str__(self):
    return self.title

class Comment(models.Model):
  blog = models.ForeignKey('book_app.Blog', related_name='comments',on_delete=models.CASCADE)
  author = models.ForeignKey(
          get_user_model(),
          on_delete=models.CASCADE,
          )
  text = models.TextField()

  def get_absolute_url(self):
    return reverse("blog_list")

  def __str__(self):
    return self.text
