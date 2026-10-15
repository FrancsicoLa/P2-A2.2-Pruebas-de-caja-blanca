# P2 A2.2 Pruebas de caja blanca documentadas

Francisco Hernández Lara · Pruebas de Software

Se conserva la función `process(values)` de P2 A2-1. Las tres funciones de
prueba usan marcadores registrados y `@pytest.mark.parametrize`.

## Preparación

```console
python -m pip install -r requirements.txt
```

## Etapa 1 Sentencias

```console
python -m pytest -m statement -v
python -m pytest -m statement --cov=process --cov-report=term-missing
```

Caso original S1: `[2]` devuelve `["positivo", "par"]`. Resultado: 1 caso
aprobado y 8 de 8 sentencias cubiertas (100 %).

## Etapa 2 Ramas

```console
python -m pytest -m branch -v
python -m pytest -m branch --cov=process --cov-branch --cov-report=term-missing
```

Caso original D1: `[1, -2]` devuelve `["positivo", "par"]`. Ambos `if`
toman sus dos salidas. Resultado: 1 caso aprobado, 8 sentencias y 6 salidas
de ramas cubiertas (100 %). El ciclo `for` aporta dos salidas al reporte.

## Etapa 3 Caminos

```console
python -m pytest -m path -v
python -m pytest -m path --cov=process --cov-branch --cov-report=term-missing
```

Se ejecutan las 16 combinaciones de dos valores con las rutas A (2), B (1),
C (-2) y D (-1), de A-A a D-D. Los resultados esperados están escritos de
forma explícita en los parámetros, sin usar `process` para calcularlos.
Resultado: 16 casos aprobados y 100 % de sentencias y ramas.

`pytest-cov` NO mide directamente cobertura de caminos. Los 16 de 16
caminos se justifican por la enumeración de las combinaciones para listas
de exactamente dos valores. No se afirma cobertura de todos los caminos
para listas de longitud arbitraria.

## Comprobación completa

```console
python -m pytest --cov=process --cov-branch --cov-report=term-missing
```

Resultado: 18 casos aprobados. Python 3.12.14, pytest 9.1.1,
pytest-cov 7.1.0 y coverage 7.16.2.

Se usa `--cov=process` porque el argumento es el nombre del módulo;
el archivo medido aparece como `process.py` en el reporte.
`python -m pytest` equivale a invocar `pytest` con ese intérprete.

## Evidencias e historial

`evidencias/` contiene seis capturas tomadas en Visual Studio Code,
con la salida real de Python y pytest en su consola, y sus registros de
texto. Cada marcador se ejecutó sin cobertura y luego con cobertura.
Se usaron copias de los archivos de cada etapa para conservar la secuencia
de 1, 2 y 18 casos recolectados que corresponde a los tres commits.
Los casos deseleccionados pertenecen a otros marcadores; no son fallos.

El historial contiene tres commits: sentencias, ramas y caminos con la
documentación final. Para revisarlo:

```console
git log --oneline --reverse
```

Repositorio: https://github.com/FrancsicoLa/P2-A2.2-Pruebas-de-caja-blanca
