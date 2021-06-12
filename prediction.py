import tensorflow.keras as keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from labels import label

model=keras.models.load_model("model.h5")

def recognizer(filename):
    
    img_width, img_height = 224,224

    img = image.load_img(filename, target_size=(img_width, img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    classes = model.predict(x)
    arr = classes[0].tolist()
    
    ind = arr.index(max(arr))
    print(label[ind])
    return (label[ind])

