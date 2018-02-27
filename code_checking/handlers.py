from pymongo import MongoClient
import re
import subprocess

from vocabulary.ingest import IngestFields
from vocabulary.distribution import DistributionFields


def is_analytics_running():
    process = subprocess.Popen("ps aux | grep start_analytics_service",
                               shell=True,
                               stdout=subprocess.PIPE)
    stdout_list = process.communicate()[0].split('\n')
    regex_object = re.compile('start_analytics_service.py')
    for line in stdout_list:
        result = regex_object.search(line)
        if result is not None:
            return True
    return False


def event_document_to_ingest_data(event_doc):
    """
    Take an Event document and extract all data that was submitted by the ingest service.
    :param event_doc: A CRITs Event document.
    :type event_doc: dict
    :return: dict
    """
    ingest_data = {}
    for obj in event_doc['objects']:
        try:
            api_field_name = IngestFields.to_api_field_name(obj['type'])
            variable_type = IngestFields.api_field_to_variable_type(api_field_name)
        except ValueError:
            continue
        if variable_type == 'int':
            try:
                ingest_data[api_field_name] = int(obj['value'])
            except (TypeError, ValueError):
                # Database entry malformed.
                continue
        elif variable_type == 'array':
            if api_field_name not in ingest_data:
                ingest_data[api_field_name] = [obj['value']]
            else:
                ingest_data[api_field_name].append(obj['value'])
        else:
            ingest_data[api_field_name] = obj['value']
    client = MongoClient()
    ips = client.crits.ips
    for relationship in event_doc['relationships']:
        ip_id = relationship['value']
        ip_doc = ips.find_one(filter={'_id': ip_id})
        if ip_doc:
            ingest_data[IngestFields.IP_ADDRESS] = ip_doc['ip']
        else:
            print "Event object doesn't correspond to any IP object."
    return ingest_data


def ip_document_to_object_data(ip_doc):
    """
    Extract all data from the objects of the input IP document.
    Note: The return value of this function uses the object types defined by CRITs as the keys.
    :param ip_doc: A CRITs IP document
    :type ip_doc: dict
    :return: dict
    """
    ip_object_data = {}
    for obj in ip_doc['objects']:
        obj_type = obj['type']
        variable_type = None
        try:
            variable_type = DistributionFields.object_type_to_variable_type(obj_type)
        except ValueError:
            pass
        # Store objects which could have multiple values in a single array.
        if variable_type == 'array':
            if obj_type not in ip_object_data:
                ip_object_data[obj_type] = [obj['value']]
            else:
                ip_object_data[obj_type].append(obj['value'])
        else:
            ip_object_data[obj_type] = obj['value']
    return ip_object_data
