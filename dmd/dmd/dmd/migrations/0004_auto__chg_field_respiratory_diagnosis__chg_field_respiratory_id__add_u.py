# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        db.execute('ALTER TABLE dmd_diagnosis DROP CONSTRAINT dmd_diagnosis_pkey CASCADE')
        db.create_primary_key('dmd_diagnosis', ['id'])

        # Changing field 'Diagnosis.patient'
        db.alter_column('dmd_diagnosis', 'patient_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, to=orm['patients.Patient']))


        db.alter_column('dmd_respiratory', 'diagnosis_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dmd.Diagnosis'], unique=True))
        db.delete_primary_key('dmd_respiratory')
        db.create_primary_key('dmd_respiratory', ['id'])


        db.alter_column('dmd_heart', 'diagnosis_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dmd.Diagnosis'], unique=True))
        db.delete_primary_key('dmd_heart')
        db.create_primary_key('dmd_heart', ['id'])


        db.alter_column('dmd_motorfunction', 'diagnosis_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dmd.Diagnosis'], unique=True))
        db.delete_primary_key('dmd_motorfunction')
        db.create_primary_key('dmd_motorfunction', ['id'])


        db.delete_primary_key('dmd_notes')
        db.create_primary_key('dmd_notes', ['id'])
        db.alter_column('dmd_notes', 'diagnosis_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dmd.Diagnosis'], unique=True))


        db.delete_primary_key('dmd_steroids')
        db.create_primary_key('dmd_steroids', ['id'])
        db.alter_column('dmd_steroids', 'diagnosis_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dmd.Diagnosis'], unique=True))


        db.delete_primary_key('dmd_surgery')
        db.create_primary_key('dmd_surgery', ['id'])
        db.alter_column('dmd_surgery', 'diagnosis_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dmd.Diagnosis'], unique=True))

    def backwards(self, orm):
        # Removing unique constraint on 'Surgery', fields ['id']
        db.delete_unique('dmd_surgery', ['id'])

        # Removing unique constraint on 'Steroids', fields ['id']
        db.delete_unique('dmd_steroids', ['id'])

        # Removing unique constraint on 'Notes', fields ['id']
        db.delete_unique('dmd_notes', ['id'])

        # Removing unique constraint on 'MotorFunction', fields ['id']
        db.delete_unique('dmd_motorfunction', ['id'])

        # Removing unique constraint on 'Heart', fields ['id']
        db.delete_unique('dmd_heart', ['id'])

        # Removing unique constraint on 'Diagnosis', fields ['id']
        db.delete_unique('dmd_diagnosis', ['id'])

        # Removing unique constraint on 'Respiratory', fields ['id']
        db.delete_unique('dmd_respiratory', ['id'])


        # Changing field 'Respiratory.diagnosis'
        db.alter_column('dmd_respiratory', 'diagnosis_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dmd.Diagnosis'], unique=True, primary_key=True))

        # Changing field 'Respiratory.id'
        db.alter_column('dmd_respiratory', 'id', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Diagnosis.patient'
        db.alter_column('dmd_diagnosis', 'patient_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, primary_key=True, to=orm['patients.Patient']))

        # Changing field 'Diagnosis.id'
        db.alter_column('dmd_diagnosis', 'id', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Heart.diagnosis'
        db.alter_column('dmd_heart', 'diagnosis_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dmd.Diagnosis'], unique=True, primary_key=True))

        # Changing field 'Heart.id'
        db.alter_column('dmd_heart', 'id', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'MotorFunction.diagnosis'
        db.alter_column('dmd_motorfunction', 'diagnosis_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dmd.Diagnosis'], unique=True, primary_key=True))

        # Changing field 'MotorFunction.id'
        db.alter_column('dmd_motorfunction', 'id', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Notes.id'
        db.alter_column('dmd_notes', 'id', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Notes.diagnosis'
        db.alter_column('dmd_notes', 'diagnosis_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dmd.Diagnosis'], unique=True, primary_key=True))

        # Changing field 'Steroids.id'
        db.alter_column('dmd_steroids', 'id', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Steroids.diagnosis'
        db.alter_column('dmd_steroids', 'diagnosis_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dmd.Diagnosis'], unique=True, primary_key=True))

        # Changing field 'Surgery.id'
        db.alter_column('dmd_surgery', 'id', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Surgery.diagnosis'
        db.alter_column('dmd_surgery', 'diagnosis_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dmd.Diagnosis'], unique=True, primary_key=True))

    models = {
        'dmd.clinicaltrials': {
            'Meta': {'object_name': 'ClinicalTrials'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dmd.Diagnosis']"}),
            'drug_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'trial_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'trial_phase': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'trial_sponsor': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'dmd.diagnosis': {
            'Meta': {'ordering': "['patient']", 'object_name': 'Diagnosis'},
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.IntegerField', [], {'default': '1', 'primary_key': 'True'}),
            'muscle_biopsy': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'patient_diagnosis'", 'unique': 'True', 'to': "orm['patients.Patient']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        'dmd.familymember': {
            'Meta': {'object_name': 'FamilyMember'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dmd.Diagnosis']"}),
            'family_member_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registry_patient': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['patients.Patient']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'dmd.heart': {
            'Meta': {'object_name': 'Heart'},
            'current': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dmd.Diagnosis']", 'unique': 'True'}),
            'failure': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'default': '1', 'primary_key': 'True'}),
            'lvef': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lvef_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'dmd.heartmedication': {
            'Meta': {'object_name': 'HeartMedication'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dmd.Diagnosis']"}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'dmd.motorfunction': {
            'Meta': {'object_name': 'MotorFunction'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dmd.Diagnosis']", 'unique': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'default': '1', 'primary_key': 'True'}),
            'sit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'walk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wheelchair_usage_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wheelchair_use': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'dmd.notes': {
            'Meta': {'object_name': 'Notes'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dmd.Diagnosis']", 'unique': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'default': '1', 'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'dmd.otherregistries': {
            'Meta': {'object_name': 'OtherRegistries'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dmd.Diagnosis']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registry': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'dmd.respiratory': {
            'Meta': {'object_name': 'Respiratory'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dmd.Diagnosis']", 'unique': 'True'}),
            'fvc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fvc_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'default': '1', 'primary_key': 'True'}),
            'invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'non_invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'dmd.steroids': {
            'Meta': {'object_name': 'Steroids'},
            'current': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dmd.Diagnosis']", 'unique': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'default': '1', 'primary_key': 'True'}),
            'previous': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'dmd.surgery': {
            'Meta': {'object_name': 'Surgery'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dmd.Diagnosis']", 'unique': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'default': '1', 'primary_key': 'True'}),
            'surgery': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
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
        'patients.nextofkinrelationship': {
            'Meta': {'object_name': 'NextOfKinRelationship'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'patients.parent': {
            'Meta': {'object_name': 'Parent'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent_date_of_migration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'parent_family_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent_given_names': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent_place_of_birth': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'patients.patient': {
            'Meta': {'ordering': "['family_name', 'given_names', 'date_of_birth']", 'unique_together': "(('family_name', 'given_names', 'working_group'),)", 'object_name': 'Patient'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'address': ('django.db.models.fields.TextField', [], {}),
            'consent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'consent_form': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'date_of_migration': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'doctors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['patients.Doctor']", 'through': "orm['patients.PatientDoctor']", 'symmetrical': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inactive_reason': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'next_of_kin_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_home_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_postcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'next_of_kin_relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.NextOfKinRelationship']", 'null': 'True', 'blank': 'True'}),
            'next_of_kin_state': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'next_of_kin_set'", 'null': 'True', 'to': "orm['patients.State']"}),
            'next_of_kin_suburb': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'next_of_kin_work_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'parents': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['patients.Parent']", 'through': "orm['patients.PatientParent']", 'symmetrical': 'False'}),
            'place_of_birth': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.IntegerField', [], {}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'patient_set'", 'to': "orm['patients.State']"}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'umrn': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
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
        'patients.patientparent': {
            'Meta': {'object_name': 'PatientParent'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Parent']"}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Patient']"}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        'patients.state': {
            'Meta': {'ordering': "['country__name', 'name']", 'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Country']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'})
        }
    }

    complete_apps = ['dmd']
