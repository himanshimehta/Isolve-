# Get Started!

1. Download the "Revised Frontend" folder and extract it somewhere.

2. Install dependencies (assuming you have python3 installed)
  
    `sudo pip3 install numpy nltk spacy sklearn pandas flask tensorflow keras h5py`

3. Download external files:
   - Download dependencies for Stanford POSTagger, and DependencyParser:
   
     Go to the following link: [Click Me!](https://drive.google.com/drive/folders/1LAyDWhVjL7S6OxW-gXMJmW06YaUAohTc), and     unpack the libs folder in your "Revised Frontend" directory.
   
   - Download models for Spacy:
   
     `sudo python3 -m spacy download en`
     
   - Download NLTK Data (all corpora and packages):
   
     ```
     python3
     >>>> import nltk
     >>>> nltk.download()
     ```
4. Navigate to your "Revised Frontend" folder with your terminal, and start the Flask server with 
   
   `python3 linking.py`.
 
5. Select your category, and enter your question (or select one from the table of examples). You get an answer. Rejoice!
