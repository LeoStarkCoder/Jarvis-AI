import datetime
import os
import smtplib
import webbrowser
import winsound
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wkipedia
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import pyowm
import geocoder
import sys
import random
from playsound import playsound
import cv2
import requests
import psutil
from bs4 import BeautifulSoup as bs




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)


print("Initiaizing Jarvis")
MASTER = "Lohith S"

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

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
# US english
LANGUAGE = "en-US,en;q=0.5"


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir...!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir...!")   

    else:
        speak("Good Evening Sir...!")   


def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        playsound("C:\\Users\\Dell\\AppData\\Roaming\\LINKS\\Customization\\Sound Effects\\System_ready.wav")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Searching...")    
        query = r.recognize_google(audio, language='en-UK')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        speak('Sorry sir,  i Didn\'t get that')
        return "None"
    return query

speak("I am online sir")

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('moderngaming2588@gmail.com', 'Lohith01')
    server.sendmail('moderngaming2588@gmail.com', to, content)
    server.close()

def week():
    days_ES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    t = datetime.datetime.now()
    f = t.strftime("{%w} ....%d %m %Y").format(*days_ES)
    speak("..........Hello sir,,,it\'s...")
    speak(f)
    print(f)
week()

def weaheth():
    speak("Sir,,,let me tell you today\'s ...Weather Forecast..")
    for key,val in temperature.items():
        print(key, val)
        speak(key)
        speak(val) 
weaheth()

def batter():
    speak(f"The battery percentage is at {psutil.sensors_battery().percent}%")
    print(f"The battery percentage is at {psutil.sensors_battery().percent}%")
batter() 

def get_weather_data(url):
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html = session.get(url)
    # create a new soup
    soup = bs(html.text, "html.parser")
    # store all results on this dictionary
    result = {}
    # extract region
    result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text
    # extract temperature now
    result['temp_now'] = soup.find("span", attrs={"id": "wob_tm"}).text
    # get the day and hour now
    result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
    # get the actual weather
    result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
    # get the precipitation
    result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
    # get the % of humidity
    result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
    # extract the wind
    result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text
    # get next few days' weather
    next_days = []
    days = soup.find("div", attrs={"id": "wob_dp"})
    for day in days.findAll("div", attrs={"class": "wob_df"}):
        # extract the name of the day
        day_name = day.find("div", attrs={"class": "vk_lgy"}).attrs['aria-label']
        # get weather status for that day
        weather = day.find("img").attrs["alt"]
        temp = day.findAll("span", {"class": "wob_t"})
        # maximum temparature in Celsius, use temp[1].text if you want fahrenheit
        max_temp = temp[0].text
        # minimum temparature in Celsius, use temp[3].text if you want fahrenheit
        min_temp = temp[2].text
        next_days.append({"name": day_name, "weather": weather, "max_temp": max_temp, "min_temp": min_temp})
    # append to result
    result['next_days'] = next_days
    return result
get_weather_data(url)    

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

            URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
            import argparse
            parser = argparse.ArgumentParser(description="Quick Script for Extracting Weather data using Google Weather")
            parser.add_argument("region", nargs="?", help="""Region to get weather for, must be available region.Default is your current location determined by your IP Address""", default="")
                                        
    # parse arguments
            args = parser.parse_args()
            region = args.region
            URL += region
    # get data
            data = get_weather_data(URL)
    # print data
            print("Your current location is", data["region"])
            print(f"The temperature is ", data['temp_now']+"°C")
            print("It\'s  ", data['weather_now'])
            print("Chances of rain is", data["precipitation"])
            print("Humidity is ", data["humidity"])
            print("The current wind speed is ", data["wind"])
            print("Next days:")
            for dayweather in data["next_days"]:
                print("="*40, dayweather["name"], "="*40)
                print("Description:", dayweather["weather"])
                print(f"Max temperature: {dayweather['max_temp']}°C")
                print(f"Min temperature: {dayweather['min_temp']}°C")    

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'will it rain' in query.lower():
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
                print("I suggest you carry an umbrella..because according to the reports...I am sure it will rain today")
                speak("I suggest you carry an umbrella..because according to the reports...I am sure it will rain today")

            elif clouds == 'True' and rain == 'False':
                print("But sir even though it won\'t rain today....It is very cloudy outside")
                speak("But sir even though it won\'t rain today....It is very cloudy outside")    
 

        elif 'sunset time' in query.lower() or 'sunrise time' in query.lower() or'what time will the sunset' in query.lower() or 'what time will the sunrise' in query.lower():
            sr = weather.get_sunrise_time(timeformat='iso')
            ss = weather.get_sunset_time(timeformat='iso')
            print(f'Sunrise = {sr}')
            print(f'Sunset = {ss}')
            speak(f"Sunrise time is {sr}")
            speak(f"Sunset time is {ss}")   

        elif 'google search' in query.lower():
            new = 2
            tabUrl = "https://google.com/?#q="
            term = takeCommand()
            webbrowser.open(tabUrl+term,new=new)

        elif 'hello' in query.lower() or 'hello lohith' in query.lower() or 'hello Lohith' in query.lower() or 'Lohith' in query.lower() or 'lohith' in query.lower():
            playsound("C:\\Users\\Dell\\Desktop\\J.A.R.V.I.S (v2.0)\\VID_20200513_151149.mp3") 

        elif 'good morning Lohith' in query.lower() or 'good morning' in query.lower() or 'Good Morning' in query.lower(): 
            playsound("C:\\Users\\Dell\\Desktop\\J.A.R.V.I.S (v2.0)\\VID_20200513_151212.mp3") 





        elif 'what day' in query.lower():
            days_ES = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

            t = datetime.datetime.now()
            f = t.strftime("{%w} %d/%m/%Y").format(*days_ES)
            print(f)
            speak(f) 

        elif 'open translate' in query.lower() or 'open google translate' in query.lower():
            speak("Okay sir,,opening Google Translate")
            webbrowser.open("https://translate.google.com/")

        elif 'the date' in query.lower() or 'today\'s date' in query.lower():
            strTime = datetime.datetime.now().strftime(" Today\'s date is %d %m %y20")
            print(strTime)
            speak(strTime) 

        elif 'how are you' in query.lower() or 'are you ok' in query.lower() or 'are you okay' in query.lower() or 'are you fine' in query.lower():
            slo = ['I\'m fine thank you sir','Oh,,I\'m all well sir']
            speak(random.choice(slo))     

        elif 'open python 3.6' in query.lower() or 'python' in query.lower():
            speak("okay sir, opening Python 3.6.8")
            pythonPath = "C://Users//Dell//Desktop//Python 3.6.8//python.exe"
            os.startfile(pythonPath)

        elif 'who are you' in query.lower():
            speak("I am Jarvis , your very own A I assistant")

        elif 'who am I' in query.lower():
            speak(f"You are {MASTER}, my boss ")   

        elif 'when is my birthday' in query.lower():
            speak("Sir, your birthday is on the eleventh of september each year")

        elif 'what is my DOB' in query.lower() or 'what is my date of birth' in query.lower():
            speak("Sir, your date of birth is eleven..nine..two thousand and six")         

        elif 'open google' in query.lower():
            speak("Okay sir, opening Google.com")
            webbrowser.open("google.com")

        elif 'open control panel' in query.lower():
            speak("Okay sir,,opening Control Panel")
            codePath = "C://Users//Dell//Desktop//Control Panel - Shortcut.lnk"
            os.startfile(codePath)    

        elif 'my location' in query.lower() or 'my latitude and longitude'in query.lower():
            g = geocoder.ip('me')
            print("Latitude:",g.latlng) 
            speak("Sir, our current Latitudes and Longitudes are ")   
            speak(g.latlng)
        
        elif 'open bing' in query.lower():
            speak("Okay sir, opening Bing.com")
            webbrowser.open("www.bing.com")    

        elif 'open gmail' in query.lower():
            speak("Okay sir, opening G Mail.com")
            webbrowser.open("www.gmail.com")
   
        elif 'open amazon.in' in query.lower() or 'open amazon india' in query.lower():
            speak("Okay sir, opening Amazon dot India")
            webbrowser.open("www.amazon.in")

        elif 'open prime video' in query.lower() or 'open amazon prime video' in query.lower():
            speak("Okay sir, opening Amazon Prime Video")
            webbrowser.open("www.primevideo.com")

        elif 'open amazon.com' in query.lower() or 'open amazon international' in query.lower():
            speak("Okay sir, opening Amazon dot com")
            webbrowser.open("wwww.amazon.com")

        elif 'open apple.com' in query.lower() or 'open apple' in query.lower():
            speak("Okay sir, opening Apple dot com")
            webbrowser.open("www.apple.com")        

        elif 'open outlook' in query.lower() or 'open outlook website' in query.lower():
            speak("Okay sir, opening Microsoft Outlook")
            webbrowser.open("outlook.live.com")

        elif 'open github' in query.lower() or 'open github website' in query.lower():
            speak("Okay sir, opening GitHub dot organisation")
            webbrowser.open("www.github.com")

        elif 'open facebook' in query.lower() or 'open facebook website' in query.lower():
            speak("Okay sir, opening FaceBook dot Incorporation")
            webbrowser.open("www.facebook.com")

        elif 'open reddit' in query.lower() or 'open reddit mail' in query.lower():
            speak("Okay sir, opening Reddit Mail")
            webbrowser.open("www.reddit.com")

        elif 'where do I search for flight tickets' in query.lower() or 'tell me a flight booking website' in query.lower():
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
            webbrowser.open("maps.google.com")                                    

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

        elif 'india\'s population' in query.lower():
            speak("Sir, as of 2020,, India\'s population is 138 billion") 

        elif 'which racer holds the record for the most grand prix wins' in query.lower():
            speak("Sir,,the answer is.. Michael Schumacher")

        elif 'which jamaican runner is an 11 time world champion and holds the record in the 100 and 200 meter race' in query.lower():
            speak("Sir,,the answer is Usain Bolt")

        elif 'fastest runner in the world' in query.lower():
            speak("Sir,, the answer is Usain Bolt")

        elif 'national anthem of india' in query.lower():
            speak("Sir,,our country\'s national anthem is Jana Gana Mana ") 

        elif 'national song of india' in query.lower():
            speak("Sir,,our country\'s national song is Vande Mataram")                

        elif 'india\'s most populated city' in query.lower():   
            speak("Sir, the answer is Mumbai,, it has nearly 18.4 million inhabitants ")  

        elif 'no of state and union territories in india' in query.lower(): 
            speak("Sir,,the answer is India has 29 states and 7 union territories,,after the Jammu and Kashmir was divided into two parts...Jammu and Kashmir...and as there added into the union territories")  

        elif 'india\'s population density' in query.lower(): 
            speak("Sir,,, India\'s population density is 382 persons per kilometer square")

        elif 'national motto of india' in query.lower(): 
            speak("Sir, our country National Motto is Satyameva Jayate") 

        elif 'india\'s total area' in query.lower(): 
            speak("Sir,, India's total area is 3.3 million square kilometer")

        elif 'when michael jordan played for the chicago bulls, how many nba championships did he win' in query.lower():
            speak("Sir,,the answer is six")   
                     
        elif 'which williams sister has won more grand slam titles' in query.lower():
            speak("Sir,,the answer is Serena Williams")   

        elif 'tell jokes' in query.lower() or 'tell me some jokes' in query.lower() or 'say jokes' in query.lower() or 'make some jokes' in query.lower() or 'crack some jokes' in query.lower():
            jokeM = ['Why can\'t astronauts eat popsicles........Because in space, no one can hear the ice cream truck','What\'s the first thing a monster eats after he\'s had his teeth checked....the answer is The Dentist','Write an essay on cricket on ......the teacher told the class..,,,,,,,,,Chintu finishes his work in 5 minutes..,,,,,,,,,,,,The teacher is impressed,,,,,,,,,,..she asks Chintu to read his essay out loud for everyone...,,,,,,,Chintu reads...,,,,The cricket match is cancelled due to rain']
            speak(random.choice(jokeM))
            speak("Ha..Ha..Ha..Ha") 
            print("Ha..Ha..Ha..Ha")

        elif 'head and tails' in query.lower() or 'toss' in query.lower():
            speak("What do you choose sir,,")
            query = takeCommand()
            if 'heads' in query.lower():
                lo = ['Well played, You won sir,,','Sorry,,you lost sir,,']
                speak(random.choice(lo))
                print(random.choice(lo))
            elif 'tails' in query.lower():
                lo = ['Well played, You won sir,,','Sorry,,you lost sir,,']
                speak(random.choice(lo))
                print(random.choice(lo))
            else:
                speak("Unknown Input sir,,")    

   
        
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
            speak("Sorry,,if  I was mean to you sir,, ")    
 
        elif 'the time' in query.lower():
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'despacito' in query.lower():
            speak("Okay sir,,playing Despacito")
            playsound('C:\\Users\\Dell\\Music\\Dono.mp3')

        elif 'my photos' in query.lower():
            speak("Okay sir,,here are some of your photos")
            img = cv2.imread("C:\\Users\\Dell\\Pictures\\Camera Roll\\LOLU pandey.jpg")
            cv2.imshow("Your Photos",img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

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

        elif 'open blue j' in query.lower() or 'open blue jay' in query.lower() or'open bluejay' in query.lower():
            codePath = "C://Program Files//BlueJ//BlueJ.exe"
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
    
        elif 'today\'s news' in query.lower():
            speak("okay sir, here are the latest news from Google News")
            for news in news_list:
                print(news.title.text)
                print(news.pubDate.text)
                print("-"*60)
                speak(news.title.text)
            
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
            
            
        elif 'email to me' in query.lower():
            speak("Okay sir...")
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "shankarappabasavegowda06864@gmail.com"    
                sendEmail(to, content)
                speak("Email sent sucessfully sir!")
                      

        
            except Exception as e:
                print(e)
                speak("Sorry sir, the email could  not be sent") 



