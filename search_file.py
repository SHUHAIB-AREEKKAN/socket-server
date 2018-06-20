# This module provide Search File in directory,return the file path and Read a file binary and return in binary
import os
import sys

file_path=''
def search_file(root,file_to_search):
	'''To Search File In The Directory and Return the Absolute File Path'''
	filenames=os.listdir(root)
	file_to_search=space_encoding_case(file_to_search)
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
	''' To Read the File in Binary and Return in Binary '''
	file_path=search_file(root,filename)
	
	try:
		file_obj=open(file_path,'rb')
		file_in_binary=file_obj.read()
	except IOError:
		print 'Unable to open file'
		return 0
	file_obj.close()
	
	return file_in_binary

def space_encoding_case(file_name):
	'''for solving the issues when browser see space  like '%20' or '+' and os see as space ,so we solve it by replacing space'''
	return file_name.replace("%20"," ") 
	

if __name__ == '__main__':
	#print search_file('.','simple_client.py')
	a=read_file('.','Screenshot from 2016-12-14 02-43-30.png')
	b=search_file('.','Screenshot from 2016-12-14 02-43-30.png')

