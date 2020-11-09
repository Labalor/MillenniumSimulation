import numpy as np 
from os import listdir
import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt 
from functions import *

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
	'.-Interval Key: '+str(listhalos)+'\n 	Note: H1-> Mainly Halo./ _int->lower m_Crit200 limit (the upper limit is +1 order of magnitude. Ex:0->1, 1->10).  \n\n .-Head key: '+str(Head)+
	'\n\n Press any key to continue.')

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
	'Note about the CSV key: inter_number ->Inter: lower m_Crit200 limit /->_number: only a reference number.\n\n.-Head key: '+str(Head)+
	'\n\nPress any key to continue.')

PlotHaloTree(HaloTree,limits)
Average,Stdev,Redshift=Average(HaloTree,limits)

plot=plt.figure(figsize=(13.0, 10.0))
ax=plot.add_subplot(111)
for i in Redshift.keys():
	logM=np.log10(Average[i]/Average[i][0])
	logz=np.log10(1+Redshift[i])
	if int(i)==0:
		plt.scatter(logz,logM, label='Masas de halos entre '+ str(i)+'-'+str(1)+' unidades de la simulación' )
	if int(i)==1000:
		plt.scatter(logz,logM, label='Masas de halos a partir de '+ str(i)+' unidades de la simulación' )		
	else:
		plt.scatter(logz,logM, label='Masas de halos entre '+ str(i)+'-'+str(int(i)*10)+' unidades de la simulación' )		
ax.text(0,-0.8, '$M_{halo,z=0}=5 x 10^{11}h^{-1}M_\odot$',fontsize=20)
ax.set_ylabel('log($M_{halo}/M_{halo,z=0})$',fontsize=25)
ax.set_xlabel('log(1+z)',fontsize=25)
plot.suptitle('Halo Tree. Lower limit of m_Crit200 in simulation units: '+str(i), fontsize=25)
plt.legend()
plt.grid()
plt.savefig('H2/Plots/Averages.png')
plt.close()