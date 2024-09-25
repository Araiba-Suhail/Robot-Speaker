
import win32com.client as wincom

import time

speak = wincom.Dispatch ("SAPI.Spvoice")

time_duration = 20

start_time = time.time() 

elapsed_time= time.time() - start_time 

speak.speak("The started has started. You have 20 seconds.")
print ("Go!")

while True :
    text = input ("Enter your message or type E to exit: ")

    elapsed_time= time.time() - start_time 

    if elapsed_time >= time_duration:
       speak.speak("Opps! The chat time has finised. Start again to restart the proggrame." )
       break

    if text.lower() == "t":
        speak.speak ("You ended the chat. Goodbye!")
        break
    speak.speak(text)









