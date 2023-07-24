from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Post"))


class Category(models.Model):
    """
    Adds a category field to
    the blog post
    """
    category_name = models.CharField(max_length=80)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    """
    Adds the structure of the Ink (post).
    Source from Code Institute:
    https://github.com/Code-Institute-Solutions/Django3blog/blob/master/11_messages/blog/models.py#:~:text=class%20Post(,.count()
    """
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField(
        'image', default=False) # Blank=True makes an image optional
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=False)
    likes = models.ManyToManyField(
        User, related_name='blog_likes', blank=True)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, default=1)


    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """
    Adds the structure of an Ink (post) comment.
    Source from Code Institute:
    https://github.com/Code-Institute-Solutions/Django3blog/blob/master/11_messages/blog/models.py#:~:text=class%20Comment(,name%7D%22
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"