import json
import requests


def send_ingest_data(username, api_key, input_data):
    """
    Send data to the data ingester service through a POST request using the exposed API.
    :param username: The name of the user submitting data.
    :type username: str
    :param api_key: The API key of the given user, which is required to access data.
    :type api_key: str
    :param input_data: The JSON packet to send in our POST message to the ingester service.
    :type input_data: dict, ideally formatted to ingest JSON schema
    :return: dict, with the following fields
            "is_error": bool, indicating if any errors occurred
            "errors": array of strings indicating errors, if any
    """
    config_json_file = open('config.json')
    config_json = json.load(config_json_file)
    url_user_info = '/?username=' + username + "&api_key=" + api_key
    post_url = config_json['ingest_url'] + url_user_info
    max_number_items_to_send = 300
    ingest_data = input_data.get('ingestData')
    results = {
        'is_error': False,
        'errors': []
    }
    if ingest_data is not None:
        start = 0
        while start < len(ingest_data):
            end = start + max_number_items_to_send
            partial_ingest_data = ingest_data[start:end]
            post_data = {
                'ProviderName': input_data['ProviderName'],
                'ingestData': partial_ingest_data
            }
            response = requests.post(url=post_url,
                                     data=json.dumps(post_data),
                                     headers={'content-type': 'application/json'})
            # TODO: will .json() conversion fail if not 200 message?
            response = response.json()
            if response['return_code'] == 1:
                results['errors'].append(response['message'])
            # Increment starting index of ingest data chunk.
            start = end
    if len(results['errors']) > 0:
        results['is_error'] = True
    return results
