import numpy as np 
from os import listdir
import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt 

def Load(folder,Head):
	buf=[]
	Buf={}
	for out in listdir('./'+folder):
		buf.append(out)
		Buf[str(out)[0:-4]]=pd.read_csv(folder+'/'+str(out),names=Head)
		Buf[str(out)[0:-4]].head()
	print('\n---------------------------------\nDIR->'+folder+'\nCSV files:' +str(buf))
	print('Dictionary items:' + str(Buf.keys()))
	return(Buf)

def Halo(limits,listhalos,Halos):
	buf={}
	for i in range(len(limits)-1):
		buf[listhalos[i]]=Halos[(Halos['m_Crit200']>limits[i]) & (Halos['m_Crit200']<limits[i+1])]
	buf[listhalos[i+1]]=Halos[(Halos['m_Crit200']>limits[i+1])]
	print('Number of Halos by mass (m_Crit200):\n [0,1]-> '+ str(len(np.array(buf[listhalos[0]]['m_Crit200'])))+'\n [1,10]-> '+ str(len(np.array(buf[listhalos[1]]['m_Crit200'])))+'\n [10,100]-> '+ str(len(np.array(buf[listhalos[2]]['m_Crit200']))) +
	 '\n [100,1000]-> '+ str(len(np.array(buf[listhalos[3]]['m_Crit200'])))+'\n [1000,-]-> '+ str(len(np.array(buf[listhalos[4]]['m_Crit200'])) ))
	return(buf)

def PlotHaloTree(HaloTree,limits):
	for i in limits:
		try:
			os.mkdir('H2/Plots/'+str(i))
		except:
			print('Make sure you have the necessary folders.')
		for j in HaloTree.keys():
			if  str(i)==str(j)[0:-2]:

				plot=plt.figure(figsize=(13.0, 10.0))
				ax=plot.add_subplot(111)	

				m_Crit200=np.array(HaloTree[j]['m_Crit200'])
				logM=np.log10(m_Crit200/m_Crit200[0])
				logz=np.log10(1+np.array(HaloTree[j]['redshift']))

				plt.plot(logz,logM)		
				ax.plot()
				ax.set_ylabel('log($M_{halo}/M_{halo,z=0}$')
				ax.set_xlabel('log(1+z)')
				plt.savefig('H2/Plots/'+str(i)+'/'+str(j))
				plt.close()

Head=['haloID','subHaloID','lastProgenitorId','treeId','snapNum','redshift','firstProgenitorId','nextProgenitorId','descendantId',
'firstHaloInFOFgroupId','nextHaloInFOFgroupId','np','m_Mean200','m_Crit200','m_TopHat','phKey','x','y','z','zIndex','ix',
'iy','iz','velX','velY','velZ','velDisp','vMax','spinX','spinY','spinZ','mostBoundID','fileNr','subhaloIndex','halfmassRadius','random']
limits=[0,1,10,100,1000]
listhalos=['H1_0','H1_1','H1_10','H1_100','H1_1000']


H1_z0=Load('H1',Head)
H1_Halos={}
for i in ((H1_z0.keys())):
	print('\n------\n->'+ str(i)+'.csv')
	H1_Halos[str(i)]=Halo(limits,listhalos,H1_z0[str(i)])

input('\nCODE Information: There are dictionaries with Halos data in critical mass 200. The following structure is used to operate with the dictionaries: '+
	'\n  	np.array( Dictionary[CSV key][Interval Key][Head key])[rows]\n\n'+ '.-CSV Key:'+str(H1_z0.keys()) +'\n\n' +
	'.-Interval Key: '+str(listhalos)+'\n 	Note: H1-> Mainly Halo./ _int->lower m_Crit200 limit (the upper limit is +1 order of magnitude. Ex:0->1, 1->10).  \n\n .-Head key: '+str(Head)+'\nPress any key to continue.')

for i in listhalos:
	print('\n#########\nHalo ID  for Interval Key: '+ str(i))
	for j in H1_z0.keys():
		print('->'+str(j)+'.csv')
		if len(np.array(H1_Halos[j][i]['haloID']))<1:
			print('None')
		else:
			print(np.array(H1_Halos[j][i]['haloID'])[0:10] )

try:
	shutil.rmtree('H2/Plots')
except:
	print('DIR. H2/Plots created')
HaloTree=Load('H2',Head)
print(HaloTree.keys())
os.mkdir('H2/Plots')

input('\nCODE Information: There are dictionaries with Halos Trees data. The following structure is used to operate with the dictionaries: '+
	'\n  	np.array( Dictionary[CSV key][Head key])[rows]\n\n'+ '.-CSV Key:'+str(HaloTree.keys()) +'\n' +
	'Note about the CSV key: inter_number ->Inter: lower m_Crit200 limit /->_number: only a reference number.\n\n.-Head key: '+str(Head)+'\nPress any key to continue.')

PlotHaloTree(HaloTree,limits)
