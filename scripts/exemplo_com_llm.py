#!/usr/bin/env python3
"""
Exemplo de uso dos scripts de geração de documentos com LLMs

Este script mostra como usar GPT-4/Codex para gerar conteúdo
e depois criar documentos automaticamente.

USO:
1. Configure sua API key no arquivo .env
2. Execute: python exemplo_com_llm.py
"""

import os
import sys

# Adiciona o diretório scripts ao path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from llm_config import chat_openai, chat_anthropic, OPENAI_API_KEY, ANTHROPIC_API_KEY


def gerar_relatorio_com_llm(tema, formato="docx"):
    """
    Usa LLM para gerar conteúdo e cria documento automaticamente

    Args:
        tema: Assunto do relatório
        formato: docx, xlsx, pptx, ou pdf
    """

    # Escolhe qual API usar (prioriza OpenAI)
    if OPENAI_API_KEY:
        chat_fn = chat_openai
        llm_name = "OpenAI"
    elif ANTHROPIC_API_KEY:
        chat_fn = chat_anthropic
        llm_name = "Anthropic"
    else:
        print("ERRO: Nenhuma API configurada!")
        print("Configure OPENAI_API_KEY ou ANTHROPIC_API_KEY no arquivo .env")
        return None

    print(f"Usando {llm_name} para gerar conteúdo...")

    # === GERAR CONTEÚDO COM LLM ===

    if formato == "docx":
        prompt = f"""
        Crie um relatório profissional sobre: {tema}

        Retorne em formato JSON com esta estrutura:
        {{
            "titulo": "Título do Relatório",
            "secoes": [
                {{"titulo": "Introdução", "conteudo": "..."}},
                {{"titulo": "Análise", "conteudo": "..."}},
                {{"titulo": "Conclusão", "conteudo": "..."}}
            ]
        }}

        Apenas o JSON, sem explicações.
        """

        resposta = chat_fn(prompt)
        if not resposta:
            return None

        # Parse JSON
        import json
        try:
            dados = json.loads(resposta)
        except:
            # Tenta extrair JSON da resposta
            import re
            match = re.search(r'\{.*\}', resposta, re.DOTALL)
            if match:
                dados = json.loads(match.group())
            else:
                print("Erro ao parsear resposta da LLM")
                return None

        # Criar documento Word
        from generate_docx import criar_documento_personalizado
        caminho = f"out/relatorio_{tema.replace(' ', '_')[:20]}.docx"
        criar_documento_personalizado(
            titulo=dados['titulo'],
            secoes=dados['secoes'],
            caminho_saida=caminho
        )
        return caminho

    elif formato == "xlsx":
        prompt = f"""
        Crie dados tabulares sobre: {tema}

        Retorne em formato JSON com esta estrutura:
        {{
            "titulo": "Título da Planilha",
            "colunas": ["Col1", "Col2", "Col3"],
            "dados": [
                ["valor1", "valor2", "valor3"],
                ["valor4", "valor5", "valor6"]
            ]
        }}

        Inclua pelo menos 5 linhas de dados numéricos realistas.
        Apenas o JSON, sem explicações.
        """

        resposta = chat_fn(prompt)
        if not resposta:
            return None

        import json
        try:
            dados = json.loads(resposta)
        except:
            import re
            match = re.search(r'\{.*\}', resposta, re.DOTALL)
            if match:
                dados = json.loads(match.group())
            else:
                print("Erro ao parsear resposta da LLM")
                return None

        # Criar planilha
        from generate_xlsx import novo_workbook, adicionar_tabela, salvar_workbook

        wb = novo_workbook()
        ws = wb.active
        ws.title = "Dados"

        # Montar dados com cabeçalho
        tabela = [dados['colunas']] + dados['dados']
        adicionar_tabela(ws, tabela, linha_inicio=1, com_cabecalho=True)

        caminho = f"out/planilha_{tema.replace(' ', '_')[:20]}.xlsx"
        salvar_workbook(wb, caminho)
        return caminho

    elif formato == "pptx":
        prompt = f"""
        Crie uma apresentação sobre: {tema}

        Retorne em formato JSON com esta estrutura:
        {{
            "titulo": "Título da Apresentação",
            "subtitulo": "Subtítulo",
            "slides": [
                {{"titulo": "Slide 1", "bullets": ["ponto 1", "ponto 2"]}},
                {{"titulo": "Slide 2", "bullets": ["ponto 1", "ponto 2"]}}
            ]
        }}

        Inclua 4-5 slides com conteúdo relevante.
        Apenas o JSON, sem explicações.
        """

        resposta = chat_fn(prompt)
        if not resposta:
            return None

        import json
        try:
            dados = json.loads(resposta)
        except:
            import re
            match = re.search(r'\{.*\}', resposta, re.DOTALL)
            if match:
                dados = json.loads(match.group())
            else:
                print("Erro ao parsear resposta da LLM")
                return None

        # Criar apresentação
        from generate_pptx import (nova_apresentacao, adicionar_slide_titulo,
                                   adicionar_slide_conteudo, salvar_apresentacao)
        from pptx.dml.color import RGBColor

        prs = nova_apresentacao()
        adicionar_slide_titulo(prs, dados['titulo'], dados.get('subtitulo', ''),
                              cor_fundo=RGBColor(31, 78, 121))

        for slide in dados['slides']:
            adicionar_slide_conteudo(prs, slide['titulo'], slide['bullets'])

        caminho = f"out/apresentacao_{tema.replace(' ', '_')[:20]}.pptx"
        salvar_apresentacao(prs, caminho)
        return caminho

    else:
        print(f"Formato não suportado: {formato}")
        return None


def exemplo_interativo():
    """Exemplo interativo de uso"""
    print("=" * 50)
    print("GERADOR DE DOCUMENTOS COM LLM")
    print("=" * 50)

    tema = input("\nDigite o tema do documento: ")
    print("\nFormatos disponíveis:")
    print("1. docx (Word)")
    print("2. xlsx (Excel)")
    print("3. pptx (PowerPoint)")

    opcao = input("\nEscolha o formato (1-3): ")
    formatos = {"1": "docx", "2": "xlsx", "3": "pptx"}
    formato = formatos.get(opcao, "docx")

    print(f"\nGerando {formato} sobre '{tema}'...")
    caminho = gerar_relatorio_com_llm(tema, formato)

    if caminho:
        print(f"\n✓ Documento criado: {caminho}")
    else:
        print("\n✗ Erro ao criar documento")


def carregar_tema(entrada):
    """
    Carrega tema de string ou arquivo

    Se entrada termina com .txt, .md ou .json, le o arquivo
    Senao, usa a string diretamente
    """
    if entrada.endswith(('.txt', '.md', '.json', '.csv')):
        if os.path.exists(entrada):
            with open(entrada, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            print(f"Arquivo carregado: {entrada} ({len(conteudo)} caracteres)")
            return conteudo
        else:
            print(f"Arquivo nao encontrado: {entrada}")
            return entrada
    return entrada


if __name__ == "__main__":
    # Verifica se há argumentos
    if len(sys.argv) > 1:
        entrada = sys.argv[1]
        formato = sys.argv[2] if len(sys.argv) > 2 else "docx"

        # Carrega tema de arquivo ou usa string direta
        tema = carregar_tema(entrada)

        gerar_relatorio_com_llm(tema, formato)
    else:
        exemplo_interativo()
