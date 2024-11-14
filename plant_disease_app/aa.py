import tensorflow as tf
import numpy as np
from PIL import Image

model_path = r"C:/Users/FA0555TX/Desktop/Minor Project/trained_plant_disease_model.keras"
model = tf.keras.models.load_model(model_path)

def model_prediction(test_image_path):
    # Load and preprocess image
    image = tf.keras.preprocessing.image.load_img(test_image_path, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])   # Normalize to [0, 1]
    
    # Predict
    predictions = model.predict(input_arr)
    predicted_index = np.argmax(predictions)
    
    # Class names
    class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                  'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                  'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                  'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                  'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                  'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                  'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                  'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                  'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                  'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                  'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                  'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                  'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                  'Tomato___healthy']
    
    # Return predicted class
    return class_name[predicted_index]

# Test with an image path
result = model_prediction("C:\\Users\\FA0555TX\\Downloads\\New Plant Diseases Dataset(Augmented)\\New Plant Diseases Dataset(Augmented)\\valid\\Potato___healthy\\3edf7c3f-73e0-439c-870d-76cfd7c3bc45___RS_HL 1859.JPG")
print("Prediction Result:", result)
