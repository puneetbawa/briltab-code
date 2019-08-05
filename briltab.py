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
ans.append('')
ans.append('')

hin = list()
hin.append('')
hin.append('')
hin.append('')
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
math.append('')
math.append('')
math.append('')
math.append('')
i=0
j=0
k=0
l=0
x=''
m=0
n=0
o=0
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
        while (l<1):
            i=0
            j=0
            k=0
            l=l+1
            speak("please press 1 for english, 2 for hindi , 3 for math","en")
        

    elif b19 == False:
        while(i<1):
            speak("English Pressed","en")
            i = i+1
            j=0
            k=0
            l=0
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
            if ans[4] != 'I' and count_e !=1:
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

      #  else:
       #     ans[4]=''



        elif b7 == False and b9 == True and b8 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            ans[1] = 'A'
            if ans[5] != 'A':   
                ans[5] = 'A' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''
                                 

        elif b7 == False and b9 == False and b8 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'B'
            if ans[5] != 'B':   
                ans[5] = 'B' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b8 == False and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'C'
            if ans[5] != 'C':   
                ans[5] = 'C' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b8 == False and b10 == False and b9 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'D'
            if ans[5] != 'D':   
                ans[5] = 'D' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b10 == False and b8 == True and b9 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'E'
            if ans[5] != 'E':   
                ans[5] = 'E' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b8 == False and b9 == False and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'F'
            if ans[5] != 'F':   
                ans[5] = 'F' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b8 == False and b9 == False and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'G'
            if ans[5] != 'G':   
                ans[5] = 'G' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b9 == False and b10 == False and b8 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'H'
            if ans[5] != 'H':   
                ans[5] = 'H' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b8 == False and b9 == False and b7 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'I'
            if ans[5] != 'I':   
                ans[5] = 'I' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b8 == False and b9 == False and b10 == False and b7 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'J'
            if ans[5] != 'J':   
                ans[5] = 'J' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b11 == False and b8 == True and b9 == True and b10 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'K'
            if ans[5] != 'K':   
                ans[5] = 'K' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b9 == False and b11 == False and b8 == True and b10 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'L'
            if ans[5] != 'L':   
                ans[5] = 'L' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b8 == False and b11 == False and b9 == True and b10 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'M'
            if ans[5] != 'M':   
                ans[5] = 'M' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b8 == False and b10 == False and b11 == False and b9 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'N'
            if ans[5] != 'N':   
                ans[5] = 'N' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b10 == False and b11 == False and b8 == True and b9 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'O'
            if ans[5] != 'O':   
                ans[5] = 'O' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b8 == False and b9 == False and b11 == False and b10 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'P'
            if ans[5] != 'P':   
                ans[5] = 'P' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b8 == False and b9 == False and b10 == False and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'Q'
            if ans[5] != 'Q':   
                ans[5] = 'Q' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b9 == False and b10 == False and b11 == False and b8 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'R'
            if ans[5] != 'R':   
                ans[5] = 'R' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b8 == False and b9 == False and b11 == False and b7 == True and b10 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'S'
            if ans[5] != 'S':   
                ans[5] = 'S' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b8 == False and b9 == False and b10 == False and b11 == False and b7 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'T'
            if ans[5] != 'T':   
                ans[5] = 'T' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b11 == False and b12 == False and b8 == True and b9 == True and b10 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'U'
            if ans[5] != 'U':   
                ans[5] = 'U' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b9 == False and b12 == False and b11 == False and b8 == True and b10 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'V'
            if ans[5] != 'V':   
                ans[5] = 'V' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b9 == False and b12 == False and b11 == False and b8 == True and b10 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'W'
            if ans[5] != 'W':   
                ans[5] = 'W' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b8 == False and b11 == False and b12 == False and b9 == True and b10 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'X'
            if ans[5] != 'X':   
                ans[5] = 'X' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b8 == False and b10 == False and b11 == False and b12 == False and b9 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'Y'
            if ans[5] != 'Y':   
                ans[5] = 'Y' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''

        elif b7 == False and b10 == False and b11 == False and b12 == False and b8 == True and b9 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[1] = 'Z'
            if ans[5] != 'Z':   
                ans[5] = 'Z' 
                print("".join(ans[:2]))
                st = "".join(ans[:2])
                speak(st, "en")
                ans[4]=''
    #    else:
    #        ans[5]=''

        elif b13 == False and b15 == True and b14 == True and b16 == True and b17 == True and b18 == True:

            ans[2] = 'A'
            if ans[6] != 'A':   
                ans[6] = 'A' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b15 == False and b14 == True and b16 == True and b17 == True and b18 == True:

            ans[2] = 'B'
            if ans[6] != 'B':   
                ans[6] = 'B' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b14 == False and b15 == True and b16 == True and b17 == True and b18 == True:

            ans[2] = 'C'
            if ans[6] != 'C':   
                ans[6] = 'C' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b14 == False and b16 == False and b15 == True and b17 == True and b18 == True:

            ans[2] = 'D'
            if ans[6] != 'D':   
                ans[6] = 'D' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b16 == False and b14 == True and b15 == True and b17 == True and b18 == True:

            ans[2] = 'E'
            if ans[6] != 'E':   
                ans[6] = 'E' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b14 == False and b15 == False and b16 == True and b17 == True and b18 == True:

            ans[2] = 'F'
            if ans[6] != 'F':   
                ans[6] = 'F' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b14 == False and b15 == False and b16 == False and b17 == True and b18 == True:

            ans[2] = 'G'
            if ans[6] != 'G':   
                ans[6] = 'G' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b15 == False and b16 == False and b14 == True and b17 == True and b18 == True:

            ans[2] = 'H'
            if ans[6] != 'H':   
                ans[6] = 'H' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b14 == False and b15 == False and b13 == True and b16 == True and b17 == True and b18 == True:

            ans[2] = 'I'
            if ans[6] != 'I':   
                ans[6] = 'I' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b14 == False and b15 == False and b16 == False and b13 == True and b17 == True and b18 == True:

            ans[2] = 'J'
            if ans[6] != 'J':   
                ans[6] = 'J' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b17 == False and b14 == True and b15 == True and b16 == True and b18 == True:

            ans[2] = 'K'
            if ans[6] != 'K':   
                ans[6] = 'K' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b15 == False and b17 == False and b14 == True and b16 == True and b18 == True:

            ans[2] = 'L'
            if ans[6] != 'L':   
                ans[6] = 'L' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b14 == False and b17 == False and b15 == True and b16 == True and b18 == True:

            ans[2] = 'M'
            if ans[6] != 'M':   
                ans[6] = 'M' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b14 == False and b16 == False and b17 == False and b15 == True and b18 == True:

            ans[2] = 'N'
            if ans[6] != 'N':   
                ans[6] = 'N' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b16 == False and b17 == False and b14 == True and b15 == True and b18 == True:

            ans[2] = 'O'
            if ans[6] != 'O':   
                ans[6] = 'O' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b14 == False and b15 == False and b17 == False and b16 == True and b18 == True:

            ans[2] = 'P'
            if ans[6] != 'P':   
                ans[6] = 'P' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b14 == False and b15 == False and b16 == False and b17 == False and b18 == True:

            ans[2] = 'Q'
            if ans[6] != 'Q':   
                ans[6] = 'Q' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b15 == False and b16 == False and b17 == False and b14 == True and b18 == True:

            ans[2] = 'R'
            if ans[6] != 'R':   
                ans[6] = 'R' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b14 == False and b15 == False and b17 == False and b13 == True and b16 == True and b18 == True:

            ans[2] = 'S'
            if ans[6] != 'S':   
                ans[6] = 'S' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b14 == False and b15 == False and b16 == False and b17 == False and b13 == True and b18 == True:

            ans[2] = 'T'
            if ans[6] != 'T':   
                ans[6] = 'T' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b17 == False and b18 == False and b14 == True and b15 == True and b16 == True:

            ans[2] = 'U'
            if ans[6] != 'U':   
                ans[6] = 'U' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b15 == False and b18 == False and b17 == False and b14 == True and b16 == True:

            ans[2] = 'V'
            if ans[6] != 'V':   
                ans[6] = 'V' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b15 == False and b18 == False and b17 == False and b14 == True and b16 == True:

            ans[2] = 'W'
            if ans[6] != 'W':   
                ans[6] = 'W' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b14 == False and b17 == False and b18 == False and b15 == True and b16 == True:

            ans[2] = 'X'
            if ans[6] != 'X':   
                ans[6] = 'X' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b14 == False and b16 == False and b17 == False and b18 == False and b15 == True:

            ans[2] = 'Y'
            if ans[6] != 'Y':   
                ans[6] = 'Y' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        elif b13 == False and b16 == False and b17 == False and b18 == False and b14 == True and b15 == True:

            ans[2] = 'Z'
            if ans[6] != 'Z':   
                ans[6] = 'Z' 
                print("".join(ans[:3]))
                st = "".join(ans[:3])
                speak(st, "en")
                ans[5]=''

        else:
            ans[6]=''
            ans[5]=''
            ans[4]=''


        

        if b1 == True and b3 == True and b2 == True and b4 == True and b5 == True and b6 == True :
                ans[4]=''
                
        if b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True  :
                ans[5]=''
        if b13 == True and b16 == True and b17 == True and b18 == True and b14 == True and b15 == True:
                ans[6]=''


        
    elif b20 == False:
        while(j<1):
            speak("Hindi Pressed","en")
            j = j+1
            i=0
            k=0
            l=0
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

     #   else:
      #      hin[4]=''
#
        elif b7 == True and b9 == True and b8 == False and b10 == False and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            hin[1] = 'आ'
            if hin[5] != 'आ':   
                hin[5] = 'आ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
            

        elif b7 == True and b9 == False and b8 == False and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'इ'
            if hin[5] != 'इ':   
                hin[5] = 'इ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''


        elif b7 == True and b9 == True and b8 == True and b10 == False and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ई'
            if hin[5] != 'ई':   
                hin[5] = 'ई' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
            

        elif b7 == False and b9 == True and b8 == True and b10 == True and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'उ'
            if hin[5] != 'उ':   
                hin[5] = 'उ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
            

        elif b7 == False and b9 == False and b8 == True and b10 == False and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ऊ'
            if hin[5] != 'ऊ':   
                hin[5] = 'ऊ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == False and b9 == True and b8 == True and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ए'
            if hin[5] != 'ए':   
                hin[5] = 'ए' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
              

        elif b7 == True and b9 == True and b8 == False and b10 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ऐ'
            if hin[5] != 'ऐ':   
                hin[5] = 'ऐ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == False and b9 == True and b8 == True and b10 == False and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ओ'
            if hin[5] != 'ओ':   
                hin[5] = 'ओ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == True and b9 == False and b8 == False and b10 == True and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'औ'
            if hin[5] != 'औ':   
                hin[5] = 'औ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == False and b9 == True and b8 == True and b10 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'क'
            if hin[5] != 'क':   
                hin[5] = 'क' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == True and b9 == True and b8 == False and b10 == True and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ख'
            if hin[5] != 'ख':   
                hin[5] = 'ख' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == False and b9 == False and b8 == False and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ग'
            if hin[5] != 'ग':   
                hin[5] = 'ग' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == False and b9 == False and b8 == True and b10 == True and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'घ'
            if hin[5] != 'घ':   
                hin[5] = 'घ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == True and b9 == True and b8 == False and b10 == True and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ङ'
            if hin[5] != 'ङ':   
                hin[5] = 'ङ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == False and b9 == True and b8 == False and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'च'
            if hin[5] != 'च':   
                hin[5] = 'च' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == False and b9 == True and b8 == True and b10 == True and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'छ'
            if hin[5] != 'छ':   
                hin[5] = 'छ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == True and b9 == False and b8 == False and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ज'
            if hin[5] != 'ज':   
                hin[5] = 'ज' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == True and b9 == True and b8 == True and b10 == False and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'झ'
            if hin[5] != 'झ':   
                hin[5] = 'झ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == True and b9 == False and b8 == True and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ञ'
            if hin[5] != 'ञ':   
                hin[5] = 'ञ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == True and b9 == False and b8 == False and b10 == False and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ट'
            if hin[5] != 'ट':   
                hin[5] = 'ट' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == True and b9 == False and b8 == False and b10 == False and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ठ'
            if hin[5] != 'ठ':   
                hin[5] = 'ठ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == False and b9 == False and b8 == False and b10 == True and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ड'
            if hin[5] != 'ड':   
                hin[5] = 'ड' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                hin[1] = 'ड'
            print("".join(hin[:2]))
            st = "".join(hin[:2])
            speak(st, "hi")

        elif b7 == False and b9 == False and b8 == False and b10 == False and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ढ'
            if hin[5] != 'ढ':   
                hin[5] = 'ढ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == True and b9 == True and b8 == False and b10 == False and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ण'
            if hin[5] != 'ण':   
                hin[5] = 'ण' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == True and b9 == False and b8 == False and b10 == False and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'त'
            if hin[5] != 'त':   
                hin[5] = 'त' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == False and b9 == True and b8 == False and b10 == False and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'थ'
            if hin[5] != 'थ':   
                hin[5] = 'थ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == False and b9 == True and b8 == False and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'द'
            if hin[5] != 'द':   
                hin[5] = 'द' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                
        elif b7 == True and b9 == True and b8 == False and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ध'
            if hin[5] != 'ध':   
                hin[5] = 'ध' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == False and b9 == True and b8 == False and b10 == False and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'न'
            if hin[5] != 'न':   
                hin[5] = 'न' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                
        elif b7 == False and b9 == False and b8 == False and b10 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'प'
            if hin[5] != 'प':   
                hin[5] = 'प' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == True and b9 == False and b8 == True and b10 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'फ'
            if hin[5] != 'फ':   
                hin[5] = 'फ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == False and b9 == False and b8 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ब'
            if hin[5] != 'ब':   
                hin[5] = 'ब' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == True and b9 == True and b8 == False and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'भ'
            if hin[5] != 'भ':   
                hin[5] = 'भ' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                

        elif b7 == False and b9 == True and b8 == False and b10 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'म'
            if hin[5] != 'म':   
                hin[5] = 'म' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                

        elif b7 == False and b9 == True and b8 == False and b10 == False and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'य'
            if hin[5] != 'य':   
                hin[5] = 'य' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                

        elif b7 == False and b9 == False and b8 == True and b10 == False and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'र'
            if hin[5] != 'र':   
                hin[5] = 'र' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                

        elif b7 == False and b9 == False and b8 == True and b10 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ल'
            if hin[5] != 'ल':   
                hin[5] = 'ल' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                
        elif b7 == False and b9 == False and b8 == True and b10 == True and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'व'
            if hin[5] != 'व':   
                hin[5] = 'व' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                

        elif b7 == False and b9 == True and b8 == False and b10 == True and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'श'
            if hin[5] != 'श':   
                hin[5] = 'श' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == False and b9 == False and b8 == False and b10 == True and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ष'
            if hin[5] != 'ष':   
                hin[5] = 'ष' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == True and b9 == False and b8 == False and b10 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'स'
            if hin[5] != 'स':   
                hin[5] = 'स' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''
                

        elif b7 == False and b9 == False and b8 == True and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            hin[1] = 'ह'
            if hin[5] != 'ह':   
                hin[5] = 'ह' 
                print("".join(hin[:2]))
                st = "".join(hin[:2])
                speak(st, "hi")
                hin[4]=''

      #  else:
         #   hin[5]=''
                

        elif b13 == False and b15 == True and b14 == True and b16 == True and b17 == True and b18 == True:
            hin[2] = 'अ'
            if hin[6] != 'अ':   
                hin[6] = 'अ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''
            

        elif b13 == True and b15 == True and b14 == False and b16 == False and b17 == False and b18 == True:

            hin[2] = 'आ'
            if hin[6] != 'आ':   
                hin[6] = 'आ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == False and b14 == False and b16 == True and b17 == True and b18 == True:

            hin[2] = 'इ'
            if hin[6] != 'इ':   
                hin[6] = 'इ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == True and b14 == True and b16 == False and b17 == False and b18 == True:

            hin[2] = 'ई'
            if hin[6] != 'ई':   
                hin[6] = 'ई' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == True and b14 == True and b16 == True and b17 == False and b18 == False:

            hin[2] = 'उ'
            if hin[6] != 'उ':   
                hin[6] = 'उ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                
        elif b13 == False and b15 == False and b14 == True and b16 == False and b17 == True and b18 == False:

            hin[2] = 'ऊ'
            if hin[6] != 'ऊ':   
                hin[6] = 'ऊ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == True and b14 == True and b16 == False and b17 == True and b18 == True:

            hin[2] = 'ए'
            if hin[6] != 'ए':   
                hin[6] = 'ए' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == True and b14 == False and b16 == True and b17 == False and b18 == True:

            hin[2] = 'ऐ'
            if hin[6] != 'ऐ':   
                hin[6] = 'ऐ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == True and b14 == True and b16 == False and b17 == False and b18 == True:

            hin[2] = 'ओ'
            if hin[6] != 'ओ':   
                hin[6] = 'ओ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == False and b14 == False and b16 == True and b17 == True and b18 == False:

            hin[2] = 'औ'
            if hin[6] != 'औ':   
                hin[6] = 'औ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

               

        elif b13 == False and b15 == True and b14 == True and b16 == True and b17 == False and b18 == True:

            hin[2] = 'क'
            if hin[6] != 'क':   
                hin[6] = 'क' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == True and b14 == False and b16 == True and b17 == True and b18 == False:

            hin[2] = 'ख'
            if hin[6] != 'ख':   
                hin[6] = 'ख' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                
        elif b13 == False and b15 == False and b14 == False and b16 == False and b17 == True and b18 == True:

            hin[2] = 'ग'
            if hin[6] != 'ग':   
                hin[6] = 'ग' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''


        elif b13 == False and b15 == False and b14 == True and b16 == True and b17 == True and b18 == False:

            hin[2] = 'घ'
            if hin[6] != 'घ':   
                hin[6] = 'घ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == True and b14 == False and b16 == True and b17 == False and b18 == False:

            hin[2] = 'ङ'
            if hin[6] != 'ङ':   
                hin[6] = 'ङ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                
        elif b13 == False and b15 == True and b14 == False and b16 == True and b17 == True and b18 == True:

            hin[2] = 'च'
            if hin[6] != 'च':   
                hin[6] = 'च' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == True and b14 == True and b16 == True and b17 == True and b18 == False:

            hin[2] = 'छ'
            if hin[6] != 'छ':   
                hin[6] = 'छ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == False and b14 == False and b16 == False and b17 == True and b18 == True:

            hin[2] = 'ज'
            if hin[6] != 'ज':   
                hin[6] = 'ज' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == True and b14 == True and b16 == False and b17 == False and b18 == False:

            hin[2] = 'झ'
            if hin[6] != 'झ':   
                hin[6] = 'झ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == False and b14 == True and b16 == False and b17 == True and b18 == True:

            hin[2] = 'ञ'
            if hin[6] != 'ञ':   
                hin[6] = 'ञ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == False and b14 == False and b16 == False and b17 == False and b18 == False:

            hin[2] = 'ट'
            if hin[6] != 'ट':   
                hin[6] = 'ट' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == False and b14 == False and b16 == False and b17 == True and b18 == False:

            hin[2] = 'ठ'
            if hin[6] != 'ठ':   
                hin[6] = 'ठ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == False and b14 == False and b16 == True and b17 == True and b18 == False:

            hin[2] = 'ड'
            if hin[6] != 'ड':   
                hin[6] = 'ड' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == False and b14 == False and b16 == False and b17 == False and b18 == False:

            hin[2] = 'ढ'
            if hin[6] != 'ढ':   
                hin[6] = 'ढ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == True and b14 == False and b16 == False and b17 == False and b18 == False:

            hin[2] = 'ण'
            if hin[6] != 'ण':   
                hin[6] = 'ण' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == False and b14 == False and b16 == False and b17 == False and b18 == True:

            hin[2] = 'त'
            if hin[6] != 'त':   
                hin[6] = 'त' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == True and b14 == False and b16 == False and b17 == True and b18 == False:

            hin[2] = 'थ'
            if hin[6] != 'थ':   
                hin[6] = 'थ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == True and b14 == False and b16 == False and b17 == True and b18 == True:

            hin[2] = 'द'
            if hin[6] != 'द':   
                hin[6] = 'द' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == True and b14 == False and b16 == True and b17 == True and b18 == True:

            hin[2] = 'ध'
            if hin[6] != 'ध':   
                hin[6] = 'ध' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == True and b14 == False and b16 == False and b17 == False and b18 == True:

            hin[2] = 'न'
            if hin[6] != 'न':   
                hin[6] = 'न' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == False and b14 == False and b16 == True and b17 == False and b18 == True:

            hin[2] = 'प'
            if hin[6] != 'प':   
                hin[6] = 'प' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == False and b14 == True and b16 == True and b17 == False and b18 == True:

            hin[2] = 'फ'
            if hin[6] != 'फ':   
                hin[6] = 'फ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == False and b14 == True and b16 == True and b17 == True and b18 == True:

            hin[2] = 'ब'
            if hin[6] != 'ब':   
                hin[6] = 'ब' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == True and b14 == False and b16 == False and b17 == True and b18 == True:

            hin[2] = 'भ'
            if hin[6] != 'भ':   
                hin[6] = 'भ' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == True and b14 == False and b16 == True and b17 == False and b18 == True:

            hin[2] = 'म'
            if hin[6] != 'म':   
                hin[6] = 'म' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == True and b14 == False and b16 == False and b17 == False and b18 == False:

            hin[2] = 'य'
            if hin[6] != 'य':   
                hin[6] = 'य' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == False and b14 == True and b16 == False and b17 == False and b18 == True:

            hin[2] = 'र'
            if hin[6] != 'र':   
                hin[6] = 'र' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == False and b14 == True and b16 == True and b17 == False and b18 == True:

            hin[2] = 'ल'
            if hin[6] != 'ल':   
                hin[6] = 'ल' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == False and b14 == True and b16 == True and b17 == False and b18 == False:

            hin[2] = 'व'
            if hin[6] != 'व':   
                hin[6] = 'व' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == True and b14 == False and b16 == True and b17 == True and b18 == False:

            hin[2] = 'श'
            if hin[6] != 'श':   
                hin[6] = 'श' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                
        elif b13 == False and b15 == False and b14 == False and b16 == True and b17 == False and b18 == False:

            hin[2] = 'ष'
            if hin[6] != 'ष':   
                hin[6] = 'ष' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == True and b15 == False and b14 == False and b16 == True and b17 == False and b18 == True:

            hin[2] = 'स'
            if hin[6] != 'स':   
                hin[6] = 'स' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''

                

        elif b13 == False and b15 == False and b14 == True and b16 == False and b17 == True and b18 == True:

            hin[2] = 'ह'
            if hin[6] != 'ह':   
                hin[6] = 'ह' 
                print("".join(hin[:3]))
                st = "".join(hin[:3])
                speak(st, "hi")
                hin[5]=''


        else:
            hin[6]=''
            hin[5]=''
            hin[4]=''

        if b1 == True and b3 == True and b2 == True and b4 == True and b5 == True and b6 == True :
                hin[4]=''
                
        if b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True  :
                hin[5]=''
        if b13 == True and b16 == True and b17 == True and b18 == True and b14 == True and b15 == True:
                hin[6]=''


    elif b21 == False:
        while(k<1):
            speak("Math Pressed","en")
            k = k+1
            i=0
            j=0
            l=0
            break
        
       
        if b1 == False and b3 == False and b2 == True and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[0] = '2'
            if math[4] != '2':
                print("".join(math[:1]))
                math[4] = '2'
                speak(math[4], "en")    
            
        elif b1 == False and b2 == False and b3 == True and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[0] = '3'
            if math[4] != '3':
                print("".join(math[:1]))
                math[4] = '3'
                speak(math[4], "en")
            
        elif b1 == False and b2 == False and b4 == False and b3 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[0] = '4'
            if math[4] != '4':
                print("".join(math[:1]))
                math[4] = '4'
                speak(math[4], "en")
            
        elif b1 == False and b4 == False and b2 == True and b3 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[0] = '5'
            if math[4] != '5':
                print("".join(math[:1]))
                math[4] = '5'
                speak(math[4], "en")
            
        elif b1 == False and b2 == False and b3 == False and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[0] = '6'
            if math[4] != '6':
                print("".join(math[:1]))
                math[4] = '6'
                speak(math[4], "en")
            
        elif b1 == False and b2 == False and b3 == False and b4 == False and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[0] = '7'
            if math[4] != '7':
                print("".join(math[:1]))
                math[4] = '7'
                speak(math[4], "en")
            
        elif b1 == False and b3 == False and b4 == False and b2 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[0] = '8'
            if math[4] != '8':
                print("".join(math[:1]))
                math[4] = '8'
                speak(math[4], "en")
            
        elif b2 == False and b3 == False and b1 == True and b4 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[0] = '9'
            if math[4] != '9':
                print("".join(math[:1]))
                math[4] = '9'
                speak(math[4], "en")
            
        elif b2 == False and b3 == False and b4 == False and b1 == True and b5 == True and b6 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[0] = '0'
            if math[4] != '0':
                print("".join(math[:1]))
                math[4] = '0'
                speak(math[4], "en")
            
        elif b1 == False and b4 == True and b5 == True and b6 == True and b2 == True and b3 == True and \
                b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[0] = '1'
            if math[4] != '1':
                print("".join(math[:1]))
                math[4] = '1'
                speak(math[4], "en")
       # else:
         #   math[4]=''
            

        elif b7 == False and b9 == True and b8 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:

            math[1] = '1'
            if math[5] != '1':   
                math[5] = '1' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(st, "en")
                math[4]=''
            

        elif b7 == False and b9 == False and b8 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[1] = '2'
            if math[5] != '2':   
                math[5] = '2' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(st, "en")
                math[4]=''
            

        elif b7 == False and b8 == False and b9 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[1] = '3'
            if math[5] != '3':   
                math[5] = '3' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(st, "en")
                math[4]=''
            

        elif b7 == False and b8 == False and b10 == False and b9 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[1] = '4'
            if math[5] != '4':   
                math[5] = '4' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(st, "en")
                math[4]=''
            

        elif b7 == False and b10 == False and b8 == True and b9 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[1] = '5'
            if math[5] != '5':   
                math[5] = '5' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(st, "en")
                math[4]=''
            

        elif b7 == False and b8 == False and b9 == False and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[1] = '6'
            if math[5] != '6':   
                math[5] = '6' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(st, "en")
                math[4]=''
            

        elif b7 == False and b8 == False and b9 == False and b10 == False and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[1] = '7'
            if math[5] != '7':   
                math[5] = '7' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(st, "en")
                math[4]=''
            

        elif b7 == False and b9 == False and b10 == False and b8 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[1] = '8'
            if math[5] != '8':   
                math[5] = '8' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(st, "en")
                math[4]=''
            

        elif b8 == False and b9 == False and b7 == True and b10 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[1] = '9'
            if math[5] != '9':   
                math[5] = '9' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(st, "en")
                math[4]=''
            

        elif b8 == False and b9 == False and b10 == False and b7 == True and b11 == True and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[1] = '0'
            if math[5] != '0':   
                math[5] = '0' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(st, "en")
                math[4]=''
            

        elif b8 == True and b9 == False and b10 == False and b7 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[1] = '+'
            if math[5] != '+':   
                math[5] = '+' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(st, "en")
                math[4]=''
                math[2]=''
            

        elif b8 == True and b9 == True and b10 == True and b7 == True and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[1] = '-'
            if math[5] != '-':   
                math[5] = '-' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(math[0]+"minus", "en")
                math[4]=''
                math[2]=''
            
    
        elif b8 == True and b9 == True and b10 == False and b7 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[1] = '*'
            if math[5] != '*':   
                math[5] = '*' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(math[0]+"multiply", "en")
                math[4]=''
                math[2]=''
            
    

        elif b8 == False and b9 == True and b10 == False and b7 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[1] = '>'
            if math[5] != '>':   
                math[5] = '>' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(st, "en")
                math[4]=''
                math[2]=''
                m=0
                n=0
                o=0
            
    

        elif b8 == True and b9 == False and b10 == True and b7 == False and b11 == True and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[1] = '<'
            if math[5] != '<':   
                math[5] = '<' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(st, "en")
                math[4]=''
                math[2]=''
                m=0
                n=0
                o=0
            
    
        elif b8 == False and b9 == True and b10 == True and b7 == True and b11 == False and b12 == True and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[1] = '/'
            if math[5] != '/':   
                math[5] = '/' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(math[0]+"divide", "en")
                math[4]=''
                math[2]=''
            

        elif b8 == True and b9 == False and b10 == False and b7 == True and b11 == False and b12 == False and \
                b13 == True and b14 == True and b15 == True and b16 == True and b17 == True and b18 == True:
            math[1] = '='
            if math[5] != '=':   
                math[5] = '=' 
                print("".join(math[:2]))
                st = "".join(math[:2])
                speak(st, "en")
                math[4]=''
                math[2]=''
                m=0
                n=0
                o=0
            
     ##  else:
       #     math[5]=''

        elif b13 == False and b15 == True and b14 == True and b16 == True and b17 == True and b18 == True:
            math[2] = '1'
            if math[6] != '1':   
                math[6] = '1' 
                print("".join(math[:3]))
                st = "".join(math[:3])
                if(math[1] == '-' or math[1]=='*' or math[1]=='/'):
                    if(math[1]=='-'):
                        speak(math[0]+"minus"+math[2],"en")
                    if(math[1]=='*'):
                        speak(math[0]+"multiply"+math[2],"en")
                    if(math[1]=='/'):
                        speak(math[0]+"divide"+math[2],"en")

                else:
                    speak(st, "en")
                math[5]=''
            

        elif b13 == False and b15 == False and b14 == True and b16 == True and b17 == True and b18 == True:
            math[2] = '2'
            if math[6] != '2':   
                math[6] = '2' 
                print("".join(math[:3]))
                st = "".join(math[:3])
                speak(st, "en")
                math[5]=''
                m=0
                n=0
                o=0

            

        elif b13 == False and b14 == False and b15 == True and b16 == True and b17 == True and b18 == True:
            math[2] = '3'
            if math[6] != '3':   
                math[6] = '3' 
                print("".join(math[:3]))
                st = "".join(math[:3])
                speak(st, "en")
                math[5]=''
                m=0
                n=0
                o=0

            
    
        elif b13 == False and b14 == False and b16 == False and b15 == True and b17 == True and b18 == True:
            math[2] = '4'
            if math[6] != '4':   
                math[6] = '4' 
                print("".join(math[:3]))
                st = "".join(math[:3])
                speak(st, "en")
                math[5]=''
                m=0
                n=0
                o=0

            

        elif b13 == False and b16 == False and b14 == True and b15 == True and b17 == True and b18 == True:
            math[2] = '5'
            if math[6] != '5':   
                math[6] = '5' 
                print("".join(math[:3]))
                st = "".join(math[:3])
                speak(st, "en")
                math[5]=''
                m=0
                n=0
                o=0
            

        elif b13 == False and b14 == False and b15 == False and b16 == True and b17 == True and b18 == True:
            math[2] = '6'
            if math[6] != '6':   
                math[6] = '6' 
                print("".join(math[:3]))
                st = "".join(math[:3])
                speak(st, "en")
                math[5]=''
                m=0
                n=0
                o=0
            

        elif b13 == False and b14 == False and b15 == False and b16 == False and b17 == True and b18 == True:
            math[2] = '7'
            if math[6] != '7':   
                math[6] = '7' 
                print("".join(math[:3]))
                st = "".join(math[:3])
                speak(st, "en")
                math[5]=''
                m=0
                n=0
                o=0
            

        elif b13 == False and b15 == False and b16 == False and b14 == True and b17 == True and b18 == True:
            math[2] = '8'
            if math[6] != '8':   
                math[6] = '8' 
                print("".join(math[:3]))
                st = "".join(math[:3])
                speak(st, "en")
                math[5]=''
                m=0
                n=0
                o=0
            

        elif b14 == False and b15 == False and b13 == True and b16 == True and b17 == True and b18 == True:
            math[2] = '9'
            if math[6] != '9':   
                math[6] = '9' 
                print("".join(math[:3]))
                st = "".join(math[:3])
                speak(st, "en")
                math[5]=''
                m=0
                n=0
                o=0
            

        elif b14 == False and b15 == False and b16 == False and b13 == True and b17 == True and b18 == True:
            math[2] = '0'
            if math[6] != '0':   
                math[6] = '0' 
                print("".join(math[:3]))
                st = "".join(math[:3])
                speak(st, "en")
                math[5]=''
                m=0
                n=0
                o=0
            

        else:
            math[6]=''
            math[5]=''
            math[4]=''

        if b1 == True and b3 == True and b2 == True and b4 == True and b5 == True and b6 == True :
                math[4]=''
                m=0
                n=0
                o=0
                
        if b7 == True and b8 == True and b9 == True and b10 == True and b11 == True and b12 == True  :
                math[5]=''
                m=0
                n=0
                o=0
        if b13 == True and b16 == True and b17 == True and b18 == True and b14 == True and b15 == True:
                math[6]=''
                m=0
                n=0
                o=0
            

        if (math[1] == '+' or math[1] == '-' or math[1] == '*' or math[1] == '/' or math[1] == '>' or math[1] =='<' or math[1] == '='):
           
            if(math[1] == '+' and math[2]!='' ):
                if math[7] != int(int(math[0]) + int(math[2])):
                    x = int(math[0]) + int(math[2])
                    print(x)
                    math[7] = int(x)
                    speak(str(x), "en")
                    math[2]=''
                    
            elif(math[1] == '-'and math[2]!=''):
                if math[7] != int(int(math[0]) - int(math[2])):
                    x = int(math[0]) - int(math[2])
                    print(x)
                    math[7] = int(x)
                    speak(str(x), "en")
                    math[2]=''
                

        
            elif(math[1] == '>'and math[2]!=''):
                while(m<1):
                    m=m+1
                    n=0
                    o=0
                    if(int(math[0])) > int(math[2]):
                        speak("True","en")
                    else:
                        speak("False", "en")
                    math[2]=''
    
            elif(math[1] == '<'and math[2]!=''):
                while(n<1):
                    n=n+1
                    m=0
                    o=0
                    if int(math[0]) < int(math[2]):
                        speak("True","en")
                    else:
                        speak("False", "en")
                    math[2]=''
    

            elif(math[1] == '='and math[2]!=''):
                while(o<1):
                    o=o+1
                    m=0
                    n=0
                    if(int(math[0]) == int(math[2])):
                        speak("Equal","en")
                    else:
                        speak("Not Equal", "en")
                    math[2]=''
    

            elif(math[1] == '*' and math[2]!=''):
                if math[7] != int(int(math[0]) * int(math[2])):
                    x = int(math[0]) * int(math[2])
                    print(x)
                    math[7] = int(x)
                    speak(str(x), "en")
                    math[2]=''
                

            elif(math[1] == '/' and math[2]!=''):
                if(math[2] == '0'):
                    if(math[7]!='0'):
                        math[7]='0'
                        math[2]=''
                        speak("Cannot divide by zero","en")
                elif math[7] != int(int(math[0]) / int(math[2])):
                    x = int(math[0]) / int(math[2])
                    print(x)
                    math[7] = int(x)
                    speak(str(x), "en")
                    math[2]=''
            else:
                m=0
                n=0
                o=0
                
            

    else:
        speak("Please check the button and try again","en")
                
GPIO.cleanup()
        

