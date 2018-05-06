import base64
import urllib2

import pyodbc

# open a database connection
connection = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=testdb;UID=me;PWD=pass')
username = 'poppulo'
password = '***'

#Function to pull subscriber data from database
def pulldata(connection):
	# prepare a cursor object using cursor() method
	cursor = connection.cursor ()
	# execute the SQL query using execute() method.
	cursor.execute ("select email,first_name,surname,country,company,position_company,city,address1,postal_code from sometable")
	# fetch all of the rows from the query
	data = cursor.fetchall ()
	return data

#Create a password manager object, add credentials and root url to it
password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, 'https://api.newsweaver.com/v2/', username, password)
#create a handler and opendirectory objects
auth_handler = urllib2.HTTPBasicAuthHandler(password_manager)
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)

#xml data supported by poppulo for posting 
xmlparameters = '<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
					<subscriber_import_job>
						<accept_terms>true</accept_terms>
						<update_existing>true</update_existing>
						<reactivate_api_removed>false</reactivate_api_removed>
						<reactivate_admin_removed>false</reactivate_admin_removed>
						<reactivate_bounced_removed>false</reactivate_bounced_removed>
						<subscriber_data>
							<columns>email,name.first name,name.surname,address.country,company,position,address.address line 1,address.postal code,status</columns>
							<skip_first_line>false</skip_first_line>
							<field_separator>comma</field_separator>
							<data>
								<!-- Subscribers to create -->
								%s
								<!-- Subscribers to update -->
								update-subscriber3@example.com,Jack,Johnson,Custom Field Value 3,,ACTIVE
								update-subscriber4@example.com,Jill,Williams,Custom Field Value 4,,ACTIVE
								update-subscriber5@example.com,Jeff,Brown,Custom Field Value 5,,ACTIVE
								<!-- Subscribers to remove -->
								remove-subscriber6@example.com,June,Davis,Custom Field Value 6,Newsletter,OPT_OUT
							</data>
						</subscriber_data>
					</subscriber_import_job>',pulldata(connection)

# Poppulo API URI
theurl = 'https://api.newsweaver.com/v2/{account code}/subscriber_imports'

#encoding with base64
encodedstring = base64.encodestring(username+":"+password)[:-1]
auth = "Basic %s" % encodedstring
headers = {"Authorization": auth}

req = urllib2.Request(theurl, xmlparameters, headers)
req.add_header('Content-Type', 'application/xml; charset=utf-8')
req.add_header('Content-Length', len(xmlparameters))
handle = urllib2.urlopen(req)
