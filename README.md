# MillenniumSimulation
We present a simulation of the growth of dark matter structure using the Millennium Simulation (based on Springel et al. 2005 paper)

**Nov 28th:**

## Puntos para rematar el pdf (by Luis): 

1. Revisar los puntos de Víctor (por mi parte, libertad absoluta de modificar y re-redactar cualquier línea)
2. Sección IIC. Explicar Figura 5 (las cinco gráficas por separado para cada rango de masa)
2.5 Añadir el cálculo que hiciste para el límite de la masa, que estaba cerca a 10^10. 
3. Rematar la sección II con lo que quieras añadir (ten en cuenta las consideraciones que hace Víctor más abajo)

4. Sección IIIA: añadir algún motivo más por el que cogemos el Rango 4. 
5. Sección IIIB: añadir un comentario más largo sobre la interpretación del las Figuras 7, 8 y 9
6. Esta misma conclusión, añadirla a la conclusión final de la sección IV. 

-1. Borrar todo el Readme, dejándo únicamente las dos primeras líneas (We present...)


## Propuesta de correcciones Víctor a día 28

### Hecho:

1.-@Luis Abalo tu nombre tiene un hipervinvulo a tres correos tuyos. Yo los correos los pondría debajo del nombre o en la cabecera, no en un footenote. Como sugerencia. 

2.- En el **asbtract** se dice que se tiene en cuanta la materia oscura para el estudio de las galaxias, Es solo barionica. Yo cambiaría exceso de color por color directamente. En diferentes bandas fotométricas pondría solo las bandas b y v.

4.- **Procedimiento** La tabla pone M_Crit, falta el 200. Hay una errata en el párrafo 3 de esta seccion nada->dada  Incluiria alguna mencion al codigo desarrollado. Es decir, para el modo H1 se ha seleccionado regiones espaciales de la simulacion sesgadas por un np para su posterior catalogación de halos mediante un programa desarrollado Creo importante que se vea reflejado que hay un programa detrás. redshif nulo-> redshift cero.

5.- **Resultados apartado B**: Para el primer párrafo-> El crecimiento ocurre en un instante de tiempo pero no porque sea fusiones, es porque las simulaciones van discretizadas en tiempo. Por tanto las fusiones estarán dadas por un Delta t.  Creo que el párrafo 2 está mal redactado. *en la verificación de la evolución* no termino de entenderlo ni qué aporta. A lo mejor algo ms sencillo como *con el objetivo de evidenciar la dependencia con la masa en la historia de los halos de materia oscura, se ha presentado la figura 1 a modo de comparacin de las medias de los halos pertenecientes a cada intervalo de masas...* Adems el *.Se calcula la media...* eso no est bien enlazado, ya que se calcula para la figura 1, no desconectado de ella.  El **píe de la figura 1** es confuso.  

Cambiara la frase *si uno se detiene en cada gráfica dentro de la figura 3. * No me convence. 

Reformularía el final del párrafo 4 (pag3) como **Finalmente, en (e), se observa una evolución muy irregular que no se suaviza par redshifts cercanos a 0, algo, que por el contrario, es común al resto de rangos de masa. Esto es una consecuencia de la limitación de la simulacion. Esta variación abrupta de masa se debe a que, como son partículas muy masivas, cuando se define un halo de baja masa, este está dado por pocas partículas, si pierde algunas pocas, ya sea por le modo del conteo dado por el radio del virial o por alguna interacccin, supone mucha prdida de masa. Esto reduce siginifcativamente la posibilidad de una estabilidad en el comportamiento de la curva a redshift cercanos a cero.  **


7-. La figura presenta el promedio de las masas de los halos para los 5 intervalos de mcrtis200. Esta grfica, como se comentaba, refleja un cambio portencual respecto al estado final a redshift 0. Por tanto, para un redhift dado se ve que un cierto halo ha ganado o perdido un cierto porcentaje de su masa final. Cabe esperar que para redshift cercanos al 0, su cambio porcentual sea muy pequeño, es decir, converja al estado final de manera suave. El halo ha llegado a una etapa estable y definida. Si ahora implementamos el concepto de desviacin típica con muchos halos con los que promediar, ésta sera mínima para esta etapa final y máxima para el estado inicial. Esto se debe a que cada halo parte con comportamientos másicos muy distintos. 

Explicado más en detalle: se interpreta la desviacin como la diferencia máxima entre un cambio porcentual de un halo respecto a otro para un redshift determinado. Conforme mayor sea la desviacin, ms distinto son los comportamientos. Los halos ganan o pierden masa de una manera más arbitraria. Si es DM, esto se debe a un intercambio por interaccin gravitatoria. Ahota bien, si la desviación se reduce, los halos cambian de manera similar, estn ms estables, tendrn menos interacciones. 

Con ello se interpreta mejor las graficas, resaltando la mala resolución que se produce en los halos de baja masa, cuya desviacin es grande de manera continuada. 

Nota importante: Si se observa alguna desviacin que es nula comprendida entre dos momentos de desviacin alta a redshift altos, esto se debe a que solo 1 halo con el que se ha promediado lelga a ese redhisft. No quiere decir por tanto, que todos los halos converjan en ese punto, si no que solo hay 1. 

### Por hacer: 

2.- En el **asbtract** no termino de ver que el objetivo principal sea el escrito. 

3.- **Introduccion** El número de particulas y el tamaño de la caja al que se accede es menor creo. Pondría ambas cosas. 

5.- **Resultados apartado B**: Erráta en el párrafo 3. Reexpresaria el final de éste párrafo. El párrafo 4 pisa al párrafo 3, vamos que hay que volverlo a redactar. EN el 3 se comienza a explicar la figura pero en el 4 se explica de nuevo qué es la figura 1. **halos más pequeños o en última instancia partculas, las cuales por ser muy masivas...** Yo quitaría el verbo sustraer y pondría algo ms simple, como *provocando una variación de la masa tan irregular*. De todas formas esta justificación es la que usábamos para los bariones, no para la materia oscura. 

**No se termina de explicar el mecanismo por el cual un halo de DM gana masa, el cual es distinto o sensiblemente distinto al de bariones**

**Se repite mucho la expresión en evidencia** No es bueno usar palabras tan subjetivas, como evidente, es mejor algo tipo *se pone de manifiesto*, *refleja un comportamiento... el cual se puede explicar por* . 

6.- **Resultados apartado C**  : Comentar que los bariones tienen una dinamica distinta

## otras cosas



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

