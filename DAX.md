# Formulas DAX

## Medidas vs Columnas
* Las **medidas** son calculos que se aplican en el dashboard (ontexto de filtro)

* Las **columnas** se calculan en la tabla, con datos de los atributos.

## Funciones esenciales:

**SUM:** Solo suma una columna

    Ventas totales = SUM(Ventas[Monto])

Cuándo usarlo:
* Cuando ya tienes el valor calculado en una columna
* Cuando NO necesitas hacer operaciones fila por fila

Error típico:
* Intentar hacer cálculos dentro → no funciona.


**SUMX:** Evalúa una expresión fila por fila
    
    SUMX(Ventas, Ventas[Precio] * Ventas[Cantidad])

Cuándo usarlo:
* Cuando necesitas multiplicar, dividir, etc.
* Cuando no tienes una columna ya calculada

Mentalidad:
“Necesito pensar fila por fila” → SUMX

**COUNT**
Cuenta valores NO vacíos en una columna    

    COUNT(Ventas[Cliente])

**COUNTROWS**
Cuenta filas de una tabla. Ej: Quieres saber cantidad de registros

    Conteo Ciudades = COUNTROWS(Values('bbdd'\[Ciudad]))

**DISTINCTCOUNT:** 
Cuenta valores únicos. Ej: Cuenta valores únicos

    DISTINCTCOUNT(Ventas[Cliente])

**AVERAGE**

**CALCULATE**

Se compone de 'CALCULATE(Expresión, filtro)' Donde expresión es la combinacion de funciones para realizar calculo

Ejemplo 1: 

    Ventas Texas = CALCULATE(SUM('bbdd'[tabla]),'bbdd'[estado]="Texas")

Ejemplo 2:

    Ventas Grandes =
    CALCULATE(
        SUM(Ventas[Monto]),
        FILTER(Ventas, Ventas[Monto] > 1000)
    )


**IF**
Shift + Enter para bajar

Ejemplo 1:
    Clasificación =
    IF(
        Ventas[Monto] > 2500,
        "Alta",
        IF(Ventas[Monto] > 1000, "Media", "Baja")
    )

Ejemplo 2:

    Tipo Venta =
    IF(Ventas[Monto] > 1000, "Alta", "Baja")

## Iteradores

Son funciones que recorren tabla fila por fila.

**AVERAGEX:** Promedio de una expresión

    Promedio Venta =
    AVERAGEX(Ventas, Ventas[Precio] * Ventas[Cantidad])


**COUNTX:** Cuenta resultados de una expresión

    Conteo =
    COUNTX(Ventas, Ventas[Precio] * Ventas[Cantidad])

## CALCULATE
Cambia el contexto de filtro

**FILTER**
Devuelve una tabla filtrada

Cuándo usarlo:
* Filtros complejos (más de una condición)
* Condiciones dinámicas

Error típico:
* Usarlo cuando puedes usar filtros simples → más lento

    Ventas Altas =
    CALCULATE(
        SUM(Ventas[Monto]),
        FILTER(Ventas, Ventas[Monto] > 1000)
    )

**ALL**

Ignora los filtros

Cuándo usarlo:
* % del total
* Comparaciones contra total general

    Ventas Totales Global =
    CALCULATE(SUM(Ventas[Monto]), ALL(Ventas))


**ALLEXCEPT**
Quita todos los filtros excepto algunos

    Ventas por Región =
    CALCULATE(
        SUM(Ventas[Monto]),
        ALLEXCEPT(Ventas, Ventas[Region])
    )

## Time Intelligence

**TOTALYTD:** Acumulado del año. Ej: Comparaciones año vs año

    Ventas YTD =
    TOTALYTD(SUM(Ventas[Monto]), Calendario[Fecha])

**SAMEPERIODLASTYEAR:** Mismo periodo año anterior

    Ventas Año Pasado =
    CALCULATE(
        SUM(Ventas[Monto]),
        SAMEPERIODLASTYEAR(Calendario[Fecha])
    )

**DATEADD:** Mover fechas

    Ventas Mes Anterior =
    CALCULATE(
        SUM(Ventas[Monto]),
        DATEADD(Calendario[Fecha], -1, MONTH)
    )
