# zadání
ovoce = ["Banán", "Pomelo", "Mandarinka", "Jablko", "Malina"]
zelenina = ["Brokolice", "Květák", "Mrkev", "Hrášek", "Petržel"]
pocet_slov = 0
opakovani = True

# seznam ovoce a zeleniny pro uživatele

print("Seznam ovoce: Banán, Pomelo, Mandarinka, Jablko, Malina.")
print("Seznam zeleniny: Brokolice, Květák, Mrkev, Hrášek, Petržel.")

# syntaxe

while opakovani:
    index_listu = input(str("Zadejte název libovolné zeleniny nebo ovoce: \n"))
    if index_listu in ovoce:
        print("Zadali jste ovoce.")
    elif index_listu in zelenina:
        print("Zadali jste zeleninu.")
    else:
        print("Tato zelenina či ovoce není na seznamu!")
    pocet_slov += 1
    opakovani_cyklu = input("Přejete si zadat další slovo ze seznamu? (ano/ne): \n")
    if opakovani_cyklu == "ano" or opakovani_cyklu == "Ano":
        continue
    else:
        break
print("Zadali jste počet slov: ", pocet_slov)
input()


    
