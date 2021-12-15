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
        print("S-a sters:  " + i)


def help():
    f = open("help.txt", "r")
    print(f.read())


def versions():
    f = open("versions.txt", "r")
    print(f.read())


def recursive(lista, inter, deleted_files):
    for i in lista:
        for (root, directories, files) in os.walk(i, topdown=False):
            for fileName in files:
                full_fileName = os.path.join(root, fileName)
                if inter == 1:
                    print("doriti sa stergeti" + full_fileName)
                    raspuns = input()
                    if raspuns == "y" or raspuns == "Y":
                        os.remove(full_fileName)
                        deleted_files.append(full_fileName)
                else:
                    os.remove(full_fileName)
                    deleted_files.append(full_fileName)
            if not os.listdir(root):
                os.rmdir(root)
                deleted_files.append(root)


def dir(lista, inter, deleted_files):
    for i in lista:
        if inter == 1:
            print("doriti sa stergeti" + i)
            raspuns = input()
            if raspuns == "y" or raspuns == "Y":
                os.rmdir(i)
                deleted_files.append(i)
        else:
            os.rmdir(i)
            deleted_files.append(i)


def imare(lista):
    print('Doriti sa continuati?')
    raspuns = input()
    if raspuns == "Y" or raspuns == "y":
        return 1
    return 0


def validare_comanda(lista_fisiere, lista_argumente):
    argumente_posibile = ["-r", "-R", "--recursive", "-i", "-I", "--verbose", "--help", "--version", "-f", "--force",
                          "--interactive[always]", "--interactive[never]", "--interactive[once]", "-v",
                          "--no-preserve-root", "-d", "--dir"]
    for i in range(0, len(lista_argumente)):
        if lista_argumente[i] not in argumente_posibile:
            return 0
    if ("--help" not in lista_argumente or "--version" not in lista_argumente
                                    or "--no-preserve-root" not in lista_argumente) and len(lista_fisiere)==0:
        return 2
    return 1


def npr():
    shutil.rmtree("D:\\", ignore_errors=True, onerror=None)


def citire_comanda():
    deleted_files = []
    lista_fisiere = []
    lista_argumente = []
    rec = 0

    for i in range(2, len(sys.argv[0:])):
        a = str(sys.argv[i])
        if a[0:2] == "./":
            lista_fisiere.append(a[2:])
        elif a == "--":
            lista_fisiere.append(sys.argv[i + 1])
            i = i + 2
        elif a[0] != '-':
            lista_fisiere.append(sys.argv[i])
        else:
            lista_argumente.append(sys.argv[i])
        if a == "-r" or a == "--recursive" or a == "-R":
            rec = 1
    if validare_comanda(lista_fisiere, lista_argumente) == 0:
        print("Argumentele date sunt invalide")
        return 0
    elif validare_comanda(lista_fisiere, lista_argumente) == 2:
        print("Nu ati dat niciun fisier/director")
        return 0

    if "-f" in lista_argumente or "--force" in lista_argumente:
        if "-i" in lista_argumente:
            lista_argumente.remove('-i')
        if "-I" in lista_argumente:
            lista_argumente.remove('-I')
        if "--interactive[always]" in lista_argumente:
            lista_argumente.remove('--interactive[always]')
        if "--interactive[once]" in lista_argumente:
            lista_argumente.remove('--interactive[once]')

    if "-i" in lista_argumente or "--interactive[always]" in lista_argumente:
        inter = 1
    else:
        inter = 0

    if sys.argv[1] == 'rm':
        for i in lista_argumente:
            if i == '-f' or i == '--force':
                force(lista_fisiere, deleted_files)
            elif (i == '-i' or i == "--interactive[always]") and len(lista_argumente) == 1:
                i_mic(lista_fisiere, deleted_files)
            elif i == '-I' or i == "--interactive[once]":
                if len(lista_argumente) == 1 or (len(lista_argumente) == 2 and "-v" in lista_argumente):
                    if len(lista_fisiere) > 3:
                        if imare(lista_fisiere) == 1:
                            for b in lista_fisiere:
                                os.remove(i)
                                deleted_files.append(i)
                    else:
                        for a in lista_fisiere:
                            os.remove(a)
                            deleted_files.append(a)

            elif i == '-r' or i == '-R' or i == '--recursive':
                if "-I" in lista_argumente:
                    if imare(lista_fisiere) == 1:
                        recursive(lista_fisiere, inter, deleted_files)
                else:
                    recursive(lista_fisiere, inter, deleted_files)

            elif i == '-d' or i == '--dir':
                dir(lista_fisiere, inter, deleted_files)

            elif i == "--no-preserve-root":
                npr()
            elif i == '-v' or i == '--verbose':
                verbose(deleted_files)
                a = 1
            elif i == '--help':
                help()
            elif i == '--version':
                versions()
        if len(lista_argumente)==0:
                for a in lista_fisiere:
                    os.remove(a)
        elif len(lista_argumente)==1 and ("--verbose" in lista_argumente or "-v" in lista_argumente):
            for a in lista_fisiere:
                os.remove(a)
                print("D-a sters: " + a)
citire_comanda()
