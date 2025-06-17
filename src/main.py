from fontes.gupy import buscar_vagas_gupy
from fontes.remotar import buscar_vagas_remotar
from util.filtros import filtrar_vagas
import pandas as pd
import os

def salvar_csv(vagas, caminho='src/output/vagas_qa.csv'):
    os.makedirs('src/output', exist_ok=True)
    df = pd.DataFrame(vagas)
    df.to_csv(caminho, index=False)
    print(f"\n✅ {len(vagas)} vaga(s) salva(s) em {caminho}")

def main():
    print("🔍 Buscando vagas no Gupy...")
    vagas_gupy = buscar_vagas_gupy()

    print("🔍 Buscando vagas no Remotar...")
    vagas_remotar = buscar_vagas_remotar()

    todas_vagas = vagas_gupy + vagas_remotar
    vagas_filtradas = filtrar_vagas(todas_vagas)

    if not vagas_filtradas:
        print("❌ Nenhuma vaga de QA encontrada.")
    else:
        for vaga in vagas_filtradas:
            print(f"- {vaga['titulo'].title()}: {vaga['link']}")

        salvar_csv(vagas_filtradas)

if __name__ == '__main__':
    main()
