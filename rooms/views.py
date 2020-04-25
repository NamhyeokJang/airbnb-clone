from django.views.generic import ListView
from django.shortcuts import render
from . import models


class HomeView(ListView):
    """ HomeView Definitions """

    model = models.Room
    paginate_by = 10
    paginate_orphans = 3
    ordering = "created"

    context_object_name = "rooms"


def room_detail(request, pk):
    print(pk)
    return render(request, "rooms/detail.html")
