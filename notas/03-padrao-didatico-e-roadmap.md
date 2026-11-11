# Padrão Didático dos Capítulos e Roadmap de Execução

## 1. O Template de Capítulo de Algoritmo

Para que o livro mantenha um alto nível de consistência e didática, cada capítulo que introduzir um modelo ou algoritmo deve seguir esta sequência de 8 passos:

```text
[1] Problema Real          -> Qual desafio prático ou decisão esse algoritmo resolve?
[2] Intuição Visual        -> Gráfico, diagrama geométrico ou metáfora física intuitiva.
[3] Fundamentação          -> Equações centrais com cada variável e subscrito explicado em prosa.
[4] Exemplo Numérico       -> Um mini-caso resolvido à mão, passo a passo, com números pequenos.
[5] Implementação Python   -> Código limpo, idiomático (Scikit-learn/NumPy), reproduzível.
[6] Confronto dos Dados    -> Comparar o cálculo manual com o output gerado pelo código.
[7] Limitações e Armadilhas-> Suposições do modelo, sensibilidade a escala/outliers e onde ele erra.
[8] Síntese & Exercícios   -> Próximos passos e questões para fixação prática.
```

---

## 2. Roadmap de Execução Editorial

Em vez de tentar reescrever toda a obra de uma só vez, o trabalho editorial deve seguir esta ordem clara de prioridades:

### Fase 1: Auditoria Técnica Imediata (concluída em 11/11/2026)
- [x] Corrigir a leitura do $F_1$-score no Capítulo 6 (o $0{,}10$ estava certo; o texto lia a linha `macro avg`. Ver nota 01).
- [x] Refazer o pipeline do Capítulo 7 com `Pipeline(TfidfVectorizer, SVC)` para eliminar data leakage.
- [x] Corrigir a seleção dos dados rotulados no Capítulo 7 (`notna()` em vez de `[:200]`).
- [x] Alinhar o texto do Capítulo 7 à proporção real de divisão (`test_size=0.2` = 80% treino / 20% teste).
- [x] Desmistificar a premissa de distribuição normal no Capítulo 2 e detalhar sensibilidade a escala.

### Fase 2: Reorganização Estrutural e Contextualização Matemática
- [ ] Introduzir notação algébrica e vetorial nos Capítulos 3 (Regressão) e 4 (Classificação).
- [ ] Modelar a regressão linear e logística através de funções de perda e gradiente descendente.
- [ ] Transferir/conectar o estudo de outliers diretamente ao comportamento das perdas quadráticas na regressão. (Parcial: o exemplo foi corrigido e virou seção própria, ainda no Capítulo 2.)

### Fase 3: Aprofundamento dos Algoritmos Existentes
- [ ] Incluir exemplos numéricos calculados passo a passo (ex.: um ajuste de reta simples à mão; uma iteração de K-Means com 4 pontos).
- [ ] Enriquecer as discussões de limitações e casos de borda em cada modelo.

### Fase 4: Padronização Didática
- [ ] Revisar todos os capítulos existentes à luz do template de 8 etapas.
- [ ] Garantir que o tom de voz permaneça autêntico, sem vícios de IA e fiel à experiência prática do autor.

### Fase 5: Expansão Futura (Deep Learning e Visão Computacional)
- [ ] Capítulo/Parte nova sobre Redes Neurais e Backpropagation.
- [ ] Projetos autorais em Visão Computacional (classificação, detecção de objetos, OCR).
