from typing import Any
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from django.views import generic
from django.contrib import messages

from main.forms import ContactForm
from main.models import (
    Skill, Blog, Certificate,
    ContactProfile,Media,PortFolio,
    Testimonial, UserProfile
)




class IndexView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs: Any):


        context =  super().get_context_data(**kwargs)

        testimonials = Testimonial.objects.filter(is_active = True)
        certificates = Certificate.objects.filter(is_active = True)
        blogs = Blog.objects.filter(is_active = True)
        portfolio = PortFolio.objects.filter(is_active = True)

        context['testimonials'] = testimonials
        context['certificates'] = certificates
        context['blogs'] = blogs
        context['portfolio'] = portfolio

        return context


class ContactView(generic.FormView):


    template_name = 'contact.html'
    success_url = '/'
    form_class = ContactForm

    def form_valid(self, form: Any) -> HttpResponse:
        
        
        form.save()
        messages.success(self.request, "Thank you. We Will Be in  touch soon")
        return super().form_valid(form)


class PortFolioListView(generic.ListView):


    model = PortFolio
    template_name = 'portfolio.html'
    paginate_by = 10


    def get_queryset(self):
        return super().get_queryset().filter(is_active = True)


class PortFolioDetailView(generic.DetailView):


    model = PortFolio
    template_name = 'portfolio-detail.html'



class BlogListView(generic.ListView):


    model = Blog
    template_name = 'blog.html'
    paginate_by = 10


    def get_queryset(self):

        return super().get_queryset().filter(is_active = True)


class PortFolioDetailView(generic.DetailView):


    model = Blog
    template_name = 'blog-detail.html'

