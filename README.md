# MSFilesAStd

Scripts Python independentes para geracao de documentos (Word, Excel, PowerPoint e PDF).
Funciona com qualquer LLM ou de forma standalone.

## Requisitos

- **Python** (3.8+) - https://python.org/

## Instalacao Rapida

```bash
pip install python-docx openpyxl python-pptx reportlab openai python-dotenv replicate
```

Para instrucoes detalhadas, veja **[INSTALACAO.md](INSTALACAO.md)**.

## Como Usar

### Gerar documentos com LLM:

```bash
# Excel
python scripts/exemplo_com_llm.py "vendas mensais 2024" xlsx

# Word
python scripts/exemplo_com_llm.py "relatorio trimestral" docx

# PowerPoint
python scripts/exemplo_com_llm.py "apresentacao de resultados" pptx

# Imagem
python scripts/gerar_imagem.py "logo minimalista tech"
```

### Gerar documentos de exemplo (sem LLM):

```bash
python scripts/generate_xlsx.py out/teste.xlsx
python scripts/generate_docx.py out/teste.docx
python scripts/generate_pptx.py out/teste.pptx
python scripts/generate_pdf.py out/teste.pdf
```

Para mais exemplos, veja **[COMO_USAR.md](COMO_USAR.md)**.

## Estrutura do Projeto

```
MSFilesAStd/
â”œâ”€â”€ .env.example         # Modelo de configuracao de APIs
â”œâ”€â”€ INSTALACAO.md        # Guia de instalacao
â”œâ”€â”€ COMO_USAR.md         # Guia de uso
â”œâ”€â”€ assets/              # Imagens e recursos
â”‚   â””â”€â”€ logo.png
â”œâ”€â”€ out/                 # Arquivos gerados
â”œâ”€â”€ scripts/             # Scripts de geracao
â”‚   â”œâ”€â”€ generate_docx.py     # Gerador Word
â”‚   â”œâ”€â”€ generate_xlsx.py     # Gerador Excel
â”‚   â”œâ”€â”€ generate_pptx.py     # Gerador PowerPoint
â”‚   â”œâ”€â”€ generate_pdf.py      # Gerador PDF
â”‚   â”œâ”€â”€ gerar_imagem.py      # Gerador de imagens
â”‚   â”œâ”€â”€ exemplo_com_llm.py   # Script principal com LLM
â”‚   â”œâ”€â”€ llm_config.py        # Configuracoes de API
â”‚   â””â”€â”€ README.md            # Documentacao tecnica
â””â”€â”€ reference/           # Arquivos de referencia
```

## Scripts Disponiveis

| Script | Formato | Biblioteca |
|--------|---------|------------|
| `generate_docx.py` | Word (.docx) | python-docx |
| `generate_xlsx.py` | Excel (.xlsx) | openpyxl |
| `generate_pptx.py` | PowerPoint (.pptx) | python-pptx |
| `generate_pdf.py` | PDF (.pdf) | reportlab |
| `gerar_imagem.py` | Imagens (PNG) | Replicate/OpenAI |

## APIs Suportadas

| API | Uso |
|-----|-----|
| OpenAI | GPT-4 + DALL-E |
| OpenRouter | Acesso a varias LLMs |
| Together AI | LLMs mais baratas |
| Replicate | Geracao de imagens |

## Documentacao

- **[INSTALACAO.md](INSTALACAO.md)** - Como instalar e configurar
- **[COMO_USAR.md](COMO_USAR.md)** - Exemplos de uso
- **[scripts/README.md](scripts/README.md)** - Documentacao tecnica dos scripts

---

Projeto adaptado da comunidade INEMA TDS - Marca Arckhe