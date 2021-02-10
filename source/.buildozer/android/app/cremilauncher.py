#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 02:38:14 2020

@author: leon
"""

#Code elements, launching a room in cremi
import urllib.request
import listId as listi
from listId import ROOMLIST
import ssl
from os import path
from cryptography.fernet import Fernet

TOPURL = "https://services.emi.u-bordeaux.fr"
PSWRDPATH = "info.cfg"
KEY = b'VOPMBynMz_wUJOtKM_BPfYKT325_bzFKckeRxcZcJ6M='
#bypass SSL
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

#Connection mamagement
def installHandler(topUrl,ident,password):
    #Install id and password
    password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None,topUrl ,ident, password)
    handler = urllib.request.HTTPBasicAuthHandler(password_mgr)
    opener = urllib.request.build_opener(handler)
    urllib.request.install_opener(opener)

def launchRoom(room):
    for elt in listi.getRoom(room):
        print(elt)
        url = "https://services.emi.u-bordeaux.fr/exam/js/getWake.php?h="+elt+"&std"
        urllib.request.urlopen(url)

def launchMachine(machinename):
    mid = listi.findMachine(machinename)
    if mid == None:
        return False
    else:
        url = "https://services.emi.u-bordeaux.fr/exam/js/getWake.php?h="+mid+"&std"
        urllib.request.urlopen(url)
        return True



#Password management
def infoExist():
    return path.exists(PSWRDPATH)

def saveInfo(ident,password):
    text = (ident + " " + password).encode()
    inf = open(PSWRDPATH,'wb')
    inf.write(Fernet(KEY).encrypt(text))
    inf.close()

def loadInfo():
    try:
        inf = open(PSWRDPATH,'rb')
    except FileNotFoundError:
        print("Erreur: Le mot de passe n'a pas encore été défini")
        return None
    text = Fernet(KEY).decrypt(inf.read())
    inf.close()
    return text.split()

def infoTest(ident,password):
    installHandler(TOPURL, ident, password)
    try:
        urllib.request.urlopen(TOPURL+"/exam/")
    except urllib.error.HTTPError:
        print("Connexion échouée")
        return False
    return True