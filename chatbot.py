#rule based ai chatbot 

import datetime
import time

name = input ("sawagat h, enter your name:")
presenthour = datetime.datetime.now().hour

if presenthour <= 12:
    print ("good morning !" , name)
elif presenthour <= 18:
    print ("good afternoon !" , name)
elif presenthour <= 21:
    print ("good evening !" , name)
else :
    print ("good night !" , name)

print ("Namaste ! welcome to nidhi's chatbot")
print ("you can ask me basic questions , Type 'bye' to exit ")

#chatbot memory creation [dictionary of responses]

responses ={
    "hello" : "hi, welcome  . how are you ?",
    "how are you" : " i am very fine . thankyou",
    "who are you" : " i am very smart ai chatbot",
    "motivate me " : "keep going . every bug of your project makes you a bug free",
    "happy" : "great to hear that "
}

#method/function to get response of chatbot 
def getresponsebot(userquestion):
    userquestion = userquestion.lower()
    for eachkey in responses:
        if eachkey in userquestion :
            return responses[eachkey]
    return "abhi mujhe nhi ata hai "

#take user input 
while True:
    userinput = input ("please ask your wuestion:")
    reply = getresponsebot(userinput)
    print ("bot response :", reply)

    if "bye" in userinput.lower():
        break
