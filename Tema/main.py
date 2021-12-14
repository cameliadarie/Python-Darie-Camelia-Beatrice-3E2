import os
import sys
import shutil

def force(lista, deleted_files):
    for i in range(0, len(lista)):
        try:
            os.remove(lista[i])
            deleted_files.append(lista[i])
        except:
            pass


def i_mic(lista, deleted_files):
    for i in range(0, len(lista)):
        print("Doriti sa stergeti acest fisier?")
        raspuns = input()
        if raspuns == 'Y' or raspuns == 'y':
            os.remove(lista[i])
            deleted_files.append(lista[i])
        else:
            print("Acest fisier nu a fost sters")


def verbose(deleted_files):
    for i in deleted_files:
        print("S-a sters: " + i + "\n")


def help():
    f = open("help.txt", "r")
    print(f.read())


def versions():
    f = open("versions.txt", "r")
    print(f.read())

def recursive(lista):
    for i in lista:
     shutil.rmtree(i, ignore_errors=False, onerror=None)

def dir(lista):
    for i in lista:
        os.rmdir(i)


def imare(lista):
    print("Doriti sa continuati?")
    raspuns = input()
    if(raspuns=="Y" or raspuns=="y"):
        return 1
    return 0

def validare_comanda (lista_fisiere,lista_argumente):
    argumente_posibile=["-r","-R","--recursive","-i","-I","--verbose","--help","--version","-f","--force","-d","--dir"]
    for i in range (0,len(lista_argumente)):
        if lista_argumente[i] not in argumente_posibile and "-f"  not in lista_argumente :
            return 0
    if(len(lista_fisiere)==0):
        print("Nu ati dat niciun fisier")
    return 1



def citire_comanda():
    deleted_files = []
    lista_fisiere = []
    lista_argumente=[]
    rec=0
    for i in range(2, len(sys.argv[0:])):
        a=str(sys.argv[i])
        if a[0]!= '-' :
            lista_fisiere.append(sys.argv[i])
        else:
            lista_argumente.append(sys.argv[i])
        if a=="-r" or a=="--recursive" or a=="-R":
            rec = 1

    if validare_comanda(lista_fisiere,lista_argumente)==0:
        print("Argumentele date sunt invalide")

    if sys.argv[1] == 'rm':
        for i in range(1, len(sys.argv)):
            if sys.argv[i] == '-f' or sys.argv[i] == '--force':
                force(lista_fisiere, deleted_files)
            elif sys.argv[i] == '-i':
                i_mic(lista_fisiere, deleted_files)
            elif sys.argv[i] == '-I':
                if len(lista_fisiere)>3 or rec==1 :
                    if(imare(lista_fisiere)==0):
                        break

            elif sys.argv[i].find("--interactive")>0:
                print("da")
                if sys.argv[i].find("always"):
                    i_mic(lista_fisiere)
                elif sys.argv[i].find("once"):
                    imare(lista_fisiere)

            elif sys.argv[i] == '--one-file-system':
                # force(subs(len(subs)-1))
                a = 1
            elif sys.argv[i] == '--no-preserve-root':
                # force(subs(len(subs)-1))
                a = 1
            elif sys.argv[i] == '-preserve - root[ = all]':
                # force(subs(len(subs)-1))
                a = 1
            elif sys.argv[i] == '-r' or sys.argv[i] == '-R' or sys.argv[i] == '--recursive':
                recursive(lista_fisiere)


            elif sys.argv[i] == '-d' or sys.argv[i] == '--dir':
                dir(lista_fisiere)

            elif sys.argv[i] == '-v' or sys.argv[i] == '--verbose':
                verbose(deleted_files)
                a = 1
            elif sys.argv[i] == '--help':
                help()
            elif sys.argv[i] == '--versions':
                versions()


citire_comanda()
