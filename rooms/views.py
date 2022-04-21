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

from django.views.generic import ListView
from django.shortcuts import render
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "rooms"


def room_detail(request, pk):
    print(pk)
    return render(request, "rooms/detail.html")
