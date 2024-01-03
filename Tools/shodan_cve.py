"""script to query Shodan for CVE information and insert into PostgreSQL database"""
import configparser
import datetime
import time
import shodan
import psycopg2

# Shodan API key
def check_if_host_in_database(cur, ip_adddress, host_name):
    """check if host is already in database"""
    cur.execute("SELECT host_id FROM hosts WHERE ip_address = %s and  host_name = %s", (ip_adddress,host_name) )
    host_id = cur.fetchone()
    return host_id
def check_if_cve_in_database(cur, cve_number, port_number):
    """check if cve is already in database"""
    cur.execute("SELECT cve_id FROM cve WHERE cve_number = %s and port_number  = %s"  , (cve_number,port_number,) )
    cve = cur.fetchone()
    return cve

def shodan_search(api,conn):
    """Query Shodan for CVE information"""
    file = open("/home/piotr/Documents/IPs_shodan.csv", "r")
    #read file and create list of IPs
    ip_list = []
    cur = conn.cursor()
    for line in file:
        ip_list.append(line.strip())
    file.close()
    for ip in ip_list:
        #sleep time to avoid api limit
        sleep_time = 10
        time.sleep(sleep_time)
        try:
            results = api.search(ip, page=1)
        except shodan.APIError as e:
            print(ip)
            print(f"!!!!!!!!!!!!!!Shodan error: {e}")
            continue
        print(f"Results found: {results['total']}")
        print(f"Results: {(len(results['matches']))}")
        for result in results['matches']:
            ip_adddress = result['ip_str']
            host_name = result['hostnames']
            #if host_name is empty set to None
            if len(host_name) == 0:
                host_name = 'None'
            os_version = result['os']
            host_id  = check_if_host_in_database(cur, ip_adddress, host_name[0])
            #if host is not in database insert it and get host_id
            if host_id is None:
                insert_query = """ INSERT INTO hosts (host_name, ip_address, ips_network_interfaces, os_version) VALUES (%s,%s,%s,%s) returning host_id"""
                insert_values = (host_name[0], ip_adddress, "None", os_version)
                cur.execute(insert_query, insert_values)
                host_id = cur.fetchone()[0]
                conn.commit()
            else:
                host_id = host_id[0]
            port_number = result['port']
            protocol = result['transport']
            #if product and version is empty set to None
            if 'product' in result:
                software_name = result['product']
            else:
                software_name = 'None'
            if  'version' in result:
                software_version = result['version']
            else:
                software_version = 'None'

            cves = result.get('vulns', '')
            #insert cves into database
            for cve_number in cves:
                if cves[cve_number]['cvss']:
                    cvss = cves[cve_number]['cvss']
                    verified = cves[cve_number]['verified']
                    print(f"cve {cve_number}  has cvss {cvss}  and verified {verified}")
                    cve_id  = check_if_cve_in_database(cur, cve_number, port_number)
                    if cve_id is None:
                        insert_query = """ INSERT INTO cve (cve_number, cve_severity, cvss, cvss_vector, software_name, software_vendor, software_version, software_type, port_number, protocol, detection_source) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) returning cve_id"""
                        insert_values = (cve_number, "None", cvss, "None", software_name, "None", software_version, "None", port_number, protocol, "shodan")
                        cur.execute(insert_query, insert_values)
                        cve_id = cur.fetchone()[0]
                        conn.commit()
                    else:
                        cve_id = cve_id[0]
                    curent_date = datetime.datetime.now()
                    insert_query = """ INSERT INTO host_cve (host_id, cve_id, detection_date) VALUES (%s,%s,%s)"""
                    insert_values = (host_id, cve_id, curent_date)
                    cur.execute(insert_query, insert_values)
                    conn.commit()
                    print(f"host: {ip_adddress}  on port {port_number}  running {software_name}  version {software_version}  protocol {protocol}  has {len(cves)}  cves")
                else:
                    print(f"cve {cve_number}  has no cvss")
                    continue
    cur.close()
# Initialize the Shodan API
def main():
    """Connect to the PostgreSQL database server and shodan API"""
    config = configparser.ConfigParser()
    pathtoconfig = '/home/piotr/Documents/VulnDataMana.ini'
    config.read(pathtoconfig)
    hostname = config['POSTGRES']['hostname']
    username = config['POSTGRES']['username']
    password = config['POSTGRES']['password']
    database = config['POSTGRES']['database']
    shodan_api_key = config['SHODAN']['key']
    api = None
    conn = None
    try:
        api = shodan.Shodan(shodan_api_key)
    except shodan.APIError as e:
        print(f"Shodan error: {e}")
    try:
        conn = psycopg2.connect(host=hostname, database=database, user=username, password=password)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None and api is not None:
            shodan_search(api,conn)
            conn.close()
            print('Database connection closed.')

if __name__ == '__main__':
    main()
