
#Import random to get a random number for determining a random sequence for testing
#also import os so that we can see all the files in the current directory
#Maybe soon i will make it smart so that you can't really fuck up the options
import random
import os
files=os.listdir()
#print(files)

#The following function is a recursive function to generate a sequence of random numbers without repeating
#We do this so that we can call random kanji out of order to make it harder
def genorder(minval,maxval):
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
	
#END FUNCTION 	



#Here will be a function to open file and read its contents into an array for us to make things look neater below
def GetData(filen):

	data=[]
	with open(filen, 'r', encoding="utf-8") as f:
		data = f.readlines()
		f.close()

	return data

#END FUNCTION TO OPEN FILE AND GET KANJI DATA


#Here will be a function to split and pretty up data
def PrettyData(linedata):

	line=[]
	line=data[i].split(",")
	line[0]=(line[0].encode("utf-8")).decode("utf-8") #Probably redundant by encoding and decoding but better to be sure
	line[1]=(line[1].encode("utf-8")).decode("utf-8")

	return line

#END FUNCTION FOR MANIPULATING FILE STRINGS



#Here will be a function to compare user entered data... god I wish pointers existed or that I used C....
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

#END FUNCTION FOR MATCHING USER INPUT TO FILE DATA

# Lets make a function to grade them huh
def Grade(cor,tot):
	perc = (cor/tot)*100
	print("You got : ",perc,"% correct")
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





#Start infinite loop to loop through and alow user to choose options
while True:
	
	print("right now only option 1 works!!!!!!!!!!!")
	print("what do you want to do? 0 to do study mode, 1=random test for one grade, 2=test on all available kanji, 3=test up to certain grade ")
	answr=input()

	#**** First option Study Option ****
	#First option (0) is study mode where we will just let you print out a line, with kanji , hiragana, english and let you
	#write it down then press enter to move on to the next character.
	#should I make the program smart and carry over buffered data to other options so that we dont have to open file multiple times?
	if answr=="0":
	
		while True:
		
			print("Enter the grade you want to test upon ")	#Get grade from user so we know what file to open
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
			#Done initing, too bad we cant make a function for this like in C.... Prob can though im just too lazy 
			
			print("Ok im going to open file now.")
			print("enter 0 at any time to stop. Remember to write out Kanji so you get good at writing too!\n\n\n")
			
			#Open file, get data, close file, populate data list
			data=GetData(filen)

			#Magic loop to print out lines for you
			for i in range(0,len(data)-1):
			
				line=PrettyData(i)
				print("\n",line[0],"   ",line[1],"    ",line[2],"\n")
				nl=input()
				if nl=="0":
					break
			
			#Ask user if they want to try again
			print("want to go again? 1=yes ")
			loopanswr=input()
			if loopanswr!="y" and loopanswr!="Y":
				break
	
	#****END OPTION 0 FOR STUDYING FILE CONTENTS****
	
	
	
	#****The first case, open one file and test on all the kanji****
	elif answr=="1":
		#Infinite loop in case you want to redo with another grade or retry same grade etc etc
		while True:
		
			print("Enter the grade you want to test upon ")	#Get grade from user so we know what file to open
			grade=input()
			#at some point we want to check if its an acceptable grade and not crash the program...
			
			#Init some variables to good start values 
			filen="./kanji"+grade+".txt"                        #Get our filename to open the correct grade 
			line=[]                                             #Line holds the contents seperated by , ' s
			i=0
			data=[]
			order=[]
			correct=0
			wrong=0
			total=0
			#Done initing, too bad we cant make a function for this like in C.... Prob can though im just too lazy 
			
			print("Ok im going to open file now. when you see a kanji, type in the english word for it then press enter")
			print("enter 0 at any time to stop and get your stats! i will allow you to do retries later, im too lazy rn tho....\n\n\n")
			
			data=GetData(filen)                                  #Open file and get data
			genorder(0,len(data)-1)                              #Generate a random sequence to print kanji
			
			for i in order:
			
				line=PrettyData(i)
				
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
			
			#Ask user if they want to go again
			print("want to go again? y=yes ")
			loopanswr=input()
			if loopanswr!="y" and loopanswr!="Y":
				break
	#****END SECOND OPTION TO TEST YOU UPON A GRADE****
	
	elif answr=="2":
		while True:
		
		
		
			print("want to go again? 1=yes ")
			loopanswr=input()
			if loopanswr!="y" and loopanswr!="Y":
				break
		
	
	
	
	else:
		break
#END PROGRAM, IF YOU GOT TO HERE THEN GOOD JOB, GOODBYE
	
