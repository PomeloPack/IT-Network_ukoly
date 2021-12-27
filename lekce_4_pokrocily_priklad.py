leva_mez_1 = int(input("Zadejte levou mez 1. intervalu: "))
leva_mez_2 = int(input("Zadejte levou mez 2. intervalu: "))
prava_mez_1 = int(input("Zadejte pravou mez 1. intervalu: "))
prava_mez_2 = int(input("Zadejte pravou mez 2. intervalu: "))

prvni_interval = range(leva_mez_1, prava_mez_1 + 1)
druhy_interval = range(leva_mez_2, prava_mez_2 + 1)

print("Dvojice čísel z prvního a druhého intervalu, jejichž součet leží alespoň v jednom z nich: ")
for i in prvni_interval:
    for j in druhy_interval:
        soucet = i + j
        if soucet in prvni_interval or soucet in druhy_interval:
            print("[", i,";",j, "]")
input()