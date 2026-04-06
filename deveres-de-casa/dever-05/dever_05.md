# Dever de Casa — Análise de Algoritmos

Apresentar o cálculo de complexidade para:

1. Merge Sort  
2. Multiplicação de matrizes  
3. Recorrências utilizando o Teorema Mestre  

---

# 1) Merge Sort

O Merge Sort é um algoritmo de ordenação baseado em divisão e conquista.

Ele funciona da seguinte forma:
- Divide o vetor em duas partes
- Ordena cada parte recursivamente
- Intercala (merge) os resultados

## Recorrencia

T(n) = 2T(n/2) + n

Onde:
- a = 2  
- b = 2  
- f(n) = n  

## Aplicação do Teorema Mestre

n^(log_b a) = n^(log₂ 2) = n  

Como:

f(n) = n = n^(log_b a)

-> Caso 2 do Teorema Mestre

## Complexidade

Θ(n log n)

- Melhor caso: Θ(n log n)  
- Caso médio: Θ(n log n)  
- Pior caso: Θ(n log n)  

---

# 2) Multiplicação de Matrizes

Considerando a multiplicação tradicional de matrizes n × n:
for i in range(n):
for j in range(n):
for k in range(n):
C[i][j] += A[i][k] * B[k][j]


## Análise

- Existem 3 loops aninhados
- Cada loop executa n vezes

Total de operações:

n × n × n = n³

## Complexidade

Θ(n³)

- Melhor caso: Θ(n³)  
- Caso médio: Θ(n³)  
- Pior caso: Θ(n³)  

---

# 3) Recorrências (Teorema Mestre)

Forma geral:

T(n) = aT(n/b) + f(n)

---

## 3.1) T(n) = 2T(n/4) + √n

### Parâmetros

- a = 2  
- b = 4  
- f(n) = √n = n^(1/2)  

Cálculo:

n^(log₄ 2) = n^(1/2)

Como:

f(n) = n^(log_b a)

-> Caso 2 do Teorema Mestre

## Resultado

Θ(√n log n)

---

## 3.2) T(n) = 2T(n/4) + n

### Parâmetros

- a = 2  
- b = 4  
- f(n) = n  

Cálculo:

n^(log₄ 2) = n^(1/2)

Comparação:

n > n^(1/2)

-> Caso 3 do Teorema Mestre

## Resultado

Θ(n)

---

## 3.3) T(n) = 16T(n/4) + n²

### Parâmetros

- a = 16  
- b = 4  
- f(n) = n²  

Cálculo:

n^(log₄ 16) = n²

Como:

f(n) = n^(log_b a)

-> Caso 2 do Teorema Mestre

## Resultado

Θ(n² log n)

---

# Resumo Final

| Problema                     | Complexidade |
|----------------------------|-------------|
| Merge Sort                 | Θ(n log n)  |
| Multiplicação de matrizes  | Θ(n³)       |
| Recorrência 1              | Θ(√n log n) |
| Recorrência 2              | Θ(n)        |
| Recorrência 3              | Θ(n² log n) |

---

# Conclusão

- Merge Sort possui complexidade eficiente de Θ(n log n)  
- Multiplicação de matrizes cresce de forma cúbica Θ(n³)  
- Recorrências foram resolvidas com o Teorema Mestre  
- A análise de complexidade permite prever o desempenho dos algoritmos  

---
