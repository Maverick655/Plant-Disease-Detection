import React, { useState } from 'react';
import { View, Text, Button, Image } from 'react-native';
import { launchCamera } from 'react-native-image-picker';
import axios from 'axios';

export default function App() {
  const [imageUri, setImageUri] = useState(null);
  const [prediction, setPrediction] = useState(null);

  const captureImage = () => {
    launchCamera({
      mediaType: 'photo',
      includeBase64: true, // to send image as base64 string if needed
    }, response => {
      if (response.assets && response.assets.length > 0) {
        setImageUri(response.assets[0].uri);
        sendImageToBackend(response.assets[0].uri);
      }
    });
  };

  const sendImageToBackend = async (uri) => {
    const formData = new FormData();
    formData.append('file', {
      uri: uri,
      type: 'image/jpeg', // Adjust according to the image type
      name: 'plant.jpg',
    });

    try {
      const response = await axios.post('http://<YOUR_BACKEND_URL>/predict/', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setPrediction(response.data.prediction);
    } catch (error) {
      console.error(error);
      setPrediction("Error occurred");
    }
  };

  return (
    <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center' }}>
      <Button title="Capture Image" onPress={captureImage} />
      {imageUri && <Image source={{ uri: imageUri }} style={{ width: 200, height: 200 }} />}
      {prediction !== null && <Text>Predicted Class: {prediction}</Text>}
    </View>
  );
}
