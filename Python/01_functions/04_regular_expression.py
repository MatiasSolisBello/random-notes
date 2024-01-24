# Son una cadena de texto que forman un patrón de busqueda
import re

# Verificar si una cadena contiene la palabra "python".
text = "Vamos a aprender expresiones regulares con python"
#print(re.search(r'python', text))  #<re.Match object; span=(43, 49), match='python'>
print('1.- ', text[43:49])

# Encontrar todas las direcciones de correo electrónico en una cadena de texto.
email = "El correo electronico es marcusalvear@gmail.com"
print('2.- ', re.findall(
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email)
)
