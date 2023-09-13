# Sprint3-IA-IOT

# Projeto Ninus 🐼📕
_A Ninus é uma solução oficial da **Smash Code!**_
> Smash Code! 

# Uma breve descrição 💬
Nosso aplicativo se chama Ninus e ele é para professores do ensino infantil que desejam reduzir significamente o tempo de montagem de aula. O foco do professor deve ser no ensinamento, e muitos professores do ensino infantil gastam entre 2 e 3 horas para montar uma aula, por justamente ser complexo e detalhado. Toda a montagem de aula deve seguir um padrão rígido da BNCC (Base Nacional Comum Curricular), e isso faz a montagem de aula ficar ainda mais complexa e demorada

A Ninus fornece uma IA (ChatGPT) que monta uma aula para um determinado eixo do ensino infantil, tudo o que o professor precisa fazer é fornecer algumas Informações de input(entrada) para que a nossa IA gere um infográfico com a aula. A IA não esquecerá de considerar os alunos inclusos (deficientes ou autistas, etc.), o professor também poderá informar nos dados de input se há alunos inclusos dentro de sala de aula.

O professor poderá criar aulas no aplicativo, marcá-las como realizadas, e favorita-las. Cada aula terá um modelo (infográfico). Além de fornecer um sistema de montagem, a Ninus fornece um sistema de análise de dados bem simples, para o professor acompanhar sua evolução. Após um professor marcar uma aula como realizada, o sistema pede um feedback e explica a importância do professor avaliar suas aulas. Com base nos feedbacks e na quantidade deles durante a semana, o sistema irá criar dashboards bem simples nada complexas, apenas para pontuar algumas coisas, ressaltar e mostrar algo. Essas análises serão semanais e caso o professor tenha avaliações o suficiente na semana, todo domingo de noite ele receberá uma notificação da Ninus o informando que ele ganhou uma análise semanal. É apenas um adereço a mais no aplicativo, caso o professor não tenha avaliações suficientes durante a semana, ele não ganhará uma análise semanal e nada mais mudará além disso.

Como dito ali em cima, todo modelo de aula deve seguir a risca os padrões BNCC, por isso é importante ressaltar que a ninus segue os padrões da BNCC para o ensino infântil.

## Informações das IAs:

Prototipo 1 - Classificador de "HateSpeech":
- **Resumo:** Uma IA de Classificação de frases com a finalidade de identificar frases de cunho discriminatorio, xenofobico, homofobico, machista, racista e outros tipos de palavras que venham a ter como finalidade ter o pre-conceito sobre certo assuntos ou que tem como finalidade espalhar o ódio.
- **Dataset:** https://www.kaggle.com/datasets/hrmello/brazilian-portuguese-hatespeech-dataset
- **Bibliotecas:** Kaggle, Re (Regex), Pandas, Seaborn, Matplotlib, Sklearn, TensorFlow, Keras, Scipy, NLTK, Unidecode e Joblib
- **Pré-Processamentos:** Remoção de caracteres especiais (e palavras atreladas) com regex, Exclusão de Acentos, Exclusão de Stopwords e palavras abreviadas, Remoção de caracteres em maiusculo , Stemmização, Tokenização e Padding.
- **Modelo de IA:** Rede Neural (Camadas: Embebedding, Convolução, LSTM e Dense).
