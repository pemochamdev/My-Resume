from django.contrib import admin

# Register your models here.

from main.models import (
    Skill, UserProfile,ContactProfile,
    Testimonial, Media, PortFolio, 
    Blog, Certificate
)

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'score', 'is_key_skill')



@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title')


@admin.register(ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'timestamp')



@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'role', 'quote', 'is_active']



@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    

    list_display = ('id', 'name', 'url', 'is_image')



@admin.register(PortFolio)
class PortFolioAdmin(admin.ModelAdmin):
    

    list_display = ('id', 'date', 'name', 'is_active')
    prepopulated_fields = {'slug':('name',)}



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):


    list_display = ('id', 'timestamp', 'author', 'name')
    prepopulated_fields = {'slug':('name',)}


@admin.register(Certificate)    
class CertificateAdmin(admin.ModelAdmin):   
    
    list_display = ('id', 'date', 'author', 'name')