"""
needle in the haystack

Criar uma função que simula o grep do linux
GREP é uma função para achar uma string dentro de um arquivo

seja haystack = 'aweabcaiwuedfabcahsiu'
needle = 'abc'

what is the best approuch?
Space complexity?
time complexity?


"""
haystack = 'aweabcaiwuedfabcahsiu
needle = 'abc'

l = []
for i in range(len(haystack)) :
    if needle == haystack[i:i+(len(needle))] :
        l.append(i)
print(l)


