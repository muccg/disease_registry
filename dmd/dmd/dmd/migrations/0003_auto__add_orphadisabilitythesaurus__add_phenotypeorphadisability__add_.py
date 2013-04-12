# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrphaDisabilityThesaurus'
        db.create_table('dmd_orphadisabilitythesaurus', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orpha', self.gf('django.db.models.fields.related.ForeignKey')(related_name='orpha', to=orm['dmd.PhenotypeOrpha'])),
            ('disease', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('disability', self.gf('smart_selects.db_fields.ChainedForeignKey')(related_name='disability_th', to=orm['dmd.PhenotypeOrphaDisability'])),
            ('disability_type', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['dmd.PhenotypeOrphaDisabilityType'])),
            ('severity', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('frequency', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('loss_of_ability', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('environmental_factor', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('dmd', ['OrphaDisabilityThesaurus'])

        # Adding model 'PhenotypeOrphaDisability'
        db.create_table('dmd_phenotypeorphadisability', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orpha', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dmd.PhenotypeOrpha'])),
            ('disability', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('dmd', ['PhenotypeOrphaDisability'])

        # Adding model 'PhenotypeOrphaDisabilityType'
        db.create_table('dmd_phenotypeorphadisabilitytype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('disability', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dmd.PhenotypeOrphaDisability'])),
            ('disability_type', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal('dmd', ['PhenotypeOrphaDisabilityType'])

        # Adding field 'Diagnosis.orpha_disability_thesaurus'
        db.add_column('dmd_diagnosis', 'orpha_disability_thesaurus',
                      self.gf('django.db.models.fields.related.OneToOneField')(to=orm['dmd.OrphaDisabilityThesaurus'], unique=True, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'OrphaDisabilityThesaurus'
        db.delete_table('dmd_orphadisabilitythesaurus')

        # Deleting model 'PhenotypeOrphaDisability'
        db.delete_table('dmd_phenotypeorphadisability')

        # Deleting model 'PhenotypeOrphaDisabilityType'
        db.delete_table('dmd_phenotypeorphadisabilitytype')

        # Deleting field 'Diagnosis.orpha_disability_thesaurus'
        db.delete_column('dmd_diagnosis', 'orpha_disability_thesaurus_id')


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
            'muscle_biopsy': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'orpha_disability_thesaurus': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dmd.OrphaDisabilityThesaurus']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'patient_diagnosis'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['patients.Patient']"}),
            'phenotype_hpo': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dmd.PhenotypeHpo']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'phenotype_orpha': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dmd.PhenotypeOrpha']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
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
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dmd.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'failure': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
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
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dmd.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'sit': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'walk': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wheelchair_usage_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wheelchair_use': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        'dmd.notes': {
            'Meta': {'object_name': 'Notes'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dmd.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'notes': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'dmd.orphadisabilitythesaurus': {
            'Meta': {'object_name': 'OrphaDisabilityThesaurus'},
            'disability': ('smart_selects.db_fields.ChainedForeignKey', [], {'related_name': "'disability_th'", 'to': "orm['dmd.PhenotypeOrphaDisability']"}),
            'disability_type': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['dmd.PhenotypeOrphaDisabilityType']"}),
            'disease': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'environmental_factor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'frequency': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'loss_of_ability': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'orpha': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'orpha'", 'to': "orm['dmd.PhenotypeOrpha']"}),
            'severity': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'dmd.otherregistries': {
            'Meta': {'object_name': 'OtherRegistries'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dmd.Diagnosis']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registry': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'dmd.phenotypehpo': {
            'Meta': {'ordering': "['code']", 'object_name': 'PhenotypeHpo'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dmd.phenotypeorpha': {
            'Meta': {'ordering': "['orpha_number']", 'object_name': 'PhenotypeOrpha'},
            'icd_10': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orpha_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'synonym': ('django.db.models.fields.TextField', [], {})
        },
        'dmd.phenotypeorphadisability': {
            'Meta': {'object_name': 'PhenotypeOrphaDisability'},
            'disability': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'orpha': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dmd.PhenotypeOrpha']"})
        },
        'dmd.phenotypeorphadisabilitytype': {
            'Meta': {'object_name': 'PhenotypeOrphaDisabilityType'},
            'disability': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dmd.PhenotypeOrphaDisability']"}),
            'disability_type': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dmd.respiratory': {
            'Meta': {'object_name': 'Respiratory'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dmd.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'fvc': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fvc_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'non_invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'dmd.steroids': {
            'Meta': {'object_name': 'Steroids'},
            'current': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dmd.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'previous': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'dmd.surgery': {
            'Meta': {'object_name': 'Surgery'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dmd.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
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
            'next_of_kin_relationship': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.NextOfKinRelationship']", 'null': 'True', 'blank': 'True'}),
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
        }
    }

    complete_apps = ['dmd']