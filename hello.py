# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

#Kas ir Framework - Flask
#faila nosaukums nedrīkst sakrist ar bibliotēkas vai framework nosaukumu
#Ieinstalē Flask ar pip
#export FLASK_APP=hello.py uz Mac
#set FLASK_APP=hello.py
#flask run
#atver IP adresi
#atver Chrome inspect, tur parādās html utt
#beigās jānostopē ar ctrl c


#ko nozīmē __name__and__main?
#izprintē, bet pārējo aizkomentē
print(__name__)
#īpašais pYthon atribūts https://docs.python.org/3/library/stdtypes.html#special-attributes
#__main__ skaidrojums: https://docs.python.org/3/library/__main__.html

if __name__=="__main__":
    app.run() #nodrošina, ka nav nepieciešams viss iepriekšējais penteris, var vienkārši nospiest run

#kas ir @?
#Python decorators
#paraugam uztaisa 4 funkcijas ar kalkulatoriem - var padot funkciju kā argumentu

#nested function - citā failā
# def areja_fja():
#     print("Es esmu ārējā funkcija")

#     def iekseja_fja():
#         print("Es esmu iekšējā funkcija")
#     #var izsaukt tikai caur ārējo
#     iekseja_fja()

# areja_fja()

#funkcijas var tikt izsauktas no citām funkcijām
# def areja_fja():
#     print("Es esmu ārējā funkcija")

#     def iekseja_fja():
#         print("Es esmu iekšējā funkcija")
#     #var izsaukt tikai caur ārējo
#     return iekseja_fja #noņem iekavas - funkcija netiek aktivizēta

# iekseja_funkcija = areja_fja()
# iekseja_funkcija()

#iekopē kodu vizualizācijā https://pythontutor.com/render.html#mode=display


#Python decorators
import time
# def decorator_function(function):
#     def wrapper_function():
#         function()
#     return wrapper_function
#decorator_function ir funkcija, kas ietin citu funkciju, lai piešķirtu tai funkcionalitāti

#izveido vienkāršu funkciju
# def say_hello():
#     time.sleep(2) #pieliek aizturi
#     print("Hello")
# say_hello()

#izveido vairākas funkcijas - bye, greeting u.c. Kā visām uzlikt time?

#decorator_function var uzlikt aizkavi
def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        #dara kaut ko pirms funkcijas
        function()
        function()
        #dara kaut ko pēc funkcijas
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")

say_greeting() #darbojas uzreiz, jo nav decorator priekšā
say_hello() #darbojas ar aizkavi

#šī sintakse ir izmantota Flask

#var veidot arī šādi
decorated_function = delay_decorator(say_greeting)
decorated_function()

#atgriežas pie Flask, var labāk saprast
#papildina ar
@app.route("/bye")
def say_bye():
    print("Bye")

# palaiž programmu caur IP saiti, adresei galā pieraksta /bye un enter
