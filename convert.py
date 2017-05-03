###################################
# Name script: knab.py            #
# Parameter  : Input file         #
# Author     : Bastiaan Krijgsman #
# Version    : 0.1                #
# Date       : 03-05-2017         #
###################################  

from datetime import datetime
import sys, csv, os

class Bank:
	ifname = ""
	ofname = ""

	def __init__(self,ifile):
		self.ifname = ifile
		self.ofname = str(os.path.splitext(ifile)[0]) + "_" + str(datetime.now().year) + ".csv"

        def gencsvk(self):	
		ifile = open(self.ifname,"rb")
		reader = csv.reader(ifile,delimiter=';')

		ofile = open(self.ofname,"wb")
		writer = csv.writer(ofile,delimiter=',',quotechar='"',quoting=csv.QUOTE_ALL)
		writer.writerow(["Rekening","Datum","Omschrijving","Toelichting","Opname","Storting"])

		## "Rekeningnummer","Transactiedatum","Valutacode","CreditDebet","Bedrag","Tegenrekeningnummer","Tegenrekeninghouder","Valutadatum;
		## Betaalwijze;Omschrijving;Type betaling;Machtigingsnummer;Incassant ID;Adres;
                reader.next()
                reader.next()
                
		for row in reader:
                        
			rekening = row[0]
			datum = row[1]
			#omschrijving = row[10] + " " + row[11] + " " + row[12] + " " + row[13] + \
			#	" " + row[14] + " " + row[15] + " " + row[16] + " " + row[17] + \
			#	" " + row[18]
                        omschrijving = row[9]
			opname = 0
			storting = 0
			toelichting = row[5] + " " + row[6] + " " + row[8] + " " + row[13] 
			if row[3] == "D":
				opname = row[4]
			if row[3] == "C":
				storting = row[4]


			nrow = rekening,datum,omschrijving,toelichting,opname,storting
			print row[4]+ " " + row[6]
			writer.writerow(nrow)

bank = Bank(sys.argv[1])
bank.gencsvk()
if len(sys.argv) < 2:
        print "No input file name given!"
        exit()
