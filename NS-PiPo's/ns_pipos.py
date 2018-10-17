from tkinter import scrolledtext
from tkinter import INSERT
import xmltodict
import requests
import tkinter as tk
from tkinter import *
root = Tk()
root.config(bg='#ffc917')
root.wm_state('zoomed')
root.title("NS Actuele vertrektijden")

def ditStation():
    auth_details = ('Pieter.pa.visser@student.hu.nl', 'JjvTmFbc1sjWDCB1Bkfs_m0Y54mVuZdbbSqDIKY0hg_gBt18beTUKA')
    station = 'Utrecht'                                                            # Declare inputfield as station.
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + station             # Fetch avt.
    response = requests.get(api_url, auth=auth_details)                            # Auth for the fetch
    scrolledtext.configure(state="normal")
    scrolledtext.delete('1.0', END)
    with open('vertrektijden.xml', 'w') as myXMLFile:                              # Open avt.xml
        output = 'Dit zijn de vertrekkende treinen uit ' + station + ":\n"         # Building output.
        output += "\n"
        scrolledtext.insert(tk.INSERT, output)                                     # Insert output in Scrolledtext frame.
        myXMLFile.write(response.text)
        vertrekXML = xmltodict.parse(response.text)
        for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:    # Loop through vertrekXML
            eindbestemming = vertrek['EindBestemming']                             # Fetch end station.
            vertrektijd = vertrek['VertrekTijd']                                   # Fetch time example:2016-09-27T18:36:00+0200
            vertrektijd = vertrektijd[11:16]                                       # Fetch hours:minutes 18:36
            TreinSoort = vertrek['TreinSoort']                                     # Train type
            VertrekSpoor = vertrek['VertrekSpoor']                                 # Start location.
            output1 = "Naar: " + eindbestemming + "\n"                             # Building output.
            output1 += "Tijd: " + vertrektijd + "\n"
            output1 += 'Trein: ' + TreinSoort + "\n"
            output1 += "Spoor: " + str(VertrekSpoor['#text']) + "\n"
            output1 += "\n"
            scrolledtext.insert(tk.INSERT, output1)                                # Insert output in Scrolledtext window.
        scrolledtext.configure(state="disable")                                    # Make Scrolledtext not editable.


def vertrektijden():
    auth_details = ('Pieter.pa.visser@student.hu.nl', 'JjvTmFbc1sjWDCB1Bkfs_m0Y54mVuZdbbSqDIKY0hg_gBt18beTUKA')
    station = stationfield.get()                                                   # Declare inputfield as station.
    if station == "":
        output = "Station kan niet leeg zijn"
        scrolledtext.configure(state="normal")
        scrolledtext.delete('1.0', END)
        scrolledtext.insert(tk.INSERT, output)
        scrolledtext.configure(state="disable")
    else:
        api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + station             # Fetch avt.
        response = requests.get(api_url, auth=auth_details)                            # Auth for the fetch
        scrolledtext.configure(state="normal")
        scrolledtext.delete('1.0', END)
        with open('vertrektijden.xml', 'w') as myXMLFile:                              # Open avt.xml
            output = 'Dit zijn de vertrekkende treinen uit ' + station + ":\n"         # Building output.
            output += "\n"
            scrolledtext.insert(tk.INSERT, output)                                     # Insert output in Scrolledtext frame.
            myXMLFile.write(response.text)
            vertrekXML = xmltodict.parse(response.text)
            for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:    # Loop through vertrekXML
                eindbestemming = vertrek['EindBestemming']                             # Fetch end station.
                vertrektijd = vertrek['VertrekTijd']                                   # Fetch time example:2016-09-27T18:36:00+0200
                vertrektijd = vertrektijd[11:16]                                       # Fetch hours:minutes 18:36
                TreinSoort = vertrek['TreinSoort']                                     # Train type
                VertrekSpoor = vertrek['VertrekSpoor']                                 # Start location.
                output1 = "Naar: " + eindbestemming + "\n"                             # Building output.
                output1 += "Tijd: " + vertrektijd + "\n"
                output1 += 'Trein: ' + TreinSoort + "\n"
                output1 += "Spoor: " + str(VertrekSpoor['#text']) + "\n"
                output1 += "\n"
                scrolledtext.insert(tk.INSERT, output1)                                # Insert output in Scrolledtext window.
            scrolledtext.configure(state="disable")                                    # Make Scrolledtext not editable.


stationframe = Frame(master=root)
stationframe.pack(fill="both", expand=True)
stationfield = Entry(master=root)
stationfield.pack(padx=40, pady=40)
stationfield.insert(0, '')
button = Button(master=root, text='Actuele verktrektijden bepaald station', command=vertrektijden)
photo = PhotoImage(file="button_vertrektijden.png")
button.config(image=photo, activebackground="black", bg="black", bd=0)
button.pack(pady=10)
button = Button(master=root, text='Dit station', command=ditStation)
photo1 = PhotoImage(file="button_huidig-station.png")
button.config(image=photo1, activebackground="black", bg="black", bd=0)
button.pack(pady=10)
outputFrame = Frame(root, width=400, height=200)
outputFrame.pack(fill=BOTH, expand=YES)
outputFrame.config(bg='#ffc917')
scrolledtext = scrolledtext.ScrolledText(root, width=400, height=200, font="Frutiger-Black", fg='#003082')
scrolledtext.pack(padx=40, pady=40, fill="both", expand=True)
scrolledtext.config(bg='#ffc917')
root.mainloop()