from django.contrib import admin
from django.urls import path
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from user.api import UserViewSet
from blog.api import CategoryViewSet, PostViewSet, CommentViewSet, TrendViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'trends', TrendViewSet)

urlpatterns = [
    path('', include("blog.urls", namespace="blog")),
    path('admin/', admin.site.urls),
    path('blog', include("blog.urls", namespace="blog")),
    path('user/', include("user.urls", namespace="user")),
    path('api/v1/', include(router.urls)),
    path('api/v2/', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)