"""Script to create a tables for the database"""
import configparser
import  psycopg2



def create_tables(conn):
    """Create tables in the PostgreSQL database"""
    commands = (
        """
      CREATE TABLE hosts (
    host_id SERIAL PRIMARY KEY,
    host_name TEXT NOT NULL,
    ip_address INET NOT NULL,
    ips_network_interfaces TEXT NOT NULL,
    os_version TEXT
    )
            """)
    commands2 = (
         """
      CREATE TABLE cve (   
    cve_id SERIAL PRIMARY KEY,
    cve_number TEXT NOT NULL,
    cve_severity TEXT NOT NULL,
    cvss TEXT NOT NULL,
    cvss_vector TEXT NOT NULL,
    software_name TEXT NOT NULL,
    software_vendor TEXT NOT NULL,
    software_version TEXT NOT NULL,
    software_type TEXT NOT NULL,
    port_number INTEGER NOT NULL,
    protocol TEXT NOT NULL,
    detection_source TEXT NOT NULL
    )
        """)
    commands3 = (
        """
    CREATE TABLE host_cve (
    host_cve_id SERIAL PRIMARY KEY,
    host_id INTEGER REFERENCES hosts(host_id),
    cve_id INTEGER REFERENCES cve(cve_id),
    detection_date DATE NOT NULL
    
)
        """)
    cur = conn.cursor()
    cur.execute(commands)
    cur.execute(commands2)
    cur.execute(commands3)
    cur.close()
    conn.commit()

def main():
    """Connect to the PostgreSQL database server"""
    config = configparser.ConfigParser()
    pathtoconfig = '/home/piotr/Documents/VulnDataMana.ini'
    config.read(pathtoconfig)
    hostname = config['POSTGRES']['hostname']
    username = config['POSTGRES']['username']
    password = config['POSTGRES']['password']
    database = config['POSTGRES']['database']
    conn = None
    try:
        # read connection parameters
        # connect to the PostgreSQL server
        conn = psycopg2.connect(host=hostname, database=database, user=username, password=password)
        create_tables(conn)
        # close communication with the PostgreSQL database server
        conn.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
if __name__ == '__main__':
    main()
    # End-of-file (EOF)