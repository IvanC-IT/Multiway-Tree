class Tree:
    def __init__(self,V):
        self.id=V
        self.f=[]

def fromLista1(lista):
    '''Create tree from a list [value, childlist]
            Where child list contains trees or is the list empty. '''
    r=Tree(lista[0])
    r.f=[fromLista1(x) for x in lista[1]]
    return r
def toLista(node):
    ''' Convert the tree to a list of lists [value, childlist]'''
    return [node.id, [toLista(x) for x in node.f]] 

def converti(root):
    if not root.f:
        #      stringa    c  w  h
        return [root.id], 0, 2, 1
    N = len(root.f)
    sottoalberi = [ converti(son) for son in root.f ]
    # se 1
    righe, c, w, H = sottoalberi[0]
    if N==1:
        prima_riga   = ' '*c + root.id + ' '*(w-c-2)
        seconda_riga = ' '*c + '|'     + ' '*(w-c-1)
        righe[0:0] = [prima_riga, seconda_riga]
        return righe, c, w, H+2
    # se N
    pad(sottoalberi)
    righe, A, B, W, H = concatena(sottoalberi)
    centro = (A+B)//2
    riga1 = ' '*centro + root.id + ' '*(W-centro-2)
    riga2 = ' '*(A+1) + '_'*(centro-A-1) + '|' + '_'*(B-centro-1) + ' '*(W-B)
    riga3 = '  '.join([ ' '*c + '|'+' '*(w-c-1) for _,c,w,_ in sottoalberi ] )
    righe[0:0] = [ riga1, riga2, riga3 ]
    return righe, centro, W, H+3

def concatena(sottoalberi):
    testi, a, W, h = sottoalberi[0]
    b = a
    for righe, c, w, h1 in sottoalberi[1:]:
        b  = W + c + 2
        W += w + 2
        for i, riga in enumerate(righe):
            testi[i] += '  ' + riga
    return testi, a, b, W, h

def pad(sottoalberi):
    H = 0
    for righe, _c, _w, _h in sottoalberi:
        H = max(H,len(righe))
    for righe, _c,  w, _h in sottoalberi:
        h = len(righe)
        if h < H:
            pad = ' '*w
            righe.extend([pad]*(H-h))

def es2(r):
    righe, c, w, h = converti(r)
    return '\n'.join(righe)
       

if __name__ == '__main__':

    # enter your personal test instructions here
    lista = ['100', [['02', [['01', []]]], ['10', [['01', []], ['02', [['03' , []], ['06', []]]], ['09', []], ['08', []], ['30', []]]], ['06', []]]]
    r = fromLista1 (lista)
    print (es2 (r))
