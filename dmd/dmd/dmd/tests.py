import json
import string
import random
from datetime import datetime, date

from django.db import IntegrityError
from django.test import TestCase
from django.test.client import RequestFactory
from django.utils import unittest
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from .models import Diagnosis
from registry.patients.models import Patient, State, Country
from registry.groups.models import WorkingGroup
from django_nose.runner import NoseTestSuiteRunner

from django.core.management import call_command

# #Add this to your settings file

# # testing settings
# INSTALLED_APPS.extend(['django_nose'])

# TEST_RUNNER = 'dmd.dmd.tests.PatchedNoseTestSuiteRunner'

# NOSE_ARGS = [
#     '--with-coverage',
#     '--cover-erase',
#     '--cover-html',
#     '--cover-branches',
#     '--cover-package=dmd',
# ]

class LoginLettuceTests(TestCase):
    def test_run_lettuce(self):
        call_command('harvest', 'dmd/dmd/features/login.feature')

class PatchedNoseTestSuiteRunner(NoseTestSuiteRunner):
    """This class required by django_nose to correctly load all models, not sure why. See,
    https://github.com/jbalogh/django-nose/issues/15 although this discussion is about loading
    tables for test classes.
    """
    def setup_test_environment(self, **kwargs):
        super(PatchedNoseTestSuiteRunner, self).setup_test_environment()
        # Unfortunately this is required for Django to correctly import models in tests and generate the database
        # structure for these models
        suite = self.build_suite(test_labels=None, extra_tests=None)


class DMDModelTests(unittest.TestCase):

    def test_diagnosis_created_when_patient_saved(self):
        self.assertEqual(1,1)

        wg, created = WorkingGroup.objects.get_or_create(name="testgroup")
        country, created = Country.objects.get_or_create(name="Australia")
        state, created = State.objects.get_or_create(short_name="WA", name="Western Australia", country=country)

        # make random name incase reusing testdb
        family_name = "".join([random.choice(string.ascii_letters + string.digits) for n in xrange(10)])

        p = Patient(working_group=wg,
                    consent=True,
                    family_name=family_name,
                    given_names="Test",
                    date_of_birth="1984-12-05",
                    state=state, postcode="6150",
                    next_of_kin_state=state,
                    next_of_kin_postcode="6150")
        p.save()

        # test that diagnosis has been created, an DoesNotExist exception will
        # be thrown if it does not
        d = Diagnosis.objects.get(patient=p)
        self.assertEqual(d.patient.id, p.id)


from registry.groups.models import *
from registry.patients.models import *
from registry.genetic.models import *
from dmd.dmd.models import *

class DMDReportTests(unittest.TestCase):
    def setUp(self):
        wg = WorkingGroup.objects.all()[0]
        self.fred = Patient.objects.create(working_group=wg, consent=True,
                                           family_name="Flintstone", given_names="Fred",
                                           sex="M", date_of_birth=date(1940,1,1),
                                           umrn="a",
                                           address="a", suburb="a", state=State.objects.all()[0],
                                           postcode="1111")
        self.barney = Patient.objects.create(working_group=wg, consent=True, #
                                             family_name="Barney", given_names="Rubble",
                                             sex="M", date_of_birth=date(1942,1,1),
                                             umrn="b",
                                             address="a", suburb="b", state=State.objects.all()[0],
                                             postcode="1111")

        # Give barney some genetic information
        gene = Gene.objects.all()[42]
        Variation.objects.create(molecular_data=self.barney.moleculardata, gene=gene,
                                 deletion_all_exons_tested=True)

        # Fred is not on steroids
        Steroids.objects.create(diagnosis=self.fred.patient_diagnosis, current=False)

        # Barney is on steroids
        Steroids.objects.create(diagnosis=self.barney.patient_diagnosis, current=True)

        # Barney is ambulant
        MotorFunction.objects.create(diagnosis=self.barney.patient_diagnosis, walk=True, sit=True,
                                     wheelchair_use="never")
        # fixme: is this field used?
        #self.barney.patient_diagnosis.walk = True

        # Barney has a good heart
        Heart.objects.create(diagnosis=self.barney.patient_diagnosis,
                             current=False, failure=False, lvef=75,
                             lvef_date=date.today())

        self.fred.patient_diagnosis.save()
        self.barney.patient_diagnosis.save()
        self.fred.save()
        self.barney.save()

    def test_missing_molecular_variation(self):
        self.assertTrue(Diagnosis.objects.filter(patient=self.fred).exists())
        self.assertTrue(MolecularData.objects.filter(patient=self.fred).exists())
        self.assertEquals(Variation.objects.count(), 1)

        #MolecularData.objects.all()[0].delete()
        self.fred.moleculardata.delete()

        date_range = map(str, (date(1900,1,1), date(2100,1,1)))
        working_group = "au"

        from dmd.dmd.views import get_dmd_results

        results = dict((t, get_dmd_results(date_range, t, working_group)) for t in (True, False))

        from pprint import pprint
        print "results"
        pprint(results)

        self.assertEquals(results[True]["total"], 1)
        self.assertEquals(results[True]["onsteroids"], 1)
        self.assertEquals(results[True]["notonsteroids"], 0)
        self.assertEquals(results[True]["steroidsunknown"], 0)
        self.assertEquals(results[True]["ambulant"], 1)
        self.assertEquals(results[True]["non-ambulant"], 0)
        self.assertEquals(results[True]["cardiomyopathy_yes"], 0)
        self.assertEquals(results[True]["cardiomyopathy_no"], 1)
        self.assertEquals(results[True]["cardiomyopathy_unknown"], 0)

        self.assertEquals(results[False]["total"], 0)
        self.assertEquals(results[False]["onsteroids"], 0)
        self.assertEquals(results[False]["notonsteroids"], 1)
        self.assertEquals(results[False]["steroidsunknown"], 0)
        self.assertEquals(results[False]["ambulant"], 0)
        self.assertEquals(results[False]["non-ambulant"], 1)
        self.assertEquals(results[False]["cardiomyopathy_yes"], 0)
        self.assertEquals(results[False]["cardiomyopathy_no"], 0)
        self.assertEquals(results[False]["cardiomyopathy_unknown"], 1)
