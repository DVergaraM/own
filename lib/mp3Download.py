from pytube import YouTube
import os
from lib.module.config import tokens
from lib.module.builtIn import op, asciiText
from colorama import Fore, Style


os.system(op.cls())

def search(url:str):
    try: 
        YT = YouTube(url)
        video = YT.streams.filter(only_audio=True).first()
        import lib.module.load
        output = video.download(output_path='./media/audio/')
        base, ext = os.path.splitext(output)
        newFile = base + '.mp3'
        os.rename(output, newFile)
        print(f'\n"{YT.title}" ha sido descargado con exito como audio')
    except FileExistsError:
        YT = YouTube(url)
        video = YT.streams.filter(only_audio=True).first()
        import lib.module.load
        output = video.download(output_path='./media/video/')
        base, ext = os.path.splitext(output)
        newFile = base + '.mp4'
        os.rename(output, newFile)
        print(f'\n"{YT.title}" ha sido descargado con exito como video')
    except OSError:
        exit()


def main():
    asciiText('./media/text/mp3Download.txt', Fore.LIGHTYELLOW_EX, Style.BRIGHT, Style.RESET_ALL, '\n')

    url = str(input('Ingrese el enlace del vídeo (Youtube): '))

    opt = 1
    while not (opt != 1):
        search(url)
        opt = int(input('\n0 para volver al menu principal\n1 para salir\n[?]: '))
        print('\n')
        if opt == 1:
            exit()
        elif opt == 0:
            break
        else: main()
main()