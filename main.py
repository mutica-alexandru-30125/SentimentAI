from data_loader import DataLoader
from preprocessor import Preprocessor
from emotion_model import EmotionModel
from emotion_gui import EmotionGUI
from sklearn.preprocessing import LabelEncoder

# 1. Încărcarea datelor
data_loader = DataLoader()
train_data, train_labels = data_loader.load_data('train.txt')
test_data, test_labels = data_loader.load_data('test.txt')
val_data, val_labels = data_loader.load_data('val.txt')

# 2. Preprocesarea datelor
label_encoder = LabelEncoder()
train_labels_enc = label_encoder.fit_transform(train_labels)
test_labels_enc = label_encoder.transform(test_labels)
val_labels_enc = label_encoder.transform(val_labels)

preprocessor = Preprocessor()
preprocessor.fit(train_data)
train_padded = preprocessor.transform(train_data)
test_padded = preprocessor.transform(test_data)
val_padded = preprocessor.transform(val_data)

# 3. Construirea și antrenarea modelului
emotion_model = EmotionModel(num_classes=len(label_encoder.classes_), max_length=50)
emotion_model.train(train_padded, train_labels_enc, val_padded, val_labels_enc)

# 4. Evaluarea modelului
emotion_model.evaluate(test_padded, test_labels_enc)

# 5. Lansarea interfeței grafice
gui = EmotionGUI(emotion_model, preprocessor, label_encoder)
gui.launch()
