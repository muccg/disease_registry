# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

class Migration(DataMigration):

    def forwards(self, orm):
        "Write your forwards methods here."
        from django.core.management import call_command
        call_command("loaddata", "dd.OrphanetChoices.json", exceptiononerror=True)

    def backwards(self, orm):
        "Write your backwards methods here."

    complete_apps = ['dd']
    symmetrical = True