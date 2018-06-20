# this module make socket server with listening port and accept connection and decode responses

from socket import *
import random
import os
import time
import handle_request


class MakeServer():
	''' Template for Server object'''
	def __init__(self,port=8080):
		self.port=port
		self.host='127.0.0.1'
		self.sock_obj=''
		
	
	def make_Socket(self):
		'''making of  socket with a port'''
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
		''' handle clients request and connection multiple connections'''
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


		
if __name__ == '__main__':
	abc=MakeServer()
	abc.make_Socket()
	
