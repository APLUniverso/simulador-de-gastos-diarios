
def colorear(color,text):
    colors = dict(BLACK = '\033[30m',RED = '\033[31m',GREEN = '\033[32m',YELLOW = '\033[33m',BLUE = '\033[34m',MAGENTA = '\033[35m',CYAN = '\033[36m',WHITE = '\033[37m',AZUL_RARO = '\033[38;5;24m',RESET = '\033[0m')
    return f"{colors.get(color)}{text}{colors.get('RESET')}"

def ERROR(mensaje):
    print(colorear("RED",mensaje))

def INPUT(mensaje):
    return colorear("GREEN",mensaje)

def GREEN(text):
    return colorear("CYAN",text)

def TITULO(titulo):
    return colorear("AZUL_RARO",titulo)