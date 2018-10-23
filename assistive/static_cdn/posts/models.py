from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify
import datetime

#from taggit.managers import TaggableManage
#ssfrom taggit.managers import TaggableManager
#import tagulous 
# Create your models here.
# MVC MODEL VIEW CONTROLLER


#Post.objects.all().published()
#Post.objects.create(user=user, title="Some time")

class PostQuerySet(models.query.QuerySet):
    def not_draft(self):
        return self.filter(draft=False)
    
    def published(self):
        return self.filter(publish__lte=timezone.now()).not_draft()

class PostManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return PostQuerySet(self.model, using=self._db)
            
    def active(self, *args, **kwargs):
        # Post.objects.all() = super(PostManager, self).all()
        return self.get_queryset().published()


def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    PostModel = instance.__class__
    if not PostModel.objects.exists():
        new_id=1
    else:
        new_id = PostModel.objects.order_by("id").last().id + 1

   # print "-----------------"+str(PostModel.objects.order_by("id").last().id + 1)
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object, 
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(new_id, filename)

class Tag(models.Model):
    word        = models.CharField(max_length=35)
    slug        = models.CharField(max_length=250)
    created_at  = models.DateTimeField(auto_now_add=False)

    def __unicode__(self):
        return self.word

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=upload_location, 
            null=True, 
            blank=True, 
            width_field="width_field", 
            height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField(max_length=3050)
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    #tags = models.ManyToManyField(Tag,related_name='photos')
    tags=models.CharField(max_length=30,default='')
   # tags = tagulous.models.TagField(max_length=5)
    objects = PostManager()

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]
       
#    @property
#    def title(self):
#        return "Title"


def u_loc(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    PostModel = instance.__class__
    if PostModel.objects==None:
        print "yoyoyoyoyoyoyo"
        new_id2=1
    else:
        new_id2=PostModel.objects.order_by("id").last().id + 1

    #print "-----------------"+(PostModel.objects.order_by("id").last().id + 1)
    #new_id = PostModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object, 
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(new_id2, filename)


# class Board(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
#     title = models.CharField(max_length=30)
#     slug = models.SlugField(unique=True)
#     image = models.ImageField(upload_to=u_loc, 
#             null=True, 
#             blank=True, 
#             width_field="width_field", 
#             height_field="height_field")
#     height_field = models.IntegerField(default=0)
#     width_field = models.IntegerField(default=0)
#     content = models.TextField(max_length=150)
#     draft = models.BooleanField(default=False)
#     publish = models.DateField(auto_now=False, auto_now_add=False)
#     updated = models.DateTimeField(auto_now=True, auto_now_add=False)
#     timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

#     #tags = models.ManyToManyField(Tag,related_name='photos')

#    # tags = tagulous.models.TagField(max_length=5)
#     objects = PostManager()

#     def __unicode__(self):
#         return self.title

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse("posts:detail", kwargs={"slug": self.slug})

#     class Meta:
#         ordering = ["-timestamp", "-updated"]


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


'''
unique_slug_generator from Django Code Review #2 on joincfe.com/youtube/
'''
from .utils import unique_slug_generator

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        # instance.slug = create_slug(instance)
        instance.slug = unique_slug_generator(instance)



pre_save.connect(pre_save_post_receiver, sender=Post)










