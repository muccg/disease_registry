# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrphanetChoices'
        db.create_table('dd_orphanetchoices', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=120)),
        ))
        db.send_create_signal('dd', ['OrphanetChoices'])

        # Adding model 'MedicalHistoryDisease'
        db.create_table('dd_medicalhistorydisease', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('disease', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('dd', ['MedicalHistoryDisease'])

        # Adding model 'MedicalHistory'
        db.create_table('dd_medicalhistory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patients.Patient'])),
        ))
        db.send_create_signal('dd', ['MedicalHistory'])

        # Adding model 'TreatmentOverview'
        db.create_table('dd_treatmentoverview', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('patient', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['patients.Patient'])),
        ))
        db.send_create_signal('dd', ['TreatmentOverview'])

        # Adding model 'Treatment'
        db.create_table('dd_treatment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('common_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('dd', ['Treatment'])

        # Adding model 'TreatmentCourse'
        db.create_table('dd_treatmentcourse', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('treatment', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.Treatment'])),
            ('overview', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.TreatmentOverview'])),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('dose_type', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('dose_other', self.gf('django.db.models.fields.TextField')()),
            ('notes', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('dd', ['TreatmentCourse'])

        # Adding model 'Diagnosis'
        db.create_table('dd_diagnosis', (
            ('patient', self.gf('django.db.models.fields.related.OneToOneField')(related_name='patient_diagnosis', unique=True, primary_key=True, to=orm['patients.Patient'])),
            ('diagnosis', self.gf('django.db.models.fields.CharField')(default='UNK', max_length=3)),
            ('affected_status', self.gf('django.db.models.fields.CharField')(default='', max_length=30)),
            ('first_suspected_by', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('date_of_first_symptom', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_of_diagnosis', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('age_at_clinical_diagnosis', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('age_at_molecular_diagnosis', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('orphanet', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.OrphanetChoices'], null=True, blank=True)),
            ('family_history', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('family_consent', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('created', self.gf('django.db.models.fields.DateTimeField')()),
            ('updated', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('dd', ['Diagnosis'])

        # Adding model 'DDMedicalHistoryRecord'
        db.create_table('dd_ddmedicalhistoryrecord', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.Diagnosis'], null=True, blank=True)),
            ('history', self.gf('django.db.models.fields.related.ForeignKey')(related_name='records', to=orm['dd.MedicalHistory'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('disease', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.MedicalHistoryDisease'])),
            ('chronic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('medical_history_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('other', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('misdiagnosed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('dd', ['DDMedicalHistoryRecord'])

        # Adding model 'EdssRating'
        db.create_table('dd_edssrating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rating', self.gf('django.db.models.fields.FloatField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('dd', ['EdssRating'])

        # Adding model 'DDClinicalData'
        db.create_table('dd_ddclinicaldata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.Diagnosis'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('date_first_symtoms', self.gf('django.db.models.fields.DateField')()),
            ('edss_rating', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.EdssRating'])),
            ('edss_evaluation_type', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('past_medical_history', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.DDMedicalHistoryRecord'], null=True, blank=True)),
            ('date_of_visits', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('dd', ['DDClinicalData'])

        # Adding model 'LabData'
        db.create_table('dd_labdata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.Diagnosis'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('protein', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('leucocytes', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('erythrocytes', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('oligoclonal_bands', self.gf('django.db.models.fields.FloatField')(default=0.0)),
            ('igg_alb', self.gf('django.db.models.fields.FloatField')(default=0.0)),
        ))
        db.send_create_signal('dd', ['LabData'])

        # Adding model 'MRIData'
        db.create_table('dd_mridata', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.Diagnosis'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('location', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('brain', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('cervical', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('thoracic', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('report_file', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('dd', ['MRIData'])

        # Adding model 'MRIFile'
        db.create_table('dd_mrifile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data', self.gf('django.db.models.fields.related.ForeignKey')(related_name='images', to=orm['dd.MRIData'])),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
        ))
        db.send_create_signal('dd', ['MRIFile'])

        # Adding model 'DDTreatmentOverview'
        db.create_table('dd_ddtreatmentoverview', (
            ('treatmentoverview_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dd.TreatmentOverview'], unique=True, primary_key=True)),
            ('diagnosis', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dd.Diagnosis'], null=True, blank=True)),
        ))
        db.send_create_signal('dd', ['DDTreatmentOverview'])

        # Adding M2M table for field treatments on 'DDTreatmentOverview'
        db.create_table('dd_ddtreatmentoverview_treatments', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('ddtreatmentoverview', models.ForeignKey(orm['dd.ddtreatmentoverview'], null=False)),
            ('treatment', models.ForeignKey(orm['dd.treatment'], null=False))
        ))
        db.create_unique('dd_ddtreatmentoverview_treatments', ['ddtreatmentoverview_id', 'treatment_id'])


    def backwards(self, orm):
        # Deleting model 'OrphanetChoices'
        db.delete_table('dd_orphanetchoices')

        # Deleting model 'MedicalHistoryDisease'
        db.delete_table('dd_medicalhistorydisease')

        # Deleting model 'MedicalHistory'
        db.delete_table('dd_medicalhistory')

        # Deleting model 'TreatmentOverview'
        db.delete_table('dd_treatmentoverview')

        # Deleting model 'Treatment'
        db.delete_table('dd_treatment')

        # Deleting model 'TreatmentCourse'
        db.delete_table('dd_treatmentcourse')

        # Deleting model 'Diagnosis'
        db.delete_table('dd_diagnosis')

        # Deleting model 'DDMedicalHistoryRecord'
        db.delete_table('dd_ddmedicalhistoryrecord')

        # Deleting model 'EdssRating'
        db.delete_table('dd_edssrating')

        # Deleting model 'DDClinicalData'
        db.delete_table('dd_ddclinicaldata')

        # Deleting model 'LabData'
        db.delete_table('dd_labdata')

        # Deleting model 'MRIData'
        db.delete_table('dd_mridata')

        # Deleting model 'MRIFile'
        db.delete_table('dd_mrifile')

        # Deleting model 'DDTreatmentOverview'
        db.delete_table('dd_ddtreatmentoverview')

        # Removing M2M table for field treatments on 'DDTreatmentOverview'
        db.delete_table('dd_ddtreatmentoverview_treatments')


    models = {
        'dd.ddclinicaldata': {
            'Meta': {'object_name': 'DDClinicalData'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'date_first_symtoms': ('django.db.models.fields.DateField', [], {}),
            'date_of_visits': ('django.db.models.fields.DateField', [], {}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.Diagnosis']"}),
            'edss_evaluation_type': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'edss_rating': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.EdssRating']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'past_medical_history': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.DDMedicalHistoryRecord']", 'null': 'True', 'blank': 'True'})
        },
        'dd.ddmedicalhistoryrecord': {
            'Meta': {'object_name': 'DDMedicalHistoryRecord'},
            'chronic': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.Diagnosis']", 'null': 'True', 'blank': 'True'}),
            'disease': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.MedicalHistoryDisease']"}),
            'history': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'records'", 'to': "orm['dd.MedicalHistory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'medical_history_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'misdiagnosed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'other': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'dd.ddtreatmentoverview': {
            'Meta': {'object_name': 'DDTreatmentOverview', '_ormbases': ['dd.TreatmentOverview']},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.Diagnosis']", 'null': 'True', 'blank': 'True'}),
            'treatmentoverview_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dd.TreatmentOverview']", 'unique': 'True', 'primary_key': 'True'}),
            'treatments': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['dd.Treatment']", 'null': 'True', 'blank': 'True'})
        },
        'dd.diagnosis': {
            'Meta': {'object_name': 'Diagnosis'},
            'affected_status': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'age_at_clinical_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'age_at_molecular_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            'date_of_diagnosis': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_of_first_symptom': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'default': "'UNK'", 'max_length': '3'}),
            'family_consent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'family_history': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'first_suspected_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'orphanet': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.OrphanetChoices']", 'null': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'patient_diagnosis'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['patients.Patient']"}),
            'updated': ('django.db.models.fields.DateTimeField', [], {})
        },
        'dd.edssrating': {
            'Meta': {'ordering': "['rating']", 'object_name': 'EdssRating'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'rating': ('django.db.models.fields.FloatField', [], {})
        },
        'dd.labdata': {
            'Meta': {'object_name': 'LabData'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.Diagnosis']"}),
            'erythrocytes': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'igg_alb': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'leucocytes': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'oligoclonal_bands': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'protein': ('django.db.models.fields.FloatField', [], {'default': '0.0'})
        },
        'dd.medicalhistory': {
            'Meta': {'object_name': 'MedicalHistory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Patient']"})
        },
        'dd.medicalhistorydisease': {
            'Meta': {'ordering': "['disease']", 'object_name': 'MedicalHistoryDisease'},
            'disease': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dd.mridata': {
            'Meta': {'object_name': 'MRIData'},
            'brain': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cervical': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.Diagnosis']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'report_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'thoracic': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'dd.mrifile': {
            'Meta': {'object_name': 'MRIFile'},
            'data': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['dd.MRIData']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'dd.orphanetchoices': {
            'Meta': {'ordering': "['code']", 'object_name': 'OrphanetChoices'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dd.treatment': {
            'Meta': {'object_name': 'Treatment'},
            'common_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'dd.treatmentcourse': {
            'Meta': {'object_name': 'TreatmentCourse'},
            'dose_other': ('django.db.models.fields.TextField', [], {}),
            'dose_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'overview': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.TreatmentOverview']"}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'treatment': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dd.Treatment']"})
        },
        'dd.treatmentoverview': {
            'Meta': {'object_name': 'TreatmentOverview'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'patient': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Patient']"})
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

    complete_apps = ['dd']