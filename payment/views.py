import json
import stripe
from django.shortcuts import render
from django.http import HttpResponse
from .services import get_item
from .keys import *

stripe.api_key = STRIPE_SECRET_KEY


def purchase_item(request, pk):
    if request.method == "GET":
        item = get_item(pk)
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.name,
                    },
                    'unit_amount': int(round(item.price * 100)),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url='http://127.0.0.1:8000/success',
            cancel_url='http://127.0.0.1:8000/cancel'
        )
        return HttpResponse(json.dumps(session), content_type='application/json')


def get_item_page(request, pk):
    if request.method == "GET":
        item = get_item(pk)
        return render(request,
                      template_name='item_purchasing.html',
                      context={
                          "id": pk,
                          "name": item.name,
                          "description": item.description,
                          "price": item.price,
                          "stripe_pk": STRIPE_PUBLIC_KEY,
                      })


def success_purchase(request):
    return render(request, template_name='success_purchase.html')


def cancel_purchase(request):
    return render(request, template_name='cancel_purchase.html')
