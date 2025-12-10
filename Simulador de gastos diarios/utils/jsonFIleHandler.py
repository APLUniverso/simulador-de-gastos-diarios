from json import dump, load

def readFile(fileName):
    try:
        fileData = None
        with open(fileName) as f:
            fileData = load(f)
        return fileData
    except FileNotFoundError:
        saveFile(fileName,{})
        return readFile(fileName)

def saveFile(fileName,data):
    with open(fileName,"w") as f:
        dump(data,f,indent=4)

def foundCategoria(gastos,categoriaToFound):
	for categoria in gastos:
		if categoria == categoriaToFound:
			return True
	return False


