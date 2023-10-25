import datetime

heure_actuelle = datetime.datetime.now().time()
heure = heure_actuelle.hour
minute = heure_actuelle.minute
second = heure_actuelle.second


date_actuelle = datetime.datetime.now().date()
print("L'heure actuelle est :", heure, "h", minute,"mn",second,"s")
print("La date actuelle est :", date_actuelle)
