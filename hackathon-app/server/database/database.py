

import ibm_db
import os
import ibm_db_dbi
from dotenv import load_dotenv


def connectToDB2():
    load_dotenv()
    host = os.getenv('HOSTNAME')
    port = os.getenv('PORTNUMBER')
    uid = os.getenv('USERID')
    pwd = os.getenv('PASSWORD')
    conn_str = 'database=bludb;hostname=' + host + ';port=' + port +';protocol=tcpip;uid=' + uid + ';pwd=' + pwd +';SECURITY=SSL;'

    print("=> Creating the connection")
    try:
        connection = ibm_db.connect(conn_str, "", "")
        conn = ibm_db_dbi.Connection(connection)
        print("=> Connected to Server ... SUCCESSFULL")
    except:
        print("=> Connection to server .... FAILED")
        print("Connection string:" + conn_str)
        print("Error Description = " + ibm_db.conn_errormsg())
        print("SQLSTATE = " + ibm_db.conn_error())
        exit(0)
    # ibm_db.exec_immediate(connection, create)
    # t = results(tables(connection))
    # sql = 'LIST * FROM ' + t[170]['TABLE_NAME']  # Using our list of tables t from before
    # rows = results(ibm_db.exec_immediate(connection, sql))
    return conn

def fetchData(conn):
    conn.tables('QWC17901', '%')
    select="select * from JOB_POSTINGS"
    cur = conn.cursor()
    cur.execute(select)
    row=cur.fetchall()

    jobs = []
    for i in range(19):
        jobs.append(row[i])

    return jobs


def results(command):

    ret = []
    result = fetch_assoc(command)
    while result:
        ret.append(result)
        result = fetch_assoc(command)
    return ret  # Ditch this line if you choose to use a generator.



