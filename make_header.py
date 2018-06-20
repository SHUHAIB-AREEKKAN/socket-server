#This module provide header for http response message with HTTP headers
import time




def http_status_header(http_status):
	''' the first line of http header, the http status'''
	http_status_dict={200:'HTTP/1.1 200 OK\n',
					404:'HTTP/1.1 404 Not Found\n',
					500:'HTTP/1.1 500 Internal Server Error\n'}
	return http_status_dict[http_status]


def content_type_header(req_service):
	''' return a line of http header content-type field'''
	content_type_dict={'html': 'text/html',
						'txt': 'text/txt',
						'jpg': 'image/jpeg',
						'png': 'image/png',
						'ico': 'icon/ico',
						'pdf': 'application/pdf',
						'gif': 'image/gif'}
	#Error Handler Needed
	return 'Content-Type:'+content_type_dict[req_service]+'\n'



def make_header(http_status,req_service):
	''' to make header for the response '''
	service_type = req_service.split('.')[-1]
	server_date_hdr='Date:'+time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())+'\n'
	print 'inputs : {},{}'.format(http_status,req_service) 
	http_header=http_status_header(http_status)
	http_header+=server_date_hdr
	http_header+='Server:Python Simple Server\n'
	http_header+=content_type_header(service_type)
	http_header+='\n'
	print 'Header Returned in (encoded) to Request_handler :{}'.format(http_header)
	return http_header.encode()



if __name__ == '__main__':
	make_header(200,'index.html')
