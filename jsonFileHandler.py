import json

def readJsonFile(fileName):
    data = ""
    try:
        with open(fileName) as json_file:
            data = json.load(json_file) # json.load lee el archivo JSON y devuelve 
                                        # el contenido como un diccionario de Python.
    except IOError:
        print("Could not read file")
    return data