# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Module'
        db.create_table('configuration_module', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('configuration', ['Module'])

        # Adding model 'EmailTemplate'
        db.create_table('configuration_emailtemplate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('module', self.gf('django.db.models.fields.CharField')(default='DD', max_length=10)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('body', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('configuration', ['EmailTemplate'])


    def backwards(self, orm):
        # Deleting model 'Module'
        db.delete_table('configuration_module')

        # Deleting model 'EmailTemplate'
        db.delete_table('configuration_emailtemplate')


    models = {
        'configuration.emailtemplate': {
            'Meta': {'object_name': 'EmailTemplate'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'default': "'DD'", 'max_length': '10'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'configuration.module': {
            'Meta': {'object_name': 'Module'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['configuration']