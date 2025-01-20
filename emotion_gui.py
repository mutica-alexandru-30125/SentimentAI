from tkinter import Tk, Label, Text, Button, Scrollbar, END

class EmotionGUI:
    def __init__(self, model, preprocessor, label_encoder):
        self.model = model
        self.preprocessor = preprocessor
        self.label_encoder = label_encoder
        self.colors = {
            'joy': 'green',
            'sadness': 'blue',
            'anger': 'red',
            'fear': 'purple',
            'love': 'pink',
            'surprise': 'orange'
        }

    def launch(self):
        self.root = Tk()
        self.root.title("Emotion Detector")

        Label(self.root, text="Enter text:").grid(row=0, column=0, padx=10, pady=10)

        self.text_area = Text(self.root, width=60, height=15, wrap='word')
        self.text_area.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        scrollbar = Scrollbar(self.root, command=self.text_area.yview)
        self.text_area['yscrollcommand'] = scrollbar.set
        scrollbar.grid(row=1, column=2, sticky='ns')

        Button(self.root, text="Analyze Emotions", command=self.predict_emotions).grid(row=2, column=0, columnspan=2, pady=10)

        self.result_area = Text(self.root, width=60, height=15, wrap='word', state='disabled')
        self.result_area.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.root.mainloop()

    def predict_emotions(self):
        input_text = self.text_area.get("1.0", END).strip()
        sentences = input_text.split('.')
        self.result_area.config(state='normal')
        self.result_area.delete("1.0", END)

        for sentence in sentences:
            if sentence.strip():
                emotion = self.model.predict(sentence.strip(), self.preprocessor, self.label_encoder)
                color = self.colors.get(emotion, 'black')
                self.result_area.insert(END, sentence.strip() + f" ({emotion})\n", (emotion,))
                self.result_area.tag_configure(emotion, foreground=color)

        self.result_area.config(state='disabled')
