import numpy as np 
import requests
import csv
import pandas as pd



def Halo(limits,listhalos,Halos):
	buf={}
	for i in range(len(limits)-1):
		buf[listhalos[i]]=Halos[(Halos['m_Crit200']>limits[i]) & (Halos['m_Crit200']<limits[i+1])]
	buf[listhalos[i+1]]=Halos[(Halos['m_Crit200']>limits[i+1])]
	print('\nNumber of Halos by mass:\n [0,1]-> '+ str(len(np.array(buf[listhalos[0]]['m_Crit200'])))+'\n [1,10]-> '+ str(len(np.array(buf[listhalos[1]]['m_Crit200'])))+'\n [10,100]-> '+ str(len(np.array(buf[listhalos[2]]['m_Crit200']))) +
	 '\n [100,1000]-> '+ str(len(np.array(buf[listhalos[3]]['m_Crit200'])))+'\n [1000,-]-> '+ str(len(np.array(buf[listhalos[4]]['m_Crit200'])) ))
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
H1_2=Halo(limits,listhalos,SmallHalos_H1)
input('\nCODE Information: There are two dictionaries with Halos data in critical mass 200. The following structure is used to operate with the dictionaries: '+
	'\n  	np.array( Dictionary[Interval Key][Head key])[rows]\n\n '+
	'.-Interval Key: '+str(listhalos)+'\n 	Note: H1-> Mainly Halo. _int->upper m_Crit200 limit.  \n\n .-Head key: '+str(Head)+'\nPress any key to continue.')

print(np.array(H1_2['H1_100']['m_Crit200'])[0:10] )



