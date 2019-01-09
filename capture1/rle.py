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
        str_count = ''
        for i in range(0, len(strings)):
            if strings[i].isalpha():
                decoded_strings += int(str_count) * strings[i]
                str_count = ''
            else:
                str_count += strings[i]
        return decoded_strings