#Python Tippspiel
import json

Teilnehmer = ["Kim", "Thomas"]
Spiele = [1, 2, 3] # Liste der Spiele

def get_ergebnis(spiel):
	with open('data.json') as datafile:
		daten = json.load(datafile)
	spielname = "Spiel " + str(spiel)
	a = daten["Ergebnisse"][spielname]
	print a
	print spielname
	return a

def get_tipp(spiel, spieler):
	t = [3,1] # nur zum testen manuell eingegeben
	return t
	
def set_tipp(spiel, spieler, tipp1, tipp2):
	with open('tipps.txt', 'a') as tippfile:
		game = str(spiel)
		player = Teilnehmer[spieler]
		tipp1string = str(tipp1)
		tipp2string = str(tipp2)
		tippfile.write(game + " " + player + " " + tipp1string + " " + tipp2string + "\n")
	return 0
	
def punkte(spiel, spieler):
	p = 0
	ergebnis = get_ergebnis(spiel)
	tipp = get_tipp(spiel, spieler)
	if (ergebnis[0]-ergebnis[1]) < 0:
		if (tipp[0]-tipp[1]) < 0: # richtiger gewinner
			p += 1
	elif (ergebnis[0]-ergebnis[1]) > 0:
		if (tipp[0]-tipp[1]) > 0:
			p += 1
	else: # unentschieden
		if (tipp[0]-tipp[1]) == 0:
			p += 1
	if (ergebnis[0]-ergebnis[1] == tipp[0]-tipp[1]): # richtiges Verhaeltnis
		p += 1
	if (ergebnis[0] == tipp[0] and ergebnis[1] == tipp[1]): # komplett richtig getippt
		p += 1	
	print p
	return p	

def gesamtpunkte(spieler):
	p = 0
	sp = spieler
	# def punkte fuer "spieler" fuer alle spiele auswerten und aufsummieren
	for x in Spiele:
		p += punkte(Spiele[x], sp)
	return p

punkte(2, 3) # noch keine sinnvolle uebergabe
set_tipp(1, 0, 1, 1)
set_tipp(1, 1, 2, 5)