from logging import exception


class WordsFinder:

    def __init__(self, *f_names: str):
        self.file_names = f_names

    def __str__(self):
        return str(self.file_names)

    def get_all_words(self):
        all_words = {}
        for f_name_ in self.file_names:
            all_words[f_name_] = []
            with (open(f_name_, 'r', encoding='utf-8') as file):
                str_ = file.read().lower().translate(str.maketrans(',/=!?;:\n', '        ')
                                                     ).replace(' - ', ' ').replace('  ', ' ').strip(' ')
                for w_ in str_.split(' '):
                    all_words[f_name_].append(w_)
        return all_words

    def find(self, word):
        out_dic = {}
        for fn_, wrds_ in self.get_all_words().items():
            try:
                n = list(wrds_).index(word.lower())
            except ValueError:
                pass
            else:
                out_dic[fn_] = n + 1
        return out_dic

    def count(self, word):
        out_dic = {}
        for fn_, wrds_ in self.get_all_words().items():
            out_dic[fn_] = wrds_.count(word.lower())
        return out_dic


# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words())
#
# print(finder2.find('TEXT'))
# print(finder2.count('teXT'))

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
finder1 = WordsFinder('Rudyard Kipling - If.txt')
print(finder1.get_all_words())

print(len(list(finder1.get_all_words()['Rudyard Kipling - If.txt'])))
#
# print(finder1.find('the'))
# print(finder1.count('the'))