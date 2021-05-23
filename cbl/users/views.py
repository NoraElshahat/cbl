from django.http import HttpResponse
from rest_framework import views, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from users.models import CblUser

from .serializers import StudenSerialiezer


class UsersView(views.APIView):

    def get(self, request):
        """
            getting all users
        """

        return Response('asdasd')

    def post(self, request):
        """
            posting info to users
        """

        return Response('post')


class StudentView(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = StudenSerialiezer
    queryset = CblUser.objects.filter(is_staff=False, is_super_admin=False, is_superuser=False)
    permission_classes = ()


