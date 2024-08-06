def e_palindromo(p):
    p= p.replace(" ", "").lower()
    if p == p[::-1]:
        return True
    else:
        return False
p = input("Digite uma palavra para verificar se é um palíndromo: ")

if e_palindromo(p):
    print(f"A palavra '{p}' é um palíndromo.")
else:
    print(f"A palavra '{p}' não é um palíndromo.")
