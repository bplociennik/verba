from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command("migrate", interactive=False)
        call_command("collectstatic", interactive=False)

        user = get_user_model()
        if (
            settings.POPULATE_SUPERUSER
            and not user.objects.filter(email=settings.SUPERUSER_EMAIL).exists()
        ):
            user.objects.create_superuser(
                email=settings.SUPERUSER_EMAIL, password=settings.SUPERUSER_PASSWORD,
            )
