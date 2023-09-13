import joblib
import re
from nltk import tokenize
import nltk
import unidecode
import pandas as pd
import scipy.sparse as sp
from sklearn.feature_extraction.text import CountVectorizer

#--------------------------------------------------------------------------

path = "input.txt"

arquivo = open(path, 'r')
input_ia = arquivo.read()
print(input_ia)
arquivo.close()

model = joblib.load("modelo_ml.pkl")

stopwords = nltk.corpus.stopwords.words("portuguese")
stopwords_sem_acento =  [unidecode.unidecode(texto) for texto in stopwords]
abreviacoes=["vc","pq","tb","tbm","mt","q","bjo","bja","blz","td","flw","msm","p","cmg","pra","vcê","agd","agr","dm","ctg","dps","gnt","msg","ngm","tô","tá","tô","qdo","qnd","to","ta","rt","q","n","ai"]
for i in abreviacoes:
  stopwords_sem_acento.append(i)

vetorize2 = CountVectorizer(lowercase = False)

#--------------------------------------------------------------------------

def remover_caracteres_especiais(texto):
    padrao_regex = r'[!@#\$%\^&\*\(\)_\+\-=\[\]\{\};:\'",<>\./?\\|]'
    return re.sub(padrao_regex, '', texto)

def pre_processamento(texto):
    lista_frase1 = list()
    lista_frase2 = list()
    tokenizer2 = tokenize.WordPunctTokenizer()
    p1 = texto.lower()
    p2 = tokenizer2.tokenize(p1)
    for i in p2:
        if i not in stopwords_sem_acento:
            lista_frase1.append(i)
    lista_frase2.append(' '.join(lista_frase1))
    return lista_frase2

#--------------------------------------------------------------------------

#Pré procesamento para ML
response2 = remover_caracteres_especiais(input_ia)
response3 = pre_processamento(response2)

frase_v = vetorize2.fit_transform(response3)
matrix_frase = pd.DataFrame.sparse.from_spmatrix(frase_v)

num_linhas, num_colunas = matrix_frase.shape
matriz_frase2 = sp.lil_matrix((num_linhas, 20))
matriz_frase2[:, :num_colunas] = matrix_frase
matriz_frase2 = matriz_frase2.tocsr()

resultado_ml = model.predict(matriz_frase2)

if resultado_ml >= 0.49:
    print("Frase ruim")
    valor = 1
elif resultado_ml <= 0.48:
    print("Frase ok")
    valor = 0

