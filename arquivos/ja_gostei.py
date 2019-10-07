print("De quem você já gostou, amor?")
print("toma-lhe a resposta por Python, amor!\n")

ja_gostei = ['Dani,', 'Fer', 'Marina', 'Amanda', 'Laura', 'Fer2', 'Eliza', 'Bruna', 'Mickaella', 'Dani2']
ja_amei = ['Marina']

for gostada in ja_gostei:
    if gostada in ja_amei:
        print("Já gostei e amo a", ja_amei[0])
    else:
        print("Já gostei mas não amei a", gostada)