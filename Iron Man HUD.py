from __future__ import print_function
import numpy 
import cv2 
from time import strftime
import smtplib,webbrowser,winsound,pyttsx3,wikipedia,bs4,pyowm,geocoder,pyautogui,sys,random,cv2,requests,psutil,face_recognition,pyaztro,pyautogui,logging,pickle,os.path,email,imaplib,cbpy as cb,numpy as np,wolframalpha
from urllib.request import urlopen
from playsound import playsound #pip install playsound
from PyDictionary import PyDictionary #pip install PyDictionary
from bs4 import BeautifulSoup #pip install bs4
from pywebostv.discovery import *
from phonenumbers import timezone
from pywebostv.discovery import *
from phonenumbers import carrier
from datetime import datetime
import pytz
import glob
import math
from phone_iso3166.country import phone_country
import pycountry
import numpy as np  
import phonenumbers
from pywebostv.connection import *
from pywebostv.controls import *
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.header import decode_header
from geopy.distance import geodesic 
from twilio.rest import TwilioRestClient
import yt_search
import urlencode
import datetime
import smtplib
import speech_recognition as sr  # pip install speechRecognition
import bs4 #pip install bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import pyowm  #pip install pyowm
import geocoder #pip install geocoder
import sys  #pip install python-sys
import random
import requests, json 
import face_recognition
import glob
import math
import pytemperature
from playsound import playsound #pip install playsound
import cv2 # pip install opencv-contrib-python
import requests #pip install requests
import psutil #pip install psutil
import urllib.request #pip install urllib.request
import urllib.parse #pip install urllib.parse
import re #pip install re
import numpy as np #pip install numpy
import face_recognition #pip install face-recognition
import wolframalpha #pip install wolframalpha
from bs4 import BeautifulSoup
from PyDictionary import PyDictionary 
# open the video 
vid = cv2.VideoCapture(0) 
import psutil
api_key = "f3852ccaeb3a2b265ccc22185e27367d"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "Bengaluru" 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
response = requests.get(complete_url) 
x = response.json() 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
dictionary=PyDictionary()
newVoiceRate = 1000
while newVoiceRate <= 300:
    engine.setProperty('rate',newVoiceRate)
    engine.runAndWait()
    newVoiceRate = newVoiceRate+50
engine.setProperty('rate', 200)
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
username = "moderngaming2588@gmail.com"
password = "Lohith01"
imap = imaplib.IMAP4_SSL("imap.gmail.com")
# authenticate
imap.login(username, password)
status, messages = imap.select("INBOX")
# number of top emails to fetch
N = 4
# total number of emails
messages = int(messages[0])
newVolume = 100
engine.setProperty('volume',newVolume)
engine.runAndWait()
newVolume = newVolume+100
engine.setProperty('volume',100)   
client = wolframalpha.Client('GTAT38-RTR7PG4P53')
print("Initializing Jarvis")
MASTER = "Leo Stark"
news_url = "https://news.google.com/news/rss"
Client = urlopen(news_url)
xml_page = Client.read()
Client.close()
soup_page = soup(xml_page, "xml")
news_list=soup_page.findAll("item")
owm = pyowm.OWM('f3852ccaeb3a2b265ccc22185e27367d')
city = 'Bengaluru'
loc = owm.weather_at_place(city)
weather = loc.get_weather()
#temperature
temperature = weather.get_temperature(unit='celsius')
humidity = weather.get_humidity()
wind = weather.get_wind()
#FaceID Scan
#playsound('C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//Jarvis FaceID.mpeg')

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
   
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound("C:\\Users\\Dell\\AppData\\Roaming\\LINKS\\Customization\\Sound Effects\\System_ready.wav")
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Searching...")    
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        return "None"
    return query 

def pauseListen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("Searching...")    
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)    
        return "None"
    return query 
  
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('moderngaming2588@gmail.com', 'Lohith01')
    server.sendmail('moderngaming2588@gmail.com', to, content)
    server.close()
 
# Get a referee to webcam #0 (the default one)
cap = cv2.VideoCapture(0)
speak("Jarvis HUD Interface Online")

# Load a sample picture and learn how to recognize it.

if x["cod"] != "404":  
    y = x["main"] 
    current_temperature = y["temp"]  
    current_pressure = y["pressure"] 
    current_humidiy = y["humidity"] 
    z = x["weather"] 
    weather_description = z[0]["description"] 
    temp = pytemperature.k2c(current_temperature)
    temp = round(temp)
    print(" Temperature (in kelvin unit) = " +
                    str(temp) + 
          "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
          "\n humidity (in percentage) = " +
                    str(current_humidiy) +
          "\n description = " +
                    str(weather_description))   

query = pauseListen()
if 'heads up display' in query.lower() or 'vision' in query.lower():
    head = False
    while head == False:
        speak("Initializing Heads Up Display!!")
        head = True
        break 
else:
    time.sleep(1)            
query = pauseListen()
if 'face recognition' in query.lower():
    face = False
    while face == False:
        speak("Initiating Enhanced Face Recognition Interface")
        face = True
        break
    else:
        time.sleep(1)
    lohith_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/Camera Roll/LOLU pandey.jpg")
    lohith_face_encoding = face_recognition.face_encodings(lohith_image)[0]
    billgates_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/bill gates.png")
    billgates_face_encoding = face_recognition.face_encodings(billgates_image)[0]
    shan_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/Shankarappa.jpg")
    shan_face_encoding = face_recognition.face_encodings(shan_image)[0]
    resh_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/Reshma.jpg")
    resh_face_encoding = face_recognition.face_encodings(resh_image)[0]
    kump_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/Kumaraswamy.jpg")
    kump_face_encoding = face_recognition.face_encodings(kump_image)[0]
    modi_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/NarendraModi.jpg")
    modi_face_encoding = face_recognition.face_encodings(modi_image)[0]
    stark_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/Tony Stark.jpg")
    stark_face_encoding = face_recognition.face_encodings(stark_image)[0]
    gandhi_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/Gandhi.jpg")
    gandhi_face_encoding = face_recognition.face_encodings(gandhi_image)[0]
    obama_image = face_recognition.load_image_file("C:/Users/Dell/Pictures/Barack Obama.jpg")
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    # Create arrays of known face encodings and their names
    known_face_encodings = [
        lohith_face_encoding,
        billgates_face_encoding,
        shan_face_encoding,
        resh_face_encoding,
        kump_face_encoding,
        modi_face_encoding,
        stark_face_encoding,
        gandhi_face_encoding,
        obama_face_encoding,
    ]
    known_face_names = [
        "Lohith.S",
        "Bill Gates",
        "Shankar",
        "Reshma",
        "Kumaraswamy",
        "Narendra Modi",
        "Tony Stark",
        "Gandhi",
        "Barack Obama"
    ]

# Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True                 
    while True:
        temp = (str(temp))
        font = cv2.FONT_HERSHEY_SIMPLEX
        ret, frame = cap.read()
        cv2.resize(frame,(1280,720),fx=0,fy=0, interpolation = cv2.INTER_CUBIC) 
        fe = psutil.sensors_battery().percent
        batt = (str(fe)) 
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        if process_this_frame:
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown face"
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)             
        
        process_this_frame = not process_this_frame

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (0, 255, 0), 1)
    #Temperature display
        cv2.putText(frame,temp,(30,150), font,1.2, (139,0,0), 2)
    #Heading Jarvis HUD
        cv2.putText(frame,'Jarvis HUD',(210,40), font,1.2, (139,0,0), 2)
        cv2.line(frame,(120,10),(200,50),(139,0,0),2)
    #Battery Status
        cv2.putText(frame,batt,(20,100), font,1.2, (139,0,0), 2)
    # %-symbol display
        cv2.putText(frame,'%',(70,100), font,1.2, (139,0,0), 2)
        cv2.line(frame,(200,50),(400,50),(139,0,0),2)
        cv2.line(frame,(500,10),(400,50),(139,0,0),2)
    #Time Dislay
        frame = cv2.putText(frame, strftime("%H:%M:%S"), (450,450), cv2.FONT_HERSHEY_SIMPLEX, 1.0,(139,0,0),2,cv2.LINE_AA) 
        cv2.imshow('Jarvis HUD', frame)  
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release() 
    cv2.destroyAllWindows()    
elif 'contour ' in query.lower():
    cap = cv2.VideoCapture(0)
    while(1): 
        ret, frame = cap.read() 
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
        lower_red = np.array([30,150,50])
        font = cv2.FONT_HERSHEY_SIMPLEX
        upper_red = np.array([255,255,180])       
        mask = cv2.inRange(hsv, lower_red, upper_red) 
        res = cv2.bitwise_and(frame,frame, mask= mask) 
        edges = cv2.Canny(frame,100,200)
        cv2.imshow('Jarvis Edge Detection',edges) 
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release() 
    cv2.destroyAllWindows() 

elif 'qr code' in query.lower():
    import pyzbar.pyzbar as pyzbar
    cap = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        _,frame = cap.read()
        decodedObjects = pyzbar.decode(frame)
        for obj in decodedObjects:
            qr = (str(obj.data))
            qr = qr.replace('b','')
            qr = qr.replace("'","")
            response = requests.get(obj.data)
            speak("Sir..I believe the QR Code leads to website!!")
            speak("Should I open the website..Sir!!")
            query = takeCommand()
            if 'yes ' in query.lower() or 'open ' in query.lower() or 'yeah ' in query.lower() or 'sure ' in query.lower() or 'yep ' in query.lower():
                webbrowser.open(obj.data)
                break
            else:
                speak(f"Sir..I suppose the QR Code translates as {obj.data}") 
                break       
                    
        cv2.imshow("Frame",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows() 
else:
    time.sleep(1)

if __name__ == "__main__":
    while True:
    # if 1:        
        speak("Jarvis AI Initialized Successfully")
        speak("At your service Sir!!")
        query = takeCommand().lower()
    
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'pause' in query.lower() or 'hold' in query.lower():
            speak("Okay sir..Listening Paused!!")
            speak("Switching to Auxillary Listening Mode")
            listen = False
            while listen == False:
                que = pauseListen()
                if 'jarvis' in que.lower() or 'Jarvis' in que.lower() or 'start' in que.lower():
                    speak("Listening Enabled")
                    listen = True
                    break           
                else:
                    time.sleep(1) 

        elif 'zoom' in query.lower() and 'mode' in query.lower():
            speak("Initiating Jarvis Zoom version 1.0!!")
            listen = False
            while listen == False:
                que = pauseListen()
                if 'mute' in que.lower() or 'unmute' in que.lower() and 'audio' in que.lower() or 'voice'in que.lower():
                    pyautogui.keyDown('alt');pyautogui.keyDown('a');pyautogui.keyUp('alt');pyautogui.keyUp('a')
                elif 'start' in que.lower() or 'stop' in que.lower() or 'video' in que.lower() or 'visual' in que.lower():
                    pyautogui.keyDown('alt');pyautogui.keyDown('v');pyautogui.keyUp('alt');pyautogui.keyUp('v')
                elif 'raise' in que.lower() and 'hand' in que.lower():
                    pyautogui.keyDown('alt');pyautogui.keyDown('y');pyautogui.keyUp('alt');pyautogui.keyUp('y')
                elif 'leave' in que.lower() or 'quit' in que.lower() or 'exit'in que.lower() or 'end' in que.lower() and 'meeting' in que.lower():
                    pyautogui.keyDown('alt');pyautogui.keyDown('q');pyautogui.keyUp('alt');pyautogui.keyUp('q')
                    time.sleep(3)
                    pyautogui.press('enter',interval=0.1)
                elif 'start' in que.lower() or 'stop' in que.lower() and 'screen' in que.lower():
                    pyautogui.keyDown('alt');pyautogui.keyDown('s');pyautogui.keyUp('alt');pyautogui.keyUp('s')
                elif 'jarvis' in que.lower() and 'deactivate' in que.lower() or 'end' in que.lower() or 'kill' in que.lower():
                    speak("Deactivating Jarvis Zoom version 1.0")
                    listen = True
                    break   
                else:
                    time.sleep(1)            

        elif 'will it rain' in query.lower() or 'umbrella' in query.lower() or 'raincoat' in query.lower():
            loc = owm.three_hours_forecast(city)
            clouds = str(loc.will_have_clouds())
            rain = str(loc.will_have_rain())  
            print(rain)
            print(clouds) 
            if rain == 'True':
                print("Yes sir....According to the weather reports it looks like it will rain today")
                speak("Yes sir....According to the weather reports it looks like it will rain today")
                print("I suggest you carry an umbrella..in case it rains today")
                speak("I suggest you carry an umbrella..in case it rains today")

            elif rain == 'False':
                print("No Sir, according to the weather reports it doesn\'t look like it will rain today")
                speak("No Sir, according to the weather reports it doesn\'t look like it will rain today ")
                print("............Sir I don\'t think  you should carry an umbrella..because it is clear outside")
                speak("............Sir I don\'t think  you should carry an umbrella..because it is clear outside")

            if clouds == 'True' and rain == 'True':
                print("Moreover sir it is very cloudy today")
                speak("Moreover sir it is very cloudy today")
              
            elif clouds == 'True' and rain == 'False':
                print("But sir even though it won\'t rain today....It is very cloudy outside")
                speak("But sir even though it won\'t rain today....It is very cloudy outside")    

        elif 'dice ' in query.lower():
            playsound()
            sm = ['One','Two','Three','Four','Five','Six']
            spf = random.choice(sm)
            speak(f"The Dice is rolled and it is {spf}")

        elif 'where are we' in query.lower() or 'locate ' in query.lower() or 'geolocation ' in query.lower():
            g = geocoder.ip('me')
            geoloc = g.latlng
            speak(f"Our current Latitudes and Longitudes are {geoloc}!!") 
            speak("Location match successful!!")
            geocity = g.city
            speak(f"Sir..we are in {geocity}!!")                

        elif 'trust ' in query.lower() or 'believe' in query.lower():
            speak("I trust you sir..kind of like Trust the Force..Luke")

        elif 'hello ' in query.lower() or 'hi ' in query.lower() or 'howdy ' in query.lower() or 'hola ' in query.lower() or 'hey 'in query.lower():
            wish = ['Hello sir,,it\'s so good to see you','Hello there Boss,,it\'s so good to see you','Howdy,,sir..it\'s so good to see you']
            speak(random.choice(wish))    

        elif 'sunset time' in query.lower() or 'sunrise time' in query.lower() or'what time will the sunset' in query.lower() or 'what time will the sunrise' in query.lower():
            sr = weather.get_sunrise_time(timeformat='iso')
            ss = weather.get_sunset_time(timeformat='iso')
            print(f'Sunrise = {sr}')
            print(f'Sunset = {ss}')
            speak(f"Sunrise time is {sr}")
            speak(f"Sunset time is {ss}")   

        elif 'applause' in query.lower() or 'clap' in query.lower() or 'clapping' in query.lower():
            playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//clapping.mpeg")

        elif 'upcoming matches' in query.lower():
            y = cb.gmatchlist()
            for x in y:
                print(x)

        elif 'live score' in query.lower():
            p = cb.plivescore(2)
            print(p) 

        elif 'tv' in query.lower():
            for status in client.register(store):
                if status == WebOSClient.PROMPTED:
                    print("Please accept to connect to the TV!!")
                elif status == WebOSClient.REGISTERED:
                    print("Registration Successful!!")
            g = input("Enter input: ")
            if g == 'youtube' or 'Youtube': 
                app = ApplicationControl(client)
                apps = app.list_apps()
                yt = [x for x in apps if "youtube" in x["title"].lower()][0]
                launch_info = app.launch(yt)
                print("Opening Youtube")
    
            if g == 'prime video' or 'amazon': 
                app = ApplicationControl(client)
                apps = app.list_apps()
                am = [x for x in apps if "amazon" in x["title"].lower()][0]
                launch_info = app.launch(am)
                print("Opening Amazon Prime Video")

            if g == 'off':
                system = SystemControl(client)
                system.notify("Turning off your TV")
                system.power_off()
                print("Turning off your TV")

            if g == 'mute':
                inp = InputControl(client)
                inp.connect_input()
                inp.mute()
                    
        elif 'shut down' in query.lower():
            speak("Okay sir..turning off your laptop")
            os.system('shutdown -s')    

        elif 'google search' in query.lower():
            new = 2
            tabUrl = "https://google.com/?#q="
            term = takeCommand()
            webbrowser.open(tabUrl+term,new=new)

        elif 'youtube' in query.lower() or 'Youtube' in query.lower() and 'tv' in query.lower():
            store = {}
            speak("Jarvis LG AI Connect Mode..Turned On!!")
            time.sleep(2)
            speak("Well..what would you like to watch sir")
            query = takeCommand()
            speak("Excellent choice Boss!!")
            text = query
            yt = yt_search.build("AIzaSyCtWMxKG8NA3LGEa5YALIURupE_lAIPa_4")
            search_result = yt.search(text, sMax=1, sType=["video"])
            ytname = search_result.title
            ytchnl = search_result.channelTitle
            ytid = search_result.videoId
            speak(f"Playing {ytname} by {ytchnl} on LG WebOS TV")
            def listToString(s):  
                str1 = " " 
                return (str1.join(s)) 
            s = ytid
            ytid = listToString(s) 
            store = {}
            client = WebOSClient('192.168.0.101')
            #client = WebOSClient.discover()[0]
            #client.register(store=store)
            client.connect()
            for status in client.register(store):
                print(status)
                print("Please accept the connect on the TV!")    
#media.mute()
            app = ApplicationControl(client)
            apps = app.list_apps()
            yt = [x for x in apps if "youtube" in x["title"].lower()][0]
            launch_info = app.launch(yt,content_id = ytid)
#client.launch_app('amazon')
            for app in client.get_apps():
                print(app)            


        elif 'screen recorder' in query.lower():
            speak("Opening DU Screen Recorder")
            codePath = "C:\\Users\\Dell\\Desktop\\J.A.R.V.I.S (v2.0)\\DU Recorder.lnk"
            os.startfile(codePath)
      
        elif 'i am back' in query.lower() or 'i\'m back' in query.lower() or 'home' in query.lower():
            speak("Welcome Back..sir..")        

        elif 'face recognition' in query.lower():
            speak("Turning on Biometric Face Recognition Mode")    
            os.startfile("C:\\Users\\Dell\\Desktop\\my python projects\\face of lohith.py") 

        elif 'play MJ' in query.lower() or 'michael jackson' in query.lower() or 'they don\'t care about us' in query.lower():
            playsound("C:\\Users\\Dell\\Desktop\\J.A.R.V.I.S (v2.0)\\Michael Jackson-They Don t Care About Us.mp3")
        
        elif 'boney' in query.lower() or 'rasputin' in query.lower():
            playsound("C:\\Users\\Dell\\Desktop\\J.A.R.V.I.S (v2.0)\\Boney M - Rasputin.mp3")
        
        elif 'read email' in query.lower() or 'read my emails' in query.lower() or 'read emails' in query.lower() or 'read my email' in query.lower():
            messages = int(messages)
            print(f"Sir,,you have {messages} emails in your Inbox")
            print(f"Here are some important emails")
            speak(f"Sir,,you have {messages} emails in your Inbox")
            speak(f"Here are some important emails")
            for i in range(messages, messages-N, -1):
    # fetch the email message by ID
                res, msg = imap.fetch(str(i), "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
            # parse a bytes email into a message object
                    msg = email.message_from_bytes(response[1])
            # decode the email subject
                    subject = decode_header(msg["Subject"])[0][0]
                    if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                        subject = subject.decode()
            # email sender
                    from_ = msg.get("From")
                    print("Subject:", subject)
                    print("From:", from_)
            # if the email message is multipart
                    if msg.is_multipart():
                # iterate over email parts
                        for part in msg.walk():
                    # extract content type of email
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                        # get the email body
                                body = part.get_payload(decode=True).decode()
                            except:
                                pass
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                        # print text/plain emails and skip attachments
                                print(body)

                    else:
                # extract content type of email
                        content_type = msg.get_content_type()
                # get the email body
                        body = msg.get_payload(decode=True).decode()
                        if content_type == "text/plain":
                    # print only text email parts
                            print(body)
                    if content_type == "text/html":
                # if it's HTML, create a new HTML file and open it in browser
                # write the file
                # open in the default browser
                        print("="*100)
            imap.close()
            imap.logout() 

        elif 'snipping tool' in query.lower():
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Snipping Tool.lnk" 
            os.startfile(codePath)  

        elif 'mute' in query.lower() or 'volume of' in query.lower() or ' volume off ' in query.lower():
            speak("Muting your speakers")
            pyautogui.keyDown('volumemute');pyautogui.keyUp('volumemute')

        elif 'volume on' in query.lower():
            speak("Unmuting your speakers")
            pyautogui.keyDown('volumemute');pyautogui.keyUp('volumemute')                

        elif 'can\'t hear you' in query.lower() or 'increase volume' in query.lower() or 'volume up' in query.lower():
            speak("Increasing Sound Volume")
            pyautogui.keyDown('volumeup');pyautogui.keyUp('volumeup')
            speak("Can you hear me now..sir") 
            query = takeCommand()
            if 'yes' in query.lower() or 'yep' in query.lower() or 'yeah' in query.lower() or 'yup' in query.lower():
                speak("Okay then...")         

        elif 'did it work' in query.lower():
            speak("Oh...I think it worked pretty great sir..")

        elif 'drop ' in query.lower() and 'needle' in query.lower():
            playsound('C://Users//Dell//Music//White Christmas - Home Alone.mpeg')  

        elif 'good morning' in query.lower():
            speak("Good Morning..sir")

        elif 'good evening' in query.lower():
            speak("Good Evening..sir")

        elif 'good afternoon' in query.lower():
            speak("Good afternoon..sir")

        elif 'good night' in query.lower():
            speak("Good Night..sir..Sweet Dreams..")

        elif ' spell ' in query.lower():
            quer = query.replace("spell"," ")
            def split(quer):
                return list(quer)
            word = quer
            print(split(quer))
            speak(split(quer))

        elif ' pronounce ' in query.lower():
            quo = query.replace("pronounce"," ")
            print(quo)
            speak(quo)           

        elif ' screenshot ' in query.lower():
            image = pyautogui.screenshot()
            image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
            speak("What should I save it..sir")
            query = takeCommand()
            scrshot = query
            cv2.imwrite(scrshot+".png", image)   
            speak("Image saved as {scrshot}.png")

        elif 'list ' in query.lower():
            speak("Creating a list")
            query = takeCommand()
            l1 = query
            speak(f"{l1} added to the list")
            speak("What\'s the next item sir..") 
            query = takeCommand()               
            l2 = query
            speak(f"{l2} added to the list")
            speak("What\'s the next item sir..") 
            query = takeCommand()
            l3 = query
            speak(f"{l3} added to the list")
            speak("What\'s the next item sir..")             
            query = takeCommand()
            l4 = query
            speak(f"{l4} added to the list")
            speak("What\'s the next item sir..")  
            query = takeCommand()
            l5 = query
            speak(f"{l5} added to the list")
            speak("What\'s the next item sir..")
            query = takeCommand()
            l6 = query
            speak(f"{l6} added to the list")
            speak("What\'s the next item sir..") 
            query = takeCommand()
            l7 = query
            speak(f"{l7} added to the list")
            speak("What\'s the next item sir..")
            query = takeCommand()
            l8 = query
            speak(f"{l8} added to the list")
            speak("What\'s the next item sir..")
            query = takeCommand()
            l9 = query
            speak(f"{l9} added to the list")
            speak("What\'s the next item sir..")                                   
            query = takeCommand()
            l10 = query
            speak(f"{l10} added to the list")
            speak("What\'s the next item sir..")

        elif 'read' in query.lower():
            speak(f"Number 1..in the list..{l1}")
            speak(f"Number 2..in the list..{l2}")
            speak(f"Number 3..in the list..{l3}")
            speak(f"Number 4..in the list..{l4}")
            speak(f"Number 5..in the list..{l5}")
            speak(f"Number 6..in the list..{l6}")
            speak(f"Number 7..in the list..{l7}")
            speak(f"Number 8..in the list..{l8}")
            speak(f"Number 9..in the list..{l9}")
            speak(f"Number 10..in the list..{l10}")

        elif 'horoscope' in query.lower():
            speak("Sir..please tell me the zodiac sign..")
            query = takeCommand()
            speak("What do you want to look for..lucky number..or..lucky day..or..lucky colour..or..description..or..mood")
            quer = takeCommand()
            if 'number' in quer.lower():
                kor = query
                horoscope = pyaztro.Aztro(sign=kor)
                print(horoscope.lucky_number)
                speak(horoscope.lucky_number)
            elif 'colour' in quer.lower():
                kor = query
                horoscope = pyaztro.Aztro(sign=kor)
                print(horoscope.color)  
                speak(horoscope.color)
            elif 'about' in quer.lower() or 'description' in quer.lower():
                kor = query
                horoscope = pyaztro.Aztro(sign=kor)
                print(horoscope.description) 
                speak(horoscope.description) 

            elif 'mood' in quer.lower():
                kor = query
                horoscope = pyaztro.Aztro(sign=kor)
                print(horoscope.mood)
                speak(horoscope.mood)
            elif 'day' in quer.lower():
                kor = query
                horoscope = pyaztro.Aztro(sign=kor)
                print(horoscope.day)
                speak(horoscope.day)
            elif 'date' in quer.lower() or 'month' in quer.lower() or 'period' in quer.lower():
                kor = query
                horoscope = pyaztro.Aztro(sign=kor)
                print(horoscope.date_range) 
                speak(horoscope.date_range) 


        elif ' wizard ' in query.lower():
            speak("Initiating Wizarding World Mode..")
            speak("Please introduce yourself..")
            query=takeCommand()
            query = query.replace('i am'," ")
            name = query
            speak(f"Hello {name}..Welcome to Hogwarts..")
            #playsound() #Voldemort lightning
            #playsound()  #we do not speak of him 
            #playsound()#we finally meet
            #playsound()#wands at the ready
            query = takeCommand()
            if 'expelliarmus' in query.lower():
                expell = ["C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//Wingardium Leviosa.mpeg","C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//Incarne.mpeg"]
                playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//Wingardium Leviosa.mpeg")
                playsound(random.choice(expell))


        elif 'music' in query.lower() or 'songs' in query.lower() or 'drop' in query.lower():
            speak("What would you like to listen to sir")
            query = takeCommand()
            if 'boney' in query.lower() or 'rasputin' in query.lower():
                playsound("C:\\Users\\Dell\\Desktop\\J.A.R.V.I.S (v2.0)\\Boney M - Rasputin.mp3")
            elif 'MJ' in query.lower() or 'michael jackson' in query.lower() or 'they don\'t care about us' in query.lower():
                playsound("C:\\Users\\Dell\\Desktop\\J.A.R.V.I.S (v2.0)\\Michael Jackson-They Don t Care About Us.mp3")

            elif 'hedwig' in query.lower() or 'harry potter' in query.lower():
                playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//Hedwig s Theme.mp3")

            elif 'fast and furious' in query.lower() or 'danza kuduro' in query.lower():
                playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//Don Omar - Danza Kuduro  feat. Lucenzo.mp3") 
                playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//Don Omar -  How We Roll (Fast Five Remix) ft. Busta Rhymes. Reek da Villian & J-doe.mp3")
            
            elif 'kung fu fighting' in query.lower() or 'kumg fu songs' in query.lower():
                playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//carldouglaskungfufightingfunk80.mp3")   
            
            elif 'despacito' in query.lower():
                playsound('C:\\Users\\Dell\\Music\\Dono.mp3')

            elif 'shape of you' in query.lower():
                playsound('C:\\Users\\Dell\\Music\\Shape of you.mp3')

            elif 'on my way' in query.lower() or ' i\'m on my way' in query.lower():
                playsound("C:\\Users\Dell\\Desktop\\J.A.R.V.I.S (v2.0)\\Alan Walker, Sabrina Carpenter & Farruko - On My Way (1) - Copy.mp3")

            elif 'something that iron man' in query.lower() or 'iron man songs' in query.lower() or 'something that tony stark' in query.lower():
                playsound("C:\\Users\Dell\\Desktop\\J.A.R.V.I.S (v2.0)\\Ratt - Back in Black (tribute AC DC) (1).mp3")
            
            elif 'cheap thrills' in query.lower():
                playsound("C:\\Users\\Dell\\Music\\Sia - Cheap Thrills (DawnFoxes.com).mp3")     
               
        elif 'what can you do' in query.lower():
            speak("I can assist you in the following jobs,,sir")
            speak("I can search things on Google")
            speak("I can tell you Weather Forecasts")
            speak("I can play Youtube Videos")
            speak("I can open plenty of websites")
            speak("I can toss the coin for you")
            speak("I can open plenty of apps")
            speak("I can set alarms")
            speak("I can send E mails")
            speak("I can play songs")
            speak("I can even make you laugh sir")
            speak("I can also recognize several faces sir")
            speak("I can spell words for you..")
            speak("I can tell you horoscopes..")
            speak("I can control your TV too...sir")
            speak("Well that\'s all I can do right now sir,,")

        elif 'geography'in query.lower() or 'distance' in query.lower() and 'matrix' in query.lower():
            query = takeCommand()
            speak("What is the name of the place of which you want to measure the distance!!")
            cityloco = query
            g = geocoder.location(cityloco)
            l = geocoder.ip('me')
            liveloco = l.latlng
            nonliveloco = g.latlng
            diff = (geodesic(liveloco,nonliveloco).km)
            milediff = (geodesic(liveloco,nonliveloco).miles)
            mldiff = round(milediff,1)
            newdiff = round(diff,1)
            speak(f"Sir..the difference between {cityloco} from our location is nearly {newdiff} kilometres or {mldiff} miles far away")
        
        elif 't rex' in query.lower() or 'T Rex' in query.lower() or 't-rex' in query.lower() or 't-rex sound' in query.lower():
            playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//t-rex-roar (1).mp3")

        elif 'what sound does a dog make' in query.lower() or 'dog bark' in query.lower() or 'dog barking' in query.lower() or 'dog sound' in query.lower():
            playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//labrador-barking-daniel_simon (1).mp3")  

        elif 'lion roar' in query.lower() or 'lion' in query.lower() or 'lion sound' in query.lower():
            playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//MGMlion (1).wav")  

        elif 'cat' in query.lower() or 'cat meowing' in query.lower() or 'cat meow' in query.lower() or 'cat sound' in query.lower():
            playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//Cat_Meow_2-Cat_Stevens-2034822903.mp3") 

        elif  'rooster sound' in query.lower() or 'rooster' in query.lower():
            playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//Rudy_rooster_crowing-Shelley-1948282641.mp3")

        elif 'meaning' in query.lower():
            speak("Okay sir..tell me the word for which you require the meaning")
            query = takeCommand()
            print (dictionary.meaning(query))
            speak (dictionary.meaning(query))

        elif  'wake up' in query.lower():
            speak("I am indeed awake sir")

        elif 'dog howling' in query.lower() or 'dog howl' in query.lower():
            playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//Dog Howling At Moon-SoundBible.com-1369876823.mp3")    
                
        elif 'crow' in query.lower():
            playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//Crow-noises.mp3")

        elif 'cow' in query.lower():
            playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//Cow-moo-sound.mp3") 

        elif 'horse' in query.lower():
            playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//Horse-whinnying animals037.wav")  

        elif 'sparrow' in query.lower() or 'birds chirping' in query.lower():
            playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//sparrow.mp3")         


        elif 'what day' in query.lower():
            days_ES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

            t = datetime.datetime.now()
            f = t.strftime("{%w} %d/%m/%Y").format(*days_ES)
            print(f)
            speak(f) 

        elif 'calculate' in query.lower():
            query = query.lower()
            res = client.query(query)
            speak("Searching for Results!!")
            results = next(res.results).text
            speak("Results Found!!")
            print(results)
            speak(results)  

        elif 'find my phone' in query.lower():
            speak("Phone Locater Mode Turned On..Sir!!")
            speak("Searching for your phone!!")
            account_sid = 'AC56c485a3d96c35c6b7710270f2f0660f'
            auth_token = '09099db01cb770a3d4847cb2a2581c6c'
            client = TwilioRestClient(account_sid, auth_token)
            call = client.calls.create(
                        #twiml='<Response><Say>Ahoy, World!</Say></Response>',
                        to='+919480255502',
                        from_='+12513571461',
                        url="http://static.fullstackpython.com/phone-calls-python.xml", method="GET")


        elif 'join'in query.lower():
            speak("Opening Zoom Cloud Meetings")
            speak("Sir..do you want to join a meeting or start your own meeting!!")
            zoomPath = "C://Users//Dell//Desktop//Zoom.lnk"
            os.startfile(zoomPath)
            query = pauseListen()
            if 'join' in query.lower() or 'connect' in query.lower():
                speak("Joining the Meeting!!")
                meet_id = '617 201 8131'
                image = "C://Users//Dell//Desktop//JoinButton.PNG"
                x,y = pyautogui.locateCenterOnScreen(image,confidence =0.9)
                print(x,y)
                pyautogui.moveTo(x,y)
                pyautogui.click(x,y)
                pyautogui.click(button='left',clicks=1,interval=0.25)
                #pyautogui.press('enter',interval=1)
                pyautogui.write(meet_id)
                password = "LeoStark"
                pyautogui.press('enter',interval=1)
                time.sleep(2)
                pyautogui.write(password)
                pyautogui.press('enter',interval=1)
                speak("Do you have an Online Class..sir")
                query = takeCommand()
                if 'yes' in query.lower() or 'yep' in query.lower() or 'yeah' in query.lower() or 'yup' in query.lower():
                    speak("Good Luck,,with your online class..sir")
                else:
                    speak("Well,,Good luck with that sir")
                    break 
            elif 'start meeting' in query.lower() or 'start' in query.lower():
                speak("Creating a new meeting!!")
                image = "C://Users//Dell//Desktop//ScheduleMeet.PNG"
                time.sleep(4)
                x,y = pyautogui.locateCenterOnScreen(image,confidence =0.9)
                print(x,y)
                pyautogui.moveTo(x,y)
                pyautogui.click(x,y)
                pyautogui.click(button='left',clicks=1,interval=0.25)
                time.sleep(4)
                pyautogui.hotkey('alt','f')

        elif 'set course for' in query.lower() or 'set cost for' in query.lower():
            destination = query.replace('set course for ',' ') or query.replace('set cost for ',' ') 
            playsound('C://Users//Dell//Desktop//Maps  Automation Pics//Maps Star Trek Voice Automated//Aye Sir.mpeg')#Aye Sir
            time.sleep(1)
            speak(f"Captain!!Setting Navigational Course for {destination}!!")
            playsound('C://Users//Dell//Desktop//Maps  Automation Pics//Maps Star Trek Voice Automated//Computer Click.mpeg')#Computer click
            pyautogui.press('esc',interval=0.1)
            pyautogui.press('win',interval=0.1)
            pyautogui.write('maps')
            time.sleep(1)
            pyautogui.press('enter',interval=1)
            time.sleep(3)
            directions= 'C://Users//Dell//Desktop//Maps  Automation Pics//Directions.PNG'
            xy = pyautogui.locateOnScreen(directions,confidence =0.9)
            pyautogui.moveTo(xy)
            pyautogui.click(xy)
            pyautogui.click(button='left',clicks=2,interval=0.25)    
            time.sleep(2)
            location = 'C://Users//Dell//Desktop//location.png'
            pq = pyautogui.locateOnScreen(location,confidence =0.9)
            pyautogui.moveTo(pq)
            pyautogui.click(pq)
            pyautogui.click(button='left',clicks=1,interval=0.25) 
            destiny = 'C://Users//Dell//Desktop//Maps  Automation Pics//DestinationPoint.PNG'
            cd = pyautogui.locateOnScreen(destiny,confidence =0.9)
            pyautogui.moveTo(cd)
            pyautogui.click(cd)
            pyautogui.click(button='left',clicks=1,interval=0.25) 
            pyautogui.write(destination)
            time.sleep(1)
            pyautogui.press('enter',interval=1)
            director = 'C://Users//Dell//Desktop//Maps  Automation Pics//GetDirections.PNG'
            ab = pyautogui.locateOnScreen(director,confidence =0.9)
            pyautogui.moveTo(ab)
            pyautogui.click(ab)
            pyautogui.click(button='left',clicks=1,interval=0.25)
            time.sleep(1)
            speak(f"Captain..Navigational Course Set for {destination}") 
            quo = pauseListen()
            if 'engage' in quo.lower() or 'fire' in quo.lower() or 'out' in quo.lower() or 'warp' in quo.lower() or 'wrap' in quo.lower():
                playsound('C://Users//Dell//Desktop//Maps  Automation Pics//Maps Star Trek Voice Automated//Aye Sir.mpeg')#aye captain
                speak("!!Warp Speed..Captain!!")
                time.sleep(0.25)
                speak("!!Bon Voyage!!")
                playsound('C://Users//Dell//Desktop//Maps  Automation Pics//Maps Star Trek Voice Automated//Warp Drive.mpeg')#warp drive
            else:
                time.sleep(1)

        elif 'who' in query.lower() or 'why' in query.lower() and 'here' in query.lower() or 'place' in query.lower():
            speak(f"Sir..I clearly remember you telling me to set course for {destination}!!")
            speak(f"So..I set a course for {destination}!!")


        elif 'video call ' in query.lower() or ' call ' in query.lower():
            contact = 'Reshma Jio'
            os.startfile('C://Users//Dell//Desktop//Google Duo.lnk')
            time.sleep(6)
            searchbar = 'C://Users//Dell//Desktop//Maps  Automation Pics//Google Duo Automation//Search Bar.PNG'
            vd = pyautogui.locateOnScreen(searchbar,confidence =0.9)
            pyautogui.moveTo(vd)
            pyautogui.click(vd)
            pyautogui.click(button='left',clicks=1,interval=0.25)
            pyautogui.write(contact)
            pyautogui.press('enter',interval=0.25)  
            videocall =  'C://Users//Dell//Desktop//Maps  Automation Pics//Google Duo Automation//Video Call.PNG'         
            vc = pyautogui.locateOnScreen(videocall,confidence =0.9)
            pyautogui.moveTo(vc)
            pyautogui.click(vc)
            pyautogui.click(button='left',clicks=1,interval=0.25)

        elif ' voice call ' in query.lower():
            query = query.replace('voice call',' ')
            if 'mom' in query.lower() or 'mum' in query.lower():
                contact = 'Reshma Jio'
                os.startfile('C://Users//Dell//Desktop//Google Duo.lnk')
                time.sleep(5)
                searchbar = 'C://Users//Dell//Desktop//Maps  Automation Pics//Google Duo Automation//Search Bar.PNG'
                vd = pyautogui.locateOnScreen(searchbar,confidence =0.9)
                pyautogui.moveTo(vd)
                pyautogui.click(vd)
                pyautogui.click(button='left',clicks=1,interval=0.25)
                pyautogui.write(contact)
                pyautogui.press('enter',interval=0.25)  
                voicecall =  'C://Users//Dell//Desktop//Maps  Automation Pics//Google Duo Automation//Voice Call.PNG'         
                vl = pyautogui.locateOnScreen(voicecall,confidence =0.9)
                pyautogui.moveTo(vl)
                pyautogui.click(vl)
                pyautogui.click(button='left',clicks=1,interval=0.25)

        elif 'Jarvy' in query.lower() or 'jarvy' in query.lower():
            speak("Yes..sir..")        
        
        elif "I/'m not finding this answer" in query.lower() or 'my homework' in query.lower():
            speak("Okay sir,,tell me the subject of which you could not find the answer")
            query = takeCommand()
            if 'Math' in query.lower() or 'maths' in query.lower() or 'mathematics' in query.lower():
                speak("What\'s the name of the chapter sir")
                query=takeCommand()
                if 'trignometry' in query.lower() or 'trigonometry' in query.lower():
                    speak("Okay sir,,opening Solutions for Trigonometrical ratios")
                    webbrowser.open("https://www.aplustopper.com/selina-icse-solutions-class-9-maths-trigonometrical-ratios/")
            elif 'physics' in query.lower():
                speak("What\'s the name of the chapter sir")
                query = takeCommand()
                if 'electricity' in query.lower():
                    speak("Okay sir,,opening Solution for Current Electricity")
                    webbrowser.open("https://www.aplustopper.com/selina-icse-solutions-class-9-physics-current-electricity/")

        elif 'thank you' in query.lower():
            speak("Oh..my pleasure...you are welcome sir")  

        elif 'you there' in query.lower():
            speak("Yes..sir,,for you,,always")

        elif 'sleep' in query.lower():
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'youtube videos' in query.lower() or 'Youtube videos' in query.lower() or 'Youtube' in query.lower() or 'youtube' in query.lower():
            speak("Well..what would you like to watch sir")
            query = takeCommand()
            speak("Excellent choice Boss!!")
            text = query
            yt = yt_search.build("AIzaSyCtWMxKG8NA3LGEa5YALIURupE_lAIPa_4")
            search_result = yt.search(text, sMax=1, sType=["video"])
            ytname = search_result.title
            ytchnl = search_result.channelTitle
            ytid = search_result.videoId
            def listToString(s):  
                str1 = " " 
                return (str1.join(s)) 
            s = ytid
            ytid = listToString(s)            
            #ytid = [i.replace("[", "") for i in ytid] #and [item.replace("]", "") for item in ytid]
            speak(f"Playing {ytname} by {ytchnl}")
            #print(s)
            ytlink = "http://www.youtube.com/watch?v="
            webbrowser.open(ytlink+ytid)


        elif 'images' in query.lower() or 'image' in query.lower() and 'protocol' in query.lower() or 'interface' in query.lower():
            speak("Initiating..Image Recognition Protocol..")
            sp =['What are you looking for sir..','What have you got in your mind..sir']
            speak(random.choice(sp))
            query = takeCommand()
            tabUrl = "https://www.google.com/search?q=" 
            taborl = "+&tbm=isch&ved=2ahUKEwjqmf2J08zpAhX4K7cAHeRPC1UQ2-cCegQIABAA&oq=star+&gs_lcp=CgNpbWcQAzIECCMQJzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQEzIECAAQE1CUMli7N2COQGgAcAB4AIABwwSIAccIkgEJMC4yLjEuNS0xmAEAoAEBqgELZ3dzLXdpei1pbWc&sclient=img&ei=b3zKXqqmKvjX3LUP5J-tqAU&bih=635&biw=1366"
            webbrowser.open(tabUrl+query+taborl)

        elif 'hedwig' in query.lower() or 'harry potter' in query.lower():
            playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//Hedwig s Theme.mp3")

        elif 'fast and furious' in query.lower() or 'danza kuduro' in query.lower():
            playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//Don Omar - Danza Kuduro  feat. Lucenzo.mp3") 
            playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//Don Omar -  How We Roll (Fast Five Remix) ft. Busta Rhymes. Reek da Villian & J-doe.mp3")
            
        elif 'kung fu fighting' in query.lower() or 'kumg fu songs' in query.lower():
            playsound("C://Users//Dell//Desktop//J.A.R.V.I.S (v2.0)//carldouglaskungfufightingfunk80.mp3")

        elif 'online' in query.lower():
            speak("I am indeed..Online..sir")

        elif 'open translate' in query.lower() or 'open google translate' in query.lower():
            speak("Okay sir,,opening Google Translate")
            webbrowser.open("https://translate.google.com/")

        elif 'date' in query.lower() or 'today\'s date' in query.lower():
            strTime = datetime.datetime.now().strftime(" Today\'s date is %d %m %y20")
            print(strTime)
            speak(strTime)

        elif ' alarm ' in query.lower():
            query = query.replace('alarm','')
            speak(f"Setting an alarm for {query} ")
            stop = False
            while stop == False:
                rn = str(datetime.datetime.now().time())
                print(rn)
                if '1 am' in query.lower() and  rn >= "01:00:00.000000":
                    stop = True
                    speak("Sir..its 1 am")    
                elif '2 am' in query.lower() and  rn >= "02:00:00.000000":
                    stop = True
                    speak("Sir..its 2 am")                      
                elif '3 am' in query.lower() and  rn >= "03:00:00.000000":
                    stop = True
                    speak("Sir..its 3 am")
                elif '4 am' in query.lower() and  rn >= "04:00:00.000000":                   
                    stop = True
                    speak("Sir..its 4 am")
                elif '5 am' in query.lower() and rn >= "05:00:00.000000":
                    stop = True
                    speak("Sir..its 5 am")
                elif '6 am' in query.lower() and rn >= "06:00:00.000000":                   
                    stop = True
                    speak("Sir..its 6 am") 
                elif '7 am' in query.lower() and rn >= "07:00:00.000000":                   
                    stop = True
                    speak("Sir..its 7 am")
                elif '8 am' in query.lower() and rn >= "08:00:00.000000":                   
                    stop = True
                    speak("Sir..its 8 am")
                elif '9 am' in query.lower() and rn >= "09:00:00.000000":                    
                    stop = True
                    speak("Sir..its 9 am")                        
                elif '10 am' in query.lower() and rn >= "10:00:00.000000":                   
                    stop = True
                    speak("Sir..its 10 am")
                elif '11 am' in query.lower() and rn >= "11:00:00.000000":                    
                    stop = True
                    speak("Sir..its 11 am")
                elif '12 am' in query.lower() and rn >= "00:00:00.000000":                   
                    stop = True
                    speak("Sir..its 12 am")                        
                elif '12 pm' in query.lower() and rn >= "12:00:00.000000":                 
                    stop = True
                    speak("Sir..its 12 pm")
                elif '1 pm' in query.lower() and rn >= "13:00:00.000000":                    
                    stop = True
                    speak("Sir..its 1 pm")
                elif '2 pm' in query.lower() and rn >= "14:00:00.000000":                   
                    stop = True
                    speak("Sir..its 2 pm")                                    
                elif '3 pm' in query.lower() and rn >= "15:00:00.000000":                  
                    stop = True
                    speak("Sir..its 3 pm")
                elif '4 pm' in query.lower() and rn >= "16:00:00.000000":                  
                    stop = True
                    speak("Sir..its 4 pm")
                elif '5 pm' in query.lower() and rn >= "17:00:00.000000":                    
                    stop = True
                    speak("Sir..its 5 pm")                        
                elif '6 pm' in query.lower() and rn >= "18:00:00.000000":                    
                    stop = True
                    speak("Sir..its 6 pm")
                elif '7 pm' in query.lower() and rn >= "19:00:00.000000":                  
                    stop = True
                    speak("Sir..its 7 pm")
                elif '8 pm' in query.lower() and rn >= "20:00:00.000000":                  
                    stop = True
                    speak("Sir..its 8 pm")  
                elif '9 pm' in query.lower() and rn >= "21:00:00.000000":                   
                    stop = True
                    speak("Sir..its 9 pm")                                              
                elif '10 pm' in query.lower() and rn >= "22:00:00.000000":                   
                    stop = True
                    speak("Sir..its 10 pm")
                elif '11 pm' in query.lower() and rn >= "23:00:00.000000":                    
                    stop = True
                    speak("Sir..its 11 pm")
                else:
                    sms = 00.000
                    #quo = (query)(double)
                    quo = float(query)
                    tm = quo+sms
                    if rn >= tm:
                        stop = True
                        speak("Alarm Successful")   

        elif 'how are you' in query.lower() or 'are you ok' in query.lower() or 'are you okay' in query.lower() or 'are you fine' in query.lower() or ' how you doing ' in query.lower():
            slo = ['I\'m fine thank you sir','Oh,,I\'m all well sir']
            speak(random.choice(slo))     

        elif 'open python 3.6' in query.lower() or 'python' in query.lower():
            speak("okay sir, opening Python 3.6.8")
            pythonPath = "C://Users//Dell//Desktop//Python 3.6.8//python.exe"
            os.startfile(pythonPath)

        elif ' into binary'in query.lower():
            query = takeCommand()
            query = query.replace("into binary", " ")
            speak(f"Converting {query} into Binary Code")
            st = query
            bi = ' '.join(format(ord(x), 'b') for x in st)
            speak(f"{query} in Binary Format is {bi}")
            print(f"{query} in Binary Format is {bi}")

        elif ' in binary'in query.lower():
            query = takeCommand()
            query = query.replace("in binary", "")
            speak(f"Converting {query} into Binary Code")
            st = query
            bi = ' '.join(format(ord(x), 'b') for x in st)
            speak(f"{query} in Binary Format is {bi}")
            print(f"{query} in Binary Format is {bi}")

        elif 'who are you' in query.lower():
            speak("I am Jarvis , your very own A I assistant")

        elif 'who am I' in query.lower():
            speak(f"You are {MASTER}, my boss ")   

        elif 'when is my birthday' in query.lower():
            speak("Sir, your birthday is on the eleventh of september each year")

        elif 'what is my DOB' in query.lower() or 'what is my date of birth' in query.lower() or 'my birthday' in query.lower():
            speak("Sir, your date of birth is eleven..nine..two thousand and six")         

        elif 'open control panel' in query.lower():
            speak("Okay sir,,opening Control Panel")
            codePath = "C://Users//Dell//Desktop//Control Panel - Shortcut.lnk"
            os.startfile(codePath)    

        elif 'my location' in query.lower() or ' latitude and longitude'in query.lower():
            g = geocoder.ip('me')
            print("Latitude:",g.latlng) 
            speak("Sir, our current Latitudes and Longitudes are ")   
            speak(g.latlng)

        elif 'corona' in query.lower() or 'covid' in query.lower():
            webbrowser.open("https://www.worldometers.info/coronavirus/country/india/")

        elif 'where are you' in query.lower():
            speak("Oh..I,,am,,right,,here,,sir")    
        
        elif 'open bing' in query.lower():
            speak("Okay sir, opening Bing.com")
            webbrowser.open("www.bing.com")    

        elif 'open gmail' in query.lower():
            speak("Okay sir, opening G Mail.com")
            webbrowser.open("www.gmail.com")

        elif 'remember' in query.lower() or 'keep in mind' in query.lower():
            query = query.replace("remember", " ") 
            rem = query
            speak("Okay sir..I will that in mind  "+rem)

        elif 'remind' in query.lower():
            speak("You asked me to remember "+rem)  

        elif 'meet' in query.lower():
            query = query.replace("meet"," ")
            nm = query
            speak("Nice to meet you!!"+nm)

        elif 'caller' in query.lower() and 'id' in query.lower() or 'ID' in query.lower() or 'Id' in query.lower() and 'interface' in query.lower():
            speak("Initiating Caller ID Interface")
            time.sleep(1.5)
            speak("Please type the phone number..Sir!!")
            UTC = pytz.utc
            cell = input("Enter Phone Number: ")
            z = phonenumbers.parse(cell, None)
            posble = phonenumbers.is_possible_number(z)
            if cell == '+919480255502':
                speak("Sir..Caller Name identified..its P.B Shankarappa")

            if posble==True:
                print("Sir..It\'s an active phone number")
                speak("Sir..It\'s an active phone number")
            else:
                print("Sir..I don\'t think this is an active number!!It may be a fake number or an inactive number!!")
                speak("Sir..I don\'t think this is an active number!!It may be a fake number or an inactive number!!")
            phone_country(cell)      
            c = pycountry.countries.get(alpha_2=phone_country(cell))
            print(f"The number appears to be of {c.name} origin or from the {c.official_name}")
            speak(f"The number appears to be of {c.name} origin or from the {c.official_name}")
            ro_number = phonenumbers.parse(cell,"RO")
            print(carrier.name_for_number(ro_number, "en"))
            speak(carrier.name_for_number(ro_number, "en"))
            print(geocell.PhoneNumberOfflineGeocoder(cell, "en"))
            speak(geocell.PhoneNumberOfflineGeocoder(cell, "en"))  

        elif 'web' in query.lower() or 'website' in query.lower():
            speak("Initiating Advanced Web Search Interface")
            speak("Okay sir..which website are you planning to visit..")  
            query = takeCommand()
            ht = "https://www."
            co = ".com"
            webbrowser.open(ht+query+co)
 
        elif 'open amazon.in' in query.lower() or 'open amazon india' in query.lower():
            speak("Okay sir, opening Amazon.in")
            webbrowser.open("www.amazon.in")

        elif 'open prime video' in query.lower() or 'open amazon prime video' in query.lower():
            speak("Okay sir, opening Amazon Prime Video")
            webbrowser.open("www.primevideo.com")

        elif 'open amazon.com' in query.lower() or 'open amazon international' in query.lower():
            speak("Okay sir, opening Amazon.com")
            webbrowser.open("wwww.amazon.com")

        elif 'open apple.com' in query.lower() or 'open apple' in query.lower():
            speak("Okay sir, opening Apple.com")
            webbrowser.open("www.apple.com")        

        elif 'open outlook' in query.lower() or 'open outlook website' in query.lower():
            speak("Okay sir, opening Microsoft Outlook")
            webbrowser.open("outlook.live.com")

        elif 'open github' in query.lower() or 'open github website' in query.lower():
            speak("Okay sir, opening GitHub")
            webbrowser.open("www.github.com")

        elif 'open facebook' in query.lower() or 'open facebook website' in query.lower():
            speak("Okay sir, opening FaceBook ")
            webbrowser.open("www.facebook.com")

        elif 'open reddit' in query.lower() or 'open reddit mail' in query.lower():
            speak("Okay sir, opening Reddit Mail")
            webbrowser.open("www.reddit.com")

        elif 'flight tickets' in query.lower() or 'tell me a flight booking website' in query.lower():
            speak("Sir,,How about you search in Google Flights")
            speak("Should I open it for you sir")   

        elif 'google flights' in query.lower() or 'open flight website' in query.lower():
            speak("Okay sir,,opening Google flights")
            webbrowser.open("https://www.google.com/flights?q=flights&sxsrf=ALeKk00WcIRzqVvD5bIrgjbsEvz0OjVgPA:1588514303267&source=lnms&impression_in_search=true&mode_promoted=true&tbm=flm&sa=X&ved=2ahUKEwj985D27JfpAhW-gUsFHfYzDRcQ_AUoAXoECA4QAw#flt=BLR..2020-05-19*.BLR.2020-05-23;c:INR;e:1;sd:1;t:h")

        elif 'open whatsapp' in query.lower():
            speak("Okay sir, opening Whatsapp.com")
            webbrowser.open("www.whatsapp.com")

        elif 'open pinterest' in query.lower():
            speak("Okay sir, opening Pinterest website")
            webbrowser.open("www.pinterest.com")

        elif 'open imdb' in query.lower():
            speak("Okay Sir, opening IMDB website ")
            webbrowser.open("www.imdb.com")

        elif 'open ebay' in query.lower():
            speak("Okay sir, opening eBAY website")
            webbrowser.open("www.ebay.com")       

        elif 'open netflix' in query.lower():
            speak("Open sir, opening Netflix") 
            webbrowser.open("www.netflix.com")

        elif 'open maps' in query.lower():
            speak("Okay sir, opening Google Maps") 
            speak("What place are you looking for sir..")  
            query = takeCommand()
            sg = "https://www.google.com/maps/search/" 
            og = "/@13.0629315,77.524434,14z/data=!3m1!4b1"
            webbrowser.open(sg+query+og)
            speak("Results found for " +query)

        elif 'open linked in' in query.lower():
            speak("Okay sir, opening Linked In")
            webbrowser.open("www.linkedin.com")

        elif 'open microsoft' in query.lower():
            speak("Okay sir, opening Microsoft dot com")
            webbrowser.open("www.microsft.com")

        elif 'open adobe' in query.lower():
            speak("Okay sir, opening Adobe dot com")
            webbrowser.open("www.adobe.com")

        elif 'open tatasky' in query.lower() or 'Tata Sky' in query.lower():
            speak("Okay sir, opening Tatasky")
            webbrowser.open("www.tatasky.com")    

        elif 'open yahoo' in query.lower():
            speak("ok..sir opening yahoo.com")
            webbrowser.open("mail.yahoo.com")  

        elif 'tell jokes' in query.lower() or 'tell me some jokes' in query.lower() or 'say jokes' in query.lower() or 'make some jokes' in query.lower() or 'crack some jokes' in query.lower():
            jokeM = ['Why can\'t astronauts eat popsicles........Because in space, no one can hear the ice cream truck','What\'s the first thing a monster eats after he\'s had his teeth checked....the answer is The Dentist','Write an essay on cricket on ......the teacher told the class..,,,,,,,,,Chintu finishes his work in 5 minutes..,,,,,,,,,,,,The teacher is impressed,,,,,,,,,,..she asks Chintu to read his essay out loud for everyone...,,,,,,,Chintu reads...,,,,The cricket match is cancelled due to rain']
            speak(random.choice(jokeM))
            speak("Ha..Ha..Ha..Ha") 
            print("Ha..Ha..Ha..Ha")

        elif 'heads and tails' in query.lower() or 'toss' in query.lower():
            speak("What do you choose sir,,")
            query = takeCommand()
            playsound("C:\\Users\\Dell\\Desktop\\J.A.R.V.I.S (v2.0)\\WhatsApp Audio 2020-06-07 at 2.41.46 PM.mpeg")
            if 'heads' in query.lower():
                speak("Heads is the call..")
                lo = ['Well played, You won sir,,','Sorry,,you lost sir,,']
                speak(random.choice(lo))
            elif 'tails' in query.lower():
                speak("Tails is the call..")
                lo = ['Well played, You won sir,,','Sorry,,you lost sir,,']
                speak(random.choice(lo))
            else:
                speak("Unknown Input..sir,,")    

        elif 'thank you' in query.lower() or 'thanks' in query.lower():
            speak("You are welcome..sir")

        elif 'my name' in query.lower() or 'who am i' in query.lower() or 'do you know who i am' in query.lower():
            speak(f"Sir, you name is {MASTER} and you are my boss..")  

        elif 'don\'t you know who i am' in query.lower() or 'you do know who i am' in query.lower():
            speak(f"In fact,, I do know who you sir,, you are {MASTER} my boss")
        
        elif 'open stackoverflow' in query:
            speak("Okay sir,, opening Stack Over Flow.com")
            webbrowser.open("stackoverflow.com")  

        elif 'weather forecast' in query.lower():
            speak("Okay sir , here is today\'s weather forecast")
            for key,val in temperature.items():
                print(f'{key} is equal to {val}')
                speak(f"{key} is equal to {val}")
            
        elif 'you are mean' in query.lower() or 'bad' in query.lower():
            speak("Sorry..sir..if..I was mean to you sir ")    
 
        elif 'time' in query.lower() and 'what\'s' in query.lower() or 'what' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            olo = (strTime)[0]
            print(olo)   
            speak(f"Sir, the time is {strTime}")

        elif 'despacito' in query.lower():
            speak("Okay sir,,playing Despacito")
            playsound('C:\\Users\\Dell\\Music\\Dono.mp3')

        elif 'my photo' in query.lower():
            speak("Okay sir,,here are some of your photos")
            img = cv2.imread("C:\\Users\\Dell\\Pictures\\Camera Roll\\LOLU pandey.jpg")
            cv2.imshow("Your Photos",img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
         
        elif 'battery' in query.lower():
            speak(f"Sir,,your current battery percentage is at {psutil.sensors_battery().percent}%")
            print(f"Sir,,your current battery percentage is at {psutil.sensors_battery().percent}%")
            if psutil.sensors_battery().percent <40:
                speak("Sir,,your device is on low battery..I suugest you charge it now..")
                print("Sir,,your device is on low battery..I suugest you charge it now..")

        elif 'shape of you' in query.lower():
            speak("Okay sir,,playing Shape of You by Ed Sheeran")
            playsound('C:\\Users\\Dell\\Music\\Shape of you.mp3')

        elif 'play on my way' in query.lower() or 'play i\'m on my way' in query.lower():
            speak("Okay sir,,playing I\'m On My Way by Alan Walker")
            playsound("C:\\Users\Dell\\Desktop\\J.A.R.V.I.S (v2.0)\\Alan Walker, Sabrina Carpenter & Farruko - On My Way (1) - Copy.mp3")

        elif 'something that iron man' in query.lower() or 'iron man songs' in query.lower() or 'something that tony stark' in query.lower():
            speak("Okay sir,,playing Iron Man songs")

        elif 'cheap thrills' in query.lower():
            speak("Okay sir,,playing Cheaps Thrills by Sia")  
            playsound("C:\\Users\\Dell\\Music\\Sia - Cheap Thrills (DawnFoxes.com).mp3")      

        elif 'play danza kuduro' in query.lower() or 'play Danza Kuduro' in query.lower():
            speak("Okay sir,,playing Danza Kuduro")
            playsound('C:\\Users\\Dell\\Desktop\\My songs\\Don Omar - Danza Kuduro  feat. Lucenzo .mp3')

        elif 'open code' in query.lower():
            speak("Okay sir,,opening Visual Studio Code")
            codePath = "C://Users//Dell//Desktop//Microsoft VS Code//Code.exe"
            os.startfile(codePath)


        elif 'open adobe reader' in query.lower() or 'open reader' in query.lower():
            codePath = "C://ProgramData//Microsoft//Windows//Start Menu//Programs//Acrobat Reader DC.lnk" 
            os.startfile(codePath)
  
        elif 'open amazon music' in query.lower():
            speak("Okay sir,,opening Amazon prime Music")
            codePath = "C://Users//Dell//Desktop//pycharm projects//Amazon Music.lnk" 
            os.startfile(codePath) 

        elif 'open voice recorder' in query.lower():
            speak("Okay sir,,opening Windows Voice Recorder")
            codePath = "C://Users//Dell//Desktop//pycharm projects//Voice Recorder.lnk" 
            os.startfile(codePath)     

        elif 'open itunes' in query.lower() or 'open i tunes' in query.lower():
            speak("Okay sir,,opening Apple i Tunes")
            codePath =  "C://Users//Dell//Desktop//pycharm projects//iTunes.lnk"
            os.startfile(codePath)   

        elif 'open vlc' in query.lower():
            speak("Okay sir,,opening VLC Media Player")
            codePath = "C://Users//Dell//Desktop//pycharm projects//VLC media player.lnk"
            os.startfile(codePath)

        elif 'open skype' in query.lower():
            speak("Okay sir,, opening Microsoft Skype")
            codePath = "C://Users//Dell//Desktop//pycharm projects//Skype.lnk"
            os.startfile(codePath)

        elif 'play lily' in query.lower():
            speak("Okay sir,,playing Lily by Alan Walker")
            playsound("C:\\Users\\Dell\\Desktop\\J.A.R.V.I.S (v2.0)\\Alan Walker, K-391 & Emelie Hollow - Lily.mp3")    

        elif 'open calculator' in query.lower():
            speak("Okay sir,,opening Calculator")
            codePath = "C://Users//Dell//Desktop//pycharm projects//Calculator.lnk"
            os.startfile(codePath)

        elif 'routine' in query.lower() or 'schedule' in query.lower() or 'what do i have' in query.lower() or 'do i have plans' in query.lower() or 'am i busy' in query.lower():                
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
            if os.path.exists('token.pickle'):
                with open('token.pickle', 'rb') as token:
                    creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
                    if not creds or not creds.valid:
                        if creds and creds.expired and creds.refresh_token:
                            creds.refresh(Request())
                    else:
                        flow = InstalledAppFlow.from_client_secrets_file(
                        'C://Users//Dell//Downloads//client_secret.json', SCOPES)
                        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
                        with open('token.pickle', 'wb') as token:
                            pickle.dump(creds, token)

                    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
                    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
                    print('Here\'s your routine for the day')
                    print('Here\'s your routine for the day')
                    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
                    events = events_result.get('items', [])

                    if not events:
                        print('No upcoming events found..sir')
                        speak('No upcoming events found..sir')
                    for event in events:
                        start = event['start'].get('dateTime', event['start'].get('date'))
                        print(start, event['summary'])
                        speak(start, event['summary'])

            
        elif 'open powerpoint' in  query.lower() or 'open power point' in query.lower() or 'open PowerPoint' in query.lower() or 'PowerPoint' in query.lower():
            speak("Okay sir,,opening Microsoft Powerpoint 2013")
            codePath = "C://Users//Dell//Desktop//pycharm projects//PowerPoint 2013.lnk"
            os.startfile(codePath)

        elif  'open chrome' in query.lower() or 'open google chrome' in query.lower():
            speak("Okay sir,,opening Google Chrome")
            codePath = "C://Users//Dell//Desktop//pycharm projects//Google Chrome.lnk"
            os.startfile(codePath)

        elif 'open word' in query.lower() or 'open microsoft word' in query.lower():
            speak("Okay sir,,opening Microsoft Word 2013")
            codePath = "C://Users//Dell//Desktop//pycharm projects//Word 2013.lnk"
            os.startfile(codePath)

        elif 'open outlook' in query.lower() or 'open microsoft outlook' in query.lower():
            speak("Okay sir,,opening Microsoft Outlook 2013")
            codePath = "C://Users//Dell//Desktop//pycharm projects//Outlook 2013.lnk"
            os.startfile(codePath)

        elif  'open camera'  in query.lower():
            speak("Okay sir,,opening Dell Camera")
            codePath = "C://Users//Dell//Desktop//pycharm projects//Camera.lnk"
            os.startfile(codePath)

        elif 'open scratch desktop' in query.lower() or 'open scratch' in query.lower():
            speak("Okay sir,,opening Scratch Desktop")
            codePath = "C://Users//Dell//Desktop//pycharm projects//Scratch Desktop.lnk"  
            os.startfile(codePath)  

        elif 'open calender' in query.lower():
            speak("Okay sir,,opening Calender")
            codePath = "C://Users//Dell//Desktop//pycharm projects//Calendar.lnk" 
            os.startfile(codePath) 

        elif 'open microsoft store' in query.lower() in 'open store' in query.lower():
            speak("Okay sir,,opening Microsoft Store")
            codePath = "C://Users//Dell//Desktop//pycharm projects//Microsoft Store.lnk"
            os.startfile(codePath)
    
        elif 'news' in query.lower():
            speak("okay sir, here are the latest news from Google News")
            for news in news_list:
                print(news.title.text[5])
                print(news.pubDate.text[5])
                print("-"*60)
                speak(news.title.text[5])
                
        elif 'quote of the day' in query.lower() or 'quote' in query.lower():
            res=requests.get("https://www.brainyquote.com/quote_of_the_day")
            soup=BeautifulSoup(res.text,'lxml')
            image_quote = soup.find('img', {'class':'p-qotd'})
            print(image_quote['alt'])   
            speak(image_quote['alt'])

        elif 'create' in query.lower() or 'add' in query.lower() or 'make' in query.lower() and 'folder' in query.lower() or 'directory' in query.lower():
            speak("Creating a new folder!!!")
            speak("What would you like to name it..sir!!")
            query = takeCommand()
            dirName = query
            try:
                path = 'C://Users//Dell//Desktop//'
                os.mkdir(path+dirName)
                print("Directory ",dirName,"Created")
                speak(f"A new folder with the name {dirName} created Successfully sir!!")
            except FileExistsError:
                print("Directory ",dirName,"already exists")
                speak(f"Sir..I believe a folder with the name {dirName} already exists!!")
            speak("Should I open it for you..Sir!!")
            query = takeCommand()
            if 'sure' in query.lower() or 'yes' in query.lower() or 'yeah' in query.lower() or 'yep' in query.lower() or 'ok' in query.lower() or 'okay' in query.lower() or 'open' in query.lower():
                folder = path+dirName
                webbrowser.open(folder)     

        elif 'open bing' in query.lower():
            speak("Okay sir, opening Bing.com")
            webbrowser.open("www.bing.com")   

        elif 'abort' in query.lower() or 'stop' in query.lower() or 'goodbye' in query.lower() or 'deactivate' in query.lower() or 'kill' in query.lower():
            speak("Okay sir") 
            speak("Powering off systems...")
            playsound("C:\\Users\\Dell\\AppData\\Roaming\\LINKS\\Customization\\Sound Effects\\ClickClose_listening_stopped.wav")
            sor = ['Farewell sir', 'Goodbye sir',]
            speak(random.choice(sor))
            sys.exit() 

        elif 'what is the humidity' in query.lower() or 'humid' in query.lower() or 'humidity' in query.lower():
            print(f"Sir,,the humidity is {humidity} percent")
            speak(f"Sir,,the humidity is {humidity} percent")
            if humidity<50:
                speak("Sir,,the humidity is low ,, and so it\'s dry")
            else:
                speak("Sir,,the humidity is high,,so it\'s very humid or wet")
                
        elif 'email' in query.lower():
            speak("Okay sir...Initiating,,Send,,Email,,Interface")
            recipient = takeCommand()
            if 'me' in recipient:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "modernnerds2588@gmail.com"    
                    sendEmail(to, content)
                    speak("Email sent sucessfully sir!")            
                except:
                    speak("Sorry sir, the email could  not be sent") 
        else:
            query = query
            try:
                res = client.query(query)
                results = next(res.results).text
                print(results)
                speak(results)       
            except:
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak(results)                                       
vid.release()  
cv2.destroyAllWindows() 