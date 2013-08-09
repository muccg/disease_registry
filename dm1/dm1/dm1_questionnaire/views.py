from django.http import HttpRequest, QueryDict, HttpResponse, HttpResponseRedirect
from django.db import transaction
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import *
import re

from registry.groups.models import WorkingGroup
from registry.patients.models import State
from registry.patients.models import Country

from registry.utils import stripspaces

@transaction.commit_on_success
def clinical(request, country):
    def save_default(form, diagnosis):
        """
        Default save handler for clinical forms: calls ModelForm.save() and
        then munges the diagnosis to link back to the right record.
        """

        o = form.save(commit=False)
        o.diagnosis = diagnosis
        o.save()

    from django.forms.models import inlineformset_factory

    def ifs(form_class):
        from models import Diagnosis
        return inlineformset_factory(Diagnosis, form_class.Meta.model, can_delete=False, extra=1,)

    def save_inline(inline_form, diagnosis):
        for form in inline_form.forms:
            if form.changed_data:
                # Don't save empty forms with no data
                o = form.save(commit=False)
                o.diagnosis = diagnosis
                o.save()

    # This is a list of the forms that need to be displayed on this page. Each
    # element within this tuple is a 3-element tuple containing the name of the
    # form (to be displayed in the fieldset legend), the form itself, and a
    # callback used to save the form's contents.
    #
    # The one-to-many forms have been commented out for now. They can be
    # re-added, but the level of complexity in rendering them is starting to
    # get daunting for a simple questionnaire.
    form_definitions = (
        ("Diagnosis", DiagnosisForm, lambda form, diagnosis: None),
        ("Motor Function", MotorFunctionForm, save_default),
        ("Surgery", SurgeryForm, save_default),
        ("Heart Function", HeartForm, save_default),
        #("Heart Medication", HeartMedicationForm, save_default),
        ("Respiratory Function", RespiratoryForm, save_default),
        ("Muscle Function", MuscleForm, save_default),
        #("Muscle Medication", MuscleMedicationForm, save_default),
        ("Difficulties Eating", FeedingFunctionForm, save_default), # 2012-01-19 Trac 16 DM1 Questionnaire #44
        ("Fatigue", FatigueForm, save_default),
        #("Fatigue Medication", FatigueMedicationForm, save_default),
        ("Socio-Economic Factors", SocioeconomicFactorsForm, save_default),
        ("General Medical Factors", GeneralMedicalFactorsForm, save_default),
        ("Genetic Test Details", GeneticTestDetailsForm, save_default),
        ("Ethnic Origin", EthnicOriginForm, save_default),
        ("Family Member", ifs(FamilyMemberForm), save_inline),
        ("Clinical Trials", ifs(ClinicalTrialsForm), save_inline),
        ("Other Registries", ifs(OtherRegistriesForm), save_inline),
        #("Consent Form", ConsentForm, save_default), # validated separately
    )

    def instantiate_form(definition, *args, **kwargs):
        """
        Given a 3-element tuple from form_definitions, instantiates and returns
        the appropriate form object. This includes setting a form prefix to
        avoid the possibility of name conflicts.
        """

        form_class = definition[1]
        pfx = prefix(definition[0])

        return form_class(prefix=pfx, *args, **kwargs)

    def prefix(name):
        """
        Converts a form name into a prefix via an incredibly dumb algorithm.
        """

        # We really shouldn't need to use regex here, but I couldn't see an
        # obvious way to get Python's string methods to do this without using
        # something equally overkill such as translate().
        return re.sub(r"[^a-zA-Z]", "", name).lower()

    family_name = ''
    given_names = ''

    patientform = request.session.get("patientform")
    if patientform:
        family_name = patientform.get("family_name", '')
        given_names = patientform.get("given_names", '')
    else:
        # either the session has timed out or the 'clinical' url was reached without going through 'personal' first
        return HttpResponseRedirect("index")

    if request.method == "POST":
        # The form has been submitted, so let's do something useful with it.
        #print "views.clinical: request.session: %s" % dir(request.session)
        #print "\nviews.clinical: request.session.iteritems: %s" % request.session.iteritems
        #print "\nviews.clinical: request.session.iteritems: %s" % dir(request.session.iteritems)

        # First, we have to loop through the forms and make sure we have no
        # validation errors.
        forms = []
        valid = True


        for definition in form_definitions:
            form = instantiate_form(definition, request.POST)

            if not form.is_valid():
                valid = False

            #print "form: %s valid: %s" % (definition[0], valid)
            forms.append((definition[0], form, definition[2]))

        # check the consent form
        consent_form = ConsentForm(request.session.get("consentform"))
        if not consent_form or not consent_form.is_valid():
            valid = False
            return HttpResponseRedirect("index")

        # If there are validation errors, we'll just fall through: Django's
        # bound form functionality means this will just work if we go through
        # the normal display code.
        if valid:
            # So, we're valid. The first step to save the questionnaire is to
            # create a patient record.
            patient_form = PatientForm(request.session["patientform"])
            patient = patient_form.save()

            # Now we need a diagnosis.
            diagnosis = DiagnosisForm(request.POST, prefix="diagnosis").save(commit=False)
            diagnosis.patient = patient
            diagnosis.save()

            # Finally, we'll iterate through the forms and save them one by
            # one.
            for name, form, save in forms:
                save(form, diagnosis)

            # 2 steps required to get the consent object, add the diagnosis link to it and save it
            consent = consent_form.save(commit=False)
            consent.diagnosis = diagnosis
            #print "consent before save: %s dir: %s" % (consent, dir(consent))
            consent.save()

            # Clean up the session and prevent accidental multiple submissions.
            del request.session["patientform"]
            del request.session["consentform"]

            # Thanks, mysterious stranger!
            return HttpResponseRedirect("thanks")
    else:
        # Seriously, words cannot express how much I love list comprehensions.
        forms = [(form[0], instantiate_form(form), None) for form in form_definitions]

    return render_to_response("dm1/questionnaire/clinical.html", {
        "forms": forms, "family_name": family_name, "given_names": given_names
    }, context_instance=RequestContext(request))

def personal(request, country):
    if request.method == "POST":
        # Process the patient form. Since we'll do all the saving in one hit
        # after the clinical questionnaire has been filled out, all we need to
        # do here is validate the form and stash the POST data in the session
        # for later.

        # Sanitize some fields, all that code to make them show sanitized in the form
        postdata = request.POST.copy() # make a mutable copy of the POST QueryDict

        familyname = postdata.get('family_name')
        if familyname:
            postdata['family_name'] = stripspaces(familyname).upper()

        givennames = postdata.get('given_names')
        if givennames:
            postdata['given_names'] = stripspaces(givennames)

        form = PatientForm(postdata)
        if form.is_valid():
            request.session["patientform"] = postdata
            return HttpResponseRedirect("clinical")
    else:
        # get the first and last names form the consent form
        consentformdata = request.session.get("consentform")
        if not consentformdata:
            return HttpResponseRedirect("index")

        familyname = consentformdata.get('lastname')
        givennames = consentformdata.get('firstname')
        #print "familyname %s givennames %s" % (familyname, givennames)

        initialvalues = {'family_name': familyname, 'given_names': givennames}

        # make the first working group in the database the default one if there is only one
        # TODO: add a 'default' attribute to WorkingGroup
        workinggroups = WorkingGroup.objects.filter(name__icontains = "western")
        #print "workinggroups: %s" % workinggroups
        if workinggroups and len(workinggroups) == 1:
            defaultworkinggroup = workinggroups[0]
            initialvalues['working_group'] = defaultworkinggroup

        states = State.objects.filter(name__icontains = "western")
        #print "states: %s" % states
        if states and len(states) == 1:
            defaultstate = states[0]
            initialvalues['state'] = defaultstate

        countries = Country.objects.filter(name__icontains = "australia")
        #print "countries: %s" % countries
        if countries and len(countries) == 1:
            defaultcountry = countries[0]
            initialvalues['country'] = defaultcountry

        form = PatientForm(initial = initialvalues)

    #print "form: %s" % dir(form)
    #print "form.errors: %s" % dir(form.errors)
    #print "form errors: %s" % str(form.errors)
    return render_to_response("dm1/questionnaire/personal.html", { 
            "form": form, 
            "label": "Personal Details"
    },  context_instance=RequestContext(request))

def index(request, country):
    country_template = "dm1/questionnaire/%s/index.html" % country
    
    if request.method == "POST":
        form = ConsentForm(request.POST) if country == 'au' else ConsentFormNz(request.POST)
        if form.is_valid():
            request.session["consentform"] = request.POST.copy() # keep the data for the "personal" & "clinical" views
            return HttpResponseRedirect("personal")
        else:
            return render_to_response(country_template, {
                "form": form,
                "country": get_country(country)
            }, context_instance=RequestContext(request))
    else:
        form = ConsentForm if country == 'au' else ConsentFormNz()

    return render_to_response(country_template, {
        "form": form,
        "country": get_country(country)
    }, context_instance=RequestContext(request))

def thanks(request, country):
    return render_to_response("dm1/questionnaire/thanks.html", {})

def get_country(code):
    return "Australia" if code == 'au' else 'New Zealand'
