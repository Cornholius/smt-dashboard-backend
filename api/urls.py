from rest_framework import routers
from .views import PostViewSet, TagViewSet

router = routers.DefaultRouter()
router.register('api/posts', PostViewSet, 'post')
router.register('api/tags', TagViewSet, 'tag')

urlpatterns = router.urls
