import optparse 
import zipfile
from time import time

#parse arguments
parser = optparse.OptionParser()
parser.add_option('-f', '--file', action="store", dest="file_path", help="Zip File Path", default=None)
parser.add_option('-w', '--word_list', action="store", dest="word_list", help="Word List Path", default=None)
options, args = parser.parse_args()

def main(file_path, word_list):
	#check if the Zip file exists
	try:
		zip_ = zipfile.ZipFile(file_path)
	except zipfile.BadZipfile:
		print ("Please check the file's path. It doesn't seem to be a zip file.")
		quit()

	password = None #just in case if the word list is empty
	i = 0 #password count 
	c_t = time() #start time
	with open(word_list, "r") as f: #open the word list
		passes = f.readlines() #read the text file line by line
		for x in passes:
			i += 1 #increment the password try count
			password = x.split("\n")[0] #splitting the newline character 
			try:
				zip_.extractall(pwd=password) #try the password
				t_t = time() - c_t #total time
				print ("\nPassword cracked: %s\n") % password #print the password
				print ("Took %f seconds to crack the password. That is, %i attempts per second.") % (t_t,i/t_t) #stats
				quit() #stop the script
			except Exception:
				pass
		print ("Sorry, password not found.")

if __name__ == '__main__':
	main(options.file_path, options.word_list)