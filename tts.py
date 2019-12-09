# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from gtts import gTTS
import os
from pygame import mixer 

mixer.init()
tts = gTTS(text='Люблю шэдоу демона без рапиры', lang='ru')
tts.save("good.mp3")
mixer.music.load("good.mp3")
mixer.music.play()
#os.system("good.mp3")
