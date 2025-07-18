import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        print(">>> Prediction started")

        # ✅ Corrected model path (you are using model/model.h5)
        model_path = os.path.join("model", "model.h5")
        print(f"Loading model from: {model_path}")

        # ✅ Skip loading training configs like loss/optimizer
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model file not found at: {model_path}")
        model = load_model(model_path, compile=False)

        # ✅ Load and preprocess image
        imagename = self.filename
        print(f"Loading image from: {imagename}")
        if not os.path.exists(imagename):
            raise FileNotFoundError(f"Image file not found at: {imagename}")

        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        print("Running model prediction...")
        result = np.argmax(model.predict(test_image), axis=1)
        print("Prediction result:", result)

        if result[0] == 1:
            prediction = 'Normal'
        else:
            prediction = 'Adenocarcinoma Cancer'

        print("Prediction completed:", prediction)
        return [{"image": prediction}]
