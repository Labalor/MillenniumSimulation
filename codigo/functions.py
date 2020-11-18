from Packages import *

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
	Value_suptitle=10
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

				plt.plot(logz[0:conbuf],logM[0:conbuf])		
		ax.set_ylabel('log($M_{halo}/M_{halo,z=0})$',fontsize=25)
		ax.set_xlabel('log(1+z)',fontsize=25)
		if int(i)==0:
			plot.suptitle('Dark Matter Halo Tree. m_Crit200 [M$_\odot$/h]: 0-1*10$^{10}$', fontsize=25)
		if int(i)==1000:
			plot.suptitle('Dark Matter Halo Tree. m_Crit200 [M$_\odot$/h]: 1*10$^{13}$-$\infty$', fontsize=25)
		if int(i)!=0 and int(i)!=1000:
			plot.suptitle('Dark Matter Halo Tree. m_Crit200 [M$_\odot$/h]: 1*10$^{'+str(Value_suptitle) +'}$-1*10$^{'+str(Value_suptitle+1)+'}$', fontsize=25)
		Value_suptitle+=1
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
							bufmatter[k]=np.array(HaloTree[j]['m_Crit200'])[p]/np.array(HaloTree[j]['m_Crit200'])[0]
							bufredshift.append([k])
						else:
							try:
								bufmatter[k]=np.append(np.array(bufmatter[k]),np.array(HaloTree[j]['m_Crit200'])[p]/np.array(HaloTree[j]['m_Crit200'])[0])
							except KeyError:
								bufmatter[k]=np.array(HaloTree[j]['m_Crit200'])[p]/np.array(HaloTree[j]['m_Crit200'])[0]
								bufredshift.append([k])

				firstLoop=True
		BufRedshift[i]=np.array(bufredshift)
		bufstdev=[]
		bufmean=[]
		for redshift in bufmatter.keys():
			bufmean.append(np.mean(np.log10(bufmatter[redshift])))
			bufstdev.append(np.std(np.log10(bufmatter[redshift])))
		BufAverages[i]=np.array(bufmean)
		Bufstdev[i]=np.array(bufstdev)
	return(BufAverages,Bufstdev,BufRedshift)

def PlotAverages(Average,Redshift,Stdev,Subplot):
	plot=plt.figure(figsize=(13.0, 10.0))
	col=0
	colores=['blue','orange','green','red','purple','brown']

	if Subplot==False:
		ax=plot.add_subplot(1,1,1)
		fontsize=20
	if Subplot==True:
		subplot=231
	for i in Redshift.keys():
		if Subplot==True:
			ax=plot.add_subplot(subplot)
			subplot+=1
			fontsize=15
			ax.set_xlabel('log(1+z)',fontsize=fontsize)
			plt.grid()

		logM=Average[i]
		logz=np.log10(1+Redshift[i])
		logStev=Stdev[i]
		if int(i)==0:
			if Subplot==True:
				plt.errorbar(logz,logM,logStev,linestyle='None', capsize=5,ecolor=colores[col])
				ax.set_ylabel('log($M_{halo}/M_{halo,z=0})$',fontsize=fontsize)

			plt.scatter(logz,logM,c=colores[col],
				label='Masas de halos entre '+ str(i)+'-'+str(1)+' unidades de la simulación' )
		if int(i)==1000:
			if Subplot==True:
				plt.errorbar(logz,logM,logStev,linestyle='None', capsize=5,ecolor=colores[col] )
			plt.scatter(logz,logM,c=colores[col],
				label='Masas de halos a partir de '+ str(i)+' unidades de la simulación' )			
		if int(i)!=1000 and int(i)!=0:
			if Subplot==True:
				plt.errorbar(logz,logM,logStev,linestyle='None', capsize=5,ecolor=colores[col] )	
				if col==3:
					ax.set_ylabel('log($M_{halo}/M_{halo,z=0})$',fontsize=fontsize)

			plt.scatter(logz,logM,color=colores[col],
				label='Masas de halos entre '+ str(i)+'-'+str(int(i)*10)+' unidades de la simulación' )	
		col+=1	
	
	plot.suptitle('Averages with standar desviation  ', fontsize=fontsize)
	if Subplot==False:
		plt.grid()
		ax.set_ylabel('log($M_{halo}/M_{halo,z=0})$',fontsize=fontsize)
		ax.set_xlabel('log(1+z)',fontsize=fontsize)
		plt.legend()
		plt.savefig('H2/Plots/Averages.png')
	if Subplot==True:
		plt.savefig('H2/Plots/AveragesSubplot.png')
	plt.close()