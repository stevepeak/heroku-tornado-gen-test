import os
from flask import Flask

import psycopg2

app = Flask(__name__)

@app.route('/')
def hello():

	conn_string = "dbname=d4jpcrom70fp6m host=ec2-54-243-180-196.compute-1.amazonaws.com user=yneijkjnhlvyji password=bWaC5ZAKxeBcjR18iStJq9BnbU port=5432 sslmode=require"
	#"host='localhost' dbname='my_database' user='postgres' password='secret'"
	# print the connection string we will use to connect
	print "Connecting to database\n	->%s" % (conn_string)
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
 
	# execute our Query
	cursor.execute("SELECT * FROM test")
 
	# retrieve the records from the database
	records = cursor.fetchall()
	return str(records)
		

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)