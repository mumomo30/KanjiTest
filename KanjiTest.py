
#Import random to get a random number for determining a random sequence for testing
#also import os so that we can see all the files in the current directory
#Maybe soon i will make it smart so that you can't really fuck up the options
import random
import os
files=os.listdir()
#print(files)


# *** The following function is a recursive function to generate a sequence of random numbers without repeating ****
#We do this so that we can call random kanji out of order to make it harder
def genorder(minval,maxval):
	global order
	#print("min and max are ",minval,maxval)
	if (maxval-minval)==1:
		order.append(maxval)
		order.append(minval)
		return 0
	if(minval>maxval):
		return 0
	if(maxval==0):
		order.append(0)
		return 0
	if(maxval-minval)==0:
		order.append(minval)
		return 0
		
	valprev=random.randint(minval,maxval)
	order.append(valprev)
	#print("picked ",valprev)
	
	genorder(minval,valprev-1)
	genorder(valprev+1,maxval)		

	return 0
	
# **** END FUNCTION To generate random sequence generation **** 	



# **** Here will be a function to open file and read its contents into an array for us to make things look neater below ****
def GetData(filen,useLen,numK):

	data=[]
	with open(filen, 'r', encoding="utf-8") as f:
		if useLen==1:
			data = f.readlines()
		else :                                          #In case we dont want to do all kanji at once! I should also make function to go between range of kanji huh? 
			for i in range(0,int(numK)+1):
				data.append(f.readline())
			
		f.close()

	return data

# **** END FUNCTION TO OPEN FILE AND GET KANJI DATA ****


# **** Here will be a function to split and pretty up data ****
def PrettyData(linedata):

	line=[]
	line=linedata.split(",")
	line[0]=(line[0].encode("utf-8")).decode("utf-8") #Probably redundant by encoding and decoding but better to be sure
	line[1]=(line[1].encode("utf-8")).decode("utf-8")

	return line

# **** END FUNCTION FOR MANIPULATING FILE STRINGS ****



# **** Here will be a function to compare user entered data... god I wish pointers existed or that I used C.... ****
def Match(usrval,correctval):
	#Split the correctval up by / in case it has multiple meanings and we dont want to make usr guess all in watver order
	vals=correctval.split("/")

	#We do this so that if the user gets any of the deffs correct they get it correct, cause it was annoying before
	if len(vals)>1:
		for meaning in vals:
			if usrval==meaning:
				return 1
	
	#If it only has one meaning then check it 
	if usrval==correctval:
		return 1

	#else they got it wrong, return 0
	return 0

# **** END FUNCTION FOR MATCHING USER INPUT TO FILE DATA ****



# **** Lets make a function to grade them huh ****
def Grade(cor,tot):

	#Make sure they didnt get 0 right or not do any or else we get / 0 condition
	if tot==0:
		print("\nYou didnt want to attempt any huh?\n")
		return 0;
	if cor==0:
		print("\nYou got none correct...\n")
		return 0;
		
	perc = (cor/tot)*100
	print("\nYou got : ",perc,"% correct\n")
	if perc>=60 and perc<70:
		print("\n\n   Final Grade:   D   Terrible   \n\n")
	elif perc>=70 and perc<80:
		print("\n\n   Final Grade:   C   Needs work!!  \n\n")
	elif perc>=80 and perc<90:
		print("\n\n   Final Grade:   B    OK!  \n\n")
	elif perc>=90:
		print("\n\n   Final Grade:   A    Excellent!!! \n\n")
	else:
		print("\n\n   Final Grade:   F    Fail  \n\n")
	
	return 0
# **** END FUNCTION FOR GRADING ****



# **** A function to search for the Kanji by typing in english word??? through all files?? ****
def FindKanji(englishWord):

	return 0;    #Zero if we found it ig

# **** END FUNCTION FOR SEARCHING BASED ON ENGLISH ****



# **** Function to prompt for main action ****
def promptoptn():
	print("Enter your option, 0 for studying, 1 for testing on a single grade, 2 for testing on multiple grades, or anything else for exiting")
	return input()
#Return what the user wants to do for an action 



#Function to prompt for retry action
def promptretry():
	print("want to go again? <y,n> ")
	return (input().lower())
#Return what the user wants to do for an action 
# **** END FUNCTION FOR PROMPTING FOR MAIN OPTIONS ****



# **** Start Infinite Loop ****
def Loop():

	while True:
		optn = promptoptn()  # Get users desired option
		if optn=="1":
			test(0)
		elif optn=="2":
			test(1)
		elif optn=="0":
			study()
		else:    #If they want to exit program, do so here
			break
	return 0
# **** END Infinite loop, if we get here its over ****



# **** Function to handle if user wants to do testing ****
def test(multiple):

	while True:
		
		if multiple==1:
			print("Enter the upper grade you want to test upon ")
			grade2=input()
			filen2="./kanji"+grade2+".txt"
			print("Now Enter the lower grade you want to test upon ")
		else:
			print("Enter the grade you want to test upon ")
		grade=input()
		filen="./kanji"+grade+".txt"
		#at some point we want to check if its an acceptable grade and not crash the program...
	
			
		#Init some variables to good start values 
		global order
		order = []                                           #Line holds the contents seperated by , ' s
		data=[]
	
		print("\nOk im going to open file now. when you see a kanji, type in the english word for it then press enter\n")
		print("\nenter 0 at any time to stop and get your stats! i will allow you to do retries later, im too lazy rn tho....\n\n\n")
			
		data=GetData(filen,1,0)                              #Open file and get data
		
		if multiple==1:
			data.extend(GetData(filen2,1,0))      #ITS APPENDING A LIST NEED IT TO JUST APPEND ELEMENTS 
			print(data)
		genorder(0,len(data)-1)                              #Generate a random sequence to print kanji
		
		#The bulk of the Test, do it now
		#Do it this way so we can use 1 function when we want to use multiple grade files!
		DoTest(data,order)
		
					
		#Ask user if they want to go again
		if promptretry()!="y":
			break

	return 0
# **** End Test Function and return back to prompt options ****




# **** Function for handling if user wants to study ****
def study():

	while True:
		
		print("Enter the grade you want to study upon ")	#Get grade from user so we know what file to open
		grade=input()
		#Init some variables to good start values 
		filen="./kanji"+grade+".txt"                        #Get our filename to open the correct grade 
		line=[]                                             #Line holds the contents seperated by , ' s
		i=0
		data=[]
		order=[]
		correct=0
		wrong=0
		total=0
		uselen=0
		#Done initing, too bad we cant make a function for this like in C.... Prob can though im just too lazy 
			
		print("how many of the Kanji do you want to study? Enter all for all of them")
		numkanji=input()
						
		print("Ok im going to open file now.")
		print("enter 0 at any time to stop. Remember to write out Kanji so you get good at writing too!\n\n\n")
			
		if numkanji.lower()=="all":
			uselen=1
		#Open file, get data, close file, populate data list
		data=GetData(filen,uselen,numkanji)
			
		#Magic loop to print out lines for you
		for i in range(0,len(data)-1):
			
			line=PrettyData(data[i])
			print("\n",line[0],"   ",line[1],"    ",line[2],"\n")
			nl=input()
			if nl=="0":
				break
			
		#Ask user if they want to try again
		if promptretry()!="y":
			break
			
	return 0
# **** End Study Function and return to prompt ****



# **** The meat an potatoes of the test, print out and match kanji ****
def DoTest(data,order):

	line=[]
	wrong=0
	correct=0
	total=0
	i=0
	ans=0
	for i in order:
			
		line=PrettyData(data[i])
				
		print("    ",line[0],end="    ")
		inp=input()
		if inp=="0":
			break
				
		ans = Match(inp.lower(),(line[2].strip()).lower())
				
		if ans==1:                                            #If correct tell them correct and keep track of how many 
			correct=correct+1
			print("\n     correct!  \n\n")
					
		else:                                                 #If wrong tell hem what it was, keep track of how many wrong
			wrong=wrong+1
			print("\n oooof sorry bub, not correct, correct response was : ", end="  ")
			print("   ",line[2] )
					
		total=total+1                                         #incriment total so if we break we know how many we did
				
	print("you got : ",correct, " out of : ",total," attempted correct response ")
	Grade(correct,total)                                      #Give them a letter grade

# **** End TEST FUNCTION ****





# **** Start of the python Script ****
Loop()



# **** If you get here then programs over, GoodBye ****
