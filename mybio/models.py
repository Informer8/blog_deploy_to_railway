from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import now

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Category(models.Model):
    name=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title=models.CharField(max_length=255)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    slug=models.CharField(max_length=130, unique=True)
    content=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField('Image', upload_to="media", blank=True, null=True)
    dateTime=models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    def __str__(self):
        return self.title

    @property
    def image_url(self):
        return '%s%s' % (settings.HOST, self.image.url) if self.image else ''

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length = 255)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

class Contact(models.Model):
    name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 255)
    address = models.CharField(max_length = 255)
    company = models.CharField(max_length = 255)
    message = models.TextField()
    date    = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return '%s' % (self.name)
