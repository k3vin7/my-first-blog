from rest_framework import viewsets
from rest_framework.routers import DefaultRouter
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_date')
    serializer_class = PostSerializer


router = DefaultRouter()
router.register(r'Post', PostViewSet, basename='post')
