from django.db import models
from django.utils import timezone
from django.utils.html import strip_tags
from django.urls import reverse
# Create your models here.
class  Post(models.Model): #class for the Blog Post fucntions in Blog Webapp
    author=models.ForeignKey('auth.User',on_delete=models.CASCADE) #only authorized super user can post
    title=models.CharField(max_length=200,)  #title for the Post
    text=models.TextField()  #Text that the user is going to Post
    created_date=models.DateTimeField(default=timezone.now) #the date when the post is created
    published_date=models.DateTimeField(blank=True,null=True)  #the date on which the post is gonna be published

    def publish(self):
        self.published_date=timezone.now() #when we click on publish the publish date is set to timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)  # only post the Approved Comments one the blog

    def get_absolute_url(self): #method which will come into action after we write a post
        return reverse("post_detail",kwargs={'pk':self.pk }) #goes to the post_detail view which will have details about the post and we pass the primary key as post that is just created

    def __str__(self):
        return self.title



class Comment(models.Model):
    post=models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE) # each comment is connected to the post on the blog page
    author=models.CharField(max_length=200) #anyone visiting the site can type a comment
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    approved_comment=models.BooleanField(default=False) #by the default the comment is not approved

    def approve(self):
        self.approved_comment=True
        self.save()


    def get_absolute_url(self):
        return reverse("post_list") #post list the view having all the post and it will work as a homepage

    def __str__(self):
        return strip_tags(self.text)
