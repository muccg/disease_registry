# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models

def replace_null_with_value(orm, to_fix, value=""):
    """
    to_fix is a list of tuples like this:
        ("app.ModelName", ["field1", "field2"...])

    This function will set all fields in all models which are NULL to
    the given value.
    """

    for model, fields in to_fix:
        for ob in orm[model].objects.all():
            for field in fields:
                if getattr(ob, field) is None:
                    setattr(ob, field, value)
                    ob.save()

class Migration(DataMigration):

    def forwards(self, orm):
        """
        Set any NULL string fields to the empty string in preparation
        for making these fields non-nullable.
        """

        to_fix = [
            ("dm1_questionnaire.Patient", ["mobile_phone"
                                           "work_phone",
                                           "home_phone",
                                           "email"]),

            ("dm1_questionnaire.FeedingFunction", ["gastic_nasal_tube", "dysphagia"]),
                  ("dm1_questionnaire.FamilyMember", ["relationship", "sex",
                                        "family_member_diagnosis"]),
                  ("dm1_questionnaire.GeneticTestDetails", ["counselling", "laboratory",
                                              "familycounselling"]),
                  ("dm1_questionnaire.SocioeconomicFactors", ["occupation",
                                                "education",
                                                "comments",
                                                "employment_effect"]),
                  ("dm1_questionnaire.Respiratory", ["non_invasive_ventilation_type",
                                       "non_invasive_ventilation",
                                       "invasive_ventilation"]),
                  ("dm1_questionnaire.Heart", ["ecg", "ecg_sinus_rhythm",
                                 "echocardiogram", "palpitations",
                                 "fainting", "racing", "condition"]),
                  ("dm1_questionnaire.OtherRegistries", ["registry"]),
                  ("dm1_questionnaire.Surgery", ["cardiac_implant", "cataract"]),
                  ("dm1_questionnaire.GeneralMedicalFactors", ["medicalert",
                                                 "occupationaltherapy",
                                                 "cancer",
                                                 "pneumonia",
                                                 "cancerothers",
                                                 "vocationaltraining",
                                                 "pneumoniainfections",
                                                 "cognitive_impairment",
                                                 "diabetes",
                                                 "cancerorgan",
                                                 "psychologicalcounseling",
                                                 "physiotherapy",
                                                 "speechtherapy"]),
                  ("dm1_questionnaire.EthnicOrigin", ["ethnic_origin"]),
                  ("dm1_questionnaire.Diagnosis",
                   ["first_symptom", "first_suspected_by"]),
                  ("dm1_questionnaire.Consent",
                   ["firstnameparentguardian",
                    "lastnameparentguardian",
                    "specialist_2",
                    "specialist_3",
                    "q1",
                    "q3",
                    "q2",
                    "q5",
                    "q4",
                    "q7",
                    "q6",
                    "doctoraddress_5",
                    "doctoraddress_4",
                    "doctoraddress_7",
                    "doctoraddress_6",
                    "doctoraddress_1",
                    "doctoraddress_0",
                    "doctoraddress_3",
                    "doctoraddress_2",
                    "doctoraddress_9",
                    "doctoraddress_8",
                    "specialist_6",
                    "specialist_7",
                    "specialist_4",
                    "specialist_5",
                    "doctor_8",
                    "doctor_9",
                    "specialist_0",
                    "specialist_1",
                    "doctor_4",
                    "doctor_5",
                    "doctor_6",
                    "doctor_7",
                    "doctor_0",
                    "doctor_1",
                    "doctor_2",
                    "doctor_3",
                    "specialist_8",
                    "specialist_9",
                    "doctortelephone_9",
                    "doctortelephone_8",
                    "doctortelephone_3",
                    "doctortelephone_2",
                    "doctortelephone_1",
                    "doctortelephone_0",
                    "doctortelephone_7",
                    "doctortelephone_6",
                    "doctortelephone_5",
                    "doctortelephone_4"]),
                  ("dm1_questionnaire.Fatigue", ["fatigue"]),
                  ("dm1_questionnaire.MotorFunction", ["best_function"]),
                  ("dm1_questionnaire.ClinicalTrials", ["trial_phase",
                                          "drug_name",
                                          "trial_sponsor",
                                          "trial_name"]),
                  ("dm1_questionnaire.Muscle", ["myotonia",
                                  "early_weakness",
                                  "face"])]

        replace_null_with_value(orm, to_fix, "")

    def backwards(self, orm):
        "Write your backwards methods here."

    models = {
        'dm1.cancertypechoices': {
            'Meta': {'ordering': "['description']", 'object_name': 'CancerTypeChoices'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'dm1_questionnaire.clinicaltrials': {
            'Meta': {'object_name': 'ClinicalTrials'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'drug_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'trial_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'trial_phase': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'trial_sponsor': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'dm1_questionnaire.consent': {
            'Meta': {'object_name': 'Consent'},
            'consentdate': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'consentdateparentguardian': ('django.db.models.fields.DateField', [], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'doctor_0': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_1': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_2': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_3': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_4': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_5': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_6': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_7': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_8': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctor_9': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'doctoraddress_0': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_1': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_2': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_3': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_4': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_5': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_6': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_7': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_8': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctoraddress_9': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '120', 'blank': 'True'}),
            'doctortelephone_0': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_1': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_2': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_3': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_4': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_5': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_6': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_7': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_8': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'doctortelephone_9': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '40', 'blank': 'True'}),
            'firstnameparentguardian': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'blank': 'True'}),
            'lastnameparentguardian': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '60', 'blank': 'True'}),
            'q1': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'q2': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'q3': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'q4': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'q5': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'q6': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'q7': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'specialist_0': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_1': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_2': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_3': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_4': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_5': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_6': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_7': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_8': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'}),
            'specialist_9': ('django.db.models.fields.CharField', [], {'default': 'None', 'max_length': '60', 'blank': 'True'})
        },
        'dm1_questionnaire.diagnosis': {
            'Meta': {'object_name': 'Diagnosis'},
            'affectedstatus': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30'}),
            'age_at_clinical_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'age_at_molecular_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.CharField', [], {'default': "'DM1'", 'max_length': '3'}),
            'first_suspected_by': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'first_symptom': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'patient': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Patient']", 'unique': 'True', 'primary_key': 'True'})
        },
        'dm1_questionnaire.ethnicorigin': {
            'Meta': {'object_name': 'EthnicOrigin'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'ethnic_origin': ('django.db.models.fields.CharField', [], {'max_length': '9', 'blank': 'True'})
        },
        'dm1_questionnaire.familymember': {
            'Meta': {'object_name': 'FamilyMember'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'family_member_diagnosis': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'relationship': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'dm1_questionnaire.fatigue': {
            'Meta': {'object_name': 'Fatigue'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'fatigue': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'in_car': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lying_down_afternoon': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'passenger_car': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sitting_inactive_public': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sitting_quietly_lunch': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sitting_reading': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'sitting_talking': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'watching_tv': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.fatiguemedication': {
            'Meta': {'object_name': 'FatigueMedication'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'dm1_questionnaire.feedingfunction': {
            'Meta': {'object_name': 'FeedingFunction'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'dysphagia': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'gastric_nasal_tube': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'dm1_questionnaire.generalmedicalfactors': {
            'Meta': {'object_name': 'GeneralMedicalFactors'},
            'anxiety': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'apathy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cancer': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'cancerorgan': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'cancerothers': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'cancertype': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'dm1questcancertypechoices'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['dm1.CancerTypeChoices']"}),
            'cholesterol': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'cognitive_impairment': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'}),
            'constipation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'depression': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diabetes': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'diabetesage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'dm1_quest.diagnosis'", 'unique': 'True', 'primary_key': 'True', 'to': "orm['dm1_questionnaire.Diagnosis']"}),
            'endocrine': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gall_bladder': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gor': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'infection': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'liver': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'medicalert': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'miscarriage': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'obgyn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'occupationaltherapy': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'physiotherapy': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'pneumonia': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'pneumoniaage': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pneumoniainfections': ('django.db.models.fields.CharField', [], {'max_length': '3', 'blank': 'True'}),
            'psychological': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'psychologicalcounseling': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'sexual_dysfunction': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'speechtherapy': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'vocationaltraining': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1', 'blank': 'True'}),
            'weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.genetictestdetails': {
            'Meta': {'object_name': 'GeneticTestDetails'},
            'counselling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'details': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'familycounselling': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'laboratory': ('django.db.models.fields.CharField', [], {'max_length': '256', 'blank': 'True'}),
            'test_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        'dm1_questionnaire.heart': {
            'Meta': {'object_name': 'Heart'},
            'age_at_diagnosis': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'condition': ('django.db.models.fields.CharField', [], {'max_length': '14', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'ecg': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'ecg_examination_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'ecg_pr_interval': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ecg_qrs_duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ecg_sinus_rhythm': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'echocardiogram': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'echocardiogram_lvef': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'echocardiogram_lvef_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fainting': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'palpitations': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'racing': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'dm1_questionnaire.heartmedication': {
            'Meta': {'object_name': 'HeartMedication'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'dm1_questionnaire.motorfunction': {
            'Meta': {'object_name': 'MotorFunction'},
            'best_function': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '8', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'dysarthria': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'walk': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1'}),
            'walk_assisted': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
            'walk_assisted_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wheelchair_usage_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'wheelchair_use': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '12'})
        },
        'dm1_questionnaire.muscle': {
            'Meta': {'object_name': 'Muscle'},
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'myotonia': ('django.db.models.fields.CharField', [], {'max_length': '6', 'blank': 'True'})
        },
        'dm1_questionnaire.musclemedication': {
            'Meta': {'object_name': 'MuscleMedication'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'drug': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '8'})
        },
        'dm1_questionnaire.otherregistries': {
            'Meta': {'object_name': 'OtherRegistries'},
            'diagnosis': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'primary_key': 'True'}),
            'registry': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        'dm1_questionnaire.patient': {
            'Meta': {'ordering': "['family_name', 'given_names', 'date_of_birth']", 'object_name': 'Patient'},
            'address': ('django.db.models.fields.TextField', [], {}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dm1_questionnaire_patient_set'", 'to': "orm['patients.Country']"}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'family_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'given_names': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'postcode': ('django.db.models.fields.IntegerField', [], {}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dm1_questionnaire_patient_set'", 'to': "orm['patients.State']"}),
            'suburb': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'work_phone': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'working_group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'dm1_questionnaire_patient_set'", 'to': "orm['groups.WorkingGroup']"})
        },
        'dm1_questionnaire.respiratory': {
            'Meta': {'object_name': 'Respiratory'},
            'age_non_invasive_ventilation': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'calculatedfvc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'fvc': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'fvc_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'non_invasive_ventilation': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
            'non_invasive_ventilation_type': ('django.db.models.fields.CharField', [], {'max_length': '5', 'blank': 'True'})
        },
        'dm1_questionnaire.socioeconomicfactors': {
            'Meta': {'object_name': 'SocioeconomicFactors'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'}),
            'education': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'employment_effect': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'occupation': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        'dm1_questionnaire.surgery': {
            'Meta': {'object_name': 'Surgery'},
            'cardiac_implant': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'cardiac_implant_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cataract': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'cataract_age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cataract_diagnosis': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'diagnosis': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['dm1_questionnaire.Diagnosis']", 'unique': 'True', 'primary_key': 'True'})
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
        'patients.state': {
            'Meta': {'ordering': "['country__name', 'name']", 'object_name': 'State'},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['patients.Country']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'short_name': ('django.db.models.fields.CharField', [], {'max_length': '3', 'primary_key': 'True'})
        }
    }

    complete_apps = ['dm1_questionnaire']
    symmetrical = True
