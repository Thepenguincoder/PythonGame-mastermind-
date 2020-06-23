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

    #Maakt een copie van de geheime code (in list vorm), zodat correcte feedback gegeven kan worden.
  copieGok = []
  for i in range(len(geheimeCode)):
    copieGok.append(geheimeCode[i])

  feedback = []
  #Eerste check: zitten de geraden kleuren op de juiste plek?
  #Verandering naar "x" voorkomt duplicaties bij de tweede check (zie hieronder)
  for i in range(aantal_kleuren):
    if gok[i] == copieGok[i]:
      feedback.append("Z")
      copieGok[i] = "X"
  
  #Tweede check: zitten de geraden kleuren in de code?
  #Verandering naar "X voorkomt duplicaties"
  for gokLetter in range(aantal_kleuren):
    for codeLetter in range(len(copieGok)):
      if gok[gokLetter] == copieGok[codeLetter]:
        feedback.append("W")
        copieGok[codeLetter] = "X"


#aantal variabelen vaststellen
aantal_kleuren = 4
kleuren = ["r", "b", "g", "c", "p", "m"]