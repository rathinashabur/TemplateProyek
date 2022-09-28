from django.shortcuts import render
from mywatchlist.models import WatchlistKu
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.
def show_mywatchlist(request):
    data_watchlist = WatchlistKu.objects.all()
    context = {
        'data_watchlist': data_watchlist,
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchlistKu.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchlistKu.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def not_watched(request):
    notwatched = WatchlistKu.objects.filter(watched = "Not Watched")
    context = {
        'data_watchlist': notwatched,
    }
    return render(request, "mywatchlist.html", context)