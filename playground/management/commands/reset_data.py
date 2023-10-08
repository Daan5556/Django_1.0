from django.core.management.base import BaseCommand
from django.conf import settings
import os
from playground.models import FormSubmission1, FormSubmission2

class Command(BaseCommand):
    help = 'Reset data for testing purposes'

    def handle(self, *args, **options):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                              'Django1.settings')  # Replace with your actual settings module


        FormSubmission1.objects.all().delete()
        FormSubmission2.objects.all().delete()

        self.stdout.write(self.style.SUCCESS('Data reset successfully'))
