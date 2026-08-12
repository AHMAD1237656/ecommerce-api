from django.db import models


class Coupon(models.Model):

    code = models.CharField(
        max_length=50,
        unique=True
    )

    discount_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    valid_from = models.DateTimeField()

    valid_until = models.DateTimeField()

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.code