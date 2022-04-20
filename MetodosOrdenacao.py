import math
from CriaVetor import CriaVetor, CriaVetor100, CriaVetor1m, CriaVetor10m, CriaVetor100m, CriaVetor1M



def MetodoTiago(vetor):

    def Insere(vetor, valor, pos):
        i=1
        while i < (len(vetor)-pos):
            vetor[len(vetor)-i] = vetor[len(vetor)-i-1]
            i+=1
        vetor[pos] = valor
        return vetor
    
    cont = 0
    a = 0
    while cont < len(vetor)+a:  
        i=1
        j=0
        while vetor[len(vetor)-i] > vetor[j]:
            j+=1
        
        Insere(vetor, vetor[len(vetor)-i], j)
                
        if len(vetor)-i == j:
            vetor[0], vetor[-i] = vetor[-i], vetor[0]
            a = cont
        cont+=1
    return vetor



def MetodoPatrick(vetor, faixa):
    resultado = []
    for z in range(1,faixa):
        for y in range(0, len(vetor)):
            if vetor[y]==z:
                resultado.append(vetor[y])
    return resultado



def BubbleSort(vetor):
    for passnum in range(len(vetor)-1,0,-1):
        for i in range(passnum):
            if vetor[i]>vetor[i+1]:
                temp = vetor[i]
                vetor[i] = vetor[i+1]
                vetor[i+1] = temp
    return vetor



def MeuInsercao(vetor):
    for i in range (1, len(vetor)):
        j = i
        while j>0:
            if vetor[j-1]>vetor[j]:
                vetor[j-1], vetor[j] = vetor[j], vetor[j-1]
                j=j-1
            else:
                j = 0
    return vetor



def Insercao(vetor):
    n = len(vetor)
    for j in range(1, n):
        chave = vetor[j]
        i = j - 1
        while i >= 0 and vetor[i] > chave:
            vetor[i + 1] = vetor[i]
            i = i - 1
        vetor[i + 1] = chave
    return vetor



def ShortBubbleSort(vetor):
    exchanges = True
    passnum = len(vetor)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if vetor[i]>vetor[i+1]:
               exchanges = True
               temp = vetor[i]
               vetor[i] = vetor[i+1]
               vetor[i+1] = temp
       passnum = passnum-1
    return vetor



def MergeSort(vetor):
    if len(vetor) > 1:
        mid = len(vetor)//2
        L = vetor[:mid]
        R = vetor[mid:]
        MergeSort(L)
        MergeSort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                vetor[k] = L[i]
                i += 1
            else:
                vetor[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            vetor[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            vetor[k] = R[j]
            j += 1
            k += 1
    return vetor



def MergeSortNR(vetor):
    passo = 2
    tamanho = len(vetor)-1
    while passo <= 2 ** (int(math.log2(tamanho)) + 1) :
        for i in range(0,tamanho,passo):        
            f = i+passo-1
            if f > tamanho:
                f = tamanho
            m = (i + f) // 2
            x = i
            y = m + 1
            vetor_auxiliar = []
            while (x <= m) and (y <= f):
                if vetor[x] < vetor[y]:
                    vetor_auxiliar.append(vetor[x])
                    x = x + 1
                else:
                    vetor_auxiliar.append(vetor[y])
                    y = y + 1
            if x > m:
                while y <= f:
                    vetor_auxiliar.append(vetor[y])
                    y = y + 1
            else:
                while x <= m:
                    vetor_auxiliar.append(vetor[x])
                    x = x + 1               
            y = i
            for x in range(len(vetor_auxiliar)):         
                vetor[y] = vetor_auxiliar[x]
                y = y + 1
            vetor_auxiliar = []
        passo = passo * 2



def MeuShellSort(vetor):
    tamanho = len(vetor)
    passo = tamanho//2
    while passo > 0:
        i=0
        while i < passo:
            x=0
            while x + i + passo < tamanho:
                if vetor[x+i] > vetor[x+i+passo]:
                    vetor[x+i], vetor[x+i+passo] = vetor[x+i+passo], vetor[x+i]
                    a = x + i - passo
                    while a >= 0:
                        if vetor[a] > vetor[a+passo]:
                            vetor[a], vetor[a+passo] = vetor[a+passo], vetor[a]
                            a = a-passo
                        else:
                            a=-1
                x = x + passo
            i+=1
        passo=passo//2



def ShellSort(vetor):
    n = len(vetor)
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = vetor[i]
            j = i
            while j >= interval and vetor[j - interval] > temp:
                vetor[j] = vetor[j - interval]
                j -= interval
            vetor[j] = temp
        interval //= 2
    return vetor



def MeuSelecao(vetor):
    for i in range(len(vetor)-1):
        j=i
        while j <= len(vetor)-2:
            k=j+1
            indexmenor = j
            while k <= len(vetor)-1:
                if vetor[j]>vetor[k]:
                    indexmenor = k
                    j = k
                    k = j+1
                else:
                    k+=1
            vetor[i], vetor[indexmenor] = vetor[indexmenor], vetor[i]
            j=len(vetor)
    return vetor



def Selecao(vetor):
    n = len(vetor)
    # Percorre o arranjo A.
    for i in range(n):
        # Encontra o elemento mínimo em A.
        minimo = i
        for j in range(i + 1, n):
            if vetor[minimo] > vetor[j]:
                minimo = j
        # Coloca o elemento mínimo na posição correta.
        vetor[i], vetor[minimo] = vetor[minimo], vetor[i]
    return vetor



def QuickSort(vetor):
   quickSortHelper(vetor,0,len(vetor)-1)
def quickSortHelper(vetor,first,last):
   if first<last:
       splitpoint = partition(vetor,first,last)
       quickSortHelper(vetor,first,splitpoint-1)
       quickSortHelper(vetor,splitpoint+1,last)
def partition(vetor,first,last):
   pivotvalue = vetor[first]
   leftmark = first+1
   rightmark = last
   done = False
   while not done:
       while leftmark <= rightmark and vetor[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while vetor[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1
       if rightmark < leftmark:
           done = True
       else:
           temp = vetor[leftmark]
           vetor[leftmark] = vetor[rightmark]
           vetor[rightmark] = temp
   temp = vetor[first]
   vetor[first] = vetor[rightmark]
   vetor[rightmark] = temp
   return rightmark



def MeuQuickSort(vetor):

    def pivotear(primeiro, ultimo, vetor):
        i = primeiro+1
        for j in range(primeiro+1,ultimo+1):
            if vetor[primeiro] >= vetor[j]:
                vetor[i], vetor[j] = vetor[j], vetor[i]
                i+=1
        vetor[primeiro], vetor[i-1] = vetor[i-1], vetor[primeiro]
        v1 = [primeiro, i-2]
        v2 = [i, ultimo]
        if (i-2)-primeiro >= 1:
            pivotear(v1[0], v1[1], vetor)
        if ultimo - i >= 1:
            pivotear(v2[0], v2[1], vetor)
        return vetor

    pivotear(0, len(vetor)-1, vetor)    

    return vetor


