import httplib
import json
import web

conn = httplib.HTTPConnection('0.0.0.0', 8080)
jsonheader = { 'Content-type': 'application/json' }

print "Creating a new scan..."
data = json.dumps([
    [5.0, 7.0, -3.4],
    [8.0, 5.0 ,2.2],
    [10.0, 12.0, 6],
    [15.1, 9.2, 2.2],
    [9.3, 10.2, 3.1]])
conn.request('POST', '/scans', data, jsonheader)
response = conn.getresponse()
print "Status: " + str(response.status)
print "Body: " + response.read()
newscan = response.getheader('Location').split('/')[-1]

print "\nGetting the new scan..."
conn.request('GET', '/scans/' + newscan)
response = conn.getresponse()
print "Status: " + str(response.status)
print "Body: " + response.read()

print "\nGetting the scan bounding box..."
conn.request('GET', '/scans/' + newscan + '/boundingbox')
response = conn.getresponse()
print "Status: " + str(response.status)
print "Body: " + response.read()

print "\nUpdating the scan..."
data = json.dumps({ 'id': newscan, 'points': [
    [5.0, 7.0, -3.4],
    [8.0, 5.0 ,2.2],
    [9.0, 11.0, 6],
    [15.1, 9.2, 2.2],
    [9.3, 10.2, 3.1]]})
conn.request('PUT', '/scans/' + newscan, data, jsonheader)
response = conn.getresponse()
print "Status: " + str(response.status)
print "Body: " + response.read()

print "\nGetting the updated scan..."
conn.request('GET', '/scans/' + newscan)
response = conn.getresponse()
print "Status: " + str(response.status)
print "Body: " + response.read()

print "\nGetting a non existent scan..."
conn.request('GET', '/scans/' + '2')
response = conn.getresponse()
print "Status: " + str(response.status)
print "Body: " + response.read()

print "\nCreating a scan with a known id..."
identifier = 10
data = json.dumps({ 'id': identifier, 'points': [
    [5.0, 7.0, -3.4],
    [8.0, 5.0 ,2.2],
    [9.0, 11.0, 6],
    [15.1, 9.2, 2.2],
    [9.3, 10.2, 3.1]]})
conn.request('PUT', '/scans/' + str(identifier), data, jsonheader)
response = conn.getresponse()
print "Status: " + str(response.status)
print "Body: " + response.read()

print "\nCreating a new scan..."
data = json.dumps([
    [5.0, 7.0, -3.4],
    [8.0, 5.0 ,2.2],
    [10.0, 12.0, 6],
    [15.1, 9.2, 2.2],
    [9.3, 10.2, 3.1]])
conn.request('POST', '/scans', data, jsonheader)
response = conn.getresponse()
print "Status: " + str(response.status)
print "Body: " + response.read()
newscan = response.getheader('Location').split('/')[-1]

print "\nGetting the newest scan..."
conn.request('GET', '/scans/' + newscan)
response = conn.getresponse()
print "Status: " + str(response.status)
print "Body: " + response.read()
