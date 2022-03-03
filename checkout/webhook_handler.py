"""source CI """
from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected wh event
        """
        return HttpResponse(
            content=f'Webhook recived: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment_intent.succeeded from Stripe
        """
        return HttpResponse(
            content=f'Webhook recived: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        """
        Handle payment_intent.payment_failed from Stripe
        """
        return HttpResponse(
            content=f'Webhook recived: {event["type"]}',
            status=200)
