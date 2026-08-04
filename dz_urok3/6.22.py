chislo = 5738503
chislo_3 = 0


while chislo != 0:
    last_chislo = chislo % 10
    chislo //= 10

    if last_chislo == 3:
        chislo_3 += 1

print(f"троек в числе: {chislo_3}")