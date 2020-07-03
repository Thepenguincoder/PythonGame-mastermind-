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


#Regel tekst
print('''WELCOME TO MASTERMIND!
In dit spel kiest de computer een code van %s letters, elke letter representeerd een kleur
R = rood   B = blauw   G = groen   C = citroengeel   P = paars   M = magenta
De computer mag dezelfde kleur vaker kiezen

Jouw doel als speler is om de code te raden, dit doe je door een code bestaande uit letters te raden
Je krijgt feedback over hoeverre de geraden code overeenkomt met de werkelijke code
Elke Z betekend de juiste kleur op de juiste plek
Elde W betekend een juiste kleur maar op de verkeerde plek
Deze feedback is niet op volgorde

Voorbeeld: ZZW betekend twee kleuren op de juiste plek en een kleur die in de code voorkomt maar niet op de juiste plek zit.\n''' % (aantal_kleuren))

#de loop van het spel zelf
while True:
  beurt = 1
  geheimeCode = maakGeheimeCode(kleuren)
  print("je hebt " + str(aantal_beurten) + " beurten")
  while beurt <= aantal_beurten:
    gokOpnieuw = False
    print("beurt " + str(beurt))
    gok = input().lower()
    for i in gok:
      if i.isdigit():
        gokOpnieuw = True
      elif i not in kleuren:
        gokOpnieuw = True

    if gokOpnieuw == True:
      print("Gebruik van getallen of ongeldige kleur, kies opnieuw graag")
      continue
    if len(gok) != aantal_kleuren:
      beurt += 1
      print("De gekoze code was te lang of kort, kies opnieuw graag")
      continue

    print(geefFeedback(gok, geheimeCode))
    beurt += 1

    if gok == geheimeCode:
      #Felicitatie bericht zit in de functie geef feedback
      break

  if beurt > aantal_beurten:
    print("Je hebt verloren")
    print("de geheime code was: %s" % (geheimeCode))
  
  if speelOpnieuw() == False:
    break
  else:
    os.system('cls' if os.name == 'nt' else 'clear')
