from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):

    queryset = Review.objects.all()

    serializer_class = ReviewSerializer

    permission_classes = [
        IsAuthenticated
    ]

    def perform_create(self, serializer):

        serializer.save(
            customer=self.request.user.customer_profile
        )