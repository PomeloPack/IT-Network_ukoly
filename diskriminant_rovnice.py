print("Program na výpočet kvadratické rovnice\nTvar rovnice: ax^2+bx+c=0")
koeficien_a = int(input("koeficient a: "))
koeficient_b = int(input("koeficient b: "))
koeficient_c = int(input("koeficient c: "))
D =  koeficient_b ** 2 - 4 * koeficien_a * koeficient_c
if D >= 0:
    x_1 = (- koeficient_b - D / D ) / 2 * koeficien_a
    x_2 = ( - koeficient_b + D / D) / 2 * koeficien_a
    print("Rovnice má dva kořeny: ")
    print("Kořen 1 je: ", x_1)
    print("Kořen 2 je: ", x_2)
else:
    print("Rovnice nemá řešení")
input()
