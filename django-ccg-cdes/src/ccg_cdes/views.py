from django.shortcuts import render_to_response
from django.forms import Form
from django.http import HttpResponseRedirect
from django.http import Http404
from django.conf import settings
from models import CDEValue, CommonDataElement
from django.core.context_processors import csrf

#todo generalise this to work across all owner types

def patient_cdes(request, patient_id):
    owner_model_func = settings.CDE_MODEL_MAP["Patient"]
    owner_model = owner_model_func()  # a Model _class_
    try:
        owner_instance = owner_model.objects.get(pk=patient_id)
    except owner_model.DoesNotExist:
        raise Http404("Patient does not exist")

    class CDEForm(Form):
        pass

    cde_map = {}
    field_map = {}

    for cde in CommonDataElement.objects.all().filter(owner='Patient'):
        print "got cde %s" % cde
        cde_field = cde.create_field()
        field_name = "cde_" + cde.name
        cde_map[field_name] = cde
        field_map[field_name] = cde_field
        setattr(CDEForm, field_name, cde_field)

    def get_data_for_instance(self, owner_instance):
        values = {}
        owner_class_name = owner_instance.__class__.__name__
        cdes = CDEValue.objects.all().filter(owner_class=owner_class_name, owner_id=owner_instance.pk)
        for field in self.fields:
            cde_element = field_map[field]  # The CDE Element corresponding to the field
            cde_value = cdes.filter(element=cde_element).get()
            if cde_value:
                values[cde_value.code] = cde_value.value







    real_form_dict = {}

    for k, v  in CDEForm.__dict__.items():
        real_form_dict[k] = v



    form_class = type('CDEForm', (Form,), real_form_dict)

    def get_value_from_code(cde_field, code):
        for (c,v) in cde_field.choices:
            if c == code:
                return v

    if request.method == "POST":
        form = form_class(request.POST)

        if form.is_valid():
            # process data
            # update/create the associated CDEValues
            for field in form.fields:
                code = form.cleaned_data[field]
                if code == "UNSET":
                    continue
                element = cde_map[field]
                cde_field = field_map[field]
                cde_value, created = CDEValue.objects.get_or_create(owner_class="Patient", owner_id=patient_id, element=element)

                # store code and the value because later will support "Other please specify" ( which has a code but allows free value )
                cde_value.code = code
                value = get_value_from_code(cde_field, code)
                cde_value.value = value
                cde_value.save()

            return HttpResponseRedirect('/cdes/patient/%s' % patient_id)
    else:
        form = form_class()

    context = {'form': form,
                                        'owner':  'patient',
                                        'owner_id': patient_id,
                                        'name': owner_instance.given_names + " " + owner_instance.family_name,
                }

    context.update(csrf(request))

    return render_to_response('ccg_cdes/cde.html', context )



