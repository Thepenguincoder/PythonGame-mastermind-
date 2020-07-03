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
  
  if len(feedback) == 0:
    return "Helaas, geen van de geraden getallen komen voor in de geheime code."
  else:
    return "".join(feedback)

#Vraagt de speler of ze opnieuw willen spelen
def speelOpnieuw():
  while True:
    opnieuw = input("Wil je nog een ronde spelen? (ja of nee)\n").lower()  
    if opnieuw == "nee":
      return False
    elif opnieuw != "ja":
      print("Zeg ja of nee alstublieft")
    else:
      return True


#aantal variabelen vaststellen
aantal_kleuren = 4
aantal_beurten = 10
kleuren = ["r", "b", "g", "c", "p", "m"]

print('''WELCOME TO MASTERMIND!
In dit spel kiest de computer een code van %s letters, elke letter representeerd een kleur
R = rood   B = blauw   G = groen   C = citroengeel   P = paars   M = magenta
De computer mag dezelfde kleur vaker kiezen, ofwel een combinatie van 4 dezelfde letters is mogelijk

Jouw doel als speler is om de code te raden, dit doe je door middel van een code van letters te gokken.
Je krijgt feedback over hoeverre de geraden code overeenkomt met de werkelijke code
Elke Z betekend de juiste kleur op de juiste plek
Elde W betekend een juiste kleur maar op de verkeerde plek
Deze feedback is niet op volgorde

Voorbeeld: ZZW betekend twee kleuren op de juiste plek en een kleur die in de code voorkomt maar niet op de juiste plek zit.\n''' % (aantal_kleuren))
