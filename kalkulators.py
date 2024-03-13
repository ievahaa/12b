def saskaiti(sk1, sk2):
    return sum((sk1,sk2))

def reiz(sk1, sk2):
    return sk1*sk2

def dali(sk1, sk2):
    return sk1/sk2

def atnem(sk1, sk2):
    return sk1-sk2

print(saskaiti(2,6))
print(atnem(2,6))
print(reiz(2,6))
print(dali(2,6))

def kalkulators(sk1, sk2, operat):
    return operat(sk1,sk2)

print(kalkulators(2,6,reiz))
print(kalkulators(45,6,dali))

# Kas ir @ - Python decorators
# nested function
# def areja_funkcija():
#     print("Es esmu ārējā funkcija")

#     def iekseja_funkcija():
#         print("Es esmu iekšējā funkcija")
#     # var izsaukt tikai caur ārējo funkciju
#     iekseja_funkcija()

# areja_funkcija()

# funkcijas var tikt izsauktas no citām funkcijām
def areja_funkcija():
    print("Es esmu ārējā funkcija")

    def iekseja_funkcija():
        print("Es esmu iekšējā funkcija")
    # var izsaukt tikai caur ārējo funkciju
    return iekseja_funkcija

ieks_fja = areja_funkcija()
ieks_fja()

#Python decorators
import time

def decorator_function(function):
    def wrapper_function():
        function()
    return wrapper_function

#izveido vienkāršu funkciju
def sveiki():
    time.sleep(2) #pieliek aizturi
    print("Sveiki!")
sveiki()

#Izveido vairākas līdzīgas funkcijas - kā uzlikt aizturi visām?
def aizkave_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()
    return wrapper_function

@aizkave_decorator
def labdien():
    print("Labdien!")

@aizkave_decorator
def labrit():
    print("Labrīt!")

def labvakar():
    print("Labvakar!")

labdien()
labrit()