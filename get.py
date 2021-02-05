from gtts import gTTS

n = 1834
for i in range(44032 + (n - 1), 44032 + 11172):
    char = chr(i)
    def save():
        try:
            tts = gTTS(char, lang='ko')
            tts.save(f'./sound/{n}.mp3')
        except:
            print(f'Error! ({char} - {n}) Retrying..')
            save()

    save()
    print(f'{char} ( {n} / 11172 )')
    n += 1
