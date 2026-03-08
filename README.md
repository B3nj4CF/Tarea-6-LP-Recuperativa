# Tarea 6 - Lenguajes de Programación (Recuperativa)

Este proyecto implementa un sistema de modelado de figuras geométricas combinando tres paradigmas de programación: **Orientado a Objetos**, **Funcional** y **Lógico**.

## Características

El código define jerarquías de figuras geométricas y resuelve cálculos de propiedades físicas mediante funciones lambda, mientras utiliza lógica formal para categorizar las capacidades de cada figura.

### 1. Programación Orientada a Objetos (POO)
Se definen clases base y derivadas para organizar las figuras:
* **Figuras Planas:** `Cuadrado` y `Triangulo`.
* **Figuras Espaciales:** `Esfera` (No Poliedro) y `Cubo` (Poliedro).

### 2. Programación Funcional
Dentro de los métodos de cada clase, los cálculos de **área, perímetro, superficie y volumen** están implementados mediante expresiones `lambda`. 
* *Nota:* Para ejecutar el cálculo, se utiliza una doble llamada: `objeto.metodo()(parametros)`.

### 3. Programación Lógica (pyDatalog)
Se utiliza la librería `pyDatalog` para establecer relaciones y reglas lógicas:
* **Hechos:** Define qué es cada figura (ej. un Cuadrado es una Figura Plana).
* **Reglas:** Determina qué atributos posee una figura según su tipo (ej. si es Figura Plana, tiene área y perímetro).

## Requisitos
* Python 3.x
* Librería `pyDatalog`

## Ejemplo de Uso
El script incluye pruebas que imprimen los cálculos físicos y realizan consultas lógicas para verificar si una figura posee ciertos atributos (como área o volumen) basándose en las reglas definidas.

---
**Autor:** Benjamin Campos Fernandez  
**Rol:** 202473094-0
