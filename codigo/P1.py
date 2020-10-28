import numpy as np 
import requests
import csv
import pandas as pd

def counts(Halos):
	CounterH1=0
	CounterH10=0
	CounterH100=0
	CounterH1000=0
	CounterH10000=0
	for i in range(len(Halos)):
		if Halos[i]>0.0 and Halos[i]<1:
			CounterH1=CounterH1+1
		if Halos[i]>1 and Halos[i]<10:
			CounterH10=CounterH10+1
		if Halos[i]>10 and Halos[i]<100:
			CounterH100=CounterH100+1
		if Halos[i]>100 and Halos[i]<1000:
			CounterH1000=CounterH1000+1
		if Halos[i]>1000 :
			CounterH10000=CounterH10000+1
	print('\nNumber of Halos by mass:\n [0,1]-> '+ str(CounterH1)+'\n [1,10]-> '+ str(CounterH10)+'\n [10,100]-> '+ str(CounterH100) +
	 '\n [100,1000]-> '+ str(CounterH1000)+'\n [1000,-]-> '+ str(CounterH10000) )

def Halo(limits,listhalos,Halos):
	buf={}
	for i in range(len(limits)-1):
		buf[listhalos[i]]=Halos[(Halos['m_Crit200']<limits[i]) & (Halos['m_Crit200']>limits[i+1])]
	buf[listhalos[i+1]]=Halos[(Halos['m_Crit200']>limits[i+1])]
	return(buf)

Head=['haloID','subHaloID','lastProgenitorId','treeId','snapNum','redshift','firstProgenitorId','nextProgenitorId','descendantId',
'firstHaloInFOFgroupId','nextHaloInFOFgroupId','np','m_Mean200','m_Crit200','m_TopHat','phKey','x','y','z','zIndex','ix',
'iy','iz','velX','velY','velZ','velDisp','vMax','spinX','spinY','spinZ','mostBoundID','fileNr','subhaloIndex','halfmassRadius','random']
BigHalos_H1 = pd.read_csv('H1_Big.csv',names=Head)
SmallHalos_H1=pd.read_csv('H1_Small.csv',names=Head)
BigHalos_H1.head()
SmallHalos_H1.head()
limits=[0,1,10,100,1000]
listhalos=['H1_1','H1_10','H1_100','H1_1000','H1_10000']
print('\n------\nH1_Big.csv')
Halos1=counts(BigHalos_H1['m_Crit200'])
H1=Halo(limits,listhalos,BigHalos_H1)

print('\n------\nH1_Small.csv')
Halos2=counts(SmallHalos_H1['m_Crit200'])
H1_2=Halo(limits,listhalos,BigHalos_H1)
input('\nCODE Information: There are two dictionaries with Halos data in critical mass 200. The following structure is used to operate with the dictionaries: '+
	'\n  	np.array( Dictionary[Interval Key][Head key])[rows]\n '+
	'Interval Key: '+str(listhalos)+'\n 	Note: H1-> Mainly Halo. _int->upper m_Crit200 limit.  \n Head key: '+str(Head))

print(np.array(H1_2['H1_10000']['m_Crit200'])[0:10] )



