import speech_recognition as voice
from google_trans import Translator

voice_data = voice.Recognizer()
trans  = Translator()

with voice.Microphone() as sourch:
  try:
    voice_data.dynamic_energy_threshold = 0.2
    voice_data.dynamic_energy_ratio = 0.3
    audio = voice_data.listen(sourch)
    recognize_voice = voice_data.recognize_google(audio)
    translation  = trans.translate([recognize_voice],dest='bn')
    print '[+]You said===>{0}'.format(recognize_voice)
    for x in translation:
        print '[+]translating in bangla==>{0}'.format(x.text.encode('utf-8'))
  except:
    print 'Something is Wrong'
