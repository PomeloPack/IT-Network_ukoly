jmeno = len(input("Zadejte své jméno: "))
if jmeno <=3:
    print("Vaše jméno je moc krátké!")
elif jmeno >3 and jmeno <10:
    print("Vaše jméno je optimální!")
else:
    print("Vaše jméno je moc dlouhé!")