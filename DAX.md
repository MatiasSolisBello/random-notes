# Formulas DAX

## Medidas vs Columnas
* Las **medidas** son calculos que se aplican en el dashboard
* Las **columnas** se calculan en la tabla, con datos de los atributos.

## Funciones esenciales:
**SUM**

    Ventas totales = SUM('bbdd'\[tabla])

COUNT

    Ventas totales = SUM('bbdd'\[tabla])

**COUNTROWS**
Conteo Ciudades = COUNTROWS(Values('bbdd'\[Ciudad]))

DISTINCTCOUNT
AVERAGE

**CALCULATE**
Ventas Texas = CALCULATE(SUM('bbdd'\[tabla]),'bbdd'\[estado]="Texas")

** IF**
Compra Grande = IF('bbdd'\[ventas]>2500, "Venta Grande", "Venta pequeña")

## Iteradores
SUMX
AVERAGEX
COUNTX

## CALCULATE
FILTER
ALL
ALLEXCEPT

## Time Intelligence
TOTALYTD
SAMEPERIODLASTYEAR
DATEADD


