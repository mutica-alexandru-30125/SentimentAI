class DataLoader:
    @staticmethod
    def load_data(file_name):
        data = []
        labels = []
        with open(file_name, 'r', encoding='utf-8') as f:
            for line in f:
                text, label = line.strip().split(';')
                data.append(text)
                labels.append(label)
        return data, labels
