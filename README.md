# Emotion Detection from Text

## Descriere

Acest program utilizează învățarea automată pentru a detecta emoțiile exprimate în texte scrise. Folosind un model de rețea neuronală, programul procesează un set de date adnotat cu emoții, antrenează un model LSTM bidirecțional pentru recunoașterea acestora și oferă un serviciu de predicție într-o aplicație grafică.

### Fluxul principal:
1. **Încărcarea datelor**: Fișierele CSV cu exemple de texte și etichete asociate sunt încărcate folosind clasa `DataLoader`.
2. **Preprocesarea datelor**: Texte sunt transformate într-o formă numerică utilizabilă pentru rețele neuronale folosind tehnici de tokenizare și padding din Keras, prin clasa `Preprocessor`.
3. **Construirea modelului**: Modelul folosește o arhitectură LSTM bidirecțională pentru a învăța relațiile între cuvinte și a detecta emoțiile. Acesta este antrenat cu datele preprocesate.
4. **Evaluare și predicții**: După antrenament, modelul este evaluat pe setul de date de test și este utilizat pentru a face predicții asupra textelor noi.
5. **Interfața grafică**: O interfață simplă în Tkinter este implementată pentru a permite utilizatorilor să introducă un text, iar aplicația va afișa emoția detectată pentru fiecare propoziție.

## Caracteristici

- **Detectare emoții**: Programul este capabil să recunoască mai multe emoții, precum: bucurie, tristețe, furie, frică, iubire, surpriză.
- **Preprocesare avansată**: Folosește tokenizare și padding pentru a gestiona texte de lungimi variate.
- **Interfață grafică**: Oferă un mediu ușor de utilizat pentru a analiza texte și a vizualiza emoțiile detectate.
- **Antrenament pe date reale**: Modelul este antrenat pe seturi de date adnotate pentru a învăța să recunoască emoțiile dintr-un text.

## Tehnologii folosite

- **Python**: Limbajul principal de programare.
- **TensorFlow/Keras**: Folosit pentru construirea și antrenarea rețelei neuronale.
- **Tkinter**: Folosit pentru crearea interfeței grafice.
- **NumPy și scikit-learn**: Folosite pentru manipularea datelor și preprocesare.

## Instalare

1. Clonează acest repository:
   ```bash
   git clone https://github.com/username/repository-name.git
