import pandas as pd

file_name = 'Characters.csv'

try:
    df = pd.read_csv(file_name, sep=';')

    print(f"Análise do arquivo: {file_name}\n")

    num_linhas, num_colunas = df.shape
    print(f"O dataset possui {num_linhas} linhas e {num_colunas} colunas.\n")

    print("="*50)
    print("Nomes das colunas:")
    print("="*50)
    for coluna in df.columns:
        print(f"- {coluna}")
    print("\n")

    print("="*50)
    print("Análise de Integridade (Valores Ausentes)")
    print("="*50)

    missing_values = df.isnull().sum()
    missing_percentage = (missing_values / num_linhas) * 100

    integrity_report = pd.DataFrame({
        'Valores Ausentes': missing_values,
        'Porcentagem Ausente (%)': missing_percentage.round(2)
    })

    integrity_report_sorted = integrity_report.sort_values(by='Valores Ausentes', ascending=False)

    print(integrity_report_sorted)
    print("\n")

except FileNotFoundError:
    print(f"--- ERRO ---")
    print(f"O arquivo '{file_name}' não foi encontrado.")
    print("Por favor, verifique se o nome do arquivo está correto e se ele está na mesma pasta que o script.")
except Exception as e:
    print(f"Ocorreu um erro inesperado ao processar o arquivo: {e}")
    print("\n--- SUGESTÃO ---")
    print("O erro pode não ser o separador ';'. Tente abrir o arquivo 'Characters.csv' em um editor de texto simples (como Bloco de Notas ou VS Code) para ver qual caractere está separando as colunas (ex: tabulação '\\t', pipe '|').")