from Packages import *
from functions import *

Head=['haloID','subHaloID','lastProgenitorId','treeId','snapNum','redshift','firstProgenitorId','nextProgenitorId','descendantId',
'firstHaloInFOFgroupId','nextHaloInFOFgroupId','np','m_Mean200','m_Crit200','m_TopHat','phKey','x','y','z','zIndex','ix',
'iy','iz','velX','velY','velZ','velDisp','vMax','spinX','spinY','spinZ','mostBoundID','fileNr','subhaloIndex','halfmassRadius','random']
limits=[0,1,10,100,1000]
listhalos=['H1_0','H1_1','H1_10','H1_100','H1_1000']


H1_z0=Load('H1',Head,True)
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
			print(np.array(H1_Halos[j][i]['haloID'])[0:25] )

try:
	shutil.rmtree('H2/Plots')
except:
	print('DIR. H2/Plots created')
HaloTree=Load('H2',Head,True)
print(HaloTree.keys())
os.mkdir('H2/Plots')

input('\nCODE Information: There are dictionaries with Halos Trees data. The following structure is used to operate with the dictionaries: '+
	'\n  	np.array( Dictionary[CSV key][Head key])[rows]\n\n'+ '.-CSV Key:'+str(HaloTree.keys()) +'\n' +
	'Note about the CSV key: inter_number ->Inter: lower m_Crit200 limit ->_number: only a reference number.\n\n.-Head key: '+str(Head)+
	'\n\nPress any key to continue.')

PlotHaloTree(HaloTree,limits)
Average,Stdev,Redshift=Average(HaloTree,limits)

PlotAverages(Average,Redshift,Stdev,Subplot=True)
PlotAverages(Average,Redshift,Stdev,Subplot=False)

try:
	shutil.rmtree('G2/Plots')
except:
	print('DIR. G2/Plots created')

MassTree=Load('G2',None,HEAD=False)
os.mkdir('G2/Plots')
PlotBaryonMassTree(MassTree,limits)
Baryon_Averages,Baryon_stdev,Baryon_Redshift=AveragesModBaryon(MassTree,limits)

BaryonPlotAverages(Baryon_Averages,Baryon_Redshift,Baryon_stdev,Subplot=True)
BaryonPlotAverages(Baryon_Averages,Baryon_Redshift,Baryon_stdev,Subplot=False)


key=['G100_1','G100_2','G100_8','G100_9']
for i in key:



	magnitude_b=MassTree[i][MassTree[i]['mag_b']!=99 ]
	magnitude_b=np.array(magnitude_b['mag_b']); 

	magnitude_v=MassTree[i][MassTree[i]['mag_b']!=99 ]
	magnitude_v=np.array(magnitude_v['mag_v']);
	magnitude=magnitude_b-magnitude_v

	FirstProg=MassTree[i][MassTree[i]['mag_b']!=99 ];
	FirstProg=np.array(FirstProg['firstProgenitorId'])
	Paquetes,Delimitadores=Filtromagnitud(MassTree[i],FirstProg)
	print(Paquetes)
	PlotArbolFusion(Paquetes,Delimitadores,magnitude,i,MassTree[i])
	



#magnitude_v=np.array((set(list(magnitude_v['mag_v'])))); 










	
	















