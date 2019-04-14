from django.urls import path,include
from . import views

app_name='book_app'

urlpatterns = [
  path('',views.IndexView.as_view(),name='index'),
  path('blog/',views.BlogListView.as_view(),name='blog_list'),
  path('blog/<int:pk>',views.BlogDetailView.as_view(),name='blog_detail'),
  path('blog/<int:pk>/comment/', views.add_comment_to_post,name='add_comment_to_post'),
  path('blog/new/', views.CreatePostView.as_view(),name='post_new'),
  path('blog/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
  path('blog/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
  path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]


