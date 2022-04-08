import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random
import getpass

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good Morning Sir")
    elif hour >=12 and hour <= 18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am Jarvis. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        if query != '':
            print(f"User said: {query}")
        else:
            speak("Couldn't hear properly")
    except Exception as e:
        # print(e)    
        speak("Say that again please...")  
        return "None"

    return query

def sendEmail(to_email,subject,message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    from_email = getpass.getpass("Enter your email: ")
    # https://support.google.com/accounts/answer/185833?hl=en/
    password = getpass.getpass("Enter your password: ")
    server.login(from_email,password)
    msg = "Subject: " + subject + '\n' + message
    server.sendmail(from_email, to_email, msg)
    server.close()

if __name__ == "__main__":
    # speak("Pratham is a good boy")
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            results = wikipedia.summary(query, sentences = 1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open gc' in query:
            webbrowser.open("https://classroom.google.com")
        
        elif 'open whatsapp':
            webbrowser.open("https://web.whatsapp.com")

        elif 'open gmail' in query:
            webbrowser.open("https://mail.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")
        
        elif 'open code' in query:
            codePath = r"C:\Users\sprat\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'play music' in query:
            music_dir = r"C:\Users\sprat\Music\FAV"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,*random.sample(population=songs,k=1)))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email to raj' in query:
            try:
                speak("What should be the subject?")
                subject = takeCommand()
                while subject =='':
                    speak("Please repeat the subject")
                    subject = takeCommand()
                speak("What should be the message you want to send?")
                message = takeCommand()
                while message =='':
                    speak("Please repeat the message")
                    message = takeCommand()
                to_email = "rajdeep55209@gmail.com"
                sendEmail(to_email,subject,message)
                speak("Email has been sent")
            except Exception as e:
                print(e)    
                print("Sorry my friend. I am not able to send this email.")           

        elif 'quit' in query:
            speak("I am closing")
            exit()
            
        else:
            speak("Sorry I am unable to hear. Please repeat")