import os
import sys


def force(lista):
    for i in range(0, len(lista)):
        try:
            os.remove(lista[i])
        except:
            pass

def i_mic(lista):
    for i in range(0, len(lista)):
        print("Doriti sa stergeti acest fisier?")
        raspuns=input()
        if raspuns=='Y' or raspuns=='y':
            os.remove(lista[i])
        else:
            print("Acest fisier nu a fost sters")

def recursive (lista):
    for i in os.walk(lista):
         print(i)


def help():
    f = open("help.txt", "r")
    print(f.read())


def versions():
    f = open("versions.txt", "r")
    print(f.read())


def citire_comanda():
    comanda = input()
    deleted_files = []
    lista_fisiere = []
    subs = comanda.split()
    for i in range(1, len(subs)):
        if subs[i][0] != '-':
            lista_fisiere.append(subs[i])
    # print(comanda)
    if subs[0] == 'rm':
        for i in range(1, len(subs)):
            if subs[i] == '-f' or subs[i] == '--force':
                force(lista_fisiere)
            elif subs[i] == '-i':
                i_mic(lista_fisiere)
            elif subs[i] == '-I':
                # force(subs(len(subs)-1))
                a = 1
            elif subs[i] == '-interactive[always]':
                i_mic(lista_fisiere)

            elif subs[i] == '--one-file-system':
                # force(subs(len(subs)-1))
                a = 1
            elif subs[i] == '--no-preserve-root':
                # force(subs(len(subs)-1))
                a = 1
            elif subs[i] == '-preserve - root[ = all]':
                # force(subs(len(subs)-1))
                a = 1
            elif subs[i] == '-r' or subs[i] == '-R' or subs[i] == '-recursive':
                 recursive(lista_fisiere)
            elif subs[i] == '-d' or subs[i] == '--dir':
                # force(subs(len(subs)-1))
                a = 1
            elif subs[i] == '-v' or subs[i] == '--verbose':
                # force(subs(len(subs)-1))
                a = 1
            elif subs[i] == '--help':
                help()
            elif subs[i] == '--versions':
                versions()


citire_comanda()
