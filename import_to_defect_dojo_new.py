import requests
import sys
import os

# Define the proxy
proxy = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

def uploadToDefectDojo(is_new_import, token, url, product_name, engagement_name, filename, scan_type,test_title):
    multipart_form_data = {
        'file': (filename, open(filename, 'rb')),
        'scan_type': (None, scan_type),
        'product_name': (None, product_name),
        'engagement_name': (None, engagement_name),
        'test_title': (None, test_title)
    }

    endpoint = '/api/v2/import-scan/' if is_new_import else '/api/v2/reimport-scan/'
    r = requests.post(
        url + endpoint,
        files=multipart_form_data,
        headers={
            'Authorization': 'Token ' + token,
        }
        #proxies=proxy,
        #verify=False
    )

    print(r.status_code)
    if r.status_code not in [200, 201]:
        sys.exit(f'Post failed: {r.text}')
    print(r.text)



if __name__ == "__main__":
    try:
        token = os.getenv("DEFECT_DOJO_API_TOKEN")
    except KeyError: 
        print("Please set the environment variable DEFECT_DOJO_API_TOKEN") 
        sys.exit(1)
    if len(sys.argv) == 13:
        url = sys.argv[2]
        product_name = sys.argv[4]
        engagement_name = sys.argv[6]
        report = sys.argv[8]
        scan_type = sys.argv[10]
        print(scan_type)
        test_title = sys.argv[12]
        print(test_title)
        #uploadToDefectDojo(False, token, url, product_name, engagement_name, report,scan_type,test_title)
    else:
        print(
            'Usage: python3 import_to_defect_dojo.py --host DOJO_URL --product PRODUCT_NAME --engagement ENGAGEMENT_NAME --report REPORT_FILE --scan-type SCAN_TYPE')
