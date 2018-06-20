import os
import sys

file_path=''
def search_file(root,file_to_search):
	'''To Search File In The Directory '''
	filenames=os.listdir(root)
	#print filenames
	for filename in filenames:
		if not os.path.isdir(os.path.join(root,filename)):
			sec=os.path.basename(filename)
			if sec == file_to_search:
				global file_path
				file_path=os.path.join(root,filename)
				
		else:
			search_file(os.path.join(root,filename),file_to_search)
	
	return file_path


def read_file(root,filename):
	''' to read the file in binary and return  '''
	file_path=search_file(root,filename)
	
	try:
		file_obj=open(file_path,'rb')
		file_in_binary=file_obj.read()
	except IOError:
		print 'Unable to open file'
		return 0
	file_obj.close()
	
	return file_in_binary

if __name__ == '__main__':
	#print search_file('.','simple_client.py')
	a=read_file('.','Screenshot from 2016-12-14 02-43-30.png')
	b=search_file('.','Screenshot from 2016-12-14 02-43-30.png')
	print type(b)
	print b
