import http.client
httpcon = http.client.HTTPConnection('localhost',12345)
httpcon.request('GET', '/')
response = httpcon.getresponse()

print("response status: ",response.status)
print("response body: ",response.read().decode())
httpcon.close()