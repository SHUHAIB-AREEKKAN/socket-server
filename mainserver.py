from socket import *
import random
import os
import time
import handle_request
class MakeServer():
	
	def __init__(self,port=8080):
		self.port=port
		self.host='127.0.0.1'
		self.sock_obj=''
		
	
	def make_Socket(self):
	
		self.sock_obj=socket(AF_INET,SOCK_STREAM)
		try:
			self.sock_obj.bind((self.host,self.port))		
		except :
			print 'Default Port already in use changing port'
			self.port=random.randint(9000,10000)
			self.sock_obj.bind((self.host,self.port))
			 
		print'server adrrs {} with port {}'.format(self.host,self.port)		
		self.handle_Clients()

	def handle_Clients(self):
		while True:
			self.sock_obj.listen(8)
			cnt,addrs=self.sock_obj.accept()
			print 'Received a connection with addrs :{}'.format(addrs)
			if os.fork()==0:
				request=cnt.recv(1024)
				dec=bytes.decode(request)
				print dec
				data_to_client=handle_request.request_Parser(dec)
				print 'Sending data to Browser or client'	
				cnt.send(data_to_client)		
				cnt.close()
				os._exit(0)
			else:
				cnt.close()
	'''def handle_Request(self,req_data):
		requested_method= req_data.split(' ')[0]
		requested_service=req_data.split(' ')[1]
		requested_version=req_data.split(' ')[2]
		final_response=''
		print 'The Service : {}'.format(requested_service)
		if requested_service=='/':
			headr='HTTP/1.1 200 OK\n'
			date = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
			headr += 'Date:' + date + '\n'
			headr += 'Server: Python-http-server\n'
			headr += 'Content-Type:'+ 'text/html' + '\n'
			headr += '\n'
			fp = open('index.html', 'rb')
			response_data = fp.read()
			fp.close()
			final_header=headr.encode()
			final_response=final_header+response_data
		else:
			print 'The Requested Resource is not index'
		return final_response	

'''




		
		
if __name__ == '__main__':
	abc=MakeServer()
	abc.make_Socket()
	

			

