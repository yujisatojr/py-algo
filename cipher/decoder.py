class Decode:
    def __init__(self):
        self.alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def cipher(self, line, key):
        for i in range(0, len(line)):
            letter = line[i]

            if (letter == ' '):
                print(' ', end='')
                continue

            index = self.alph.index(letter)
            index += key

            if (index > 26):
                index -= 26

            index = index % 26
            cipher = self.alph[index]
            print(cipher, end='')

decode = Decode()
# specify your decoded message and key here
decode.cipher('PBZOBQ QBUQP', 3)
