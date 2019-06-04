from google_speech import Speech

import RPi.GPIO as GPIO
import time
import subprocess


def speak(text, lang):
    speech = Speech(text, lang)
    speech.play()


GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_UP)

ans = list()
ans.append('')
ans.append('')
ans.append('')
ans.append('')
ans.append('')

hin = list()
hin.append('')
hin.append('')
hin.append('')
hin.append('')
hin.append('')

math = list()
math.append('')
math.append('')
math.append('')
math.append('')
i=0
j=0
k=0
while True:
    b1 = GPIO.input(2)
    b2 = GPIO.input(17)
    b3 = GPIO.input(3)
    b4 = GPIO.input(27)
    b5 = GPIO.input(24)
    b6 = GPIO.input(22)
    b7 = GPIO.input(23)
    b8 = GPIO.input(16)
    b9 = GPIO.input(19)
    b10 = GPIO.input(20)
    b11 = GPIO.input(26)
    b12 = GPIO.input(21)
    b13 = GPIO.input(14)
    b14 = GPIO.input(25)
    b15 = GPIO.input(15)
    b16 = GPIO.input(8)
    b17 = GPIO.input(18)
    b18 = GPIO.input(7)
    b19 = GPIO.input(10)
    b20 = GPIO.input(5)
    b21 = GPIO.input(9)
    
    if b19 == True and b20 == True and b21 == True:
        speak("please press 1 for english, 2 for hindi , 3 for math","en")
        

    elif b19 == False:
        while(i<2):
            speak("English Pressed","en")
            i = i+1
            j=0
            k=0
            break
            
        if b1 == False and b3 == False and b2 == True and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'B'
            if ans[4] != 'B':
                print("".join(ans[:1]))
                ans[4] = 'B'
                speak(ans[4], "en")
        elif b1 == False and b2 == False and b3 == True and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'C'
            if ans[4] != 'C':
                print("".join(ans[:1]))
                ans[4] = 'C'
                speak(ans[4], "en")
        elif b1 == False and b2 == False and b4 == False and b3 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'D'
            if ans[4] != 'D':
                print("".join(ans[:1]))
                ans[4] = 'D'
                speak(ans[4], "en")
        elif b1 == False and b4 == False and b2 == True and b3 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'E'
            if ans[4] != 'E':
                print("".join(ans[:1]))
                ans[4] = 'E'
                speak(ans[4], "en")
        elif b1 == False and b2 == False and b3 == False and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'F'
            if ans[4] != 'F':
                print("".join(ans[:1]))
                ans[4] = 'F'
                speak(ans[4], "en")
        elif b1 == False and b2 == False and b3 == False and b4 == False and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'G'
            if ans[4] != 'G':
                print("".join(ans[:1]))
                ans[4] = 'G'
                speak(ans[4], "en")
        elif b1 == False and b3 == False and b4 == False and b2 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'H'
            if ans[4] != 'H':
                print("".join(ans[:1]))
                ans[4] = 'H'
                speak(ans[4], "en")
        elif b2 == False and b3 == False and b1 == True and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'I'
            if ans[4] != 'I':
                print("".join(ans[:1]))
                ans[4] = 'I'
                speak(ans[4], "en")
        elif b2 == False and b3 == False and b4 == False and b1 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'J'
            if ans[4] != 'J':
                print("".join(ans[:1]))
                ans[4] = 'J'
                speak(ans[4], "en")

        elif b1 == False and b5 == False and b2 == True and b3 == True and b4 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'K'
            if ans[4] != 'K':
                print("".join(ans[:1]))
                ans[4] = 'K'
                speak(ans[4], "en")
        elif b1 == False and b3 == False and b5 == False and b2 == True and b4 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'L'
            if ans[4] != 'L':
                print("".join(ans[:1]))
                ans[4] = 'L'
                speak(ans[4], "en")
        elif b1 == False and b2 == False and b5 == False and b3 == True and b4 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'M'
            if ans[4] != 'M':
                print("".join(ans[:1]))
                ans[4] = 'M'
                speak(ans[4], "en")
        elif b1 == False and b2 == False and b4 == False and b5 == False and b3 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'N'
            if ans[4] != 'N':
                print("".join(ans[:1]))
                ans[4] = 'N'
                speak(ans[4], "en")
        elif b1 == False and b4 == False and b5 == False and b2 == True and b3 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'O'
            if ans[4] != 'O':
                print("".join(ans[:1]))
                ans[4] = 'O'
                speak(ans[4], "en")
        elif b1 == False and b2 == False and b3 == False and b5 == False and b4 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'P'
            if ans[4] != 'P':
                print("".join(ans[:1]))
                ans[4] = 'P'
                speak(ans[4], "en")
        elif b1 == False and b2 == False and b3 == False and b4 == False and b5 == False and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'Q'
            if ans[4] != 'Q':
                print("".join(ans[:1]))
                ans[4] = 'Q'
                speak(ans[4], "en")
        elif b1 == False and b3 == False and b4 == False and b5 == False and b2 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'R'
            if ans[4] != 'R':
                print("".join(ans[:1]))
                ans[4] = 'R'
                speak(ans[4], "en")
        elif b2 == False and b3 == False and b5 == False and b1 == True and b4 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'S'
            if ans[4] != 'S':
                print("".join(ans[:1]))
                ans[4] = 'S'
                speak(ans[4], "en")
        elif b2 == False and b3 == False and b4 == False and b5 == False and b1 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'T'
            if ans[4] != 'T':
                print("".join(ans[:1]))
                ans[4] = 'T'
                speak(ans[4], "en")
        elif b1 == False and b5 == False and b6 == False and b2 == True and b3 == True and b4 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'U'
            if ans[4] != 'U':
                print("".join(ans[:1]))
                ans[4] = 'U'
                speak(ans[4], "en")
        elif b1 == False and b3 == False and b6 == False and b5 == False and b2 == True and b4 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'V'
            if ans[4] != 'V':
                print("".join(ans[:1]))
                ans[4] = 'V'
                speak(ans[4], "en")
        elif b1 == False and b3 == False and b6 == False and b5 == False and b2 == True and b4 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'W'
            if ans[4] != 'W':
                print("".join(ans[:1]))
                ans[4] = 'W'
                speak(ans[4], "en")
        elif b1 == False and b2 == False and b5 == False and b6 == False and b3 == True and b4 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'X'
            if ans[4] != 'X':
                print("".join(ans[:1]))
                ans[4] = 'X'
                speak(ans[4], "en")
        elif b1 == False and b2 == False and b4 == False and b5 == False and b6 == False and b3 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'Y'
            if ans[4] != 'Y':
                print("".join(ans[:1]))
                ans[4] = 'Y'
                speak(ans[4], "en")
        elif b1 == False and b4 == False and b5 == False and b6 == False and b2 == True and b3 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'Z'
            if ans[4] != 'Z':
                print("".join(ans[:1]))
                ans[4] = 'Z'
                speak(ans[4], "en")
        elif b1 == False and b4 == True and b5 == True and b6 == True and b2 == True and b3 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[0] = 'A'
            if ans[4] != 'A':
                print("".join(ans[:1]))
                ans[4] = 'A'
                speak(ans[4], "en")

        elif b7 == False and b9 == True and b8 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'A'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b9 == False and b8 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'B'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b8 == False and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'C'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b8 == False and b10 == False and b9 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'D'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b10 == False and b8 == True and b9 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'E'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b8 == False and b9 == False and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'F'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b8 == False and b9 == False and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'G'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b9 == False and b10 == False and b8 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'H'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b8 == False and b9 == False and b7 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'I'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b8 == False and b9 == False and b10 == False and b7 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'J'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b11 == False and b8 == True and b9 == True and b10 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'K'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b9 == False and b11 == False and b8 == True and b10 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'L'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b8 == False and b11 == False and b9 == True and b10 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'M'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b8 == False and b10 == False and b11 == False and b9 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'N'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b10 == False and b11 == False and b8 == True and b9 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'O'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b8 == False and b9 == False and b11 == False and b10 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'P'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b8 == False and b9 == False and b10 == False and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'Q'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b9 == False and b10 == False and b11 == False and b8 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'R'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b8 == False and b9 == False and b11 == False and b7 == True and b10 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'S'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b8 == False and b9 == False and b10 == False and b11 == False and b7 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'T'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b11 == False and b12 == False and b8 == True and b9 == True and b10 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'U'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b9 == False and b12 == False and b11 == False and b8 == True and b10 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'V'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b9 == False and b12 == False and b11 == False and b8 == True and b10 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'W'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b8 == False and b11 == False and b12 == False and b9 == True and b10 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'X'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b8 == False and b10 == False and b11 == False and b12 == False and b9 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'Y'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b7 == False and b10 == False and b11 == False and b12 == False and b8 == True and b9 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'Z'
            print("".join(ans[:2]))
            st = "".join(ans[:2])
            speak(st, "en")

        elif b13 == False and b15 == True and b14 == True and b16 == True and b17 == True and b18 == True:

            ans[2] = 'A'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b15 == False and b14 == True and b16 == True and b17 == True and b18 == True:

            ans[2] = 'B'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b14 == False and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[2] = 'C'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b14 == False and b16 == False and b15 == True and b17 == True and b18 == True:

            ans[2] = 'D'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b16 == False and b14 == True and b15 == True and b17 == True and b18 == True:

            ans[2] = 'E'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b14 == False and b15 == False and b16 == True and b17 == True and b18 == True:

            ans[2] = 'F'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b14 == False and b15 == False and b16 == False and b17 == True and b18 == True:

            ans[2] = 'G'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b15 == False and b16 == False and b14 == True and b17 == True and b18 == True:

            ans[2] = 'H'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b14 == False and b15 == False and b13 == True and b16 == True and b17 == True and b18 == True:

            ans[2] = 'I'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b14 == False and b15 == False and b16 == False and b13 == True and b17 == True and b18 == True:

            ans[2] = 'J'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b17 == False and b14 == True and b15 == True and b16 == True and b18 == True:

            ans[2] = 'K'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b15 == False and b17 == False and b14 == True and b16 == True and b18 == True:

            ans[2] = 'L'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b14 == False and b17 == False and b15 == True and b16 == True and b18 == True:

            ans[2] = 'M'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b14 == False and b16 == False and b17 == False and b15 == True and b18 == True:

            ans[2] = 'N'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b16 == False and b17 == False and b14 == True and b15 == True and b18 == True:

            ans[2] = 'O'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b14 == False and b15 == False and b17 == False and b16 == True and b18 == True:

            ans[2] = 'P'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b14 == False and b15 == False and b16 == False and b17 == False and b18 == True:

            ans[2] = 'Q'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b15 == False and b16 == False and b17 == False and b14 == True and b18 == True:

            ans[2] = 'R'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b14 == False and b15 == False and b17 == False and b13 == True and b16 == True and b18 == True:

            ans[2] = 'S'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b14 == False and b15 == False and b16 == False and b17 == False and b13 == True and b18 == True:

            ans[2] = 'T'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b17 == False and b18 == False and b14 == True and b15 == True and b16 == True:

            ans[2] = 'U'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b15 == False and b18 == False and b17 == False and b14 == True and b16 == True:

            ans[2] = 'V'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b15 == False and b18 == False and b17 == False and b14 == True and b16 == True:

            ans[2] = 'W'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b14 == False and b17 == False and b18 == False and b15 == True and b16 == True:

            ans[2] = 'X'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b14 == False and b16 == False and b17 == False and b18 == False and b15 == True:

            ans[2] = 'Y'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

        elif b13 == False and b16 == False and b17 == False and b18 == False and b14 == True and b15 == True:

            ans[2] = 'Z'
            print("".join(ans[:3]))
            st = "".join(ans[:3])
            speak(st, "en")

    elif b20 == False:
        while(j<2):
            speak("Hindi Pressed","en")
            j = j+1
            i=0
            k=0
            break
        if b1 == False and b3 == True and b2 == True and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'अ'
            if hin[4] != 'अ':
                print("".join(hin[:1]))
                hin[4] = 'अ'
                speak(hin[4], "hi")

        elif b1 == True and b3 == True and b2 == False and b4 == False and b5 == False and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'आ'
            if hin[4] != 'आ':
                print("".join(hin[:1]))
                hin[4] = 'आ'
                speak(hin[4], "hi")

        elif b1 == True and b3 == False and b2 == False and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'इ'
            if hin[4] != 'इ':
                print("".join(hin[:1]))
                hin[4] = 'इ'
                speak(hin[4], "hi")

        elif b1 == True and b3 == True and b2 == True and b4 == False and b5 == False and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ई'
            if hin[4] != 'ई':
                print("".join(hin[:1]))
                hin[4] = 'ई'
                speak(hin[4], "hi")

        elif b1 == False and b3 == True and b2 == True and b4 == True and b5 == False and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'उ'
            if hin[4] != 'उ':
                print("".join(hin[:1]))
                hin[4] = 'उ'
                speak(hin[4], "hi")

        elif b1 == False and b3 == False and b2 == True and b4 == False and b5 == True and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ऊ'
            if hin[4] != 'ऊ':
                print("".join(hin[:1]))
                hin[4] = 'ऊ'
                speak(hin[4], "hi")

        elif b1 == False and b3 == True and b2 == True and b4 == False and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ए'
            if hin[4] != 'ए':
                print("".join(hin[:1]))
                hin[4] = 'ए'
                speak(hin[4], "hi")

        elif b1 == True and b3 == True and b2 == False and b4 == True and b5 == False and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ऐ'
            if hin[4] != 'ऐ':
                print("".join(hin[:1]))
                hin[4] = 'ऐ'
                speak(hin[4], "hi")

        elif b1 == False and b3 == True and b2 == True and b4 == False and b5 == False and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ओ'
            if hin[4] != 'ओ':
                print("".join(hin[:1]))
                hin[4] = 'ओ'
                speak(hin[4], "hi")

        elif b1 == True and b3 == False and b2 == False and b4 == True and b5 == True and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'औ'
            if hin[4] != 'औ':
                print("".join(hin[:1]))
                hin[4] = 'औ'
                speak(hin[4], "hi")

        elif b1 == False and b3 == True and b2 == True and b4 == True and b5 == False and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'क'
            if hin[4] != 'क':
                print("".join(hin[:1]))
                hin[4] = 'क'
                speak(hin[4], "hi")

        elif b1 == True and b3 == True and b2 == False and b4 == True and b5 == True and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ख'
            if hin[4] != 'ख':
                print("".join(hin[:1]))
                hin[4] = 'ख'
                speak(hin[4], "hi")

        elif b1 == False and b3 == False and b2 == False and b4 == False and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ग'
            if hin[4] != 'ग':
                print("".join(hin[:1]))
                hin[4] = 'ग'
                speak(hin[4], "hi")

        elif b1 == False and b3 == False and b2 == True and b4 == True and b5 == True and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'घ'
            if hin[4] != 'घ':
                print("".join(hin[:1]))
                hin[4] = 'घ'
                speak(hin[4], "hi")

        elif b1 == True and b3 == True and b2 == False and b4 == True and b5 == False and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ङ'
            if hin[4] != 'ङ':
                print("".join(hin[:1]))
                hin[4] = 'ङ'
                speak(hin[4], "hi")

        elif b1 == False and b3 == True and b2 == False and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'च'
            if hin[4] != 'च':
                print("".join(hin[:1]))
                hin[4] = 'च'
                speak(hin[4], "hi")

        elif b1 == False and b3 == True and b2 == True and b4 == True and b5 == True and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'छ'
            if hin[4] != 'छ':
                print("".join(hin[:1]))
                hin[4] = 'छ'
                speak(hin[4], "hi")

        elif b1 == True and b3 == False and b2 == False and b4 == False and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ज'
            if hin[4] != 'ज':
                print("".join(hin[:1]))
                hin[4] = 'ज'
                speak(hin[4], "hi")

        elif b1 == True and b3 == True and b2 == True and b4 == False and b5 == False and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'झ'
            if hin[4] != 'झ':
                print("".join(hin[:1]))
                hin[4] = 'झ'
                speak(hin[4], "hi")

        elif b1 == True and b3 == False and b2 == True and b4 == False and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ञ'
            if hin[4] != 'ञ':
                print("".join(hin[:1]))
                hin[4] = 'ञ'
                speak(hin[4], "hi")

        elif b1 == True and b3 == False and b2 == False and b4 == False and b5 == False and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ट'
            if hin[4] != 'ट':
                print("".join(hin[:1]))
                hin[4] = 'ट'
                speak(hin[4], "hi")

        elif b1 == True and b3 == False and b2 == False and b4 == False and b5 == True and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ठ'
            if hin[4] != 'ठ':
                print("".join(hin[:1]))
                hin[4] = 'ठ'
                speak(hin[4], "hi")

        elif b1 == False and b3 == False and b2 == False and b4 == True and b5 == True and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ड'
            if hin[4] != 'ड':
                print("".join(hin[:1]))
                hin[4] = 'ड'
                speak(hin[4], "hi")

        elif b1 == False and b3 == False and b2 == False and b4 == False and b5 == False and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ढ'
            if hin[4] != 'ढ':
                print("".join(hin[:1]))
                hin[4] = 'ढ'
                speak(hin[4], "hi")

        elif b1 == True and b3 == True and b2 == False and b4 == False and b5 == False and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ण'
            if hin[4] != 'ण':
                print("".join(hin[:1]))
                hin[4] = 'ण'
                speak(hin[4], "hi")

        elif b1 == True and b3 == False and b2 == False and b4 == False and b5 == False and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'त'
            if hin[4] != 'त':
                print("".join(hin[:1]))
                hin[4] = 'त'
                speak(hin[4], "hi")

        elif b1 == False and b3 == True and b2 == False and b4 == False and b5 == True and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'थ'
            if hin[4] != 'थ':
                print("".join(hin[:1]))
                hin[4] = 'थ'
                speak(hin[4], "hi")

        elif b1 == False and b3 == True and b2 == False and b4 == False and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'द'
            if hin[4] != 'द':
                print("".join(hin[:1]))
                hin[4] = 'द'
                speak(hin[4], "hi")

        elif b1 == True and b3 == True and b2 == False and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ध'
            if hin[4] != 'ध':
                print("".join(hin[:1]))
                hin[4] = 'ध'
                speak(hin[4], "hi")

        elif b1 == False and b3 == True and b2 == False and b4 == False and b5 == False and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'न'
            if hin[4] != 'न':
                print("".join(hin[:1]))
                hin[4] = 'न'
                speak(hin[4], "hi")

        elif b1 == False and b3 == False and b2 == False and b4 == True and b5 == False and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'प'
            if hin[4] != 'प':
                print("".join(hin[:1]))
                hin[4] = 'प'
                speak(hin[4], "hi")

        elif b1 == True and b3 == False and b2 == True and b4 == True and b5 == False and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'फ'
            if hin[4] != 'फ':
                print("".join(hin[:1]))
                hin[4] = 'फ'
                speak(hin[4], "hi")

        elif b1 == False and b3 == False and b2 == True and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ब'
            if hin[4] != 'ब':
                print("".join(hin[:1]))
                hin[4] = 'ब'
                speak(hin[4], "hi")

        elif b1 == True and b3 == True and b2 == False and b4 == False and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'भ'
            if hin[4] != 'भ':
                print("".join(hin[:1]))
                hin[4] = 'भ'
                speak(hin[4], "hi")

        elif b1 == False and b3 == True and b2 == False and b4 == True and b5 == False and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'म'
            if hin[4] != 'म':
                print("".join(hin[:1]))
                hin[4] = 'म'
                speak(hin[4], "hi")

        elif b1 == False and b3 == True and b2 == False and b4 == False and b5 == False and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'य'
            if hin[4] != 'य':
                print("".join(hin[:1]))
                hin[4] = 'य'
                speak(hin[4], "hi")

        elif b1 == False and b3 == False and b2 == True and b4 == False and b5 == False and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'र'
            if hin[4] != 'र':
                print("".join(hin[:1]))
                hin[4] = 'र'
                speak(hin[4], "hi")

        elif b1 == False and b3 == False and b2 == True and b4 == True and b5 == False and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ल'
            if hin[4] != 'ल':
                print("".join(hin[:1]))
                hin[4] = 'ल'
                speak(hin[4], "hi")

        elif b1 == False and b3 == False and b2 == True and b4 == True and b5 == False and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'व'
            if hin[4] != 'व':
                print("".join(hin[:1]))
                hin[4] = 'व'
                speak(hin[4], "hi")

        elif b1 == False and b3 == False and b2 == True and b4 == True and b5 == False and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'व'
            if hin[4] != 'व':
                print("".join(hin[:1]))
                hin[4] = 'व'
                speak(hin[4], "hi")

        elif b1 == False and b3 == True and b2 == False and b4 == True and b5 == True and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'श'
            if hin[4] != 'श':
                print("".join(hin[:1]))
                hin[4] = 'श'
                speak(hin[4], "hi")

        elif b1 == False and b3 == False and b2 == False and b4 == True and b5 == False and b6 == False and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ष'
            if hin[4] != 'ष':
                print("".join(hin[:1]))
                hin[4] = 'ष'
                speak(hin[4], "hi")

        elif b1 == True and b3 == False and b2 == False and b4 == True and b5 == False and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'स'
            if hin[4] != 'स':
                print("".join(hin[:1]))
                hin[4] = 'स'
                speak(hin[4], "hi")

        elif b1 == False and b3 == False and b2 == True and b4 == False and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[0] = 'ह'
            if hin[4] != 'ह':
                print("".join(hin[:1]))
                hin[4] = 'ह'
                speak(hin[4], "hi")

        elif b7 == True and b9 == True and b8 == False and b10 == False and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'आ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == False and b8 == False and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'इ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == True and b8 == True and b10 == False and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ई'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == True and b8 == True and b10 == True and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'उ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == False and b8 == True and b10 == False and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ऊ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == True and b8 == True and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ए'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == True and b8 == False and b10 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ऐ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == True and b8 == True and b10 == False and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ओ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == False and b8 == False and b10 == True and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'औ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == True and b8 == True and b10 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'क'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == True and b8 == False and b10 == True and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ख'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == False and b8 == False and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ग'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == False and b8 == True and b10 == True and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'घ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == True and b8 == False and b10 == True and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ङ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == True and b8 == False and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'च'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == True and b8 == True and b10 == True and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'छ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == False and b8 == False and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ज'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == True and b8 == True and b10 == False and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'झ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == False and b8 == True and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ञ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == False and b8 == False and b10 == False and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ट'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == False and b8 == False and b10 == False and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ठ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == False and b8 == False and b10 == True and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ड'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == False and b8 == False and b10 == False and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ढ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == True and b8 == False and b10 == False and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ण'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == False and b8 == False and b10 == False and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'त'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == True and b8 == False and b10 == False and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'थ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == True and b8 == False and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'द'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == True and b8 == False and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ध'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == True and b8 == False and b10 == False and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'न'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == False and b8 == False and b10 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'प'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == False and b8 == True and b10 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'फ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == False and b8 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ब'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == True and b8 == False and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'भ'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == True and b8 == False and b10 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'म'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == True and b8 == False and b10 == False and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'य'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == False and b8 == True and b10 == False and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'र'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == False and b8 == True and b10 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ल'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == False and b8 == True and b10 == True and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'व'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == True and b8 == False and b10 == True and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'श'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == False and b8 == False and b10 == True and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ष'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == True and b9 == False and b8 == False and b10 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'स'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == False and b8 == True and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ह'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b13 == False and b15 == True and b14 == True and b16 == True and b17 == True and b18 == True:

            hin[2] = 'अ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == True and b14 == False and b16 == False and b17 == False and b18 == True:

            hin[2] = 'आ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == False and b14 == False and b16 == True and b17 == True and b18 == True:

            hin[2] = 'इ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == True and b14 == True and b16 == False and b17 == False and b18 == True:

            hin[2] = 'ई'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == True and b14 == True and b16 == True and b17 == False and b18 == False:

            hin[2] = 'उ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == False and b14 == True and b16 == False and b17 == True and b18 == False:

            hin[2] = 'ऊ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == True and b14 == True and b16 == False and b17 == True and b18 == True:

            hin[2] = 'ए'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == True and b14 == False and b16 == True and b17 == False and b18 == True:

            hin[2] = 'ऐ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == True and b14 == True and b16 == False and b17 == False and b18 == True:

            hin[2] = 'ओ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == False and b14 == False and b16 == True and b17 == True and b18 == False:

            hin[2] = 'औ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == True and b14 == True and b16 == True and b17 == False and b18 == True:

            hin[2] = 'क'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == True and b14 == False and b16 == True and b17 == True and b18 == False:

            hin[2] = 'ख'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == False and b14 == False and b16 == False and b17 == True and b18 == True:

            hin[2] = 'ग'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == False and b14 == True and b16 == True and b17 == True and b18 == False:

            hin[2] = 'घ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == True and b14 == False and b16 == True and b17 == False and b18 == False:

            hin[2] = 'ङ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == True and b14 == False and b16 == True and b17 == True and b18 == True:

            hin[2] = 'च'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == True and b14 == True and b16 == True and b17 == True and b18 == False:

            hin[2] = 'छ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == False and b14 == False and b16 == False and b17 == True and b18 == True:

            hin[2] = 'ज'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == True and b14 == True and b16 == False and b17 == False and b18 == False:

            hin[2] = 'झ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == False and b14 == True and b16 == False and b17 == True and b18 == True:

            hin[2] = 'ञ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == False and b14 == False and b16 == False and b17 == False and b18 == False:

            hin[2] = 'ट'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == False and b14 == False and b16 == False and b17 == True and b18 == False:

            hin[2] = 'ठ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == False and b14 == False and b16 == True and b17 == True and b18 == False:

            hin[2] = 'ड'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == False and b14 == False and b16 == False and b17 == False and b18 == False:

            hin[2] = 'ढ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == True and b14 == False and b16 == False and b17 == False and b18 == False:

            hin[2] = 'ण'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == False and b14 == False and b16 == False and b17 == False and b18 == True:

            hin[2] = 'त'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == True and b14 == False and b16 == False and b17 == True and b18 == False:

            hin[2] = 'थ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == True and b14 == False and b16 == False and b17 == True and b18 == True:

            hin[2] = 'द'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == True and b14 == False and b16 == True and b17 == True and b18 == True:

            hin[2] = 'ध'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == True and b14 == False and b16 == False and b17 == False and b18 == True:

            hin[2] = 'न'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == False and b14 == False and b16 == True and b17 == False and b18 == True:

            hin[2] = 'प'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == False and b14 == True and b16 == True and b17 == False and b18 == True:

            hin[2] = 'फ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == False and b14 == True and b16 == True and b17 == True and b18 == True:

            hin[2] = 'ब'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == True and b14 == False and b16 == False and b17 == True and b18 == True:

            hin[2] = 'भ'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == True and b14 == False and b16 == True and b17 == False and b18 == True:

            hin[2] = 'म'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == True and b14 == False and b16 == False and b17 == False and b18 == False:

            hin[2] = 'य'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == False and b14 == True and b16 == False and b17 == False and b18 == True:

            hin[2] = 'र'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == False and b14 == True and b16 == True and b17 == False and b18 == True:

            hin[2] = 'ल'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == False and b14 == True and b16 == True and b17 == False and b18 == False:

            hin[2] = 'व'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == True and b14 == False and b16 == True and b17 == True and b18 == False:

            hin[2] = 'श'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == False and b14 == False and b16 == True and b17 == False and b18 == False:

            hin[2] = 'ष'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == True and b15 == False and b14 == False and b16 == True and b17 == False and b18 == True:

            hin[2] = 'स'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

        elif b13 == False and b15 == False and b14 == True and b16 == False and b17 == True and b18 == True:

            hin[2] = 'ह'
            print("".join(hin[:3]))
            st = "".join(hin[:3])
            speak(st, "hi")

    elif b21 == False:
        while(k<2):
            speak("Math Pressed","en")
            k = k+1
            i=0
            j=0
            break
        
       
        if b1 == False and b3 == False and b2 == True and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[0] = '2'
            print("".join(math[:1]))
            speak(math[0], "en")
        elif b1 == False and b2 == False and b3 == True and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[0] = '3'
            print("".join(math[:1]))
            speak(math[0], "en")
        elif b1 == False and b2 == False and b4 == False and b3 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[0] = '4'
            print("".join(math[:1]))
            speak(math[0], "en")
        elif b1 == False and b4 == False and b2 == True and b3 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[0] = '5'
            print("".join(math[:1]))
            speak(math[0], "en")
        elif b1 == False and b2 == False and b3 == False and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[0] = '6'
            print("".join(math[:1]))
            speak(math[0], "en")
        elif b1 == False and b2 == False and b3 == False and b4 == False and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[0] = '7'
            print("".join(math[:1]))
            speak(math[0], "en")
        elif b1 == False and b3 == False and b4 == False and b2 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[0] = '8'
            print("".join(math[:1]))
            speak(math[0], "en")
        elif b2 == False and b3 == False and b1 == True and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[0] = '9'
            print("".join(math[:1]))
            speak(math[0], "en")
        elif b2 == False and b3 == False and b4 == False and b1 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[0] = '0'
            print("".join(math[:1]))
            speak(math[0], "en")
        elif b1 == False and b4 == True and b5 == True and b6 == True and b2 == True and b3 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[0] = '1'
            print("".join(math[:1]))
            speak(math[0], "en")

        elif b7 == False and b9 == True and b8 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '1'
            print("".join(math[:2]))
            st = "".join(math[:2])
            speak(st, "en")

        elif b7 == False and b9 == False and b8 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '2'
            print("".join(math[:2]))
            st = "".join(math[:2])
            speak(st, "en")

        elif b7 == False and b8 == False and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '3'
            print("".join(math[:2]))
            st = "".join(math[:2])
            speak(st, "en")

        elif b7 == False and b8 == False and b10 == False and b9 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '4'
            print("".join(math[:2]))
            st = "".join(math[:2])
            speak(st, "en")

        elif b7 == False and b10 == False and b8 == True and b9 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '5'
            print("".join(math[:2]))
            st = "".join(math[:2])
            speak(st, "en")

        elif b7 == False and b8 == False and b9 == False and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '6'
            print("".join(math[:2]))
            st = "".join(math[:2])
            speak(st, "en")

        elif b7 == False and b8 == False and b9 == False and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '7'
            print("".join(math[:2]))
            st = "".join(math[:2])
            speak(st, "en")

        elif b7 == False and b9 == False and b10 == False and b8 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '8'
            print("".join(math[:2]))
            st = "".join(math[:2])
            speak(st, "en")

        elif b8 == False and b9 == False and b7 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '9'
            print("".join(math[:2]))
            st = "".join(math[:2])
            speak(st, "en")

        elif b8 == False and b9 == False and b10 == False and b7 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '0'
            print("".join(math[:2]))
            st = "".join(math[:2])
            speak(st, "en")

        elif b8 == True and b9 == False and b10 == False and b7 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '+'
            print("".join(math[:2]))
            st = "".join(math[:2])
            speak(st, "en")

        elif b8 == True and b9 == True and b10 == True and b7 == True and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '-'
            print("".join(math[:2]))
            st = "".join(math[:2])
            speak(st, "en")	
	
        elif b8 == True and b9 == True and b10 == False and b7 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '*'
            print("".join(math[:2]))
            st = "".join(math[:2])
            speak("multiply", "en")
    

        elif b8 == False and b9 == True and b10 == False and b7 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '>'
            print("".join(math[:2]))
            st = "".join(math[:2])
            speak("multiply", "en")
    

        elif b8 == True and b9 == False and b10 == True and b7 == False and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '<'
            print("".join(math[:2]))
            st = "".join(math[:2])
            speak("multiply", "en")
    
        elif b8 == False and b9 == True and b10 == True and b7 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '/'
            print("".join(math[:2]))
            st = "".join(math[:2])
            speak(st, "en")

        elif b13 == False and b15 == True and b14 == True and b16 == True and b17 == True and b18 == True:

            math[2] = '1'
            print("".join(math[:3]))
            st = "".join(math[:3])
            speak(st, "en")

        elif b13 == False and b15 == False and b14 == True and b16 == True and b17 == True and b18 == True:

            math[2] = '2'
            print("".join(math[:3]))
            st = "".join(math[:3])
            speak(st, "en")

        elif b13 == False and b14 == False and b15 == True and b16 == True and b17 == True and b18 == True:

            math[2] = '3'
            print("".join(math[:3]))
            st = "".join(math[:3])
            speak(st, "en")
    
        elif b13 == False and b14 == False and b16 == False and b15 == True and b17 == True and b18 == True:

            math[2] = '4'
            print("".join(math[:3]))
            st = "".join(math[:3])
            speak(st, "en")

        elif b13 == False and b16 == False and b14 == True and b15 == True and b17 == True and b18 == True:

            math[2] = '5'
            print("".join(math[:3]))
            st = "".join(math[:3])
            speak(st, "en")

        elif b13 == False and b14 == False and b15 == False and b16 == True and b17 == True and b18 == True:

            math[2] = '6'
            print("".join(math[:3]))
            st = "".join(math[:3])
            speak(st, "en")

        elif b13 == False and b14 == False and b15 == False and b16 == False and b17 == True and b18 == True:

            math[2] = '7'
            print("".join(math[:3]))
            st = "".join(math[:3])
            speak(st, "en")

        elif b13 == False and b15 == False and b16 == False and b14 == True and b17 == True and b18 == True:

            math[2] = '8'
            print("".join(math[:3]))
            st = "".join(math[:3])
            speak(st, "en")

        elif b14 == False and b15 == False and b13 == True and b16 == True and b17 == True and b18 == True:

            math[2] = '9'
            print("".join(math[:3]))
            st = "".join(math[:3])
            speak(st, "en")

        elif b14 == False and b15 == False and b16 == False and b13 == True and b17 == True and b18 == True:

            math[2] = '0'
            print("".join(math[:3]))
            st = "".join(math[:3])
            speak(st, "en")

        if (math[1] == '+' or math[1] == '-' or math[1] == '*' or math[1] == '/' or math[1] == '>' or math[1] =='<'):
	    	
    	    if(math[1] == '+' and math[2]!=''):
                x = int(math[0]) + int(math[2])
                print(x)
                speak(str(x), "en")
    	   	    
    	    elif(math[1] == '-'and math[2]!=''):
                x = int(math[0]) - int(math[2])
                print(x)
                speak(str(x), "en")

		
    	    elif(math[1] == '>'and math[2]!=''):
                if(math[0]) > int(math[2]):
			speak("True","en")
                else:
                	speak("False", "en")
	
    	    elif(math[1] == '<'and math[2]!=''):
                if(math[0]) < int(math[2]):
			speak("True","en")
                else:
                	speak("False", "en")
	

    	    elif(math[1] == '*' and math[2]!=''):
                x = int(math[0]) * int(math[2])
                print(x)
                speak(str(x), "en")

    	    elif(math[1] == '/' and math[2]!=''):
                if(math[2] == '0'):
                    speak("Cannot divide by zero","en")
                else:
                    x = int(int(math[0]) / int(math[2]))
                    print(x)
                    speak(str(x), "en")
    else:
        speak("Please check the button and try again","en")
        

GPIO.cleanup()
