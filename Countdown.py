#Designed for use in OBS: Countdown to a certain timestamp in the future, when achieved, display 00:00

from time import sleep
import datetime
import sys

dateObject = datetime.date(1,1,1) #Create a placeholder date object

def manualTargetInput():
    """If the configuration file fails to read correctly
    allow the user to enter a timestamp into the console"""
    
    def inputIter(text,inputValueMin,inputValueMax,hasRecurred=False):
        """Recursive argument validation for each unit of time"""
        try:
            
            #Input and verify is integer
            if (hasRecurred == True): #If user failed input first try, show the validation bounds
                userInput = int(input("{} (min {}, max {}): ".format(text,inputValueMin,inputValueMax)))
            else:
                userInput = int(input("{}: ".format(text)))
                
            #Check input within bounds
            if (userInput <= inputValueMax and userInput >= inputValueMin):
                return userInput
            else:
                raise Exception
        except:
            return inputIter(text, inputValueMin, inputValueMax,hasRecurred=True)    
        
    #Have user input each unit of time one-by-one, if the user makes an error, 
    # keep asking the user to submit that unit until they get it right
    H = inputIter("Please enter an hour (24h time)",0,23)
    M = inputIter("Please enter a minute",0,59)
    S = inputIter("Please enter a second",0,59)
    print("Time Accepted")
    
    return datetime.time(H,M,S) #Manual timestamp accepted

def getTargetTime():
    """Attempt to read timestamp configuration file, bypassing manual input
    if it fails, have user submit timestamp manually"""
    
    try:
        f = open("./Countdown.cfg","r") #Attempt to open config file in read mode
        lineArray = f.read().splitlines()[0:3] #We only need the first three lines, move these into an array
        H,M,S = int(lineArray[0]), int(lineArray[1]), int(lineArray[2]) #Assign each line to a variable and check they are integers
        if ((H <= 23 and H >= 0) and (M <= 59 and M >= 0) and (S <= 59 and S >= 0)): #Check integers are within bounds
            print("Configuration Accepted")
            
            return datetime.time(H,M,S) #Configuration timestamp accepted
        else:
            raise Exception
    except: #Something was wrong with configuration file, either file missing or invalid data, switch to manual entry
        print("Configuration Rejected, Switching to manual time entry")
        return manualTargetInput()

def recordNewDate(delta):
    """Take the current timeDelta, save it as a string to Timer.txt located in the same directory as the applet, 
    if there is less than an 3600 seconds left, remove the hour's place in the produced string"""
    
    f = open("./Countdown.txt", "w") #Open the file and replace all existing data
    outputString = ""
    if(delta.seconds < 3600): #Hours place not needed, remove it
        outputString = str(delta)[2:]
    else:
        outputString = str(delta)
        
    f.write(outputString) #Save and close
    print(outputString)
    f.close()
     
# Configure the target timestamp
timeTarget = datetime.datetime.combine(dateObject, getTargetTime()) #Format target time into timeDelta
sleep(1)
while True: #Main loop
    sleep(0.5) #Sleep a second so windows isn't constantly abused by file updates
    timeCurrent = datetime.datetime.combine(dateObject, datetime.datetime.now().time().replace(microsecond=0)) #Get and format current time into timeDelta
    
    timeRemaining = timeTarget - timeCurrent #Delta T equation to get difference
    if (timeRemaining > datetime.timedelta(0)): #Check if timeRemaining (till target) is greater than 0 seconds
        #Current time has not reached target
        recordNewDate(timeRemaining)
    else:
        #Current time has reached target, ignore timestamp and set time to 0
        recordNewDate(datetime.timedelta(0))
        print("Target Reached, Exiting...")
        break #Exit main loop