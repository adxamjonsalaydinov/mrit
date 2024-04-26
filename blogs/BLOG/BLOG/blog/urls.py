from django.urls import path
from .views import home, about, blog, contact, blog_detail, category_view

urlpatterns = [
    path('', home, name="home_page"),
    path('about/', about, name="about_page"),
    path("blog/", blog, name="blog_page"),
    path("contact/", contact, name="contact_page"),
    path('<int:id>/', blog_detail, name="blog_detail_page"),
    path("categories/<category>", category_view, name= "category_page"),
]