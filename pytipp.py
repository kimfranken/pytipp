#Python Tippspiel

Teilnehmer = ["Kim", "Thomas"]
Spiele = [1, 2, 3] # Liste der Spiele

def ergebnis(spiel):
	a = [1,3] # nur zum testen manuell eingegeben
	return a

def tipp(spiel, spieler):
	t = [0,2] # nur zum testen manuell eingegeben
	return t
	
def punkte(spiel, spieler):
	p = 0
	ergebnisarray = ergebnis(1) # noch keine sinnvolle uebergabe
	tipparray = tipp(5, 5) # noch keine sinnvolle uebergabe
	if (ergebnisarray[0]-ergebnisarray[1])	< 0:
		if (tipparray[0]-tipparray[1])	< 0: # richtiger gewinner
			p +=1
			if (ergebnisarray[0]-ergebnisarray[1] == tipparray[0]-tipparray[1]): # richtiges Verhaeltnis
				p+=1
				if (ergebnisarray[0] == tipparray[0] and ergebnisarray[1] == tipparray[1]): # komplett richtig getippt
					p+=1
	if (ergebnisarray[0]-ergebnisarray[1])	> 0:
		if (tipparray[0]-tipparray[1])	> 0:
			p +=1
			if (ergebnisarray[0]-ergebnisarray[1] == tipparray[0]-tipparray[1]):
				p+=1
				if (ergebnisarray[0] == tipparray[0] and ergebnisarray[1] == tipparray[1]):	
					p+=1
				
	print p
	return p	

def gesamtpunkte(spieler):
	p = 0
	x = 0
	sp = spieler
	# def punkte fuer "spieler" fuer alle spiele auswerden und aufsummieren
	for x in Spiele:
		p += punkte(Spiele[x], sp)
	return p

punkte(3, 3) # noch keine sinnvolle uebergabe
print len(Spiele)