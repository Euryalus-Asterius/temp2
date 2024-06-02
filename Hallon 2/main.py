import random
import math

def Main():
    with open('text.txt', 'r') as file_obj:
        first_char = file_obj.read(1)
        if not first_char:
            print("text.txt is empty")
            return
        
    # om text.txt inte är tom
    Generator(delayMin, delayMax)
    print("Payload generated...")

    Inject()
    print("Payload successfully injected!")

def GetValues():
    valuesF = open('values.txt')
    values = valuesF.readlines()
    valuesF.close()
    delayMin = values[0].strip('\n')[4:]
    delayMax = values[1].strip('\n')[4:]
    autoUPD = values[2].strip('\n')[8:]

    return [int(delayMin), int(delayMax), autoUPD]

def Generator(min, max):
    text = open('text.txt', encoding='utf-8')
    payload = open('payload.txt', "w")
    payload.close()
    payload = open('payload.txt', "a", encoding='utf-8')

    payload.write("REM Tangentbord ska vara SVENSKA \n")
    payload.write("REM Funkar inte for < och > \n")
    payload.write("REM < byts mot __M__ \n")
    payload.write("REM > byts mot __S__ \n\n")

    payload.write("DELAY 1000")

    if autoUPD == "true" or autoUPD == "True":
        payload.write("UPD\n")

    for line in text:
        payload.write("\nSTRING ")
        for letter in line:
            if letter == "“":
                letter = '"'
        
            if letter == "Å":
                payload.write("\nSHIFT STRING [\nSTRING ")
            elif letter == "Ä":
                payload.write("\nSHIFT STRING '\nSTRING ")
            elif letter == "Ö":
                payload.write("\nSHIFT STRING ;\nSTRING ")
            elif letter == "å":
                payload.write("[")
            elif letter == "ä":
                payload.write("'")
            elif letter == "ö":
                payload.write(";")
            elif letter == "+":
                payload.write("-")
            elif letter == "´":
                payload.write("=")
            elif letter == "¨":
                payload.write("]")
            elif letter == "'":
                payload.write("\ ")
            elif letter == "-":
                payload.write("/")
            elif letter == ".":
                payload.write(".")
            elif letter == ",":
                payload.write(",")
            elif letter == "<":
                payload.write("??M??")
            elif letter == '"':
                payload.write("@")
            elif letter == "¤":
                payload.write("$")
            elif letter == "&":
                payload.write("^")
            elif letter == "/":
                payload.write("&")
            elif letter == "(":
                payload.write("*")
            elif letter == ")":
                payload.write("(")
            elif letter == "=":
                payload.write(")")
            elif letter == "?":
                payload.write("_")
            elif letter == "`":
                payload.write("+")
            elif letter == "^":
                payload.write("}")
            elif letter == "*":
                payload.write("|")
            elif letter == "_":
                payload.write("?")
            elif letter == ":":
                payload.write(">")
            elif letter == ";":
                payload.write("<")
            elif letter == ">":
                payload.write("??S??")
            elif letter == " ":
                payload.write("\nSPACE")
            else:
                payload.write(letter)
            
            payload.write("\nDELAY " + str(math.floor(random.uniform(min, max))) + "\nSTRING ")

        payload.write("\nENTER")

    payload.close()
    text.close()

def Inject():
    text = open('d:\\payload.dd', 'w')
    payload = open('payload.txt', encoding='utf-8')
    for line in payload:
        text.write(line)
    text.close()
    
values = GetValues()
delayMin = values[0]
delayMax = values[1]
autoUPD = values[2]
    
Main()