import csv

def lasit_people_csv(datnes_nosaukums):
    darbinieki = []

    with open(datnes_nosaukums, newline='', encoding='utf-8') as csvfile:
        datu_avots = csv.DictReader(csvfile)
        for rinda in datu_avots:
            vards = rinda['First Name']
            uzvards = rinda['Last Name']
            darbinieka_info = {'vards': vards, 'uzvards': uzvards}
            darbinieki.append(darbinieka_info)

    return darbinieki

# Izmantojot funkciju un norādot people.csv datnes nosaukumu
datnes_nosaukums = 'people.csv'
darbinieki = lasit_people_csv(datnes_nosaukums)

# Parādīt rezultātus
for darbinieks in darbinieki:
    print(f"{darbinieks['vards']} {darbinieks['uzvards']}")