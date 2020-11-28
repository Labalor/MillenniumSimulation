# MillenniumSimulation
We present a simulation of the growth of dark matter structure using the Millennium Simulation (based on Springel et al. 2005 paper)

**Nov 28th:**

### Propuesta de correcciones Víctor a día 28

1.-@Luis Abalo tu nombre tiene un hipervinvulo a tres correos tuyos. Yo los correos los pondría debajo del nombre o en la cabecera, no en un footenote. Como sugerencia. 
2.- En el asbtract se dice que se tiene en cuanta la materia oscura para el estudio de las galaxias, Es solo barionica. Yo cambiaría exceso de color por color directamente. En diferentes bandas fotométricas pondría solo las bandas b y v. No termino de ver que el objetivo principal sea el escrito. 
3.- Introduccion El número de particulas y el tamaño de la caja al que se accede es menor creo. Pondría ambas cosas. 
4.- Procedimiento La tabla pone M_Crit, falta el 200. Hay una errata en el párrafo 3 de esta seccion nada->dada  Incluiria alguna mencion al codigo desarrollado. Es decir, para el modo H1 se ha seleccionado regiones espaciales de la simulacion sesgadas por un np para su posterior catalogación de halos mediante un programa desarrollado Creo importante que se vea reflejado que hay un programa detrás. redshif nulo-> redshift cero.
5.-





**Tareas pendientes**
.  
-  [ ] **Completar nombres y correos electrónicos**: líneas 13 y 14. 
-  [x] **¿Con cuántas partículas se ha hecho la simulación?** N = 2160^3 (Millennium Simulaition)/ 270^3 (mili.millenium) Pero con misma resolución. hay recorte en espacio.
-  [x] **Dar una explicación:** ¿por qué eliminamos los picos de las figuras de cada rango? [Al final no se elimina para grafcas de mCrit200, pero hay que comentarlo: fala de precisión. Se debe quitar los picos para graficas de masa bariónica]

  **Mi propuesta:** "En las gráficas se observan intervalos de crecimiento negativos, los cuales se deben a las limitaciones de la simulación. Se considera que estos intervalos son periodos en los que el halo no ha experimentado ningún cambio relevante, es decir, no ha sufrido ninguna fusión. Esta circunstancia se explica a través del concepto del radio del virial: un halo pequeño saliendo del radio del virial del halo principal para un SnapNum determinado, dejando así de ser considerado por la simulación, pues el modelo interpreta que no pertenece al halo masivo, restando así su masa. Sin embargo, debido al colapso gravitacional, dicho halo pequeño acaba volviendo a entrar al radio del virial del halo principal adicionando, de nuevo, su masa.
  De esta manera, en la representación gráfica, hay que tener en cuenta que el crecimiento de los halos es debido a fusiones de halos más pequeños. Por lo tanto, dicho crecimiento no ocurre homogéneamente entre dos SnapNum, sino ocurre de manera instantánea." 
  - $$1+z=\dfrac{1}{a}$$, **¿está bien?** O sería $1+z=\dfrac{a}{a_0}$,
  

**Tener en cuenta:**

- La masa está en unidades de 10^{10} masas solares. Siendo M_p 8.61 x 10^8 M sol/h. 1+z el factor de expansin del universo relativo al presente.
- La masa del bulbo es fundamentalmente la masa estelar, o casi ella. Para halos sin masa en el bulbo: posiblemente no tenga suficiente resolucin para que exista o bien para que identifique uno. 
- Las figuras de la Seccion 2 se nombran de la siguiente manera: 
   1) average 
   2) average 
   3) DM 
   4) DM_dev
   5) baryon
   6) baryon_dev

**Sugerencias:**

- [x] Poner el eje y con esta notacion: $\dfrac{M(z)}{M_0}$, donde M(z) es la masa crítica a un redshift determinado, y M_0 es la masa crítica a redshift nulo. 
**Sobre el título y leyenda de gráficos**
- [x] No poner título ni leyenda a las gráficas cuando las generamos con Python. Si nos fijamos en los artículos científicos, con el caption de la figura es suficiente. 
- Sin embargo, ¡¡¡podemos generar estas gráficas con título y leyenda para la presentación!!!

