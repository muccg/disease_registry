class BaseReport(object):

    def get_data(self):
        raise NotImplementedError("Implement me")
    
    def get_spec(self):
        raise NotImplementedError("Implement me")
    
    def get_value(self, key):
        data = self.get_data()
        parts = key.split(".")
        try:
            value = reduce(lambda data,part: data[part], parts, data)
            return value
        except KeyError:
            print "Key %s not found" % parts
            return "#ERROR"
    
    def get_header(self, ):
        header = [s[0] for s in self.get_spec()]
        return header
    
    def get_fields(self):
        fields = []
        for field in self.get_spec():
            fields.append(self.get_value(field[1]))
        return fields
    
    def write_with(self, writer):
        header = self.get_header()
        writer.writerow(header)
        
        writer.writerow(self.get_fields())
    