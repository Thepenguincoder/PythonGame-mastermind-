import os
import random

#Genereerd een geheime code
def maakGeheimeCode(kleuren):
  geheimeCode = ""
  for i in range (0,4):
    plek = random.randint(0,5)
    geheimeCode += kleuren[plek]
  
  return geheimeCode

#geeft feedback
def geefFeedback(gok, geheimeCode):
  if gok == geheimeCode:
    return "Je hebt de geheime code geraden!"

#aantal variabelen vaststellen
kleuren = ["r", "b", "g", "c", "p", "m"]