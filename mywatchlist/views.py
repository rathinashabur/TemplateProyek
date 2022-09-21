from django.shortcuts import render
from mywatchlist.models import WatchlistKu

# TODO: Create your views here.
def show_mywatchlist(request):
    data_watchlist = WatchlistKu.objects.all()
    context = {
        'data_watchlist': data_watchlist,
    }
    return render(request, "mywatchlist.html", context)