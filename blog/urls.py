from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('new_ink/', views.AddInkPost.as_view(), name='create_ink'),
    path('like/<slug:slug>', views.InkLike.as_view(), name='inkpost_like'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    
]