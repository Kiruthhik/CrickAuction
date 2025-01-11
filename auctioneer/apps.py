from django.apps import AppConfig
from django.db.models.signals import post_migrate
class AuctioneerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auctioneer'   

    def ready(self):
        from auctioneer.tasks import check_scheduled_auctions
        from background_task.models import Task

        def schedule_task(sender, **kwargs):
            if not Task.objects.filter(task_name="auctioneer.tasks.check_scheduled_auctions").exists():
                check_scheduled_auctions(repeat=60)

        post_migrate.connect(schedule_task, sender=self)