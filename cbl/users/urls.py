from django.conf.urls import include
from users.views import StudentView, UsersView
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('list', StudentView)

app_name = 'users'


urlpatterns = [
    path('', UsersView.as_view()),
    path('students/', include(router.urls) ),
]

