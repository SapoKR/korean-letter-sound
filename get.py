from gtts import gTTS

def save(char, n):
    try:
        tts = gTTS(char, lang='ko')
        tts.save(f'./sound/{n}.mp3')
    except:
        print(f'Error! ({char} - {n}) Retrying..')
        save(char, n)

for n in range(1, 11173):
    char = chr(44031 + n)
    save(char, n)
    print(f'{char} ( {n} / 11172 )')
