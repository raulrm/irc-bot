from irc_class import *
import config_file as cfg
import os
import random


irc = IRC()
#irc.connect(cfg.server, cfg.port, cfg.channel, cfg.botnick, cfg.botpass, cfg.botnickpass)

irc.connect("irc.freenode.net", 6667, "#raulrm", "KeimaKat", "b0nd10l4", "nose")


while True:
    text = irc.get_response()
    print(text)
 
    if "PRIVMSG" in text and "#raulrm" in text and "hola" in text:
        irc.send("#raulrm", "Hola!")