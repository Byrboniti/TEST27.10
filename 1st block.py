import re
class ekr_email():
    def ekr(self,email):
        box = (email.split('@'))[0]
        for i in range(0,len(box)):
            box = box[:i] + 'x'
        return (box+'@'+(email.split('@'))[1])

class ekr_phone():
    def ekr(self,len_ekr,phone):
        list_phone = (phone.split())
        new = ''
        for i in list_phone:
            new = new+ i
        lst = list(new)[::-1]
        for i in lst:
            if lst.index(i) < len_ekr:
                lst[lst.index(i)] = 'X'
        lst.insert(3,' ')
        lst.insert(7,' ')
        lst.insert(11,' ')
        lst = lst[::-1]
        fin=''
        for i in lst:
            fin = fin +i
        return fin
class ekr_skype():
    def ekr(self,skype):

        pattern = 'skype:'
        skype= re.split(pattern,skype)

        if len(skype[0])!=0:
            end = skype[1]
            lst = end.split('?')

            print(skype[0]+'skype:xxx'+'?'+lst[1])
        else:
            print('skype:xxx')




