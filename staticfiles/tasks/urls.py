
from django.urls import path
from tasks.views import PersonasViewset, getRoutes, MyTokenObtainPairView
from rest_framework import routers

from rest_framework_simplejwt.views import (
   TokenRefreshView
)

TaskRouter = routers.DefaultRouter()
TaskRouter.register(r'person', PersonasViewset)


urlpatterns =[
   path("",getRoutes),
   path('token/',MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('token/refresh/',TokenRefreshView.as_view(), name='token_refresh')
]


from django.urls import URLPattern, path
from tasks.views import PersonasViewset
from rest_framework import routers
TaskRouter = routers.DefaultRouter()
TaskRouter.register(r'person', PersonasViewset)


