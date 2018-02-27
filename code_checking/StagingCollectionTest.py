import csv
from datetime import datetime
import pendulum
from pymongo import MongoClient

from send_ingest_data import send_ingest_data
from BaseTest import BaseTest
import handlers
from vocabulary.ingest import IngestFields


class StagingCollectionTest(BaseTest):
    """
    This class performs tests to check that all data submitted to the ingest service was saved to the
    staging_crits_data.new_events collection.
    Note: Code does allow duplicates (documents with all fields except ID the same) to exist in staging collection,
    but this test does not submit duplicates.
    """

    def run_tests(self):
        print "Staging Collection Test, with data submitted by Admin"
        if handlers.is_analytics_running():
            raise Exception("Analytics service still running. Service should be shutdown before running test.")
        client = MongoClient()
        staging_new_events = client.staging_crits_data.new_events
        username = self.admin_login['username']
        api_key = self.admin_login['api_key']
        source = self.admin_login['source_name']
        for ingest_data in self.ingest_data_samples:
            staging_new_events.delete_many({})
            input_data = {
                'ProviderName': source,
                'ingestData': ingest_data
            }
            results = send_ingest_data(username, api_key, input_data)
            if results['is_errors']:
                print "Errors occured."
                print results['errors']

            # Wait until ingest process adds all data to staging collection, and see how long it takes.
            start_time = pendulum.now()
            while staging_new_events.count() < len(ingest_data):
                continue
            duration = pendulum.now() - start_time
            print "All data ingested."
            with open('ingest_save_times.csv', 'a') as times_file:
                times_writer = csv.writer(times_file)
                row = [len(ingest_data), duration]
                times_writer.writerow(row)

            # Check that documents in staging collection have fields added by ingest service, with correct types.
            for staging_event_doc in staging_new_events.find():
                if 'analyst' not in staging_event_doc:
                    print "'analyst' missing from staged entry."
                elif not isinstance(staging_event_doc['analyst'], basestring):
                    print "'analyst' is not a string."
                if 'source' not in staging_event_doc:
                    print "'source' missing from staged entry."
                elif not isinstance(staging_event_doc['source'], basestring):
                    print "'source' is not a string."
                if 'timeReceived' not in staging_event_doc:
                    print "'timeReceived' missing from staged entry."
                elif not isinstance(staging_event_doc['timeReceived'], datetime):
                    print "'timeReceived' is not a datetime object."

            # Check that each submitted item appears in staging collection.
            for ingest_data_item in ingest_data:
                ip_address = ingest_data_item[IngestFields.IP_ADDRESS]
                staging_event_docs = staging_new_events.find(filter={IngestFields.IP_ADDRESS: ip_address})
                if not staging_event_docs:
                    print "No data exists for IP '" + ip_address + "'."
                    continue
                # Search for ingest data within staging documents.
                for staging_event_doc in staging_event_docs:
                    if username != staging_event_doc.get('analyst') or source != staging_event_doc.get('source'):
                        continue
                    for key, value in ingest_data_item.iteritems():
                        if key not in staging_event_doc or value != staging_event_doc[key]:
                            # Found field in ingest item that does not have expected value in staging doc.
                            break
                    else:
                        # Final check that staging doc does not have extraneous data.
                        all_keys = ingest_data_item.keys()
                        all_keys.extend(['_id', 'analyst', 'source', 'timeReceived'])
                        for key in staging_event_doc.keys():
                            if key not in all_keys:
                                print "Additional key found:", key
                                break
                        else:
                            # Found staging doc that matches ingest item.
                            break
                else:
                    print "No staging IP matches current ingest item."
        return


staging_test = StagingCollectionTest()
staging_test.run_tests()
