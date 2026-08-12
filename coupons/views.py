from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Coupon
from .serializers import CouponSerializer


class CouponViewSet(ModelViewSet):

    queryset = Coupon.objects.all()

    serializer_class = CouponSerializer

    permission_classes = [
        IsAuthenticated
    ]