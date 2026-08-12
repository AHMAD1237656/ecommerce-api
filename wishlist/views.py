from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Wishlist
from .serializers import WishlistSerializer


class WishlistViewSet(ModelViewSet):

    queryset = Wishlist.objects.all()

    serializer_class = WishlistSerializer

    permission_classes = [
        IsAuthenticated
    ]