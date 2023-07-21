from rest_framework import routers
from warehouse.api.v1.views import TaskViewSet

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = router.urls