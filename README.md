# mi-calculadora-python
Script básico de calculadora en Python (Semana 1)

## Verificación local

Ejercicio de aprendizaje con funciones importables, validación de entrada y pruebas sin dependencias externas.

```powershell
python -X utf8 mi-calculadora-python.py
python -X utf8 -m unittest discover -v
```

La entrada inválida devuelve código de salida 1 sin traceback. Las pruebas verifican límites y la consola.

La división por cero se indica como no definida; no se representa como infinito.

## Validación automática

GitHub Actions ejecuta las pruebas de regresión offline y la compilación de fuentes en Python 3.13 y 3.14 para cada PR y cambio en main. El workflow usa permisos de lectura y acciones fijadas por SHA. No instala dependencias ni inicia servidores.
