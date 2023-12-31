from rest_framework.generics import DestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from user.serializers import UserSerializer
from user.models import User


class UserDestoryAPIView(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self):
        return self.current_user

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
