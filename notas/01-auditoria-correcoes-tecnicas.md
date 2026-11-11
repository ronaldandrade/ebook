# Auditoria Técnica e Correções Concretas

Este documento lista as inconsistências conceituais, matemáticas e de código identificadas no manuscrito.

> **Status (11/11/2026):** os itens das seções 1, 2 e 3 foram aplicados no `ebook.tex`. A seção 4 registra outras correções feitas na mesma revisão.

---

## 1. Capítulo 2 — Estatística e Preparação de Dados

### A. Desmistificar a Premissa de Normalidade
- **Problema:** O texto passa a impressão de que a distribuição normal é um pré-requisito geral para treinar modelos de Machine Learning.
- **Correção:** Esclarecer que a normalidade é uma premissa específica de determinados métodos estatísticos e modelos paramétricos (ex.: regressão linear com inferência clássica, Linear Discriminant Analysis, Gaussian Naive Bayes). 
- **Ressalva didática:** Modelos baseados em árvores (Decision Trees, Random Forest, XGBoost), KNN, SVM e redes neurais não exigem que as features sigam distribuição normal.

### B. Sensibilidade ao Escalonamento e Normalização
- **Problema:** A necessidade de escalonamento não diferencia as famílias de algoritmos.
- **Correção:** 
  - **Sensíveis à escala:** Algoritmos baseados em cálculo de distância geométrica (KNN, K-Means, SVM) ou otimização por gradiente descendente (Redes Neurais, Regressão Logística) dependem criticamente de normalização/padronização.
  - **Invariantes à escala:** Algoritmos baseados em particionamento e regras de decisão (Árvores de Decisão, Random Forest) não sofrem impacto pela escala das variáveis.

### C. Reposicionamento de Outliers
- **Ação:** Retomar ou aprofundar a discussão de outliers no **Capítulo 3 (Regressão)**, demonstrando visual e numericamente como um ponto extremo "puxa" a reta de regressão e inflaciona métricas sensíveis como o MSE (Mean Squared Error).

---

## 2. Capítulo 6 — Avaliação de Modelos (Leitura do Relatório de Fraudes)

> **Revisado em 11/11/2026.** O diagnóstico original desta seção estava invertido: o $F_1 = 0{,}10$ estava certo e o erro estava no texto.

### O Erro Identificado
O texto interpretava a classe "Fraude" com precisão $\approx 0{,}53$ e recall $= 0{,}95$. Esses valores são a linha `macro avg` do relatório (média simples das duas classes), e não a linha da classe "Fraude".

### Conferência pela Matriz de Confusão
Com VP = 90, FP = 1551 e FN = 8:

- Precisão $= 90 / (90 + 1551) \approx 0{,}05$
- Recall $= 90 / (90 + 8) \approx 0{,}92$
- $F_1 = 2 \cdot \frac{0{,}05 \cdot 0{,}92}{0{,}05 + 0{,}92} \approx 0{,}10$

O relatório e a matriz são coerentes entre si. Trocar o $F_1$ para $0{,}68$ criaria uma inconsistência nova.

### Correção Aplicada
O parágrafo de interpretação passou a usar precisão 0,05, recall 0,92 e $F_1$ 0,10, com um alerta sobre a leitura da linha `macro avg`.

---

## 3. Capítulo 7 — Classificação de Notícias (Pipeline de NLP)

Este capítulo apresenta 5 pontos que fragilizam o rigor metodológico e devem ser reestruturados:

### 1. Seleção dos Exemplos Rotulados (Filtro por Posição vs. Presença de Rótulo)
- **Problema:** O código utiliza `[:200]` para filtrar os dados rotulados dos 845 registros totais. Se os dados rotulados não estiverem perfeitamente nas 200 primeiras linhas, registros sem rótulo são capturados e tratados como ruído ou negativos.
- **Correção:** Filtrar explicitamente por registros não nulos:
  ```python
  df_rotulado = df[df['sentimento'].notna()].copy()
  ```

### 2. Incoerência Texto vs. Código (Divisão Treino/Teste)
- **Problema:** O texto afirma que a separação foi de "20% treino e 80% teste", enquanto o código executa `test_size=0.2` (80% treino e 20% teste).
- **Correção:** Ajustar o texto para afirmar claramente que 80% dos dados foram destinados ao treinamento e 20% ao teste.

### 3. Vazamento de Dados (Data Leakage) no Vetorizador TF-IDF
- **Problema:** O `TfidfVectorizer.fit_transform` foi aplicado ao conjunto completo antes de chamar o `train_test_split`. Isso permite que o vocabulário e os pesos IDF do conjunto de teste contaminem o treinamento.
- **Correção:** Utilizar a classe `Pipeline` do Scikit-Learn ou ajustar (`fit`) estritamente sobre o conjunto de treino:
  ```python
  from sklearn.pipeline import Pipeline
  from sklearn.feature_extraction.text import TfidfVectorizer
  from sklearn.svm import SVC

  pipeline = Pipeline([
      ('tfidf', TfidfVectorizer()),
      ('svm', SVC(kernel='linear', class_weight='balanced'))
  ])

  pipeline.fit(X_train, y_train)
  y_pred = pipeline.predict(X_test)
  ```

### 4. Interpretação Realista dos Resultados
- **Problema:** O texto conclui de forma excessivamente otimista que o modelo funciona bem, apesar de métricas modestas (Acurácia: $0{,}60$, Precisão: $0{,}58$, Recall: $0{,}70$).
- **Correção:** Apresentar esse resultado como um estudo de caso honesto. Ensinar o leitor a reconhecer as limitações de treinar um modelo com apenas ~160 exemplos de treino em PLN e discutir os próximos passos (aumento de dados, n-grams, stop-words, embeddings).

### 5. Delimitação do Problema de Rotulagem
- **Problema:** O conceito de "positivo" e "negativo" para manchetes jornalísticas (ex.: inflação, juros, deportações) é subjetivo e ambíguo.
- **Correção:** Explicar a distinção entre análise de sentimento textual (tom emocional das palavras) e avaliação do fato reportado (impacto socioeconômico da notícia), definindo a diretriz que guiou o dataset.

---

## 4. Outras Correções Aplicadas em 11/11/2026

Todos os exemplos do livro foram executados e os números do texto conferidos com a saída real.

- **Cap. 2, desvio padrão:** o cálculo manual dava 1,66 e o código 1,67; o valor correto é 1,67 nos dois.
- **Cap. 2, teste t:** a saída real é t = 1,83 e p = 0,104 (o texto trazia 1,73 e 0,119).
- **Cap. 2, outliers:** os coeficientes do texto (3897,42 e 2518,52) não correspondiam ao código. Os reais são inclinação $-356{,}81$ com outlier e 3470,86 sem. A interpretação foi reescrita: o outlier achata a reta (o texto dizia que a inclinava mais). Limite superior do IQR: R\$522.500. O código tinha uma linha inválida e f-strings quebradas.
- **Cap. 3, regressão manual:** $\sum x_i y_i$ e $\sum x_i^2$ estavam errados (95.600 e 41.900; corretos: 156.600 e 44.500), e a conta chegava a 3,46 a partir de um numerador negativo. Equação correta: $y = 3{,}15x + 36{,}5$; previsão para 100 m²: 351,50.
- **Cap. 3, árvore:** os resultados eram hipotéticos ("suponha"). Agora são os reais: teste com as casas de 85 e 70 m², previsões 280.000 e 200.000, MSE 850.000.000, RMSE $\approx$ 29.155. A árvore só divide por tamanho. Figura trocada por `arvore_regressao.png`.
- **Cap. 3, métricas:** MAE e $R^2$ incluídos na tabela (o sumário já os prometia).
- **Cap. 6, exemplo de regressão:** o teste real é a Casa 2 (previsão 278,55), e não a Casa 4.
- **Cap. 6, código de fraudes:** removido o `pd.read_excel` que antecedia o `read_csv`.
- **Cap. 7:** `read_excel` trocado por `read_csv`; a seção opcional sobrescrevia os 200 rótulos manuais e agora preenche só as 645 linhas sem rótulo. Com o `Pipeline`, as métricas ficaram iguais (0,60 / 0,58 / 0,70), mas a manchete fictícia sobre deportações passou a ser classificada como positiva; o texto agora discute esse erro.
- **Cap. 1:** AlphaGo aparecia como exemplo de videogame; punição do robô aspirador estava descrita como recompensa por "evitar" a parede.
