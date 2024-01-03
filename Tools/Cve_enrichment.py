import requests
import json
import psycopg2
import nvdlib
import configparser

def cvss_vector_query(cve_number):
    r = requests.get('https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=' + cve_number,  verify=False, timeout=60)
    jsons = json.loads(r.text)
    cvss_version =  jsons['vulnerabilities'][0]['cve']['metrics']
    if "cvssMetricV31" in cvss_version:
        cvs31 = jsons['vulnerabilities'][0]['cve']['metrics']['cvssMetricV31']
        for  source in cvs31:
            if source['source'] == "nvd@nist.gov":
                cvss_vector = source['cvssData']['vectorString']
    return cvss_vector

"""Connect to the PostgreSQL database server and shodan API"""
config = configparser.ConfigParser()
pathtoconfig = '/home/piotr/Documents/VulnDataMana.ini'
config.read(pathtoconfig)

table_name = "MISP_feeds"
# Enter all authentication info
DB_hostname = config['POSTGRES']['hostname']
DB_username = config['POSTGRES']['username']
DB_password = config['POSTGRES']['password']
database = config['POSTGRES']['database']



conn = psycopg2.connect(host=DB_hostname, user=DB_username, password=DB_password, dbname=database)
cur = conn.cursor()
commands = "SELECT cve_number, cve_id FROM cve where cvss_vector = 'None' "
cur.execute(commands)  

records = cur.fetchall()
print(records)
for cve_data in records:
    print(cve_data[0])
    try:
        r = nvdlib.searchCVE(cveId=cve_data[0])[0]
        cvss_vector_results = r.v31vector
        #cvss_vector_results = cvss_vector_query(cve_data[0], proxy)
        print(cvss_vector_results)
        print("cve_ide: "+str(cve_data[1]))
        print("cve_number: "+str(cve_data[0]))
        command  =  "UPDATE cve set cvss_vector = %s where cve_id = %s and cve_number = %s "
        record_to_insert = (cvss_vector_results ,cve_data[1] ,cve_data[0])
        cur.execute(command, record_to_insert)
        #records = cur.fetchall()
        conn.commit()
        #print(records)
    except Exception as e:
        print("ERROR !!")
        print(cve_data[0])
        print(e)

