import xml.etree.ElementTree as ET

class ReportParser(object):
    CDE_CODE = 'textbox12'
    CDE_NAME = "VariableName"
    CDE_DATATYPE = 'textbox26'
    GROUP_CODE = "textbox22"
    PV_CODE = "textbox34"
    PV_VALUE = "textbox7"


    def parse_file(self, xml_file_name):
        cdes = {}
        groups = {}

        tree = ET.parse(xml_file_name)
        root = tree.getroot()
        table1 = root.getchildren()[0]
        group1coll = table1.getchildren()[0]
        for g1 in group1coll.getchildren():
            code = g.get(self.CDE_CODE)
            if not code in cdes:
                cdes[code] = {}

            cde[code]['datatype'] = g.get(self.CDE_DATATYPE)
            cde[code]["name"] = g.get(self.CDE_NAME)

            g2coll = g1.getchildren()[0]
            g2 = g2coll.getchildren()[0]
            group_code = g2.get(self.GROUPCODE)
            cde[code]["group_code"] = group_code
            if not group_code in groups:
                groups[group_code] = []


            detailcoll = g2.getchildren()[0]
            details = detailcoll.getchildren() # ugh
            for detail in details:
                pv_code = detail.get(self.PV_CODE)
                pv_value = detail.get(self.PV_VALUE)
                pair = (pv_code, pv_value)
                if not pair in groups[code]:
                    groups[code].append(pair)


        return cdes, groups

    def create_groups(self, groups):
        from models import CDEPermittedValueGroup, CDEPermittedValue
        for group_code in groups:
            group = groups[group_code]

            try:
                pvg = CDEPermittedValueGroup.objects.all().filter(code=group_code).get()
            except CDEPermittedValueGroup.DoesNotExist:
                pvg = CDEPermittedValueGroup(code=group_code, name=groups)
                pairs = groups[group_code]







