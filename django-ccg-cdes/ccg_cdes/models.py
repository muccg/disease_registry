from django.db import models

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

    OWNER_CHOICES = (("Patient", "Patient"),
                     ("D", "Diagnosis"),
                     ("U", "Unused"))

    owner = models.CharField(max_length=1, choices=OWNER_CHOICES)

    def __unicode__(self):
        return "CDE %s:%s" % (self.code, self.name)

    def create_field(self, owner_model_class):
        from django import forms

        choices = []
        has_specify = False
        field_name = self.name
        for permitted_value in self.pv_group.permitted_value_set.all():
            choice_tuple = (permitted_value.value, permitted_value.desc)
            print "added choice %s" % permitted_value.value
            choices.append(choice_tuple)

        if len(choices) == 0:
            # just have a pure data type
            raise NotImplementedError("Pure datatype not yet")
        else:
            # choice field - ignore the "other - please specify for now
            # complication
            print "returning choices %s for field %s" % (choices, field_name)

            return forms.ChoiceField(choices=choices,label=field_name)


class CDEValue(models.Model):
    element = models.ForeignKey(CommonDataElement)
    owner_id = models.IntegerField()
    owner_class = models.CharField(max_length=50) # the class name this cde value belongs to
    data = models.TextField() # the value selected or entered by the user
    code = models.CharField(max_length=50) # the code for this choice



















