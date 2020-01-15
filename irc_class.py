import socket
import time
import sys

class IRC:
    irc = socket.socket()

    def __init__(self):
        self irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, channel, msg):
        self.irc.send(bytes("PRIVMSG " + channel + " " + msg + "\n", "UTF-8"))

    def connect(self, server, port, channel,  botnick, botpass, botnickpass):
        print("Conectando a  " + server)
        self.irc.connect((server, port))

        self.irc.send(bytes("USER " + botnick + " " + botnick +" " + botnick + " :python\n", "UTF-8"))
        self.irc.send(bytes("NICK " + botnick + "\n", "UTF-8"))
        self.irc.send(bytes("NICKSERV IDENTIFY " + botnickpass + " " + botpass + "\n", "UTF-8"))
        time.sleep(5)

        self.irc.send(bytes("JOIN " + channel + "\n", "UTF-8"))

    def get_response(self):
        time.sleep(1)

        resp = self.irc.recv(2040).decode("UTF-8")

        if resp.find('PING') != -1: 
            self.irc.send(bytes('PONG ' + resp.split().decode("UTF-8") [1] + '\r\n', "UTF-8"))

        return resp

