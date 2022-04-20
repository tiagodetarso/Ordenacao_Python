import random

def CriaVetor(tamanho):
    vetor = []
    for i in range(tamanho):
        vetor.append(random.randint(1,10))
    return vetor

def CriaVetor100(tamanho):
    vetor = []
    for i in range(tamanho):
        vetor.append(random.randint(1,100))
    return vetor

def CriaVetor1m(tamanho):
    vetor = []
    for i in range(tamanho):
        vetor.append(random.randint(1,1000))
    return vetor

def CriaVetor10m(tamanho):
    vetor = []
    for i in range(tamanho):
        vetor.append(random.randint(1,10000))
    return vetor

def CriaVetor100m(tamanho):
    vetor = []
    for i in range(tamanho):
        vetor.append(random.randint(1,100000))
    return vetor

def CriaVetor1M(tamanho):
    vetor = []
    for i in range(tamanho):
        vetor.append(random.randint(1,100000))
    return vetor
