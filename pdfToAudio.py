import pyttsx3
from PyPDF2 import PdfReader

pdf_reader = PdfReader('C:\\Users\\xxxx\\OneDrive\\Desktop\\cover letter gov of Ont.pdf')
reader = pyttsx3.init()

voices = reader.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():
        reader.setProperty('voice', voice.id)
        break

reader.setProperty('rate', 150)

for page in pdf_reader.pages:
    text = page.extract_text()
    legible_text = text.strip().replace('\n', ' ')
    print(legible_text)
    reader.say(legible_text)

reader.save_to_file(legible_text, 'file.mp3')
reader.runAndWait()
reader.stop()
