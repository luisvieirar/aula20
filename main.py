import os
import time
import multiprocessing

# Função de processamento (Igual à sua)
def processar_arquivo(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            conteudo = f.readlines()
        total_linhas = len(conteudo)
        total_palavras = 0
        total_caracteres = 0
        contagem = {"erro": 0, "warning": 0, "info": 0}
        for linha in conteudo:
            palavras = linha.split()
            total_palavras += len(palavras)
            total_caracteres += len(linha)
            for p in palavras:
                if p.lower() in contagem:
                    contagem[p.lower()] += 1
            for _ in range(1000): pass # Simulação de peso
        return {"linhas": total_linhas, "palavras": total_palavras, "caracteres": total_caracteres, "contagem": contagem}
    except:
        return None

def consolidar_resultados(resultados):
    resumo = {"linhas": 0, "palavras": 0, "caracteres": 0, "contagem": {"erro": 0, "warning": 0, "info": 0}}
    for r in resultados:
        if r:
            resumo["linhas"] += r["linhas"]
            resumo["palavras"] += r["palavras"]
            resumo["caracteres"] += r["caracteres"]
            for k in resumo["contagem"]:
                resumo["contagem"][k] += r["contagem"][k]
    return resumo

if __name__ == "__main__":
    # Tenta encontrar a pasta log2 no mesmo local do script
    diretorio_script = os.path.dirname(os.path.abspath(__file__))
    pasta = os.path.join(diretorio_script, "log2")

    if not os.path.exists(pasta):
        print(f"ATENÇÃO: Pasta {pasta} não encontrada!")
        print("Criando pasta 'log2' de teste automaticamente...")
        os.makedirs(pasta, exist_ok=True)
        # Cria 10 arquivos rápidos para o código não travar
        for i in range(10):
            with open(os.path.join(pasta, f"teste_{i}.txt"), "w") as f:
                f.write("erro warning info processo dados\n" * 100)
    
    arquivos = [os.path.join(pasta, f) for f in os.listdir(pasta) if f.endswith('.txt')]
    
    print(f"Processando {len(arquivos)} arquivos da pasta: {pasta}")
    
    for n in [2, 4, 8, 12]:
        inicio = time.time()
        with multiprocessing.Pool(processes=n) as pool:
            resultados = pool.map(processar_arquivo, arquivos)
        
        fim = time.time()
        resumo = consolidar_resultados(resultados)
        print(f"\n[ {n} PROCESSOS ]")
        print(f"Tempo: {fim - inicio:.4f}s")
        print(f"Logs: {resumo['contagem']}")