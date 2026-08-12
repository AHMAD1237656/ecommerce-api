from django.core.mail import send_mail


def send_order_confirmation(order):

    send_mail(
        subject=f"Order Confirmation - {order.order_number}",

        message=(
            f"Your order {order.order_number} "
            f"has been received successfully.\n\n"
            f"Total Amount: ${order.total_amount}\n"
            f"Status: {order.status}"
        ),

        from_email="noreply@example.com",

        recipient_list=[
            order.customer.user.email
        ],

        fail_silently=True,
    )