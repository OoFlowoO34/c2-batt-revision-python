print("calculer la factorial du nombre: ")

number = int(input())

def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)

result = factorielle(number)

print("La factorielle de", number, "est", result)