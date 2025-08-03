from rest_framework import serializers

from .models import Listing, Booking

class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ["listing_id", "host_id", "name", "description", "location", "updated_at", "price_per_night", "created_at"]


class BookingSerializer(serializers.ModelSerializer):
    """
    API endpoint that allows bookings to be viewed or edited.
    """
    listing = ListingSerializer(read_only=True)
    listing_id = serializers.UUIDField(write_only=True)
    class Meta:
        model = Booking
        fields = ["booking_id", "user_id", "end_date", "start_date", "total_price", "status", "listing"]
        read_only_fields = ["booking_id", "status"]

# class ReviewSerializer(serializers.ModelSerializer):
#     """
#     API endpoint that allows review to be viewed or edited.
#     """
#     class Meta:
#         model = Review
#         fields = ["review_id", "user_id", "comment", "rating", "created_at", "listing"]
#         read_only_fields = ["review_id", "created_at"]