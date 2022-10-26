from platform import system

class op:
    def cls():
        clear = ''

        if system() != 'Windows':
            clear = 'clear'
        else:
            clear = 'cls'

        return clear
    