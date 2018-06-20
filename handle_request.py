# this module will process and identify the requested serivce


import search_file
import make_header

def request_Parser(request_str):
	''' proceesing the request and return the service if possibel '''
	print 'the service requested :{}'.format(str(request_str.split(' ')[1]))
	print 'the service method    :{}'.format(request_str.split(' ')[0])
	print 'the Http method       :{}'.format(request_str.split(' ')[2][0:8])
	req_service=request_str.split(' ')[1]
	req_method=request_str.split(' ')[0]
	http_version=request_str.split(' ')[2][0:8]
	
	# start the serving
	if req_method == 'GET':
		print 'oky Get method caught'
		if req_service== '/':
			req_service='index.html'
			print 'req _service is :',req_service
			res_data=search_file.read_file('.',req_service)
			if res_data==0:
				res_data=b'<html><body><p> Error 404 File not found</p></body></html>'
				res_header=make_header.make_header(404,'.html')
				return res_header+res_data
			res_header=make_header.make_header(200,req_service)
                        return res_header+res_data
			
		else:
			res_data=search_file.read_file('.',req_service.split('/')[-1])
			if res_data==0:
                                res_data=b'<html><body><p> Error 404 File not found</p></body></html>'
                                res_header=make_header.make_header(404,'.html')
                                return res_header+res_data
			res_header=make_header.make_header(200,req_service)
			return res_header+res_data

	else:
		print 'Html For client Post is Not accepted'





if __name__ == '__main__':

	str1='''GET /image2.jpg HTTP/1.1
Host: localhost:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36
Accept: image/webp,image/apng,image/*,*/*;q=0.8
Referer: http://localhost:8080/
Accept-Language: en-US,en;q=0.8
Accept-Encoding: gzip


Received a connection with addrs :('127.0.0.1', 60908)
GET /favicon.ico HTTP/1.1
Host: localhost:8080
User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36
Accept: image/webp,image/apng,image/*,*/*'''

	request_Parser(str1)
	
