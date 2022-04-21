""" Function-Based View
from django.shortcuts import render
from django.core.paginator import Paginator
from . import models

def all_rooms(request):

    page = request.GET.get("page", 1)
    room_list = models.Room.objects.all()

    paginator = Paginator(room_list, 10, orphans=5)
    rooms = paginator.page(int(page))
    return render(request, "rooms/home.html", {"page": rooms})
"""

from itertools import count
from django.views.generic import ListView
from django.http import Http404
from django.shortcuts import render
from django_countries import countries
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
        return render(request, "rooms/detail.html", {"room": room})
    except models.Room.DoesNotExist:
        raise Http404()


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    room_types = models.RoomType.objects.all()
    return render(
        request,
        "rooms/search.html",
        {"city": city, "countries": countries, "room_types": room_types},
    )
