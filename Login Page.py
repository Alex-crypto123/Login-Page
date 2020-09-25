#Made By Alessandro
while True:
    import pynput
    import os
    import time
    from pynput.keyboard import Key, Controller
    from datetime import datetime
     
    keyboard = Controller()
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    #Made By Alessandro
    username_sbagliati = ("giuseppe" "alessandro" "giovanni" "paolo" "pasquale")
    username = input("Inserisci Codice Dipendente - Nome Utente: ")
    login = open("database_login.txt","a")
    if username == "giuseppe":
        login
        login.write("\n Giuseppe ha eseguito l'accesso il " + dt_string)
        os.startfile("#program directory")
        login.close()
        time.sleep(0.12)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)
        keyboard.type('12345678')
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        #Made By Alessandro
        break
    elif username == "alessandro":
        login
        login.write("\n Alessandro ha eseguito l'accesso il " + dt_string)
        os.startfile("#program directory")
        login.close()
        time.sleep(0.12)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)
        keyboard.type('12345678')
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        break
    elif username == "giovanni":
        login
        login.write("\n Giovanni ha eseguito l'accesso il " + dt_string)
        os.startfile("#program directory")
        login.close()
        time.sleep(0.12)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)
        keyboard.type('12345678')
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        break
    elif username == "paolo":
        login
        login.write("\n Paolo ha eseguito l'accesso il " + dt_string)
        os.startfile("#program directory")
        login.close()
        time.sleep(0.12)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)
        keyboard.type('12345678')
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        break
    elif username == "pasquale":
        login
        login.write("\n Pasquale ha eseguito l'accesso il " + dt_string)
        os.startfile("#program directory")
        login.close()
        time.sleep(0.12)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(1)
        keyboard.type('12345678')
        time.sleep(1)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        break
    elif username != username_sbagliati:
        print("Codice Errato, Non Sei Autorizzato")
        login.write("\n accesso non autorizzato: " + username + " il: " + dt_string )
        #Made By Alessandro
        
