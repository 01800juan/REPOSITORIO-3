Automatización de Formulario con PyAutoGUI

Descripción

Este script automatiza el llenado de un formulario web utilizando la librería pyautogui en Python. Simula acciones de teclado y ratón para seleccionar opciones, escribir respuestas y enviar el formulario de manera automatizada.

Requisitos

Antes de ejecutar el script, asegúrate de tener instalados los siguientes paquetes:

Python 3.x

pyautogui

Instalación de dependencias

Para instalar pyautogui, usa el siguiente comando:

pip install pyautogui

Uso

Pasos a seguir:

Abre la página web donde se encuentra el formulario que deseas automatizar.

Ajusta la ventana para que los elementos del formulario se ubiquen en las coordenadas esperadas.

Ejecuta el script con el siguiente comando:

python script.py

Funcionamiento del Script

El script selecciona opciones de un formulario en una página web simulando clics y presionando teclas.

Escribe respuestas en los campos de texto.

Usa combinaciones de teclas como AltGr + q para escribir el símbolo @ en direcciones de correo electrónico.

Realiza pausas con time.sleep() para asegurar que las acciones se ejecuten correctamente.

Envía el formulario y repite el proceso para un segundo conjunto de datos.

Consideraciones

Las coordenadas de los clics (x, y) pueden variar dependiendo de la resolución y el zoom de la página. Asegúrate de ajustarlas si es necesario.

No muevas el ratón ni cambies de ventana mientras el script esté en ejecución para evitar interrupciones.

Puede ser necesario ajustar los tiempos de sleep() si la velocidad de carga del formulario varía.
