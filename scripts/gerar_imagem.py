#!/usr/bin/env python3
"""
Gerador de Imagens com IA

Suporta: Replicate (FLUX, Stable Diffusion), Banana.dev, OpenAI (DALL-E)

USO:
    python gerar_imagem.py "um gato astronauta" out/gato.png
    python gerar_imagem.py "paisagem cyberpunk" out/cyber.png --modelo flux
    python gerar_imagem.py "retrato realista" out/retrato.png --servico openai

CONFIGURACAO:
    1. Copie .env.example para .env
    2. Preencha a API key do servico que vai usar:
       - REPLICATE_API_TOKEN (mais facil)
       - BANANA_API_KEY + BANANA_MODEL_KEY
       - OPENAI_API_KEY (DALL-E)
"""

import sys
import os
import argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from llm_config import (
    gerar_imagem_replicate,
    gerar_imagem_banana,
    gerar_imagem_openai,
    REPLICATE_API_TOKEN,
    BANANA_API_KEY,
    OPENAI_API_KEY
)

# Modelos disponiveis no Replicate
MODELOS_REPLICATE = {
    "sdxl": "stability-ai/sdxl:latest",
    "sd": "stability-ai/stable-diffusion:latest",
    "flux": "black-forest-labs/flux-schnell",
    "flux-pro": "black-forest-labs/flux-pro",
}


def gerar_imagem(prompt, output_path="out/imagem.png", servico="auto", modelo="sdxl"):
    """
    Gera imagem usando o servico especificado

    Args:
        prompt: Descricao da imagem
        output_path: Caminho para salvar
        servico: "replicate", "banana", "openai", ou "auto"
        modelo: Nome do modelo (sdxl, flux, etc)
    """

    # Auto-detecta servico baseado nas chaves configuradas
    if servico == "auto":
        if REPLICATE_API_TOKEN:
            servico = "replicate"
        elif BANANA_API_KEY:
            servico = "banana"
        elif OPENAI_API_KEY:
            servico = "openai"
        else:
            print("ERRO: Nenhuma API de imagem configurada!")
            print("\nConfigure uma das seguintes no arquivo .env:")
            print("  - REPLICATE_API_TOKEN (recomendado)")
            print("  - BANANA_API_KEY + BANANA_MODEL_KEY")
            print("  - OPENAI_API_KEY")
            return None

    print(f"Servico: {servico}")
    print(f"Prompt: {prompt}")
    print(f"Gerando imagem...")

    if servico == "replicate":
        modelo_id = MODELOS_REPLICATE.get(modelo, modelo)
        print(f"Modelo: {modelo_id}")
        return gerar_imagem_replicate(prompt, modelo_id, output_path)

    elif servico == "banana":
        return gerar_imagem_banana(prompt, output_path)

    elif servico == "openai":
        return gerar_imagem_openai(prompt, output_path)

    else:
        print(f"Servico desconhecido: {servico}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Gera imagens com IA",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos:
  python gerar_imagem.py "um gato fofo"
  python gerar_imagem.py "paisagem futurista" out/paisagem.png
  python gerar_imagem.py "retrato artistico" out/retrato.png --modelo flux
  python gerar_imagem.py "logo minimalista" out/logo.png --servico openai

Modelos Replicate disponiveis:
  sdxl      - Stable Diffusion XL (padrao)
  sd        - Stable Diffusion classico
  flux      - FLUX Schnell (rapido)
  flux-pro  - FLUX Pro (alta qualidade)
        """
    )

    parser.add_argument("prompt", help="Descricao da imagem a gerar")
    parser.add_argument("output", nargs="?", default="out/imagem.png",
                       help="Caminho do arquivo de saida (default: out/imagem.png)")
    parser.add_argument("--servico", "-s", choices=["auto", "replicate", "banana", "openai"],
                       default="auto", help="Servico a usar (default: auto)")
    parser.add_argument("--modelo", "-m", default="sdxl",
                       help="Modelo a usar (default: sdxl)")

    args = parser.parse_args()

    resultado = gerar_imagem(args.prompt, args.output, args.servico, args.modelo)

    if resultado:
        print(f"\n[OK] Imagem salva em: {resultado}")
    else:
        print("\n[ERRO] Falha ao gerar imagem")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Modo interativo
        print("=" * 50)
        print("GERADOR DE IMAGENS COM IA")
        print("=" * 50)

        prompt = input("\nDescreva a imagem que deseja: ")
        output = input("Nome do arquivo (enter para out/imagem.png): ").strip()
        if not output:
            output = "out/imagem.png"

        print("\nServicos disponiveis:")
        print("1. Replicate (FLUX/Stable Diffusion)")
        print("2. Banana.dev")
        print("3. OpenAI (DALL-E)")
        print("4. Auto (detecta automaticamente)")

        opcao = input("\nEscolha (1-4, enter para auto): ").strip()
        servicos = {"1": "replicate", "2": "banana", "3": "openai", "4": "auto", "": "auto"}
        servico = servicos.get(opcao, "auto")

        gerar_imagem(prompt, output, servico)
    else:
        main()
