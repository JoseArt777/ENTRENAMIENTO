# ENTRENAMIENTO – Clasificador de Imágenes en Tiempo Real con Python y TensorFlow

## Descripción del Proyecto

El proyecto **ENTRENAMIENTO** consiste en el desarrollo de un clasificador de imágenes en tiempo real utilizando Python, TensorFlow y OpenCV. La aplicación está diseñada para reconocer objetos o categorías visuales a través de la cámara web, mostrando en pantalla la predicción junto con el nivel de confianza. Este sistema facilita la automatización y el análisis visual en escenarios de entrenamiento y pruebas de modelos de machine learning.

## Características Principales

- Carga y uso de modelos entrenados en Keras/TensorFlow.
- Predicción de clase y nivel de confianza en tiempo real desde la cámara.
- Visualización directa de resultados sobre el video.
- Preprocesamiento automatizado de imágenes capturadas.
- Interfaz sencilla y orientada a practicidad en laboratorio.

## Tecnologías Utilizadas

- **Lenguaje Principal:** Python
- **Framework:** TensorFlow (Keras)
- **Librerías:** OpenCV, NumPy
- **Base de datos:** Archivos de modelo y etiquetas locales (`h5`, `txt`)
- **Entorno de ejecución recomendado:** Python 3.x

## Requisitos Previos

- Python 3 instalado.
- Instalar las dependencias:
  ```bash
  pip install tensorflow opencv-python numpy
  ```
- Cámara web funcional conectada al equipo.
- Modelo preentrenado (`modelo/keras_model.h5`) y archivo de etiquetas (`modelo/labels.txt`).

## Instrucciones de Instalación y Ejecución

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/JoseArt777/ENTRENAMIENTO.git
   ```
2. **Instala los requerimientos**
   ```bash
   pip install tensorflow opencv-python numpy
   ```
3. **Verifica los archivos del modelo**
   - Ubica `keras_model.h5` y `labels.txt` en la carpeta `modelo/`.
4. **Ejecuta el sistema**
   ```bash
   python tu_codigo.py
   ```
5. **Presiona 'q' para salir de la visualización en tiempo real.**

## Estructura del Proyecto

- `tu_codigo.py`: Código principal de detección y visualización en tiempo real.
- `modelo/keras_model.h5`: Archivo de modelo entrenado (necesario para la predicción).
- `modelo/labels.txt`: Etiquetas de las clases a predecir.
- Otros archivos/recursos pueden estar dedicados a pruebas y entrenamiento.

## Endpoints

Este proyecto no expone endpoints, ya que se trata de una aplicación de escritorio para clasificación visual en tiempo real.

## Capturas o Ejemplos de Uso

```python
# Fragmento de código para predicción y visualización
prediction = model.predict(img)
predicted_index = np.argmax(prediction)
label = labels[predicted_index]
confidence = prediction[0][predicted_index]
cv2.putText(frame, f'{label} ({confidence:.2f})', (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow("Clasificador en vivo", frame)
```

## Buenas Prácticas Implementadas

- Separación clara entre carga de modelo, preprocesamiento y predicción.
- Gestión eficiente de recursos (liberación de la cámara y ventanas).
- Uso de convenciones estándar de Python y documentación básica.
- Simplicidad en la ejecución y portabilidad del entorno.

## Aprendizajes Obtenidos

Este proyecto permitió aplicar conceptos de machine learning, manejo de imágenes y procesamiento en tiempo real, así como integrar diferentes librerías de alto nivel en Python. Se reforzaron habilidades de desarrollo en TensorFlow y OpenCV, con especial énfasis en la implementación de sistemas prácticos de inteligencia artificial.

## Posibles Mejoras Futuras

- Integrar interfaz gráfica adicional para gestión de modelos y visualización avanzada.
- Optimizar el preprocesamiento para diversas resoluciones y tipos de cámara.
- Ajustar el sistema para detección en múltiples frames y categorías simultáneas.
- Implementar soporte para modelos remotos y actualización dinámica de etiquetas.
- Agregar reportes automáticos y almacenamiento de resultados.

---
Para más detalles y actualización de archivos visita el [repositorio en GitHub](https://github.com/JoseArt777/ENTRENAMIENTO).
