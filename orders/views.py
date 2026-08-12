import stripe

from django.conf import settings
from django.http import HttpResponse

from reportlab.pdfgen import canvas

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Order
from .serializers import OrderSerializer
from .utils import send_order_confirmation


stripe.api_key = settings.STRIPE_SECRET_KEY


class OrderViewSet(ModelViewSet):

    queryset = Order.objects.all()

    serializer_class = OrderSerializer

    permission_classes = [
        IsAuthenticated
    ]


    def perform_create(self, serializer):

        order = serializer.save()

        send_order_confirmation(
            order
        )


    @action(
        detail=True,
        methods=["get"],
        url_path="tracking"
    )
    def tracking(self, request, pk=None):

        order = self.get_object()

        return Response({
            "order_number": order.order_number,
            "status": order.status,
            "updated_at": order.updated_at,
        })


    @action(
        detail=True,
        methods=["post"],
        url_path="payment"
    )
    def payment(self, request, pk=None):

        order = self.get_object()

        amount = int(
            order.total_amount * 100
        )

        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency="usd",
            metadata={
                "order_id": order.id,
                "order_number": order.order_number,
            }
        )

        return Response({
            "order_id": order.id,
            "order_number": order.order_number,
            "client_secret": payment_intent.client_secret,
        })


    @action(
        detail=True,
        methods=["get"],
        url_path="invoice"
    )
    def invoice(self, request, pk=None):

        order = self.get_object()

        response = HttpResponse(
            content_type="application/pdf"
        )

        response["Content-Disposition"] = (
            f'attachment; '
            f'filename="invoice_{order.order_number}.pdf"'
        )

        pdf = canvas.Canvas(response)

        pdf.setTitle(
            f"Invoice - {order.order_number}"
        )

        y = 800

        pdf.setFont(
            "Helvetica-Bold",
            18
        )

        pdf.drawString(
            50,
            y,
            "E-Commerce Invoice"
        )

        y -= 40

        pdf.setFont(
            "Helvetica",
            11
        )

        pdf.drawString(
            50,
            y,
            f"Order: {order.order_number}"
        )

        y -= 20

        pdf.drawString(
            50,
            y,
            f"Status: {order.status}"
        )

        y -= 20

        pdf.drawString(
            50,
            y,
            f"Total: ${order.total_amount}"
        )

        y -= 40

        for item in order.items.all():

            text = (
                f"{item.product.name} | "
                f"Qty: {item.quantity} | "
                f"Price: ${item.price}"
            )

            pdf.drawString(
                50,
                y,
                text
            )

            y -= 20

            if y < 50:

                pdf.showPage()

                y = 800

                pdf.setFont(
                    "Helvetica",
                    11
                )

        pdf.save()

        return response