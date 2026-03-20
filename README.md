# aula20

Aqui está o conteúdo completo para o seu arquivo **README.md**, seguindo rigorosamente o modelo fornecido (`RELATORIO_MODELO.MD`) e utilizando os dados reais que você obteve no terminal.

Basta copiar e colar o texto abaixo:

---

# Relatório de Avaliação de Logs Paralelo

**Disciplina:** Programação Paralela e Distribuída  
**Aluno(s):** Luís Henrique  
**Turma:** 5° semestre  
**Professor:** Rafael Marconi  
**Data:** 13/03/2026

---

# 1. Descrição do Problema

O programa resolve o problema de processamento de grandes volumes de arquivos de log textuais. O objetivo é extrair métricas de desempenho e contagem de palavras-chave específicas em um cenário onde o processamento sequencial é muito lento.

* **Objetivo:** Reduzir o tempo de análise de logs utilizando o modelo Produtor-Consumidor.
* **Volume de dados:** 1.000 arquivos de texto (pasta `log2`), contendo um total de 10.000.000 de linhas.
* **Algoritmo:** Utilizou-se um Pool de Processos onde cada processo trabalhador (consumidor) realiza a leitura, contagem de linhas, palavras, caracteres e busca pelas strings "erro", "warning" e "info".
* **Complexidade:** A complexidade aproximada é $O(n)$, onde $n$ é o número total de linhas/caracteres nos arquivos.

---

# 2. Ambiente Experimental

| Item | Descrição |
| :--- | :--- |
| Processador | Intel(R) Core(TM) i5-1135G7 @ 2.40GHz |
| Número de núcleos | 4 núcleos físicos / 8 núcleos lógicos |
| Memória RAM | 8 GB DDR4 |
| Sistema Operacional | Windows |
| Linguagem utilizada | Python 3.13 |
| Biblioteca de paralelização | `multiprocessing` (Pool) |
| Compilador / Versão | Python 3.13.0 |

---

# 3. Metodologia de Testes

Os testes foram conduzidos comparando uma execução serial de referência contra execuções paralelas variando o número de processos trabalhadores.
* **Configurações:** 1 (Serial), 2, 4, 8 e 12 processos.
* **Carga:** Cada arquivo processado possui uma simulação de carga pesada (loop de 1000 iterações) para evidenciar o ganho da paralelização de CPU.

---

# 4. Resultados Experimentais

| Nº de Processos | Tempo de Execução (s) |
| :--- | :--- |
| 1 (Serial) | 115.9621 |
| 2 | 57.6676 |
| 4 | 29.2327 |
| 8 | 20.5816 |
| 12 | 17.8815 |

---

# 5. Tabela de Speedup e Eficiência

| Processos | Tempo (s) | Speedup | Eficiência |
| :--- | :--- | :--- | :--- |
| 1 | 115.9621 | 1.00 | 100% |
| 2 | 57.6676 | 2.01 | 100.5% |
| 4 | 29.2327 | 3.96 | 99% |
| 8 | 20.5816 | 5.63 | 70.3% |
| 12 | 17.8815 | 6.48 | 54% |

---

# 6. Análise dos Resultados

* **O speedup obtido foi próximo do ideal?** Sim, até 4 processos o speedup foi quase linear (3.96x para 4 núcleos), o que é excelente.
* **A aplicação apresentou escalabilidade?** Sim, houve redução de tempo em todas as progressões, embora o ganho tenha diminuído após 8 processos.
* **Em qual ponto a eficiência começou a cair?** A eficiência caiu significativamente ao passar de 4 para 8 processos (de 99% para 70%).
* **O número de threads/processos ultrapassa o número de núcleos físicos?** Sim. O processador tem 4 núcleos físicos. Ao usar 8 ou 12 processos, há disputa por recursos de hardware (Hyper-threading), o que explica a queda na eficiência.
* **Houve overhead de paralelização?** Sim, especialmente com 12 processos, onde o tempo de gerenciamento dos processos pelo Sistema Operacional começa a limitar o ganho de performance.

---

# 7. Conclusão

O experimento demonstrou que a biblioteca `multiprocessing` é altamente eficaz para problemas de processamento de logs em Python, pois contorna o limite do GIL (Global Interpreter Lock). Conseguimos reduzir o tempo de execução de **115 segundos para menos de 18 segundos**. O melhor custo-benefício (equilíbrio entre tempo e uso de CPU) nesta máquina específica foi de **4 processos**, aproveitando totalmente os núcleos físicos disponíveis.
