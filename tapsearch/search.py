class Search:
    def __init__(self, text, word):
        self.text = text

        self.word = word
    def search(self):
        self.text = self.text.lower()
        text = "".join(c for c in self.text if c not in ('!','.',':'))
        paras = text.split('\r\n\r\n')
        l = len(paras)
        dic = {}
        for para in range(len(paras)):
            words = paras[para].split()
            for word in words:
                if word not in dic:
                    li = [0] * l
                    dic[word] = li
                    dic[word][para] = 1

                else:
                    dic[word][para] += 1
        # found_index = list(zip(found, list(range(l))))
        # found_index.sort(key = lambda elem:elem[0], reverse=True)
        a = dic[self.word]
        ans = [i+1 for i in range(len(a)) if a[i] > 0]
        return (ans[:10])

    def paras_no(self):
        self.text = self.text.lower()
        text = "".join(c for c in self.text if c not in ('!','.',':'))
        paras = text.split('\r\n\r\n')
        return len(paras)
