import numpy as np 
from os import listdir
import os
import shutil
import pandas as pd
import matplotlib.pyplot as plt 
##################################################################################################################################
def Load(folder,Head):
	buf=[]
	Buf={}
	for out in listdir('./'+folder):
		buf.append(out)
		Buf[str(out)[0:-4]]=pd.read_csv(folder+'/'+str(out),names=Head)
		Buf[str(out)[0:-4]].head()
	print('\n---------------------------------\n//DIR->'+folder+'\nCSV files:' +str(buf))
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
		plot=plt.figure(figsize=(13.0, 10.0))
		ax=plot.add_subplot(111)

		for j in HaloTree.keys():
			HaloTree[j]=HaloTree[j][HaloTree[j]['m_Crit200']>0 ] 
			if  str(i)==str(j)[0:-2]:
				m_Crit200Array=np.array(HaloTree[j]['m_Crit200'])
				logM=np.log10(m_Crit200Array/m_Crit200Array[0])
				logz=np.log10(1+np.array(HaloTree[j]['redshift']))
				conbuf=0
				for k in HaloTree[j]['firstProgenitorId']:
					if int(k)==-1:
						break
					conbuf+=1

				print("Halo's masses: ", m_Crit200Array[0:conbuf])
				plt.plot(logz[0:conbuf],logM[0:conbuf], label='Halo con masa a z=0 de: '+str(round(np.array(HaloTree[j]['m_Crit200'])[0],2) ))		
		ax.text(0,min(logM[0:conbuf]), '$M_{halo,z=0}=5 x 10^{11}h^{-1}M_\odot$',fontsize=20)
		ax.set_ylabel('log($M_{halo}/M_{halo,z=0})$',fontsize=25)
		ax.set_xlabel('log(1+z)',fontsize=25)
		plt.legend(fontsize=11)
		plot.suptitle('Halo Tree. Lower limit of m_Crit200 in simulation units: '+str(i), fontsize=25)
		plt.grid()
		plt.savefig('H2/Plots/'+str(i))
		plt.close()

def Average(HaloTree,limits):
	BufAverages={}
	Bufstdev={}
	BufRedshift={}
	for i in limits:
		bufmatter={}
		bufredshift=[]
		firstLoop=False
		for j in HaloTree.keys():
			HaloTree[j]=HaloTree[j][HaloTree[j]['m_Crit200']>0 ] 
			if  str(i)==str(j)[0:-2]:
				for k,p in zip(np.array(HaloTree[j]['redshift']),range(len(np.array(HaloTree[j]['redshift'])))) :
					if int(np.array(HaloTree[j]['firstProgenitorId'])[p])==-1:
						break
					else:
						if firstLoop==False:
							bufmatter[k]=np.array(HaloTree[j]['m_Crit200'])[p]
							bufredshift.append([k])
						else:
							try:
								bufmatter[k]=np.append(np.array(bufmatter[k]),np.array(HaloTree[j]['m_Crit200'])[p])
							except KeyError:
								bufmatter[k]=np.array(HaloTree[j]['m_Crit200'])[p]
								bufredshift.append([k])

				firstLoop=True
		BufRedshift[i]=np.array(bufredshift)
		bufstdev=[]
		bufmean=[]
		for redshift in bufmatter.keys():
			bufmean.append(np.mean(bufmatter[redshift]))
			bufstdev.append(np.std(bufmatter[redshift]))
		BufAverages[i]=np.array(bufmean)
		Bufstdev[i]=np.array(bufstdev)
	return(BufAverages,Bufstdev,BufRedshift)

