'''
Script realiza um encurtamento da URL usando o TinyURL.
Após ser encurtada, a URL é copiada para área de transferência.

- Necessário instalar as lib pyshorteners e clipboard
- pip install pyshorteners
- pip install clipboard
'''

import pyshorteners
import clipboard

url = input("Digite url a ser encurtada: ")

url_encurtada = pyshorteners.Shortener().tinyurl.short(url)

print('---------------------------------------')
print("Sua url: ", url_encurtada)
print('---------------------------------------')

clipboard.copy(url_encurtada)
print("Url foi copiada para a área de transferencia")