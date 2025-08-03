from .serializers import ListingSerializer, BookingSerializer
from rest_framework import viewsets
from .models import Listing, Booking

class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows listings to be viewed or edited.
    """
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


