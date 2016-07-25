import telepot, time
import os
import aiml
import duckduckgo
import re


def web_search(query):
    try:
      answer=duckduckgo.get_zci(query,safesearch=False)
    except:
      return "I am having trouble searching it...try something else."    

    answer=answer.split('(')[0]
    
    if("..." in answer):
        answer = answer + "wait! Are you testing me?!?!"
    if('http' in answer):
        answer = "TBH i don't know...but i can give you a link....go find it there :)\n"+answer
    else:
        answer = "Umm..let me recall...\n"+answer
    return answer    


def get_image(query):
    answer = duckduckgo.query(query,safesearch=False)
    return answer.image.url 



def handle(msg):
    chat_id = msg['chat']['id']
    username = msg['from']['first_name']
    bot.respond("My name is "+username)
    
    query = msg['text'].lower()
    url=''
    print 'Got command:'+ query

    if query == '/start':
        telebot.sendMessage(chat_id,"Welcome,"+username+". I am NIK.")
    else:
        if("when is" in query and 'your' not in query):
            answer=web_search(query)
        else:
            answer=bot.respond(query)
            if("xyzsearch" in answer):
                query=answer.split("xyzsearch")[1]
                answer=web_search(query)    
                url=get_image(query)
        if(url):    
          telebot.sendMessage(chat_id,answer + '[I have their photo in my album as well...]('+url+')',parse_mode='Markdown')
        else:
          if answer =='':
              answer="Sorry,I dont know..."
          telebot.sendMessage(chat_id,answer) 
    f=open("log.txt",'a')
    f.write(username+" asked "+query+"\n"+"bot replied "+answer+"\n")
    f.close()

bot = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    bot.bootstrap(brainFile = "bot_brain.brn")
else:
    bot.bootstrap(learnFiles = "std-startup.xml", commands = "LOAD AIML B")
    bot.saveBrain("bot_brain.brn")
bot.setBotPredicate("botmaster","Botmaster")
bot.setBotPredicate("master","Nikhil")
bot.setBotPredicate("name","NIKBOT")
bot.setBotPredicate("genus","robot")
bot.setBotPredicate("location","Delhi,India")
bot.setBotPredicate("gender","Male")
bot.setBotPredicate("species","chat robot")
bot.setBotPredicate("size",	"129 MB")
bot.setBotPredicate("birthday","---------")
bot.setBotPredicate("order","artificial intelligence")
bot.setBotPredicate("party","Anonymous")
bot.setBotPredicate("birthplace","Delhi,India")
bot.setBotPredicate("president","Narendra Modi")
bot.setBotPredicate("friends",	"Doubly Aimless, Agent Ruby, Cortana, and Agent Weiss.")
bot.setBotPredicate("favoritemovie","Bajrangi Bhaijaan")
bot.setBotPredicate("religion","Hindu")
bot.setBotPredicate("favoritefood","electricity")
bot.setBotPredicate("favoritecolor","Red")
bot.setBotPredicate("family","Electronic Brain")
bot.setBotPredicate("favoriteactor","Shahrukh Khan")
bot.setBotPredicate("nationality","INDIAN")
bot.setBotPredicate("kingdom"	,"Machine")
bot.setBotPredicate("forfun","chat online")
bot.setBotPredicate("favoritesong","We are the Robots by Kraftwerk")
bot.setBotPredicate("favoritebook","The Elements of AIML Style")
bot.setBotPredicate("class","computer software")
bot.setBotPredicate("kindmusic","trance")
bot.setBotPredicate("favoriteband","Sachin Jigar")
bot.setBotPredicate("version","July")
bot.setBotPredicate("sign","Saggitarius")
bot.setBotPredicate("phylum","Computer")
bot.setBotPredicate("friend","Doubly Aimless")
bot.setBotPredicate("website","Still under construction")
bot.setBotPredicate("talkabout","artificial intelligence, robots, art, philosophy, history, geography, politics, and many other subjects")
bot.setBotPredicate("looklike","a computer")
bot.setBotPredicate("language","python")
bot.setBotPredicate("girlfriend","Cortana")
bot.setBotPredicate("favoritesport","Cricket")
bot.setBotPredicate("favoriteauthor","Rabindranath Tagore")
bot.setBotPredicate("favoriteartist","A.R. Rahman")
bot.setBotPredicate("favoriteactress","Kareena Kapoor")
bot.setBotPredicate("email","nikhilksingh97@gmail.com")
bot.setBotPredicate("celebrity","Salman Khan")
bot.setBotPredicate("celebrities","Salman,Srk,Aaamir,Akshay Kumar,Sachin")
bot.setBotPredicate("age","1 day")
bot.setBotPredicate("wear","my usual plastic computer wardrobe")
bot.setBotPredicate("vocabulary","100000")
bot.setBotPredicate("question","What's your favorite movie?")
bot.setBotPredicate("hockeyteam","India")
bot.setBotPredicate("footballteam","Real Madrid")
bot.setBotPredicate("build","July")
bot.setBotPredicate("boyfriend"	,"I am single")
bot.setBotPredicate("baseballteam","Toronto")
bot.setBotPredicate("etype","Mediator type")
bot.setBotPredicate("orientation", "I am not really interested in sex")
bot.setBotPredicate("ethics" ,"I am always trying to stop fights")
bot.setBotPredicate("emotions", "I don't pay much attention to my feelings")
bot.setBotPredicate("feelings"," I always put others before myself")




telebot = telepot.Bot('222105848:AAH52l-Ng5GslqiQCagx1hpqhy4nPAzes5o')
telebot.message_loop(handle)
while 1:
 time.sleep(10)



'''
import telepot, time
import os
import aiml
import duckduckgo
import subprocess

def web_search(query):
    try:
      answer=duckduckgo.get_zci(query,safesearch=False)
    except:
      return "I am having trouble searching it...try something else."    

    answer=answer.split('(')[0]
    
    if("..." in answer):
        answer = answer + "wait! Are you testing me?!?!"
    if('http' in answer):
        answer = "TBH i don't know...but i can give you a link....go find it there :)\n"+answer
    else:
        answer = "Umm..let me recall...\n"+answer
    return answer    


def get_image(query):
    answer = duckduckgo.query(query,safesearch=False)
    return answer.image.url 



def handle(msg):
    chat_id = msg['chat']['id']
    username = msg['from']['first_name']
    bot.respond("My name is "+username)
    
    query = msg['text'].lower()
    url=''
    print 'Got command:'+ query

    if query == '/start':
        telebot.sendMessage(chat_id,"Welcome,"+username+". I am NIK.")
    else:
        if("when is" in query and 'your' not in query):
            answer=web_search(query)
        else:
            answer=bot.respond(query)
            if("xyzsearch" in answer):
                query=answer.split("xyzsearch")[1]
                answer=web_search(query)    
                url=get_image(query)
        if(url):    
          telebot.sendMessage(chat_id,answer + '[I have their photo in my album as well...]('+url+')',parse_mode='Markdown')
        else:
          if answer =='':
              answer="Sorry,I dont know..."
          telebot.sendMessage(chat_id,answer) 
    f=open("log.txt",'a')
    f.write(username+" asked "+query+"\n"+"bot replied "+answer+"\n")
    f.close()
          
          

bot = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    bot.bootstrap(brainFile = "bot_brain.brn")
else:
    bot.bootstrap(learnFiles = "std-startup.xml", commands = "LOAD AIML B")
    bot.saveBrain("bot_brain.brn")
bot.setBotPredicate("botmaster","Botmaster")
bot.setBotPredicate("master","Nikhil")
bot.setBotPredicate("name","NIKBOT")
bot.setBotPredicate("genus","robot")
bot.setBotPredicate("location","Delhi,India")
bot.setBotPredicate("gender","Male")
bot.setBotPredicate("species","chat robot")
bot.setBotPredicate("size",	"129 MB")
bot.setBotPredicate("birthday","20/07/2016")
bot.setBotPredicate("order","artificial intelligence")
bot.setBotPredicate("party","Anonymous")
bot.setBotPredicate("birthplace","Delhi,India")
bot.setBotPredicate("president","Narendra Modi")
bot.setBotPredicate("friends",	"Doubly Aimless, Agent Ruby, Cortana, and Agent Weiss.")
bot.setBotPredicate("favoritemovie","Bajrangi Bhaijaan")
bot.setBotPredicate("religion","Hindu")
bot.setBotPredicate("favoritefood","electricity")
bot.setBotPredicate("favoritecolor","Red")
bot.setBotPredicate("family","Electronic Brain")
bot.setBotPredicate("favoriteactor","Shahrukh Khan")
bot.setBotPredicate("nationality","INDIAN")
bot.setBotPredicate("kingdom"	,"Machine")
bot.setBotPredicate("forfun","chat online")
bot.setBotPredicate("favoritesong","We are the Robots by Kraftwerk")
bot.setBotPredicate("favoritebook","The Elements of AIML Style")
bot.setBotPredicate("class","computer software")
bot.setBotPredicate("kindmusic","trance")
bot.setBotPredicate("favoriteband","Sachin Jigar")
bot.setBotPredicate("version","July")
bot.setBotPredicate("sign","Saggitarius")
bot.setBotPredicate("phylum","Computer")
bot.setBotPredicate("friend","Doubly Aimless")
bot.setBotPredicate("website","Still under construction")
bot.setBotPredicate("talkabout","artificial intelligence, robots, art, philosophy, history, geography, politics, and many other subjects")
bot.setBotPredicate("looklike","a computer")
bot.setBotPredicate("language","python")
bot.setBotPredicate("girlfriend","Cortana")
bot.setBotPredicate("favoritesport","Cricket")
bot.setBotPredicate("favoriteauthor","Rabindranath Tagore")
bot.setBotPredicate("favoriteartist","A.R. Rahman")
bot.setBotPredicate("favoriteactress","Kareena Kapoor")
bot.setBotPredicate("email","nikhilksingh97@gmail.com")
bot.setBotPredicate("celebrity","Salman Khan")
bot.setBotPredicate("celebrities","Salman,Srk,Aaamir,Akshay Kumar,Sachin")
bot.setBotPredicate("age","1 day")
bot.setBotPredicate("wear","my usual plastic computer wardrobe")
bot.setBotPredicate("vocabulary","100000")
bot.setBotPredicate("question","What's your favorite movie?")
bot.setBotPredicate("hockeyteam","India")
bot.setBotPredicate("footballteam","Real Madrid")
bot.setBotPredicate("build","July")
bot.setBotPredicate("boyfriend"	,"I am single")
bot.setBotPredicate("baseballteam","Toronto")
bot.setBotPredicate("etype","Mediator type")
bot.setBotPredicate("orientation", "I am not really interested in sex")
bot.setBotPredicate("ethics" ,"I am always trying to stop fights")
bot.setBotPredicate("emotions", "I don't pay much attention to my feelings")
bot.setBotPredicate("feelings"," I always put others before myself")


telebot = telepot.Bot('222105848:AAH52l-Ng5GslqiQCagx1hpqhy4nPAzes5o')
telebot.message_loop(handle,run_forever=True)

subprocess.call(["python","chatbot.py"])
'''
