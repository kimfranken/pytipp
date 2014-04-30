#Python Tippspiel
import json

Teilnehmer = ["Kim", "Thomas", "Karl", "Lukas", "Isa"]
Spiele = [1, 2, 3] # Liste der Spiele

def get_ergebnis(spiel):
	with open('data.json') as datafile:
		daten = json.load(datafile)
	spielname = "Spiel " + str(spiel)
	a = daten["Ergebnisse"][spielname]
	
	print "Spielergebnis von " + spielname + ":"
	print a
	
	return a
	
def set_ergebnis(spiel, ergebnis1, ergebnis2):
	spielnr = "Spiel " + str(spiel)
	# ganzes File laden, in daten speichern
	with open('data.json') as datafile: 
		daten = json.load(datafile)
	# tipps in daten eintragen
	daten["Ergebnisse"][spielnr] = [ergebnis1, ergebnis2]
	# daten wieder als json komplett neu schreiben
	with open('data.json', 'w+') as datafile:
		json.dump(daten, datafile, indent=4)
	return 0

def get_tipp(spiel, spieler):
	with open('data.json') as datafile:
		daten = json.load(datafile)
	spielname = "Spiel " + str(spiel)
	player = Teilnehmer[spieler] # sollte wahrscheinlich auch noch durch lesen der json ersetzt werden
	t = daten["Tipps"][spielname][player]
	
	print "Tipp von " + player + ":"
	print t
	
	return t
	
def set_tipp(spiel, spieler, tipp1, tipp2):
	spielnr = "Spiel " + str(spiel)
	spielername = Teilnehmer[spieler]
	# ganzes File laden, in daten speichern
	with open('data.json') as datafile: 
		daten = json.load(datafile)
	# tipps in daten eintragen
	try:
		daten["Tipps"][spielnr][spielername] = [tipp1, tipp2]
	except:
		print "SHIT" # hier gibts noch was zu tun!!
		
	# daten wieder als json komplett neu schreiben
	with open('data.json', 'w+') as datafile:
		json.dump(daten, datafile, indent=4)
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
	
	punkte = str(p)
	spielname = "Spiel " + str(spiel)
	print "Punkte von " + Teilnehmer[spieler] + " in " + spielname + ": " + punkte
	
	return p

def gesamtpunkte(spieler):
	p = 0
	spielername = Teilnehmer[spieler]
	with open('data.json') as datafile:
		daten = json.load(datafile)
	# def punkte fuer "spieler" fuer alle spiele auswerten und aufsummieren
	for x in daten["Ergebnisse"]:
		print x
		numberstr = x[6:] # loescht "Spiel "
		number = int(numberstr)
		try:
			daten["Tipps"][x][spielername] 
			# wirft einen Error wenn es zum Spiel keinen Tipp gibt -> springt aus try block raus, sodass danach nicht mehr auf etwas zugegriffen wird, was nicht existiert.
			
			p += punkte(number, spieler)
		except:
			print "KEIN TIPP VORHANDEN"
	print p
	return p

#punkte(2, 2)
#set_tipp(1, 0, 11, 1)
#set_tipp(2, 0, 2, 15)
#set_tipp(1, 2, 24, 42)
#set_tipp(1, 3, 23, 23)
#set_tipp(4, 0, 3, 3)
#set_ergebnis(6, 3, 2)
gesamtpunkte(0)