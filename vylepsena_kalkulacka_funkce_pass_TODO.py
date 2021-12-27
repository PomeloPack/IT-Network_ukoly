print("Kalkulačka\n")
pokračovat = True
while pokračovat:
    první_číslo = int(input("Zadejte první číslo: "))
    druhé_číslo = int(input("Zadejte druhé číslo: "))
    print("1 - sčítání")
    print("2 - odčítání")
    print("3 - násobení")
    print("4 - dělené")
    číslo_operace = int(input("Zadejte číslo operace: "))
    if číslo_operace == 1:
        print("Následuje sčítání", první_číslo + druhé_číslo)
    elif číslo_operace == 2:
        print("Následuje odčítání", první_číslo - druhé_číslo)
    elif číslo_operace == 3:
        print("Následuje násobení", první_číslo  * druhé_číslo)
    elif číslo_operace == 4:
         print("Následuje dělení", první_číslo / druhé_číslo)
    else:
        print("Zadal jste špatnou volbu")
nezadáno = True
while nezadáno:
    odpověď = str(input("\nPřejete si zadat další příklad? y / n: "))
    if (odpověď == "y" or odpověď == "Y"):
        nezadáno = False
    elif (odpověď == "n" or odpověď == "N"):
        nezadáno = False
        pokračovat = True
    else:
        pass
input("\nStiskněte libovolnou klávesu...")