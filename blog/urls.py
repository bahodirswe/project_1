from django.urls import path
from blog import views

app_name = "blog"

urlpatterns = [
    path('', views.home,name="home"),
    path('search/<str:query>/', views.search,name="search"),
    path('post-detail/<int:id>/', views.post_detail, name='post_detail'),
    path('post-create/', views.post_create, name="post_create"),
    path('post-update/<int:id>/', views.post_update, name="post_update"),
    path('post-delate/<int:id>/', views.post_delate, name="post_delate"),
    
   
]