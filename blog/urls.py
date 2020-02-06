from django.urls import path

from . import views as blog_views

urlpatterns = [
    path('', blog_views.all_blogs, name='all_blogs'),
]