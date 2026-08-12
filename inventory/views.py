from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Inventory
from .serializers import InventorySerializer


class InventoryViewSet(ModelViewSet):

    queryset = Inventory.objects.all()

    serializer_class = InventorySerializer

    permission_classes = [
        IsAuthenticated
    ]