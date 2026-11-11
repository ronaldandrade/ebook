# Sumário e Roteiro da Obra: Meu Aprendizado de Máquinas

## Informações Gerais
- **Título:** Meu Aprendizado de Máquinas
- **Autor:** Ronald A. Mendonça
- **Ano:** 2027
- **Formato:** LaTeX (`ebook.tex`) -> PDF (`ebook.pdf`, 64 páginas)
- **Repositório Git:** `https://github.com/ronaldandrade/ebook.git`
- **Público-alvo:** Estudantes, profissionais e entusiastas que desejam uma introdução prática e matematicamente intuitiva ao aprendizado de máquina com Python.

---

## Tabela de Capítulos e Progresso

| # | Seção / Capítulo | Tópicos Centrais | Figuras e Recursos | Status |
|---|---|---|---|:---:|
| **—** | **Prefácio e Agradecimentos** | A trajetória pessoal (GTI, pós em Data Science e IA, cadernos escolares) e motivação da obra | - | `[Prefácio escrito; Agradecimentos pendente]` |
| **—** | **Introdução** | O que é ML, papel dos dados, relevância prática, objetivo do livro | - | `[Escrito]` |
| **01** | **Conceitos Fundamentais: Dados e Aprendizado** | Dados qualitativos e quantitativos, tipos de aprendizado (supervisionado, não supervisionado, por reforço, semissupervisionado) | - | `[Escrito]` |
| **02** | **Estatística Essencial para Machine Learning** | Média, variância, desvio padrão, distribuição normal, correlação de Pearson, testes de hipótese, normalização e padronização, outliers | `curva_normal_temperaturas.png`, `distribuição_de_alturas.png`, `Correlação_de_Person.png`, `outliers_detection.png` | `[Escrito]` |
| **03** | **Regressão: Previsão de Valores Contínuos** | Regressão linear, previsão de preço de imóveis, árvores de decisão, métricas (MSE, RMSE, MAE, R²) | `regressao_linear.png`, `arvore_regressao.png` | `[Escrito]` |
| **04** | **Classificação: Previsão de Categorias** | Regressão logística, KNN, fronteira de decisão | `fronteira_decisao.png` | `[Escrito]` |
| **05** | **Clustering: Agrupamento de Dados** | Aprendizado não supervisionado, algoritmo K-Means, segmentação de clientes por compras | `clusters_clientes.png` | `[Escrito]` |
| **06** | **Avaliação e Melhoria de Modelos** | Overfitting vs. Underfitting, divisão treino/teste, validação cruzada, accuracy, precision, recall, F1, matriz de confusão (detecção de fraudes) | `matriz de confusao.png` | `[Escrito]` |
| **07** | **Aplicando o Aprendizado em Dados Reais** | Projeto prático end-to-end: vetorização TF-IDF e SVM em um `Pipeline`, classificação de sentimento em notícias | `noticias.csv` | `[Escrito]` |
| **08** | **Melhorias e Recursos** | Síntese conceitual, próximos passos de estudo, recursos recomendados e referências | `referencias.bib` | `[Escrito]` |

---

## Galeria de Imagens do Livro
Todas as figuras ficam em `images/` (o `ebook.tex` usa `\graphicspath{{images/}}`).

- `curva_normal_temperaturas.png`: Histograma e curva normal das temperaturas de uma semana.
- `distribuição_de_alturas.png`: Curva normal aplicada a dados simulados de altura.
- `Correlação_de_Person.png`: Relação linear positiva entre duas variáveis.
- `outliers_detection.png`: Dispersão com as retas de regressão ajustadas com e sem o outlier.
- `regressao_linear.png`: Linha de melhor ajuste aos pontos de dispersão.
- `arvore_regressao.png`: Árvore de regressão treinada no exemplo de preços de casas (gerada com `plot_tree`).
- `decision_tree.png`: Diagrama genérico de árvore de classificação (em inglês); não é mais usado no livro.
- `fronteira_decisao.png`: Fronteira de decisão da regressão logística no exemplo de spam.
- `clusters_clientes.png`: Visualização de clusters gerados pelo K-Means.
- `matriz de confusao.png`: Verdadeiros/falsos positivos e negativos da classificação.
