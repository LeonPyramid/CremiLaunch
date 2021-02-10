#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:14:55 2020

@author: leon
"""

import cremilauncher as cl
import time
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.core.window import Window
Window.clearcolor = (0.5, 0, 0, 1)
popup_size = (0.8,0.3)
text_size = 50
button_text_color = [0,0,0,1]
button_background_color = [255/100,215/100,0,1]

class MainApp(App):
    def build(self):
        layout = GridLayout(cols=4,spacing=5,padding=5)
        for elt in cl.ROOMLIST:
            but = Button(text="Salle %s" % elt,
                         color=button_text_color,font_size=text_size,
                         background_color=button_background_color,font_name="Ubuntu-Title.ttf")
            but.bind(on_press=self.on_event)
            layout.add_widget(but)
        small = BoxLayout(orientation="vertical",spacing=5)
        pop = Button(text = "Changer \n l'identifiant",
                     color=button_text_color,font_size=text_size,
                     background_color=button_background_color,font_name="Ubuntu-Title.ttf")
        pop.bind(on_press=passPop.popup.open)
        small.add_widget(pop)
        mac = Button(text = "Lancer \n une machine",
                     color=button_text_color,font_size=text_size,
                     background_color=button_background_color,font_name="Ubuntu-Title.ttf")
        mac.bind(on_press=machPop.popup.open)
        small.add_widget(mac)
        layout.add_widget(small)
        return layout
    def close_passPopup(self):
        if cl.infoExist():
            passPop.popup.dismiss()
    def submit_passPopup(self):
        idt=passPop.ident.text
        pswrd=passPop.passwrd.text
        if cl.infoTest(idt, pswrd):
            cl.saveInfo(idt, pswrd)
            cl.installHandler(cl.TOPURL, idt, pswrd)
            passPop.popup.dismiss()
        else:
            popup = ErrorLayout.createPopup(3)
            popup.open()
    def on_event(self, obj):
        room = obj.text[-3:]
        popup = RoomPopup("la salle "+room)
        Clock.schedule_once(popup.open)
        Clock.schedule_once((lambda x : (cl.launchRoom(room))),0.5)
        Clock.schedule_once(popup.dismiss,0.7)
    
    def machineLaunch(self):
        found = cl.listi.findMachine(machPop.machname.text)
        if found == None:
            popup = ErrorLayout.createPopup(1)
            popup.open()
        else:
            popup = RoomPopup(machPop.machname.text)
            Clock.schedule_once(popup.open)
            Clock.schedule_once((lambda x :cl.launchMachine(machPop.machname.text)),0.5)
            Clock.schedule_once(popup.dismiss,0.7)
            machPop.popup.dismiss()
    
    def first_password(self):
        if not cl.infoExist():
            passPop.popup.open()
        else:
            print("autoconnect")
            idt,psd = cl.loadInfo()
            cl.installHandler(cl.TOPURL, idt.decode(), psd.decode())
    Clock.schedule_once(first_password,.5)

class MachinePop():
    layout = BoxLayout(orientation="vertical",spacing=50,padding=10)
    machname=TextInput(hint_text="Nom de la Machine",multiline=False)
    submit = Button(text="Subbmit")
    submit.bind(on_press=MainApp.machineLaunch)
    layout.add_widget(machname)
    layout.add_widget(submit)
    popup = Popup(title='Lancer une machine',
                    content=layout,
                    size_hint=popup_size)
    

machPop = MachinePop()

#Popup d'erreur
class ErrorLayout():
    def createPopup(errcode):
        codeswitch={
        1:"Cette machine n'existe pas",
        2:"La Connexion a échoué",
        3:"Mauvais identifiant"
        }
        text = codeswitch[errcode]
        layout = BoxLayout(orientation="vertical",spacing=10)
        txt = Label(text=("Erreur: "+text),font_size=text_size)
        close = Button(text="close")
        layout.add_widget(txt)
        layout.add_widget(close)
        pop = Popup(title="Erreur",content=layout,size_hint=popup_size,auto_dismiss=False)
        close.bind(on_press=pop.dismiss)
        return pop

def RoomPopup(roomnum):
    layout = BoxLayout(orientation="vertical",spacing=10)
    textl = "Lancement de "+roomnum
    txt = Label(text=textl,font_size=text_size)
    layout.add_widget(txt)
    pop = Popup(title="Lancement",content=layout,size_hint=popup_size,auto_dismiss=False)
    return pop

class PasswordPop():
    ident = TextInput(hint_text="identifiant",multiline=False)
    passwrd = TextInput(hint_text="mot de passe",
                        multiline=False,password=True)
    ident.next_focus = passwrd
    def on_enter_ident_focus(self):
        self.next_focus.focus = True
    ident.bind(on_text_validate = on_enter_ident_focus)
    passwrd.bind(on_text_validate=MainApp.submit_passPopup)
    layout = BoxLayout(orientation="vertical",spacing=5)
    layout.add_widget(ident)
    layout.add_widget(passwrd)
    buttonsL = BoxLayout(orientation="horizontal",spacing=10)
    exitB = Button(text="Close")
    exitB.bind(on_press=MainApp.close_passPopup)
    buttonsL.add_widget(exitB)
    submitB = Button(text="Subbmit")    
    submitB.bind(on_press=MainApp.submit_passPopup)
    buttonsL.add_widget(submitB)
    layout.add_widget(buttonsL)
    popup = Popup(title='Définir les identiifiants',
                    content=layout,
                    size_hint=popup_size,auto_dismiss=False)

passPop = PasswordPop()

if __name__ == '__main__':
    app = MainApp()
    app.run()

