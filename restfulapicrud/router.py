from user.viewsets import EmployeeViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user',EmployeeViewset)

# localhost:p/api/user/5
# GET, POST, PUT, DELETE
# list , retrive