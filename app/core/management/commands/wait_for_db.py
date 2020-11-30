#make app sleep for a few seconds in between each db check
import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until db available"""
    def handle(self, *args, **options):
        #print in screen
        self.stdout.write('Waiting for database...')
        db_conn = None
        #while falsie
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second.')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Database available!'))