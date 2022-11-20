from .models import Item
from django.http import Http404


def get_item(pk):
    try:
        return Item.objects.get(pk=pk)
    except:
        raise Http404
