from django import forms
from django.utils.webhelpers import url
from models import *
from registry.forms.widgets import ComboWidget, LiveComboWidget, StaticWidget

from genetic.models import *

class GeneChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        print 'doing label from instance %i', obj.id
        return obj.symbol

    def prepare_value(self, value):
        print 'preparing value: ', str(value)
        #newval = ""
        #try:
        #    newval = Gene.objects.get(symbol=value).id
        #except:
        #    pass

        return super(GeneChoiceField, self).prepare_value(value)
        

    def validate(self, value):
        print 'validating model: ', value, str(dir(value)) 
        return super(GeneChoiceField, self).validate(value)

class VariationWidget(forms.TextInput):
    class Media:
        css = {"all": [url("/static/css/variation.css")]}
        js = [url("/static/js/json2.js"), url("/static/js/xhr.js"), url("/static/js/variation.js")]

    def __init__(self, attrs={}, backend=None, popup=None):
        """
        The backend will have genetic variation strings POSTed to it as plain
        text, and is expected to respond with a 204 No Content if the string is
        valid, or 400 Bad Request if the string isn't valid. In the latter
        case, a JSON array of strings containing the relevant errors should be
        returned.
        """

        attrs["backend"] = backend

        if popup:
            attrs["variation-popup"] = popup

        if "class" in attrs:
            attrs["class"] += " variation"
        else:
            attrs["class"] = "variation"

        super(VariationWidget, self).__init__(attrs)


class MolecularDataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MolecularDataForm, self).__init__(*args, **kwargs)
        # make the patient field static if not a new molecular data record
        if "instance" in kwargs:
            self.fields["patient"] = forms.ModelChoiceField(Patient.objects.all(), widget=StaticWidget(text=unicode(kwargs["instance"])))

    class Meta:
        model = MolecularData


class VariationForm(forms.ModelForm):
    gene = GeneChoiceField(queryset=Gene.objects.all(), label="Gene", widget=LiveComboWidget(backend=url("/admin/genetic/gene/search/")))
    exon = forms.CharField(label="Exon", required=False, widget=VariationWidget(backend=url("/admin/genetic/moleculardata/validate/exon"), attrs={"minchars": "0"}))
    protein_variation = forms.CharField(label="Protein variation", required=False, widget=VariationWidget(backend=url("/admin/genetic/moleculardata/validate/protein")))
    dna_variation = forms.CharField(label="DNA variation", required=False, widget=VariationWidget(backend=url("/admin/genetic/moleculardata/validate/sequence"), popup=url("/genetic/variation/")))
    rna_variation = forms.CharField(label="RNA variation", required=False, widget=VariationWidget(backend=url("/admin/genetic/moleculardata/validate/sequence"), popup=url("/genetic/variation/")))
    technique = forms.CharField(label="Technique", widget=ComboWidget(options=["MLPA", "Genomic DNA sequencing", "cDNA sequencing", "Array"]))

    class Meta:
        model = Variation
