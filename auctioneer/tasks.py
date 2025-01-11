from background_task import background
from .models import LiveAuction
from datetime import datetime, timedelta
from pytz import UTC
#import logging
#logger = logging.getLogger(__name__)
auction_started = False
@background(schedule=60)  # Runs every 60 seconds
def check_scheduled_auctions():
    """
    This task checks if any auctions are scheduled to start
    and triggers the auction process.
    """
    global auction_started
    print("Checking scheduled auctions...")
    now = datetime.now().replace(tzinfo=UTC)
    print(now)
    print("status:",auction_started)
    auctions = LiveAuction.objects.filter(scheduled_time__lte=now, scheduled_time__gt=now - timedelta(minutes=1))
    if not auction_started and auctions:
        for auction in auctions:
            start_auction(auction)
        auction_started = True

def start_auction(auction):
    # Logic to start the auction
    print(f"Starting auction: {auction.name}")
    # Add backend logic for auction processing
