import json
import string
import random
from datetime import datetime

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


