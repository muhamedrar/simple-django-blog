from django.urls import path
from . import views
from .views import PostViews

urlpatterns =[
    # path('', view=views.home, name='blog-home'),
    path('', view=PostViews.as_view(), name='blog-home'),
    path('about/', view=views.about, name='blog-about'),

]