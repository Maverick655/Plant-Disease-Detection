import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO
from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn
# Load the trained model
MODEL = tf.keras.models.load_model("C:\\Users\\FA0555TX\\Desktop\\Minor Project\\trained_plant_disease_model.keras")


# FastAPI app
app = FastAPI()


# Feature extraction using pre-trained model
def extract_features(image: np.ndarray) -> np.ndarray:
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    features = MODEL.predict(image)  # Extract features
    features = tf.reshape(features, (features.shape[0], -1))  # Flatten features to 1D
    return features
@app.get("/")
async def home():
    return {"message": "Welcome to the Plant Disease Classification API!"}

def read_file_as_image(data: bytes) -> np.ndarray:
    try:
        # Open and resize the image
        image = Image.open(BytesIO(data)).convert("RGB")
        image = image.resize((128, 128))  # Resize image to (128, 128)
        
        # Convert to numpy array and normalize
        image = np.array(image) / 255.0  # Normalize to [0, 1]
        
        # Ensure the image has 3 channels (RGB)
        if image.shape[-1] != 3:
            raise ValueError("Image must have 3 channels (RGB).")
        
        return image
    except Exception as e:
        raise ValueError(f"Error occurred while processing the image: {e}")

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        # Read and preprocess the image
        image = read_file_as_image(await file.read())
        
        # Add batch dimension to image for prediction
        image_batch = np.expand_dims(image, axis=0)  # Shape becomes (1, 128, 128, 3)
        
        # Make the prediction
        predictions = MODEL.predict(image_batch)
        
        # Get the predicted class (highest score index)
        predicted_class = np.argmax(predictions)
        confidence = float(np.max(predictions))

        # Return the result as a dictionary
        return {"predicted_class": int(predicted_class), "confidence": confidence}
    
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)