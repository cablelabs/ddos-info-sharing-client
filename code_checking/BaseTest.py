import json


class BaseTest:
    """
    This is a base class that loads data from config files. The data is used in tests defined in inheriting classes.
    """

    def __init__(self):
        admin_login_file_path = "login_json_files/local_admin_login.json"
        with open(admin_login_file_path, 'r') as admin_login_file:
            self.admin_login = json.load(admin_login_file)
        ingest_data_directory = "ingest_data"
        ingest_data_all_fields_file_path = ingest_data_directory + "/all_fields.json"
        self.ingest_data_all_fields = self.load_ingest_data(ingest_data_all_fields_file_path)
        ingest_data_half_with_all_fields_file_path = ingest_data_directory + "/half_with_all_fields.json"
        self.ingest_data_half_with_all_fields = self.load_ingest_data(ingest_data_half_with_all_fields_file_path)
        ingest_data_no_optional_fields_file_path = ingest_data_directory + "/no_optional_fields.json"
        self.ingest_data_no_optional_fields = self.load_ingest_data(ingest_data_no_optional_fields_file_path)
        self.ingest_data_samples = [
            self.ingest_data_all_fields,
            self.ingest_data_half_with_all_fields,
            self.ingest_data_no_optional_fields
        ]

    @staticmethod
    def load_ingest_data(file_path):
        with open(file_path, 'r') as ingest_file:
            ingest_data_json = json.load(ingest_file)
            return ingest_data_json['ingestData']
