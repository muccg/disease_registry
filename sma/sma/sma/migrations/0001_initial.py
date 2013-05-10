# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Diagnosis'
        db.create_table('sma_diagnosis', (
            ('patient', self.gf('django.db.models.fields.related.OneToOneField')(related_name='patient_diagnosis', unique=True, primary_key=True, to=orm['patients.Patient'])),
            ('diagnosis', self.gf('django.db.models.fields.CharField')(max_length=3)),
            ('classification', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('sma', ['Diagnosis'])

        # Adding model 'MotorFunction'
        db.create_table('sma_motorfunction', (
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sma.Diagnosis'], unique=True, primary_key=True)),
            ('walk', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sit', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('best_function', self.gf('django.db.models.fields.CharField')(max_length=7)),
            ('acquisition_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('wheelchair_use', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('wheelchair_usage_age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('sma', ['MotorFunction'])

        # Adding model 'Surgery'
        db.create_table('sma_surgery', (
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sma.Diagnosis'], unique=True, primary_key=True)),
            ('surgery', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('sma', ['Surgery'])

        # Adding model 'FeedingFunction'
        db.create_table('sma_feedingfunction', (
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sma.Diagnosis'], unique=True, primary_key=True)),
            ('gastric_nasal_tube', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal('sma', ['FeedingFunction'])

        # Adding model 'Respiratory'
        db.create_table('sma_respiratory', (
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sma.Diagnosis'], unique=True, primary_key=True)),
            ('non_invasive_ventilation', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('invasive_ventilation', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('fvc', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('fvc_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal('sma', ['Respiratory'])

        # Adding model 'ClinicalTrials'
        db.create_table('sma_clinicaltrials', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sma.Diagnosis'])),
            ('drug_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('trial_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('trial_sponsor', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('trial_phase', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sma', ['ClinicalTrials'])

        # Adding model 'OtherRegistries'
        db.create_table('sma_otherregistries', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sma.Diagnosis'])),
            ('registry', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('sma', ['OtherRegistries'])

        # Adding model 'FamilyMember'
        db.create_table('sma_familymember', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sma.Diagnosis'])),
            ('registry_patient', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='sma_familymember_related', unique=True, null=True, to=orm['patients.Patient'])),
            ('sex', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('relationship', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('family_member_diagnosis', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('sma', ['FamilyMember'])

        # Adding model 'Notes'
        db.create_table('sma_notes', (
            ('diagnosis', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['sma.Diagnosis'], unique=True, primary_key=True)),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('sma', ['Notes'])


    def backwards(self, orm):
        # Deleting model 'Diagnosis'
        db.delete_table('sma_diagnosis')

        # Deleting model 'MotorFunction'
        db.delete_table('sma_motorfunction')

        # Deleting model 'Surgery'
        db.delete_table('sma_surgery')

        # Deleting model 'FeedingFunction'
        db.delete_table('sma_feedingfunction')

        # Deleting model 'Respiratory'
        db.delete_table('sma_respiratory')

        # Deleting model 'ClinicalTrials'
        db.delete_table('sma_clinicaltrials')

        # Deleting model 'OtherRegistries'
        db.delete_table('sma_otherregistries')

        # Deleting model 'FamilyMember'
        db.delete_table('sma_familymember')

        # Deleting model 'Notes'
        db.delete_table('sma_notes')


    models = {
        'groups.workinggroup': {
            'Meta': {'ordering': "['name']", 'object_name': 'WorkingGroup'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'patients.country': {
            'Meta': {'ordering': "['name']", 'object_name': 'Country'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        },
        'patients.doctor': {
            'Meta': {'object_name': 'Doctor'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'speciality': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.State']"}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'surgery_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'patients.patient': {
            'Meta': {'ordering': "['family_name', 'given_names', 'date_of_birth']", 'unique_together': "(('family_name', 'given_names', 'working_group'),)", 'object_name': 'Patient'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'address': ('django.db.models.fields.TextField', [], {}),
            'consent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'doctors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['patients.Doctor']", 'through': "orm['patients.PatientDoctor']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_address': ('django.db.models.fields.TextField', [], {}),
            'next_of_kin_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_family_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'next_of_kin_given_names': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'next_of_kin_home_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_postcode': ('django.db.models.fields.IntegerField', [], {}),
            'next_of_kin_state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'next_of_kin_set'", 'to': "orm['patients.State']"}),
            'next_of_kin_suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'next_of_kin_work_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.IntegerField', [], {}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'patient_set'", 'to': "orm['patients.State']"}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'working_group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['groups.WorkingGroup']"})
        },
        'patients.patientdoctor': {
            'Meta': {'object_name': 'PatientDoctor'},
            'doctor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Doctor']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Patient']"}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'patients.state': {
            'Meta': {'ordering': "['country__name', 'name']", 'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Country']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'})
        },
        'sma.clinicaltrials': {
            'Meta': {'object_name': 'ClinicalTrials'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sma.Diagnosis']"}),
            'drug_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'trial_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'trial_phase': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'trial_sponsor': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sma.diagnosis': {
            'Meta': {'ordering': "['patient']", 'object_name': 'Diagnosis'},
            'classification': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'patient': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'patient_diagnosis'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['patients.Patient']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        'sma.familymember': {
            'Meta': {'object_name': 'FamilyMember'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sma.Diagnosis']"}),
            'family_member_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registry_patient': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'sma_familymember_related'", 'unique': 'True', 'null': 'True', 'to': "orm['patients.Patient']"}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'sma.feedingfunction': {
            'Meta': {'object_name': 'FeedingFunction'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sma.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'gastric_nasal_tube': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        'sma.motorfunction': {
            'Meta': {'object_name': 'MotorFunction'},
            'acquisition_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'best_function': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sma.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'sit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'walk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wheelchair_usage_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wheelchair_use': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'sma.notes': {
            'Meta': {'object_name': 'Notes'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sma.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'sma.otherregistries': {
            'Meta': {'object_name': 'OtherRegistries'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sma.Diagnosis']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registry': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'sma.respiratory': {
            'Meta': {'object_name': 'Respiratory'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sma.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'fvc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fvc_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'non_invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'sma.surgery': {
            'Meta': {'object_name': 'Surgery'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['sma.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'surgery': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['sma']