
# coding: utf-8

# In[1]:


#Spiel Hangman

#Import Modul random (für die Erzeugung eines zufälligen Wortes aus der Wortliste)
import random

#Auswahl Wortliste -Ausbau Worteliste importieren
word_list = ['Berlin', 'Paris', 'Mailand', 'New York', 'London', 'Rom', 'Verona', 'Venedig', 'Boston']
#Gelöste Wörter
word_solved = []
#Anzahl Versuche
trys = 15

#Erstellung eines Tupels, für jedes Zeichen wird eine 0 dargestellt und eine 1, wenn es sich um ein Leerzeichen handelt 
def word_zero(word):
    tmp = ""
    for i in range(len(word)):
        if word[i]==" ":
            tmp +="1"
        else:
            tmp +="0"
    return (word,tmp)

# Funktion Anzeige des aktuellen Spielstandes (der Runde)    
def show(word_tpl):
    word_tmp = word_tpl[0]
    show_tmp = word_tpl[1]
    tmp = ""
    """Spielstandsanzeige, wenn ein eingegebenes Zeichen gefunden wurde, wird statt der eins das Zeichen ausgeben und 
    wenn das Zeichen noch nicht gefunden wurde wird statt einer 0 ein Unterstrich (_) dargestellt, 
    gefolgt von einemen Leerzeichen für die bessere Lesbarkeit; Die Ausgabe erfolgt in Großbuchstaben"""
    for i in range(len(word_tmp)):
        if show_tmp[i]=="1":
            tmp += word_tmp[i] + " "
        else:
            tmp += "_ "
    print(tmp.upper())

# Funktion Überprüfung, ob der eingegeben Buchstabe im Wort vorkommt (Umwandlung der Eingabe in Großbuchstaben)        
def check_word_tpl(word_tpl,letter):
    word_tmp = word_tpl[0]
    show_tmp = word_tpl[1]
    tmp = ""
    for i in range(len(word_tmp)):
        if word_tmp[i].upper()==letter.upper():
            tmp +="1"
        else:
            tmp += show_tmp[i]
    return (word_tmp,tmp)

#Funktion Überprüfung, ob das Wort schon gelöst wurde oder noch nicht und entsprechende Statusrückgabe
def check_solved(word_tpl):
    show_tmp = word_tpl[1]
    solved = True
    for i in range(len(show_tmp)):
        if show_tmp[i] == "0":
            solved = False
    return (solved)
    

 #Funktion Runde   
def round():
    #aktuelle Anzahl Versuche
    trys_current = trys
    #Zufallswort aus aktueller Wortliste wählen
    word_current = random.choice(word_list)
    
    #Wort in ein Tupel mit Wort, 0 Anz. Buchstaben wandeln
    word_current_tpl = word_zero(word_current)
    
    #Zeige den aktuellen Wortspielstand
    show(word_current_tpl)
    
    #while Schleife - solange Versuche (trys_current) größer 0 ist, Eingabeaufforderung
    while (trys_current > 0):
        #Eingabeaufforderung für den Buchstaben
        trys_input = input("Please enter a letter! Try left: " + str(trys_current) + "\n")
        #Zufallswort an Funktion übergeben => Nutzerabfrage und Wortbehandlung einer Runde
        word_current_tpl = check_word_tpl(word_current_tpl,trys_input)
        trys_current -=1
        show(word_current_tpl)
        if check_solved(word_current_tpl):
            print("Found soultion in " + str(trys-trys_current) + " steps.")
            #gesuchte Wort aus der Wortliste entfernen
            word_list.remove(word_current)
            #Wort in Lösungsliste aufnehmen
            word_solved.append(word_current)
            break
        
    print ("Solution: " + word_current_tpl[0] + "\n")
    print ("*********ROUND*FINISHED*********")

#Funktion Spielstart
def start_game():
    #solange der Spieler weiterspielen möchte, soll die nächste Runde gestartet werden
    game_entry = "y"
    while (game_entry=="y"):
        #falls die Wortliste komplett gefunden wurde, bekommt der User einen Hinweis und das Spiel endet
        if not word_list:
            print("Congratulation, you solved all words.")
            break
        round()
        game_entry = input("Play another round? (y/n) ")
    
    #Ausgabe der Lösung und Anzeige "Spielende"    
    print ("You found the following soulutions: " + str(word_solved) + "\n")
    print ("*********GAME*OVER*********")
        
#User Begruessung und Eingabe Aufforderung - Spielregeln lesen (y/s)
print ("Welcome to Hangman")

read_rule=input("Do you want to read the rules (press: y) or start directly (press: s)? ")

#If-Schleife: Auswertung User Eingabe - 1. Regeln, 2. Starten, 3. Falsche Eingabe
if read_rule.lower()=="y":
    print ("Rules:")
    print ("Geben Sie Buchstaben ein, um das Wort zu erraten.")
    print ("Bei jedem richtigen Buchstaben, wird dieser an die entsprechenden Stellen eingesetzt.")
    print ("Bei jedem falschen Buchstaben, gibt es ein Minuspunkt (ein Versuch weniger).")
    print ("Sie haben maximal 15 Versuche, um das Wort zu erraten.")
    print ("Es werden keine Umlaute oder Sonderzeichen verwendet, nur die Buchstaben A-Z.")
    print ("Hinweis: Derzeit werden nur Städte in deutscher Schreibweise gesucht.")
    print (" ")
    print ("The game is starting...")
    start_game()
elif read_rule.lower()=="s":
    print ("The game is starting...")
    start_game()
else: 
    print("Please enter only the letter y (read the rules) or s (start the game)!")

