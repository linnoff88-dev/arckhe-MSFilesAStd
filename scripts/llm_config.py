#!/usr/bin/env python3
"""
Configuraçêo de APIs para LLMs

Suporta: OpenAI (GPT-4, Codex), Anthropic (Claude), Google (Gemini), etc.

USO:
1. Copie o arquivo .env.example para .env
2. Preencha suas chaves de API
3. Importe este módulo nos seus scripts
"""

import os
from pathlib import Path

# Tenta carregar do .env se existir
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).parent.parent / '.env'
    load_dotenv(env_path)
except ImportError:
    pass  # python-dotenv nêo instalado, usar variáveis de ambiente diretamente


# =============================================
# CONFIGURAÇÕES DE API
# =============================================

# OpenAI (GPT-4, GPT-3.5, Codex)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '')
OPENAI_ORG_ID = os.getenv('OPENAI_ORG_ID', '')  # Opcional
OPENAI_MODEL = os.getenv('OPENAI_MODEL', 'gpt-4')

# Anthropic (Claude)
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY', '')
ANTHROPIC_MODEL = os.getenv('ANTHROPIC_MODEL', 'claude-3-opus-20240229')

# Google (Gemini)
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '')
GOOGLE_MODEL = os.getenv('GOOGLE_MODEL', 'gemini-pro')

# Azure OpenAI
AZURE_OPENAI_KEY = os.getenv('AZURE_OPENAI_KEY', '')
AZURE_OPENAI_ENDPOINT = os.getenv('AZURE_OPENAI_ENDPOINT', '')
AZURE_OPENAI_DEPLOYMENT = os.getenv('AZURE_OPENAI_DEPLOYMENT', '')

# OpenRouter (acesso a multiplas LLMs)
# https://openrouter.ai/
OPENROUTER_API_KEY = os.getenv('OPENROUTER_API_KEY', '')
OPENROUTER_MODEL = os.getenv('OPENROUTER_MODEL', 'openai/gpt-4')  # ou anthropic/claude-3, meta-llama/llama-3, etc

# Banana.dev (modelos de ML/imagens)
# https://www.banana.dev/
BANANA_API_KEY = os.getenv('BANANA_API_KEY', '')
BANANA_MODEL_KEY = os.getenv('BANANA_MODEL_KEY', '')  # Key do modelo especifico

# Replicate (modelos de imagem - Stable Diffusion, DALL-E, etc)
# https://replicate.com/
REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN', '')

# Together AI (Llama, Mistral, etc)
# https://together.ai/
TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY', '')
TOGETHER_MODEL = os.getenv('TOGETHER_MODEL', 'meta-llama/Llama-3-70b-chat-hf')


# =============================================
# FUNÇÕES DE CLIENTE
# =============================================

def get_openai_client():
    """Retorna cliente OpenAI configurado"""
    try:
        from openai import OpenAI
        return OpenAI(
            api_key=OPENAI_API_KEY,
            organization=OPENAI_ORG_ID if OPENAI_ORG_ID else None
        )
    except ImportError:
        print("Instale: pip install openai")
        return None

def get_anthropic_client():
    """Retorna cliente Anthropic configurado"""
    try:
        import anthropic
        return anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    except ImportError:
        print("Instale: pip install anthropic")
        return None

def get_google_client():
    """Retorna cliente Google Gemini configurado"""
    try:
        import google.generativeai as genai
        genai.configure(api_key=GOOGLE_API_KEY)
        return genai.GenerativeModel(GOOGLE_MODEL)
    except ImportError:
        print("Instale: pip install google-generativeai")
        return None

def get_openrouter_client():
    """Retorna cliente OpenRouter (usa API compativel com OpenAI)"""
    try:
        from openai import OpenAI
        return OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url="https://openrouter.ai/api/v1"
        )
    except ImportError:
        print("Instale: pip install openai")
        return None

def get_banana_client():
    """Retorna cliente Banana.dev"""
    try:
        import banana_dev as banana
        return banana
    except ImportError:
        print("Instale: pip install banana-dev")
        return None

def get_replicate_client():
    """Retorna cliente Replicate"""
    try:
        import replicate
        # Replicate usa variavel de ambiente automaticamente
        os.environ['REPLICATE_API_TOKEN'] = REPLICATE_API_TOKEN
        return replicate
    except ImportError:
        print("Instale: pip install replicate")
        return None

def get_together_client():
    """Retorna cliente Together AI"""
    try:
        from openai import OpenAI
        return OpenAI(
            api_key=TOGETHER_API_KEY,
            base_url="https://api.together.xyz/v1"
        )
    except ImportError:
        print("Instale: pip install openai")
        return None


# =============================================
# FUNÇÕES DE CHAT SIMPLES
# =============================================

def chat_openai(prompt, system_prompt="Você é um assistente útil."):
    """Envia prompt para OpenAI e retorna resposta"""
    client = get_openai_client()
    if not client:
        return None

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def chat_anthropic(prompt, system_prompt="Você é um assistente útil."):
    """Envia prompt para Anthropic e retorna resposta"""
    client = get_anthropic_client()
    if not client:
        return None

    response = client.messages.create(
        model=ANTHROPIC_MODEL,
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text

def chat_google(prompt):
    """Envia prompt para Google Gemini e retorna resposta"""
    model = get_google_client()
    if not model:
        return None

    response = model.generate_content(prompt)
    return response.text

def chat_openrouter(prompt, system_prompt="Voce e um assistente util.", model=None):
    """
    Envia prompt para OpenRouter e retorna resposta
    Modelos disponiveis: openai/gpt-4, anthropic/claude-3, meta-llama/llama-3, etc
    """
    client = get_openrouter_client()
    if not client:
        return None

    response = client.chat.completions.create(
        model=model or OPENROUTER_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def chat_together(prompt, system_prompt="Voce e um assistente util.", model=None):
    """Envia prompt para Together AI e retorna resposta"""
    client = get_together_client()
    if not client:
        return None

    response = client.chat.completions.create(
        model=model or TOGETHER_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content


# =============================================
# FUNCOES DE GERACAO DE IMAGENS
# =============================================

def gerar_imagem_replicate(prompt, modelo="stability-ai/sdxl:latest", output_path="out/imagem.png"):
    """
    Gera imagem usando Replicate (Stable Diffusion, DALL-E, etc)

    Modelos populares:
    - stability-ai/sdxl:latest (Stable Diffusion XL)
    - stability-ai/stable-diffusion:latest
    - black-forest-labs/flux-schnell (rapido)
    - black-forest-labs/flux-pro (qualidade)
    """
    replicate = get_replicate_client()
    if not replicate:
        return None

    try:
        output = replicate.run(
            modelo,
            input={"prompt": prompt}
        )

        # Baixa a imagem
        import urllib.request
        if isinstance(output, list):
            url = output[0]
        else:
            url = output

        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        urllib.request.urlretrieve(url, output_path)
        print(f"Imagem salva: {output_path}")
        return output_path

    except Exception as e:
        print(f"Erro ao gerar imagem: {e}")
        return None

def gerar_imagem_banana(prompt, output_path="out/imagem.png"):
    """
    Gera imagem usando Banana.dev

    Requer BANANA_API_KEY e BANANA_MODEL_KEY configurados
    """
    banana = get_banana_client()
    if not banana:
        return None

    try:
        result = banana.run(
            BANANA_API_KEY,
            BANANA_MODEL_KEY,
            {"prompt": prompt}
        )

        # Decodifica imagem base64
        import base64
        if 'image' in result.get('modelOutputs', [{}])[0]:
            img_data = base64.b64decode(result['modelOutputs'][0]['image'])
            os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
            with open(output_path, 'wb') as f:
                f.write(img_data)
            print(f"Imagem salva: {output_path}")
            return output_path

    except Exception as e:
        print(f"Erro ao gerar imagem: {e}")
        return None

def gerar_imagem_openai(prompt, output_path="out/imagem.png", size="1024x1024"):
    """
    Gera imagem usando DALL-E (OpenAI)
    """
    client = get_openai_client()
    if not client:
        return None

    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality="standard",
            n=1,
        )

        url = response.data[0].url

        import urllib.request
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        urllib.request.urlretrieve(url, output_path)
        print(f"Imagem salva: {output_path}")
        return output_path

    except Exception as e:
        print(f"Erro ao gerar imagem: {e}")
        return None


# =============================================
# VERIFICAÇêO
# =============================================

def verificar_configuracao():
    """Verifica quais APIs estêo configuradas"""
    print("=" * 50)
    print("VERIFICAÇêO DE CONFIGURAÇêO DE APIs")
    print("=" * 50)

    apis = [
        ("OpenAI", OPENAI_API_KEY),
        ("Anthropic", ANTHROPIC_API_KEY),
        ("Google", GOOGLE_API_KEY),
        ("Azure OpenAI", AZURE_OPENAI_KEY),
        ("OpenRouter", OPENROUTER_API_KEY),
        ("Banana.dev", BANANA_API_KEY),
        ("Replicate", REPLICATE_API_TOKEN),
        ("Together AI", TOGETHER_API_KEY),
    ]

    for nome, chave in apis:
        status = "[OK] Configurada" if chave else "[X] Nao configurada"
        print(f"{nome}: {status}")

    print("=" * 50)
    print("\nPara configurar, crie um arquivo .env na raiz do projeto:")
    print("OPENAI_API_KEY=sk-...")
    print("ANTHROPIC_API_KEY=sk-ant-...")
    print("GOOGLE_API_KEY=...")


if __name__ == "__main__":
    verificar_configuracao()
