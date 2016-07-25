import os
import aiml
import duckduckgo
import re

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


client="Nikhil"    
bot.respond("My name is "+client)

while True:
    query=raw_input("Enter your message >> ")
    query=query.lower()
    
    if("when is" in query):
        answer=web_search(query)
    else:
        answer=bot.respond(query)
        if("xyzsearch" in answer):
          query=answer.split("xyzsearch")[1]
          answer=web_search(query)    
    print answer
        


