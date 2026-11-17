# Instalação e Configuração

Guia para instalar e configurar os scripts de geração de documentos.

---

## Requisitos

- Python 3.8 ou superior
- Conexão com internet (para APIs)

---

## Passo 1: Instalar Python

### Windows

1. Baixe em: https://www.python.org/downloads/
2. Execute o instalador
3. **IMPORTANTE:** Marque a opção "Add Python to PATH"
4. Clique em "Install Now"

### Verificar instalação

Abra o terminal (CMD ou PowerShell) e digite:
```bash
python --version
```

Deve aparecer algo como: `Python 3.11.x`

---

## Passo 2: Instalar Bibliotecas

Abra o terminal na pasta do projeto e execute:

```bash
pip install python-docx openpyxl python-pptx reportlab openai python-dotenv replicate
```

### O que cada biblioteca faz:

| Biblioteca | Função |
|------------|--------|
| `python-docx` | Criar documentos Word |
| `openpyxl` | Criar planilhas Excel |
| `python-pptx` | Criar apresentações PowerPoint |
| `reportlab` | Criar PDFs |
| `openai` | Conectar com OpenAI/OpenRouter/Together |
| `python-dotenv` | Ler arquivo .env |
| `replicate` | Gerar imagens com IA |

---

## Passo 3: Configurar API

### 3.1 Criar arquivo .env

Na pasta do projeto, copie o arquivo de exemplo:

**Windows (CMD):**
```bash
copy .env.example .env
```

**Windows (PowerShell) / Linux / Mac:**
```bash
cp .env.example .env
```

### 3.2 Obter chave de API

Escolha **UMA** das opções abaixo:

#### Opção A: OpenAI (GPT-4 + DALL-E)

1. Acesse: https://platform.openai.com/api-keys
2. Faça login ou crie conta
3. Clique em "Create new secret key"
4. Copie a chave (começa com `sk-`)

#### Opção B: OpenRouter (Acesso a várias LLMs)

1. Acesse: https://openrouter.ai/keys
2. Faça login com Google/GitHub
3. Clique em "Create Key"
4. Copie a chave (começa com `sk-or-`)

#### Opção C: Together AI (Mais barato)

1. Acesse: https://api.together.xyz/
2. Crie conta
3. Vá em Settings > API Keys
4. Copie a chave

#### Opção D: Replicate (Para imagens)

1. Acesse: https://replicate.com/account/api-tokens
2. Faça login com GitHub
3. Clique em "Create token"
4. Copie o token (começa com `r8_`)

### 3.3 Editar arquivo .env

Abra o arquivo `.env` com qualquer editor de texto (Notepad, VS Code, etc).

Cole sua chave na linha correspondente:

```env
# Se escolheu OpenAI:
OPENAI_API_KEY=sk-sua-chave-aqui

# Se escolheu OpenRouter:
OPENROUTER_API_KEY=sk-or-sua-chave-aqui

# Se escolheu Together AI:
TOGETHER_API_KEY=sua-chave-aqui

# Se escolheu Replicate (para imagens):
REPLICATE_API_TOKEN=r8_sua-chave-aqui
```

**Salve o arquivo.**

---

## Passo 4: Testar

### Testar geração de documento (sem LLM):

```bash
python scripts/generate_xlsx.py out/teste.xlsx
```

Se aparecer `Planilha criada: out/teste.xlsx` está funcionando.

### Testar com LLM:

```bash
python scripts/exemplo_com_llm.py "teste simples" xlsx
```

Se gerar o arquivo, a API está configurada corretamente.

### Verificar configuração:

```bash
python scripts/llm_config.py
```

Mostra quais APIs estão configuradas.

---

## Estrutura de Pastas

```
MSFilesA/
├── .env                 ← Suas chaves de API (NÃO compartilhe!)
├── .env.example         ← Modelo de configuração
├── COMO_USAR.md         ← Como usar os scripts
├── INSTALACAO.md        ← Este arquivo
├── scripts/
│   ├── exemplo_com_llm.py    ← Script principal
│   ├── gerar_imagem.py       ← Gerar imagens
│   ├── generate_docx.py      ← Gerar Word
│   ├── generate_xlsx.py      ← Gerar Excel
│   ├── generate_pptx.py      ← Gerar PowerPoint
│   ├── generate_pdf.py       ← Gerar PDF
│   └── llm_config.py         ← Configurações
└── out/                 ← Arquivos gerados
```

---

## Problemas Comuns

### "python não é reconhecido"

Python não está no PATH. Reinstale marcando "Add to PATH".

### "No module named 'xxx'"

Biblioteca não instalada. Execute:
```bash
pip install nome-da-biblioteca
```

### "API key not found" ou "Unauthorized"

- Verifique se o arquivo `.env` existe
- Verifique se a chave está correta (sem espaços extras)
- Verifique se tem créditos na conta da API

### "Permission denied" ao salvar arquivo

- Feche o arquivo Excel/Word se estiver aberto
- Verifique permissões da pasta `out/`

---

## Custos das APIs

| API | Custo |
|-----|-------|
| OpenAI GPT-4 | ~$0.03 por 1K tokens |
| OpenRouter | Varia por modelo |
| Together AI | ~$0.001 por 1K tokens |
| Replicate | ~$0.01 por imagem |

**Dica:** Together AI é o mais barato para texto. Replicate tem modelos gratuitos (FLUX Schnell).

---

## Próximos Passos

Após instalar, veja o arquivo **COMO_USAR.md** para aprender a gerar documentos.
