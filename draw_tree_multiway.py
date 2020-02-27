# - * - coding: utf-8 - * -
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

def convert(root):
    if not root.f:
        #      string     c  w  h
        return [root.id], 0, 2, 1
    N = len(root.f)
    subtrees = [convert (son) for son in root.f]
    # if 1
    rows, c, w, H = subtrees [0]
    if N == 1:
        first_line = '' * c + root.id + '' * (w-c-2)
        second_line = '' * c + '|' + '' * (w-c-1)
        rows [0: 0] = [first_line, second_line]
        return rows, c, w, H + 2
    # if N
    pad(subtrees)
    rows, A, B, W, H = concatenate(subtrees)
    center = (A + B) // 2
    row1 = '' * center + root.id + '' * (W-center-2)
    row2 = '' * (A + 1) + '_' * (center-A-1) + '|' + '_' * (B-center-1) + '' * (W-B)
    row3 = '' .join (['' * c + '|' + '' * (w-c-1) for _, c, w, _ in subtrees])
    rows[0:0] = [row1, row2, row3]
    return rows, center, W, H + 3

def concatenate(subtrees):
    '' 'concatenate rows of subtrees of the same number of rows by entering 2 spaces' ''
    texts, a, W, h = subtrees [0]
    b = a
    for lines, c, w, h1 in subtrees [1:]:
        b = W + c + 2
        W += w + 2
        for i,row in enumerate(rows):
            texts [i] += '' + row
    return texts, a, b, W, h

def pad(subtrees):
    H = 0
    for lines, _c, _w, _h in subtrees:
        H = max (H, len (lines))
    for lines, _c, w, _h in subtrees:
        h = len (lines)
        if h <H:
            pad = '' * w
            rows.extend ([pad] * (H-h))

def es2(r):
    #insert your code here
    lines, c, w, h = convert (r)
    return '\ n'.join (lines)


if __name__ == '__main__':
    # enter your personal test instructions here
    list = ['100', [['02', [['01', []]]], ['10', [['01', []], ['02', [['03' , []], ['06', []]]], ['09', []], ['08', []], ['30', []]]], ['06', []]]]
    r = fromLista1 (list)
    print (es2 (r))