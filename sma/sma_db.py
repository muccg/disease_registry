import pprint
import json

from django.db.models import get_app
from django.db.models import get_models

apps =["sma", "genetic"]

models = []

for app_item in apps:
    app = get_app(app_item)

    for model in get_models(app):
        m = {}
        fields = []
        for field in model._meta.fields:
            fields.append(field.get_attname_column()[0])
        m[model._meta.db_table.replace("_",".")] = fields
        models.append(m)


pprint.pprint(models)

f = open("sma.json", "w")
f.write(json.dumps(models, indent=4))
f.close()
