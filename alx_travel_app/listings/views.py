from .serializers import ListingSerializer, BookingSerializer
from rest_framework import viewsets
from .models import Listing, Booking


# TODO
# Add perform Create
# Create user model for listing and review model
# Update the seed file
class ListingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows listings to be viewed or edited.
    """
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()

    # def perform_create(self, serializer):
    #     serializer.save(host=self.request.user)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)