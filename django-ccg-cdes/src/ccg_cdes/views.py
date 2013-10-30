from django.shortcuts import render_to_response
from django.forms import BaseForm
from django.http import HttpResponseRedirect
from django.http import Http404
from django.conf import settings
from models import CDEValue, CommonDataElement
from django.core.context_processors import csrf
import logging

logger = logging.getLogger("dmd")

#todo generalise this to work across all owner types

def patient_cdes(request, patient_id):
    owner_model_func = settings.CDE_MODEL_MAP["Patient"]
    owner_model = owner_model_func()  # a Model _class_
    try:
        owner_instance = owner_model.objects.get(pk=patient_id)
    except owner_model.DoesNotExist:
        raise Http404("Patient does not exist")

    cde_map = {}
    field_map = {}

    for cde in CommonDataElement.objects.all().filter(owner='Patient'):
        logger.debug("got cde %s" % cde)
        cde_field = cde.create_field()
        field_name = cde.code
        cde_map[field_name] = cde
        field_map[field_name] = cde_field

    def get_data_for_instance(owner_instance):
        values = {}
        owner_class_name = owner_instance.__class__.__name__
        cdes = CDEValue.objects.all().filter(owner_class=owner_class_name, owner_id=owner_instance.pk)

        for field in field_map:
            cde_element = cde_map[field]  # The CDE Element corresponding to the field
            try:
                cde_value = cdes.filter(element=cde_element).get()
                values[cde_element.code] = cde_value.code
            except CDEValue.DoesNotExist:
                # may happen if we unset
                pass

        print "values for post = %s" % values
        return values

    class Media:
         css = {
            'all': ('dmd_admin.css',)
         }


    form_class = type('CDEForm', (BaseForm,), {"base_fields": field_map, 'Media': Media})

    def get_value_from_code(cde_field, code):
        for (c,v) in cde_field.choices:
            if c == code:
                return v

    if request.method == "POST":
        form = form_class(request.POST)
        print "in post"
        if form.is_valid():

            logger.debug("form is valid")
            # process data
            # update/create the associated CDEValues
            for field in form.fields:
                logger.debug("updating data from field %s" % field)
                code = form.cleaned_data[field]
                element = cde_map[field]
                cde_field = field_map[field]
                cde_value, created = CDEValue.objects.get_or_create(owner_class="Patient", owner_id=patient_id, element=element)
                if created:
                    logger.debug("created CDEValue for field")
                else:
                    logger.debug("updating existing data for field")

                if code == "UNSET":
                    # delete the value
                    cde_value.delete()
                    continue

                # store code and the value because later will support "Other please specify" ( which has a code but allows free value )
                cde_value.code = code
                if element.datatype in ['Boolean','String']:
                    value = form.cleaned_data[field]
                else:
                    value = get_value_from_code(cde_field, code)
                cde_value.value = value
                cde_value.save()
                logger.debug("CDEValue saved: %s" % cde_value)

            return HttpResponseRedirect('/cdes/patient/%s' % patient_id)
    else:
        form = form_class(get_data_for_instance(owner_instance))

    context = {'form': form, 'owner':  'patient',
                                        'owner_id': patient_id,
                                        'name': owner_instance.given_names + " " + owner_instance.family_name,
                }

    context.update(csrf(request))

    return render_to_response('ccg_cdes/cde.html', context )



