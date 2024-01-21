from django.db import models

# Create your models here.

from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Skill(models.Model):


    name = models.CharField(max_length=200, blank=True, null = True)
    score = models.IntegerField(default = 80, blank=True, null = True)
    image = models.FileField(upload_to='skills', blank=True, null = True)
    is_key_skill = models.BooleanField()

    def __str__(self):
        return self.name
    

    class Meta:


        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'


class UserProfile(models.Model):


    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name  = 'profile')
    title = models.CharField(max_length=200, blank=True, null = True)
    avatar = models.ImageField(blank=True, null = True, upload_to='profile')
    skills = models.ForeignKey(Skill, on_delete = models.CASCADE, related_name  = 'skill')
    cv = models.FileField(upload_to='CV', blank=True, null = True)


    def __str__(self):
        return str(self.user.username)
    
    
    class Meta:
      
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'


class ContactProfile(models.Model):

    timestamp = models.DateTimeField(auto_now_add = True)
    name = models.ForeignKey(User, on_delete = models.CASCADE)
    email = models.EmailField()
    message = RichTextField()


    def __str__(self):
        return self.name
    

    class Meta:
        
        verbose_name = 'Contact Profile'
        verbose_name_plural = 'Contact Profiles'
    

class Testimonial(models.Model):


    thumbnail = models.ImageField(blank=True, null = True, upload_to='Testimonial')
    name = models.CharField(max_length=200, blank=True, null = True)
    role = models.CharField(max_length=200, blank=True, null = True)
    quote = models.CharField(max_length=200, blank=True, null = True)

    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name
    

    class Meta:
       
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
    


class Media(models.Model):


    image = models.ImageField(blank=True, null = True, upload_to='Media')
    name = models.CharField(max_length=200, blank=True, null = True)
    url = models.URLField(blank=True, null = True)

    is_image = models.BooleanField(default = True)


    def __str__(self):
        return self.name
    
    
    class Meta:
       
        verbose_name = 'Media'
        verbose_name_plural = 'Medias'
        ordering = ['name']
    
    def save(self, *args, **kwargs):
        if self.url:
            self.is_image = False
        
        super(Media, self).save(*args, **kwargs)


class PortFolio(models.Model):

    date = models.DateTimeField(null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null = True)
    description = models.CharField(max_length=500, blank=True, null = True)
    body = RichTextField(blank=True, null = True)   
    image = models.ImageField(blank=True, null = True, upload_to='PortFolio')
    slug = models.SlugField()
    is_activate = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.slug:
            self.slug = slugify(self.name)
        
        super(PortFolio, self).save(*args, **kwargs)


    def __str__(self):
        return self.name
    

    class Meta:
      
        verbose_name = 'PortFolio'
        verbose_name_plural = 'PortFolio'
        ordering = ['date']
    

    def get_absolute_url(self):
        return reverse("porfolio", kwargs={"slug": self.slug})


class Blog(models.Model):

    timestamp = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog')
    name = models.CharField(max_length=200, blank=True, null = True)
    body = RichTextField(blank=True, null = True)   
    image = models.ImageField(blank=True, null = True, upload_to='blog')
    slug = models.SlugField()
    is_activate = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        
        super(Blog, self).save(*args, **kwargs)


    def __str__(self):
        return self.name
    

    class Meta:
      
        verbose_name = 'Blog'
        verbose_name_plural = 'Blog'
        ordering = ['timestamp']
    

    def get_absolute_url(self):
        return reverse("blog", kwargs={"slug": self.slug})



class Certificate(models.Model):

    date = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog')
    name = models.CharField(max_length=200, blank=True, null = True)
    title = models.CharField(max_length=200, blank=True, null = True)
    description = models.CharField(max_length=500, blank=True, null = True)
    is_activate = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

    class Meta:
      
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'
        ordering = ['date']
    

    def get_absolute_url(self):
        return reverse("certificate", kwargs={"name": self.name})