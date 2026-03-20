# aula20

RELATÓRIO DA ATIVIDADE - AVALIADOR DE LOGS PARALELO
Disciplina: Análise e Desenvolvimento de Sistemas 
Aluno: Luís Henrique  
Turma: 5° semestre  
Professor: Rafael Marconi  
Data: 20/03/2026

1. Descrição do Problema
Problema: Implementação de um sistema para processar grandes volumes de arquivos de log (texto), extraindo métricas operacionais. Atualmente, o sistema opera de forma serial, o que é ineficiente para grandes demandas.
Objetivo: Evoluir o sistema para uma versão paralela utilizando o modelo Produtor-Consumidor com buffer limitado, visando reduzir o tempo total de execução.
Volume de Dados: 1.000 arquivos de texto (pasta log2), totalizando 10 milhões de linhas processadas.
Algoritmo: Foi utilizado o módulo multiprocessing.Pool do Python para criar um pool de processos trabalhadores (consumidores) que processam arquivos de forma independente.

2. Ambiente Experimental
| Componente | Especificação |
| Processador | Intel(R) Core(TM) i5-1135G7 @ 2.40GHz |
| Núcleos | 4 núcleos físicos / 8 núcleos lógicos |
| Memória RAM | 8 GB DDR4 |
| Linguagem | Python 3.13 |
| Sistema Operacional | Windows |

3. Metodologia de Testes
1. Referência Serial: Tempo base fornecido de **115.9621s**.
2. Execuções Paralelas: Realização de baterias de testes com 2, 4, 8 e 12 processos.
3. Métricas:** Cálculo de Speedup ($T_{serial} / T_{paralelo}$) e Eficiência ($Speedup / N_{processos}$).

4. Resultados Experimentais (Pasta log2)
O sistema validou a corretude dos dados (Erro: 33.332.083, Warning: 33.330.520, Info: 33.329.065) e obteve os seguintes tempos:

| Configuração | Tempo de Execução (s) | Speedup | Eficiência |
| 1 Processo (Serial) | 115.9621 | 1.000 | 100,0% |
| 2 Processos | 57.6676 | 2.011 | 100,5% |
| 4 Processos | 29.2327 | 3.967 | 99,1% |
| 8 Processos | 20.5816 | 5.634 | 70,4% |
| 12 Processos | 17.8815 | 6.485 | 54,0% |

5. Análise de Resultados
Escalabilidade: Observou-se um ganho quase linear até 4 processos. Isso ocorre porque o processador possui 4 núcleos físicos dedicados, permitindo paralelismo real sem concorrência direta por recursos de CPU.
Hyper-Threading: O ganho entre 4 e 8 processos continua existindo devido aos núcleos lógicos, mas a eficiência cai (70%), pois os núcleos lógicos compartilham recursos dos núcleos físicos.
Saturação: Com 12 processos, o tempo de execução estabilizou (apenas 2.7s de ganho em relação a 8 processos). Isso demonstra o *overhead* de gerenciamento do sistema operacional e a limitação física do hardware.

6. Conclusão
A paralelização utilizando multiprocessing mostrou-se extremamente superior ao modelo serial e ao modelo de threads (limitado pelo GIL). Conseguimos reduzir o tempo de processamento de 1 minuto e 55 segundos para apenas 17,8 segundos. O melhor equilíbrio entre desempenho e eficiência para esta máquina foi encontrado com 4 processos.
