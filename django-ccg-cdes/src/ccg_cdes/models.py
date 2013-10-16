from django.db import models


def get_owner_choices():
    """
    Get choices for CDE owner drop down.
    Used to get the list of classes which CDEs can be attached to.
    UNUSED means this CDE will not be used to construct any forms in the registry.

    """
    from django.conf import settings
    choices = [('UNUSED', 'UNUSED')]
    for display_name, owner_model_func in settings.CDE_MODEL_MAP.items():
        owner_class_name = owner_model_func().__name__
        choices.append((owner_class_name, display_name))
    return choices

class CDEPermittedValueGroup(models.Model):
    code = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return "PVG %s:%s" % (self.code,self.name)

class CDEPermittedValue(models.Model):
    code = models.CharField(max_length=30, primary_key=True)
    value = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)
    pv_group = models.ForeignKey(CDEPermittedValueGroup,related_name='permitted_value_set')

    def __unicode__(self):
        return "PV %s:%s of %s" % (self.code,self.value,self.pv_group)

class CommonDataElement(models.Model):
    code = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    desc = models.TextField()
    datatype = models.CharField(max_length=50)
    instructions = models.TextField()
    references = models.TextField()
    population = models.CharField(max_length=30)
    classification = models.CharField(max_length=30)
    version = models.CharField(max_length=10)
    version_date = models.CharField(max_length=10)
    variable_name = models.CharField(max_length=30)
    aliases_for_variable_name = models.CharField(max_length=30)
    crf_module = models.CharField(max_length=30)
    subdomain = models.CharField(max_length=30)
    domain = models.CharField(max_length=30)
    disease = models.CharField(max_length=50)
    pv_group = models.ForeignKey(CDEPermittedValueGroup)

    OWNER_CHOICES = get_owner_choices()

    owner = models.CharField(max_length=50, choices=OWNER_CHOICES, default="UNUSED")

    def __unicode__(self):
        return "CDE %s:%s" % (self.code, self.name)

    def create_field(self):
        from django import forms

        choices = [('UNSET', '---')]  # default unselected option
        has_specify = False
        field_name = self.name
        for permitted_value in self.pv_group.permitted_value_set.all():
            choice_tuple = (permitted_value.code, permitted_value.value)
            print "added choice %s" % permitted_value.value
            choices.append(choice_tuple)

        if len(choices) - 1 == 0:
            # just have a pure data type
            if self.datatype == "Boolean":
                return forms.BooleanField(label=field_name, required=False)
            else:
                return forms.Textarea(label=field_name)

            #raise NotImplementedError("Pure datatype not yet")
        else:
            # choice field - ignore the "other - please specify for now
            # complication
            # add default unset option


            print "returning choices %s for field %s" % (choices, field_name)

            return forms.ChoiceField(choices=choices,label=field_name, initial='UNSET', required=True)


class CDEValue(models.Model):
    element = models.ForeignKey(CommonDataElement)
    owner_id = models.IntegerField()
    owner_class = models.CharField(max_length=50)   # the class name this cde value belongs to
    code = models.CharField(max_length=50)          # the code for this choice   ( e.g. PV001 etc )
    value = models.TextField()                      #the value selected or entered by the user



















