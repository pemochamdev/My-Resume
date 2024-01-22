from django.urls import path

from main import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("portfolio/", views.PortFolioListView.as_view(), name="list-portfolio"),
    path("portfolio/<slug>/", views.PortFolioDetailView.as_view(), name="detail-portfolio"),
    path("blog/", views.BlogListView.as_view(), name="list-blog"),
    path("blog/<slug>/", views.BloglioDetailView.as_view(), name="detail-blog"),
]
