from django.urls import path
from . import views
from .views import PostViews,PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,UserPostViews

urlpatterns =[
    # path('', view=views.home, name='blog-home'),
    path('', view=PostViews.as_view(), name='blog-home'),
    path('user/<str:username>/', view=UserPostViews.as_view(), name='user-posts'),
    path('post/<int:pk>/', view=PostDetailView.as_view(), name='post-detail'),
    path('post/create/', view=PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', view=PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', view=PostDeleteView.as_view(), name='post-delete'),
    path('about/', view=views.about, name='blog-about'),

]

