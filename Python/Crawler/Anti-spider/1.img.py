from PIL import Image
import pytesseract
import pygame
import time
import asyncio
import edge_tts
import os


im = Image.open('H:/MyGitCodes/Python/Crawler/Anti-spider/test.png')
result = pytesseract.image_to_string(im)
print(result)
# rate:0~3
# pitch:0~2


async def getaudio_edge(text, file_mp3, spk_name='Xiaoxiao', rate=1, pitch=1):
    voice = 'Microsoft Server Speech Text to Speech Voice(zh-CN,%sNeural)' % (
        spk_name)
    if pitch >= 1:
        str_pitch = '+%d%%' % (int((pitch-1)*50))
    else:
        str_pitch = '%d%%' % (int((pitch-1)*50))
    if rate >= 1:
        str_rate = '+%d%%' % (int((rate-1)*100))
    else:
        str_rate = '%d%%' % (int((rate-1)*100))
    communicate = edge_tts.Communicate()
    with open(file_mp3, 'wb') as f:
        async for i in communicate.run(text, voice=voice, rate=str_rate, pitch=str_pitch):
            if i[2] is not None:
                f.write(i[2])


def gen_voice(file, volume=0.5):
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(start=0.0)
    while pygame.mixer.music.get_busy():
        pass
    pygame.mixer.quit()


def tts_edge(text, spk_name='Xiaoxiao', rate=1, pitch=1, volume=1):
    asyncio.get_event_loop().run_until_complete(getaudio_edge(
        text, "test.mp3", spk_name=spk_name, rate=rate, pitch=pitch))
    gen_voice("test.mp3", volume=volume)


# if __name__ == "__main__":
#     voice_list = ['Xiaoxiao', 'Yunyang', 'Xiaochen', 'Xiaohan', 'Xiaomo', 'Xiaoqiu',
#                   'Xiaorui', 'Xiaoshuang', 'Xiaoxuan', 'Xiaoyan', 'Xiaoyou', 'Yunxi', 'Yunye']
text = "您好"
# for spk in voice_list:
#     print(spk)
tts_edge(text, spk_name='Xiaoxiao', rate=1, pitch=1, volume=1)
