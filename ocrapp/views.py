from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np

def ocr(request):
    if request.method == 'POST':
        # Get the uploaded image from the request
        image_file = request.FILES['image']
        image = Image.open(image_file).convert('L')
        image = image.resize((28, 28))
        
        # Convert the image to a NumPy array
        image_array = np.array(image) / 255.0
        image_array = np.expand_dims(image_array, axis=0)
        image_array = np.expand_dims(image_array, axis=-1)
        
        # Load the trained model and use it to make a prediction
        model = load_model('model.h5')
        prediction = model.predict(image_array)
        digit = np.argmax(prediction)
        accuracy = round(float(np.max(prediction)), 2)
        
        # Render the result template with the predicted digit and accuracy
        return render(request, 'result.html', {'digit': digit, 'accuracy': accuracy, 'image': image_file})
    else:
        # Render the upload template
        return render(request, 'upload.html')
