from keras.models import load_model
from PIL import Image
import numpy as np

# Загрузка модели и словаря классов
model = load_model('black_model.h5')
class_dict = {
    0: 'bishop', 
    1: 'king', 
    2: 'knight', 
    3: 'pawn', 
    4: 'queen', 
    5: 'rook'
}
color_dict = {
    0: 'black',
    1: 'white'
}

def predict_chess_figure(image_path):
    # Загрузка изображения и преобразование в массив numpy
    img = Image.open(image_path)
    img = img.resize((224, 224))
    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    
    # Нормализация данных
    x = x / 255.0
    
    # Получение предсказаний класса и цвета
    preds = model.predict(x)
    class_idx = np.argmax(preds[0])
    color_idx = np.argmax(preds[1])
    
    print(class_idx)
    exit()
    # Возврат имени класса и цвета
    return class_dict[class_idx], color_dict[color_idx]



print(predict_chess_figure('square862.jpg'))