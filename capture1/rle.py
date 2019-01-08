class RunLength(object):

    @classmethod
    def encode(self, strings):
        start = 0
        encoded_strings = ''
        strings += ' '
        for i in range(1, len(strings)):
            if strings[i] != strings[i-1]:
                encoded_strings += str(i - start) + strings[start]
                start = i
        return encoded_strings

    @classmethod
    def decode(self, strings):
        decoded_strings = ''
        for i in range(0, len(strings), 2):
            decoded_strings += int(strings[i]) * strings[i+1]
        return decoded_strings