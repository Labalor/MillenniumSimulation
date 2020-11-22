# MillenniumSimulation
We present a simulation of the growth of dark matter structure using the Millennium Simulation (based on Springel et al. 2005 paper)

**Nov 9th:**

**Tareas pendientes**
.  
-  [ ] **Completar nombres y correos electrónicos**: líneas 13 y 14. 
-  [x] **¿Con cuántas partículas se ha hecho la simulación?** N = 2160^3 (Millennium Simulaition)
-  [ ] **Dar una explicación:** ¿por qué eliminamos los picos de las figuras de cada rango? [Al final no se elimina, pero hay que comentarlo: fala de precisión]
  **Mi propuesta:** "En las gráficas se observan intervalos de crecimiento negativos, los cuales se deben a las limitaciones de la simulación. Se considera que estos intervalos son periodos en los que el halo no ha experimentado ningún cambio relevante, es decir, no ha sufrido ninguna fusión. Esta circunstancia se explica a través del concepto del radio del virial: un halo pequeño saliendo del radio del virial del halo principal para un SnapNum determinado, dejando así de ser considerado por la simulación, pues el modelo interpreta que no pertenece al halo masivo, restando así su masa. Sin embargo, debido al colapso gravitacional, dicho halo pequeño acaba volviendo a entrar al radio del virial del halo principal adicionando, de nuevo, su masa.
  De esta manera, en la representación gráfica, hay que tener en cuenta que el crecimiento de los halos es debido a fusiones de halos más pequeños. Por lo tanto, dicho crecimiento no ocurre homogéneamente entre dos SnapNum, sino ocurre de manera instantánea." 
  - $$1+z=\dfrac{1}{a}$$, **¿está bien?** O sería $1+z=\dfrac{a}{a_0}$,
  

**Tener en cuenta:**

- La masa está en unidades de 10^{10} masas solares. 

**Sugerencias:**

- [x] Poner el eje y con esta notacion: $\dfrac{M(z)}{M_0}$, donde M(z) es la masa crítica a un redshift determinado, y M_0 es la masa crítica a redshift nulo. 
**Sobre el título y leyenda de gráficos**
- [x] No poner título ni leyenda a las gráficas cuando las generamos con Python. Si nos fijamos en los artículos científicos, con el caption de la figura es suficiente. 
- Sin embargo, ¡¡¡podemos generar estas gráficas con título y leyenda para la presentación!!!

