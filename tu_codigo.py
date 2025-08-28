import tensorflow as tf
import numpy as np
import cv2

# Cargar modelo y etiquetas
model = tf.keras.models.load_model('modelo/keras_model.h5')
with open("modelo/labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]

# Dirección del stream de DroidCam

# Captura de la cámara
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("No se pudo abrir la cámara. Verifica la IP y puerto.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo leer el frame.")
        break

    # Preprocesar la imagen
    img = cv2.resize(frame, (224, 224))
    img = img.astype(np.float32) / 255.0
    img = np.expand_dims(img, axis=0)

    # Predicción
    prediction = model.predict(img)
    predicted_index = np.argmax(prediction)
    label = labels[predicted_index]
    confidence = prediction[0][predicted_index]

    # Mostrar resultados
    cv2.putText(frame, f'{label} ({confidence:.2f})', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Clasificador en vivo", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
