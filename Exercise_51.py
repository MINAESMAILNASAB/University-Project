class kharchang:
    def setDNA(self, str):
        stmp = ""
        if len(str) < 10:
            stmp = str + str
        else:
            stmp = str
            s = str[0:10]
            stmp += s
        return stmp

    def RepDNA(self, s):
        tmp = s
        tmp = tmp.replace("tt", "o")
        return tmp
        
class bobEsfanji(kharchang):
    def bublesort(self, s):
        a = len(s)
        st = str(a)
        charArr = list(st)
        for i in range(len(st) - 1):
            for j in range(len(st) - i - 2):
                if charArr[j] > charArr[j + 1]:
                    as1 = charArr[j]
                    charArr[j] = charArr[j + 1]
                    charArr[j + 1] = as1
        st = ''.join(charArr)
        return st
        
class okhtapos:
    def LSearch(self, s):
        tmp = s
        for i in range(len(s)):
            if s[i] == 'x':
                tmp = tmp + str(i)
                return tmp
        return tmp

    def OO(self, s):
        for i in range(len(s) - 2):
            tmp = s[i:i+3]
            if tmp[0] == tmp[1] == tmp[2]:
                s = s.replace(tmp, "(0_0)")
        return s
        
stri = input()
if len(stri) >= 10 and len(stri) <= 10000:
            if stri[0] == 'm':
                c1 = kharchang()
                r = c1.RepDNA(c1.setDNA(str))
                print(r)
            else:
                if stri[0] == 's' and stri[1] != 'b':
                    oc = okhtapos()
                    r = oc.LSearch(oc.OO(stri))
                    print(r)
                elif stri[0] == 's' and stri[1] == 'b':
                    bc = bobEsfanji()
                    r = bc.RepDNA(bc.setDNA(stri))
                    print(r)
                    print(bc.bublesort(stri))
                else:
                    print("invalid input")