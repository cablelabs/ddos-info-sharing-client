import datetime
import json
import operator
import random
import re
import string

import ipaddress


def generate_test_ingest_data_files(limit=10):
    ingest_data_with_all_fields = generate_ingest_data_list(limit, 100)
    ingest_data_half_with_all_fields = generate_ingest_data_list(limit, 50)
    ingest_data_no_optional_fields = generate_ingest_data_list(limit, 0)
    ingest_data_with_all_fields_json = {"ingestData": ingest_data_with_all_fields}
    ingest_data_half_with_all_fields_json = {"ingestData": ingest_data_half_with_all_fields}
    ingest_data_no_optional_fields_json = {"ingestData": ingest_data_no_optional_fields,}
    ingest_data_directory = "ingest_data"
    create_config_json(ingest_data_with_all_fields_json, ingest_data_directory+"/all_fields.json")
    create_config_json(ingest_data_half_with_all_fields_json, ingest_data_directory+"/half_with_all_fields.json")
    create_config_json(ingest_data_no_optional_fields_json, ingest_data_directory+"/no_optional_fields.json")


def generate_ingest_data_list(limit, percent_data_all_fields):
    """
    Return a list of 'limit' objects to use for the 'ingestData' field of the data ingester API call.
    
    :param limit: The maximum number of entries to return. Ideally, we return exactly this many entries.
    :type limit: int
    :param percent_data_all_fields: The maximum percentage of generated data that should include all optional fields.
    All other data will have none of the optional fields.
    :type percent_data_all_fields: float
    :return: list of dictionaries, each conforming to 'ingestDataItem' object in data ingester input schema
    :raise ValueError: 'percent_data_all_fields' is not within 0 and 100, inclusive.
    """
    with open('dshield-data.txt', 'r') as infile:
        file_lines = infile.readlines()
    # These indices indicate which sets of lines contain actual IP data.
    first_ip_line_index = 9
    last_ip_line_index = 10009
    # TODO: should I throw error beforehand if "limit" is too big?
    random_file_lines = random.sample(file_lines[first_ip_line_index:last_ip_line_index], limit)
    number_of_entries_with_optional_fields = limit * (percent_data_all_fields / 100.0)
    ingest_data_list = []
    for line in random_file_lines:
        record = line.strip()
        include_optional_fields = float(len(ingest_data_list)) < number_of_entries_with_optional_fields
        new_ingest_data = create_ingest_data_from_record(record, include_optional_fields)
        ingest_data_list.append(new_ingest_data)
    return ingest_data_list


def create_ingest_data_from_record(record, include_optional_fields):
    """
    Create a new ingest data object from the input record.    
    
    :param record: A line from the file 'dshield-data.txt'.
    :type record: str
    :param include_optional_fields: Indicates whether to include all optional fields. Otherwise, exclude all optional fields.
    :type include_optional_fields: bool
    :return: dict, conforming to 'ingestDataItem' object in data ingester input schema
    """
    data = record.split()

    # Remove leading zeros
    ipstring = re.sub('\.00?', '.', data[0].lstrip('0'))

    # Parse if this is valid dshield formatted data
    try:
        # NOTE: Zane added 'unicode()' around the string so it would work in Python 2.7.
        ip_address = ipaddress.IPv4Address(unicode(ipstring))
        #p_count = int(data[1])
        #targets = int(data[2])
        attack_start_time = datetime.datetime.strptime(data[3], '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
        attack_stop_time = datetime.datetime.strptime(data[4], '%Y-%m-%d').strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    except (ValueError, IndexError):
        raise Exception('Bad input provided: {record}'.format(record=record))

    # Put the parsed info into the JSON structure.
    if include_optional_fields:
        entry = {
            'IPaddress': str(ip_address),
            # TODO: how generate random dates? not very important at the moment.
            'attackStartTime': attack_start_time,
            'attackStopTime': attack_stop_time,
            'attackTypes': random_attack_types(),
            'totalBytesSent': random.randint(0, 999999),
            'totalPacketsSent': random.randint(0, 999999),
            'peakBPS': random.randint(0, 999999),
            'peakPPS': random.randint(0, 999999),
            'sourcePort': random.randint(0, 999999),
            'destinationPort': random.randint(0, 999999),
            'protocol': random_string(10)
        }
    else:
        entry = {'IPaddress': str(ip_address)}
    return entry


def random_attack_types():
    potential_attack_types = [
        'chargen Amplification',
        'DNS',
        'DNS Amplification',
        'IP Fragmentation',
        'NTP Amplification',
        'SSDP Amplification',
        'TCP NULL',
        'TCP RST',
        'TCP SYN',
        'Total Traffic',
        'UDP'
    ]
    number_of_attack_types = random.randint(1, len(potential_attack_types))
    indices = random.sample(range(0, len(potential_attack_types)), number_of_attack_types)
    attack_types = operator.itemgetter(*indices)(potential_attack_types)
    if number_of_attack_types > 1:
        return list(attack_types)
    return [attack_types]


def random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


# Currently unused because we get IP addresses from dshield-data.txt, not by randomly generating IPs.
def random_ipv6():
    return str(ipaddress.IPv6Address(random.randint(0, 2**128-1)))


def create_config_json(config_dict, file_name):
    with open(file_name, 'w') as config_file:
        json.dump(config_dict, config_file, indent=4)
    return
