import string
abecedario = string.ascii_uppercase
k = 13
plaintext = "be sure to drink your Ovaltine"
ciphertext = ""
for l in plaintext:
    # si letra no esta en abecedario, caracter no debe ser cifrado
    if l.upper() not in abecedario:
        ciphertext = ciphertext + l
        continue
        
    # Cifrando letra
    c = (abecedario.find(l.upper()) + k) %26
    
    # 
    if l.isupper():
          x = abecedario[c]
    else:
        x = abecedario[c].lower()
    
    # nueva cadena
    ciphertext = ciphertext + x
    
print(ciphertext)