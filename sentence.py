"""
file sentence.py
Goal: to count the number of sentences in a text file 
"""

def main():

	file1 = open("paragraph.txt", "r")


	numOfSentences = 0 #Initially Zero 

	while True:

		char = file1.read(1) #Read one character 

		if not char:
			break		

		#Else 
		if char == ".":
			numOfSentences = numOfSentences + 1 #


	print("Number Of Sentences are: " + str(numOfSentences))

	file1.close()


if __name__ == "__main__":
	main()