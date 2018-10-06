import json
import datetime
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from products.models import Product, GiftCard, ProductPrice


def price_request(request, code, date, gc_code=''):
    """Retrieves the price of a product given a user-entered date and product code (required) and an optional gift card code

    Args:
        user_data:
            * 'code': must match an entry on Product.code AND at least one entry on ProductPrice.code,
            * 'date': date in YYYY-MM-DD format,
            * 'gc_code': (optional) gift card code representing a number of dollars off the price

    Returns:
        response_data:
            * all fields from user_data
            * 'name': the user-friendly name of the product,
            * 'price': the final price of the product given any active sales and activated coupon codes

    """
    response_data = {
        'code': '',
        'name': '',
        'date': '',
        'gift_card': '',
        'price': ''
    }

    if validate_product_code(code):
        response_data['code'] = code
    else:
        return JsonResponse({'error': 'Product not found.'}, status=400)

    if validate_date(date):
        response_data['date'] = date
    else:
        return JsonResponse({'error': 'Enter a date in "YYYY-MM-DD" format.'}, status=400)

    if gc_code == '':
        pass
    elif validate_gift_card(gc_code, date):
        response_data['gift_card'] = gc_code
    else:
        return JsonResponse({'error': 'Invalid gift card code or gift card expired.'}, status=400)

    response_data['name'] = model_to_dict(
        Product.objects.get(code=code))['name']

    # TODO: calculate the price
    # TODO: return the object
    # TODO: get that thing in the browser


def validate_product_code(code):
    """Checks that the product code exists in both the Product and ProductPrice tables"""

    if Product.objects.filter(code=code).exists() and ProductPrice.objects.filter(code=code).exists():
        return True
    else:
        return False


def validate_date(date_str):
    """Checks that the date is correctly formatted"""

    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except:
        return false


def validate_gift_card(gc_code, date_str):
    """Checks that the gift card code is in the GiftCard table and that it is valid for the given date"""

    gift_card_start = model_to_dict(
        GiftCard.objects.get(code=code))['date_start']
    gift_card_end = model_to_dict(GiftCard.objects.get(code=code))['date_end']

    if GiftCard.objects.filter(code=gc_code).exists() and date_in_range(date_str, gift_card_start, gift_card_end):
        return True
    else:
        return False


def date_in_range(given_date, range_start, range_end):
    """Validates the given date is inside the range of dates, used for checking valid gift cards and sale dates"""

    if str(range_start) <= given_date and str(range_end) >= given_date:
        return True
    else:
        return False
