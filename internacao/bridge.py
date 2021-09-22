import pyodbc
import psycopg2
from datetime import datetime , date
import sys
import os
import time



def getdados():
	dados = []
	date1 = date.today()
	cnxn = pyodbc.connect(

		'DRIVER={Devart ODBC Driver for Oracle};Direct=True;Host=10.250.250.6;Service Name=tasy.sub10261738100.vpnhospsaojudas.oraclevcn.com;User ID=tasy;Password=aloisk'
		
		)
	cursor = cnxn.cursor()
	cursor.execute(

		"SELECT QT_PRESCRITA, NM_PRESCRITOR, DS_ITEM, DT_ITEM, NR_PRESCRICAO   FROM TASY.PRESCR_PROCEDIMENTO_SIT_V WHERE  DS_SETOR_PACIENTE = 'Pronto Atendimento' AND DS_TP_ITEM = 'PROCEDIMENTOS'  "
		
		)

	cc = cursor.fetchall()
	n = 0
	for row in cc:
		n += 1

		lista = []
		lista.append(row)

		dados += lista
	print(n)
	return dados


