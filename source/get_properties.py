import os


class GetProperties:
    __instance = None

    def __init__(self):
        self.properties = {}

    @staticmethod
    def get_inst():
        if GetProperties.__instance is None:
            GetProperties.__instance = GetProperties()
        return GetProperties.__instance

    def get_properties(self):
        paths = [os.path.curdir, '../source/driver.properties']
        for path in paths:
            try:
                with open(path) as properties_file:
                    self.create_properties_dict(properties_file)
            except (PermissionError, FileNotFoundError):
                pass
            else:
                break

    def create_properties_dict(self, properties_file):
        for line in properties_file:
            try:
                key, value = line.split('=')
                self.properties[key.rstrip()] = value.rstrip()
            except:
                pass

    def get_property(self, property_name):
        return self.properties[property_name]
