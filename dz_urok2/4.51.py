konvert_a = 50
konvert_b = 80

otkrytka_c = int(input("длина: "))
otkrytka_d = int(input("ширина: "))

if otkrytka_c > konvert_a and otkrytka_d > konvert_a:
    print("не влезет")
    exit()
elif otkrytka_c < konvert_a and otkrytka_d > konvert_a:
    print("влезет")
    exit()
elif otkrytka_c > konvert_a and otkrytka_d < konvert_a:
    print("влезет")
    exit()
elif otkrytka_c < konvert_a and otkrytka_d < konvert_a:
    print("влезет")
    exit()
elif otkrytka_c < konvert_b:
    print("не влезет")
    exit()
elif otkrytka_d < konvert_b:
    print("не влезет")
    exit()