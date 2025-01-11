from django.core.management.base import BaseCommand
from background_task.models import Task
from auctioneer.tasks import check_scheduled_auctions

class Command(BaseCommand):
    help = 'Triggers the check_scheduled_auctions task'

    def handle(self, *args, **kwargs):
        #if not Task.objects.filter(task_name="auctioneer.tasks.check_scheduled_auctions").exists():
            check_scheduled_auctions(repeat=60)
            self.stdout.write(self.style.SUCCESS("Scheduled the check_scheduled_auctions task."))
        #else:
            #self.stdout.write(self.style.WARNING("Task is already scheduled."))
