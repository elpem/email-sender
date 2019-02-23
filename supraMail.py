"""This code provides automatic email sending from txt files."""
# coding:utf-8

import smtplib
import time
import threading

def read_contact():
    """read file "addresses.txt" and fill a contact_tab with the addresses
    and the personalization variables for each contact.
    In the file : one address per line
    Still work if empty line."""

    file = open("addresses.txt", "r")
    line_tab = []
    line = "8==>"  # doesn't matter while it isn't empty string

    while line != "":
        line = file.readline()
        processed = line.split('\n')
        if processed[0] != '':
            line_tab.append(processed[0])

    file.close()

    # each line is a contact. The first column is the e-mail address
    # and the other columns are personalization variables.
    contact_tab = [[] for i in line_tab]
    for j, line in enumerate(line_tab):
        contact_tab[j] = line.split("\t")

    return contact_tab


def read_body():
    """returns the subject and the body of the mail from reading it in "body.txt"
    The body file must be written in html
    It can be personalized with items %s
    The first line of the body must me the subject (subject : <your_subject>)"""

    file = open("body.txt", "r")
    subject = process_line(file.readline())

    body = file.read()

    file.close()

    return subject, body


def read_config():
    """returns the config from file "config.txt" """
    file = open("config.txt", "r")
    param = []

    for i in range(3):
        line = file.readline()
        param.append(process_line(line))

    #print("read_config : ",param)
    return param


def process_line(line):
    """keeps the useful part (param) of typical lines in file. "title : param" """
    processed = line.split(':')[1]
    # removing possible first space
    if processed[0] == " ":
        processed = processed[1:]

    processed = processed.split('\n')[0]

    return processed


def make_msg(contact):
    """Returns the ready-to-send message."""

    # normal message creation
    msg = """Content-Type: text/html; charset=utf-8,
Content-Disposition: inline,
Content-Transfer-Encoding: 8bit
From: {0}
Date: {1}
To: {2}
Subject: {3}

{4}

""".format(my_address, date, contact[0], subject, body)

    # message personalization
    try:
        msg = msg % personalization(contact)
    except TypeError:
        print("""Erreur. Il y a sans doute un problème au niveau de tes variables de personnalisation.
-Soit il n'y a pas le même nombre de %s dans le body que de variables par contact
-Soit le séparateur dans le fichier "addresses.txt" n'est pas une tabulation.
-Soit il manque une/des variable(s) de personnalisation pour au moins un contact

Le contact concerné est : {}

""".format(contact[0])
              )
        if input("Envoyer tous les mails malgré l'erreur ? O/n    ") == 'n':
            quit()

    return msg


def personalization(contact):
    """returns personalization variables in a tuple"""
    pers = []

    if len(contact) > 1:
        for i in contact[1:]:
            pers.append(i)
        return tuple(pers)

    else:
        return ()


def get_tiny_address(ad):
    """returns @mail from "name <@mail>" """
    return ad.split("<")[1].split(">")[0]


def send(msg, target_address):
    """sends the message.
     msg:  the formatted message
     target_address: the target address."""
    s.sendmail(my_address, target_address, msg.encode('utf-8'))


def test():
    for contact in tab:
        make_msg(contact)


def login(s):
    try:
        s.login(get_tiny_address(my_address), pw)  # id, password
    except smtplib.SMTPAuthenticationError:
        input("""Erreur à l'identification au serveur SMTP:
-Vérifier identifiant et mot de passe
-Si vous utilisez Gmail, assurez vous d'avoir ouvert l'utilisation de gmail 
 à des application moins sécurisées : https://support.google.com/mail/?p=WantAuthError
 
 [appuyez sur entrée pour quitter]""")
        quit()
    print("logged in")


if __name__ == "__main__":
    # initialization
    print("init...")
    tab = read_contact()
    date = time.ctime(time.time())
    subject, body = read_body()
    param = read_config()
    my_address = param[0]
    smtp_serv = param[1]
    port = int(param[2])
    pw = input("Entre le Mot de Passe :    ")

    # open smtp connection
    s = smtplib.SMTP(smtp_serv, port)
    s.starttls()
    login(s)
    s.set_debuglevel(1)

    print("Testing message fabric before sending")
    test()

    # sending command
    print("Start Sending...")
    for contact in tab:
        print("Sending to ", contact)
        send(make_msg(contact), contact[0])

    s.quit()

    print("Ended well !")
