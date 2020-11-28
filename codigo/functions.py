from Packages import *

##################################################################################################################################


def Load(folder,Head,HEAD):
	buf=[]
	Buf={}
	for out in listdir('./'+folder):
		buf.append(out)
		if HEAD==True:
			Buf[str(out)[0:-4]]=pd.read_csv(folder+'/'+str(out),names=Head)
			Buf[str(out)[0:-4]].head()

		else:
			Buf[str(out)[0:-4]]=pd.read_csv(folder+'/'+str(out))
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
	Value_suptitle=9
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
			plot.suptitle('Dark Matter Halo Tree. m_Crit200 [M$_\odot$/h]: 0-10$^{10}$', fontsize=25)
		if int(i)==1000:
			plot.suptitle('Dark Matter Halo Tree. m_Crit200 [M$_\odot$/h]: 10$^{13}$-$\infty$', fontsize=25)
		if int(i)!=0 and int(i)!=1000:
			plot.suptitle('Dark Matter Halo Tree. m_Crit200 [M$_\odot$/h]: 10$^{'+str(Value_suptitle) +'}$-10$^{'+str(Value_suptitle+1)+'}$', fontsize=25)
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
				label='Masas de halos entre 0-10$^{10} M_\odot/h$ ' )
		if int(i)==1000:
			if Subplot==True:
				plt.errorbar(logz,logM,logStev,linestyle='None', capsize=5,ecolor=colores[col] )
			plt.scatter(logz,logM,c=colores[col],
				label='Masas de halos a partir de 10$^{13} M_\odot/h$' )			
		if int(i)!=1000 and int(i)!=0:
			if Subplot==True:
				plt.errorbar(logz,logM,logStev,linestyle='None', capsize=5,ecolor=colores[col] )	
				if col==3:
					ax.set_ylabel('log($M_{halo}/M_{halo,z=0})$',fontsize=fontsize)

			plt.scatter(logz,logM,color=colores[col],
				label='Masas de halos entre  10$^{'+str(9+col)+'}$-10$^{'+str(col+10)+'}$ M$_\odot$/h' )	
		col+=1	
	if Subplot==True:
		plot.suptitle('Dark Matter Halos. Averages of mass evolution & standar desviation.  ', fontsize=fontsize)
	if Subplot==False:
		plot.suptitle('Dark Matter Halos. Averages of mass evolution',fontsize=fontsize)
	if Subplot==False:
		plt.grid()
		ax.set_ylabel('log($M_{halo}/M_{halo,z=0})$',fontsize=fontsize)
		ax.set_xlabel('log(1+z)',fontsize=fontsize)
		plt.legend()
		plt.savefig('H2/Plots/Averages.png')
	if Subplot==True:
		plt.savefig('H2/Plots/AveragesSubplot.png')

	plt.close()

def PlotBaryonMassTree(G2csv,limits,Value_suptitle=9):

	for i in limits:
		plot=plt.figure(figsize=(13.0, 10.0))
		ax=plot.add_subplot(111)
		for j in G2csv.keys():
			if  str(i)==((str(j)[0:-2])[1:]):
				MassArray=np.array(G2csv[j]['coldGas'])+np.array(G2csv[j]['stellarMass'])+np.array(G2csv[j]['hotGas'])
				logM=np.log10(MassArray/MassArray[0])
				logz=np.log10(1+np.array(G2csv[j]['redshift']))
				conbuf=0
				for k in G2csv[j]['firstProgenitorId']:
					if int(k)==-1:
						break
					conbuf+=1

				plt.plot(logz[0:conbuf],logM[0:conbuf])		
		ax.set_ylabel('log($M_{Baryon}/M_{Baryon,z=0})$',fontsize=25)
		ax.set_xlabel('log(1+z)',fontsize=25)
		if int(i)==0:
			plot.suptitle('Baryon Mass Halo Tree. m_Crit200 [M$_\odot$/h]: 0-10$^{10}$', fontsize=25)
		if int(i)==1000:
			plot.suptitle('Baryon Mass  Halo Tree. m_Crit200 [M$_\odot$/h]: 10$^{13}$-$\infty$', fontsize=25)
		if int(i)!=0 and int(i)!=1000:
			plot.suptitle('Baryon Mass  Halo Tree. m_Crit200 [M$_\odot$/h]: 10$^{'+str(Value_suptitle) +'}$-10$^{'+str(Value_suptitle+1)+'}$', fontsize=25)
		Value_suptitle+=1
		plt.grid()
		plt.savefig('G2/Plots/Baryon_'+str(i))
		plt.close()

def AveragesModBaryon(G2csv,limits):
	BufAverages={}
	Bufstdev={}
	BufRedshift={}
	for i in limits:
		bufmatter={}
		bufredshift=[]
		firstLoop=False
		for j in G2csv.keys():
			if  str(i)==((str(j)[0:-2])[1:]):
				for k,p in zip(np.array(G2csv[j]['redshift']),range(len(np.array(G2csv[j]['redshift'])))) :
					if int(np.array(G2csv[j]['firstProgenitorId'])[p])==-1:
						break
					else:
						if firstLoop==False:
							up=np.array(G2csv[j]['coldGas'])[p]+np.array(G2csv[j]['stellarMass'])[p]+np.array(G2csv[j]['hotGas'])[p]
							down=np.array(G2csv[j]['coldGas'])[0]+np.array(G2csv[j]['stellarMass'])[0]+np.array(G2csv[j]['hotGas'])[0]

							bufmatter[k]=up/down
							bufredshift.append([k])
						else:
							try:
								up=np.array(G2csv[j]['coldGas'])[p]+np.array(G2csv[j]['stellarMass'])[p]+np.array(G2csv[j]['hotGas'])[p]
								down=np.array(G2csv[j]['coldGas'])[0]+np.array(G2csv[j]['stellarMass'])[0]+np.array(G2csv[j]['hotGas'])[0]

								bufmatter[k]=np.append(np.array(bufmatter[k]),up/down)
							except KeyError:
								up=np.array(G2csv[j]['coldGas'])[p]+np.array(G2csv[j]['stellarMass'])[p]+np.array(G2csv[j]['hotGas'])[p]
								down=np.array(G2csv[j]['coldGas'])[0]+np.array(G2csv[j]['stellarMass'])[0]+np.array(G2csv[j]['hotGas'])[0]



								bufmatter[k]=up/down
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



def BaryonPlotAverages(Average,Redshift,Stdev,Subplot):
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
				ax.set_ylabel('log($M_{baryon}/M_{baryon,z=0})$',fontsize=fontsize)

			plt.scatter(logz,logM,c=colores[col],
				label='Masas barionicas de halos entre 0-10$^{10} M_\odot/h$ ' )
		if int(i)==1000:
			if Subplot==True:
				plt.errorbar(logz,logM,logStev,linestyle='None', capsize=5,ecolor=colores[col] )
			plt.scatter(logz,logM,c=colores[col],
				label='Masas barionicas de halos a partir de 10$^{13} M_\odot/h$' )			
		if int(i)!=1000 and int(i)!=0:
			if Subplot==True:
				plt.errorbar(logz,logM,logStev,linestyle='None', capsize=5,ecolor=colores[col] )	
				if col==3:
					ax.set_ylabel('log($M_{baryon}/M_{baryon,z=0})$',fontsize=fontsize)

			plt.scatter(logz,logM,color=colores[col],
				label='Masas barionicas de halos entre  10$^{'+str(9+col)+'}$-10$^{'+str(col+10)+'}$ M$_\odot$/h' )	
		col+=1	
	if Subplot==True:
		plot.suptitle('Baryon Mass Halos. Averages of mass evolution & standar desviation.  ', fontsize=fontsize)
	if Subplot==False:
		plot.suptitle('Baryon Mass Halos. Averages of mass evolution',fontsize=fontsize)
	if Subplot==False:
		plt.grid()
		ax.set_ylabel('log($M_{Baryon}/M_{Baryon,z=0})$',fontsize=fontsize)
		ax.set_xlabel('log(1+z)',fontsize=fontsize)
		plt.legend()
		plt.savefig('G2/Plots/Averages.png')
	if Subplot==True:
		plt.savefig('G2/Plots/AveragesSubplot.png')

	plt.close()





def Filtromagnitud(G2cs,progenitor):
	delimitadores=[];count=0
	Paquetes={}
	for i in range(len(progenitor)):
		if progenitor[i]==-1:
			delimitadores.append([]);
			delimitadores[count]=i;count+=1

	delimitadores=np.array(delimitadores);
	for i in range(len(delimitadores)):
		if i==0:
			Paquetes[i]=G2cs[0:delimitadores[i]+1]
		if i!=0 and i!=(len(delimitadores)-1):
			Paquetes[i]=G2cs[delimitadores[i-1]+1:delimitadores[i]+1]
		if i==(len(delimitadores)-1):
			Paquetes[i]=G2cs[delimitadores[i-1]+1:]
	for i in range(len(delimitadores)):
		Paquetes[i]=Paquetes[i][Paquetes[i]['mag_b']!=99 ] 
	return(Paquetes,delimitadores)



def PlotArbolFusion(Data,delimitadores,magnitude,key,AllData):

	cm1 = mcol.LinearSegmentedColormap.from_list("Mag_b-v",["b","r"])
	cnorm = mcol.Normalize(vmax=max(magnitude),vmin=min(magnitude))
	cpick = cm.ScalarMappable(norm=cnorm,cmap=cm1)
	cpick.set_array([])
	fig, ax = plt.subplots(figsize=(12,8))

	for i in range(len(delimitadores)):
		Masa=np.array(Data[i]['coldGas'])+np.array(Data[i]['stellarMass'])+np.array(Data[i]['hotGas'])
		for j, J in zip(magnitude,range(len(magnitude))):
			for k in range(len(Data[i]['galaxyID'])):
				if j==(np.array(Data[i]['mag_b'])[k]-np.array(Data[i]['mag_v'])[k]):
					if k==0 and i>0:
						plt.plot(np.array(Data[i]['lastProgenitorId'])[k],np.array(Data[i]['snapnum'])[k],'o',linestyle='solid',linewidth=50,color=cpick.to_rgba(j),markersize=Masa[k]*2,markeredgecolor='black',alpha=0.8)
						try:
							limitex=np.array(Data[0][Data[0]['galaxyID']==np.int(np.array(Data[i]['descendantId'])[k]) ]['lastProgenitorId'] )
							plt.plot([np.array(Data[i]['lastProgenitorId'])[k],limitex],[np.array(Data[i]['snapnum'])[k],np.array(Data[0][Data[0]['galaxyID']==np.int(np.array(Data[i]['descendantId'])[k]) ]['snapnum'] )],'-',linestyle='solid',linewidth=1.5,color=cpick.to_rgba(j),alpha=0.8)
						except:
							plt.plot([np.array(Data[i]['lastProgenitorId'])[k],np.array(Data[i]['lastProgenitorId'])[k]],[np.array(Data[i]['snapnum'])[k],np.array(AllData[AllData['galaxyID']==np.int(np.array(Data[i]['descendantId'])[k]) ]['snapnum'] )],'-',linestyle='solid',linewidth=1.5,color=cpick.to_rgba(j),alpha=0.8)
					if k==(len(Data[i]['galaxyID'])-1):
						plt.plot(np.array(Data[i]['lastProgenitorId'])[k],np.array(Data[i]['snapnum'])[k],'o',linestyle='solid',linewidth=50,color=cpick.to_rgba(j),
							markersize=Masa[k]*2,markeredgecolor='black',alpha=0.8)
						plt.plot([np.array(Data[i]['lastProgenitorId'])[k],np.array(Data[i]['lastProgenitorId'])[k]],[np.array(Data[i]['snapnum'])[k],np.array(AllData[AllData['galaxyID']==np.int(np.array(Data[i]['descendantId'])[k]) ]['snapnum'] )],'-',linestyle='solid',linewidth=1.5,color=cpick.to_rgba(j),alpha=0.8)

					if k!=0:
						plt.plot([np.array(Data[i]['lastProgenitorId'])[k-1],np.array(Data[i]['lastProgenitorId'])[k]],[np.array(Data[i]['snapnum'])[k-1],np.array(Data[i]['snapnum'])[k]],'-',linestyle='solid',linewidth=1.5,color=cpick.to_rgba(j),alpha=0.8)

						plt.plot(np.array(Data[i]['lastProgenitorId'])[k],np.array(Data[i]['snapnum'])[k],'o',linestyle='solid',linewidth=50,color=cpick.to_rgba(j),
							markersize=Masa[k]*2,markeredgecolor='black',alpha=0.8)

	ax.set_ylim( min(np.array(Data[0]['snapnum']))-1,max(np.array(Data[0]['snapnum']))+2) 
	ax.set_ylabel('snapnum',fontsize=20)	
	#pylab.rcParams['ytick.major.pad']='0.5'
			
	plt.colorbar(cpick,label="B-V")
	mng = plt.get_current_fig_manager();mng.resize(*mng.window.maxsize())
	plt.savefig('G2/Plots/FussionTree_'+str(key)+'.png')
	plt.close()
	for i in range(len(delimitadores)):
		Masa=np.array(Data[i]['coldGas'])+np.array(Data[i]['stellarMass'])+np.array(Data[i]['hotGas'])
		for j in magnitude:
			for k in range(len(Data[i]['galaxyID'])):
				if j==(np.array(Data[i]['mag_b'])[k]-np.array(Data[i]['mag_v'])[k]):
					if np.array(Data[i]['firstProgenitorId'])[k]==-1:
						
						plt.plot(np.array(Data[i]['x'])[k],np.array(Data[i]['snapnum'])[k],'o-',linestyle='solid',linewidth=50,color=cpick.to_rgba(j),
							markeredgecolor='black',alpha=0.5)
					else:
						plt.plot(np.array(Data[i]['x'])[k],np.array(Data[i]['snapnum'])[k],'o-',linestyle='solid',linewidth=50,color=cpick.to_rgba(j),
							markeredgecolor='black',alpha=0.5)
	ax.set_ylim( min(np.array(Data[i]['snapnum'])-5),max(np.array(Data[i]['snapnum']))+9) 
	ax.set_ylabel('Redshift',fontsize=20)				
	plt.colorbar(cpick,label="B-V")
	mng = plt.get_current_fig_manager();mng.resize(*mng.window.maxsize())
	plt.savefig('G2/Plots/FussionTree2_'+str(key)+'.png')
	plt.close()
	figCM= plt.figure(figsize=(13.0, 10.0))
	ax=figCM.add_subplot(111,projection='3d')
	for i in range(len(delimitadores)):
		Masa=np.array(Data[i]['coldGas'])+np.array(Data[i]['stellarMass'])+np.array(Data[i]['hotGas'])
		for j in magnitude:
			for k in range(len(Data[i]['galaxyID'])):
				if j==(np.array(Data[i]['mag_b'])[k]-np.array(Data[i]['mag_v'])[k]):
					if np.array(Data[i]['firstProgenitorId'])[k]==-1:
						
						ax.scatter(np.array(Data[i]['x'])[k],np.array(Data[i]['y'])[k],np.array(Data[i]['redshift'])[k],'o',color=cpick.to_rgba(j),
							alpha=0.8)
					else:
						ax.scatter(np.array(Data[i]['x'])[k],np.array(Data[i]['y'])[k],np.array(Data[i]['redshift'])[k],'o',color=cpick.to_rgba(j),
							alpha=0.8)
	ax.set_xlabel('X')
	ax.set_ylabel('Y')
	ax.set_zlabel('redshift')
	ax.view_init(elev=25, azim=70);
	plt.savefig('G2/Plots/FussionTree3_'+str(key)+'.png')
	plt.close()







