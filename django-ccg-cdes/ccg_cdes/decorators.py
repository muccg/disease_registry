from models import CommonDataElement, CDEValue



def add_cdes(owner):
    def decorator(form_cls):
        owner_model = form_cls.Meta.model
        for cde in CommonDataElement.objects.all().filter(owner=owner):
            field_name = "cde_" + cde.name

            def getter(self):
                my_id = self.id
                cde_value = CDEValue.objects.all().filter(owner_id=my_id,owner_class=owner).get()
                if cde_value:
                    return cde_value.data
                else:
                    return ""

            def setter(self, value):
                my_id = self.id
                cde_value = CDEValue.objects.all().filter(owner_id=my_id,owner_class=owner).get()
                if cde_value:
                    cde_value.data = value
                    cde_value.save()

                else:
                    cde_value = CDEValue(owner_id=my_id, owner_class=owner,data=value)
                    cde_value.save()

            prop = property(getter, setter)
            setattr(owner_model,field_name, prop)






        old_init = form_cls.__init__

        def new__init__(self, *args, **kwargs):
            print "in new init - calling the old init"
            old_init(self, *args, **kwargs)
            print "old init called - now adding cde field. looking for cdes with owner %s" % owner

            if not kwargs.has_key('instance'):

                for cde in CommonDataElement.objects.all().filter(owner=owner):
                    cde_field = cde.create_field(owner_model)
                    field_name = "cde_" + cde.name
                    self.fields[field_name] = cde_field
                    self.base_fields[field_name] = cde_field
                    print "added field %s" % field_name


                print "fields = %s" % self.fields
                for field_name in self.fields:
                    field = self.fields[field_name]
                    for attr in  field.__dict__:
                        v = getattr(field, attr)
                        if not callable(v):
                            print "field %s.%s = %s" % (field_name, attr, v)


                print "dir(self) = %s" % str(dir(self))
                print "visible fields = %s" % self.visible_fields
                setattr(form_cls.Meta , "fields", self.fields.keys())
                setattr(form_cls.Meta, 'declared_fields', self.fields.keys())


        form_cls.__init__ = new__init__
        print "created new __init__"
        print "new form class created"
        return form_cls
    return decorator
