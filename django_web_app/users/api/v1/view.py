from rest_framework.viewsets import ModelViewSet
from users.models import Profile
from .serializer import ProfileSerializer


class UserApiView(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.author)