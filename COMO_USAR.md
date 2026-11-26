# Como Usar

Guia prático para gerar documentos no dia a dia.

---

## Gerar Planilha Excel

```bash
python scripts/exemplo_com_llm.py "seu assunto" xlsx
```

**Exemplos:**
```bash
python scripts/exemplo_com_llm.py "vendas mensais 2024" xlsx
python scripts/exemplo_com_llm.py "controle de estoque" xlsx
python scripts/exemplo_com_llm.py "gastos departamento" xlsx
```

---

## Gerar Documento Word

```bash
python scripts/exemplo_com_llm.py "seu assunto" docx
```

**Exemplos:**
```bash
python scripts/exemplo_com_llm.py "relatório trimestral" docx
python scripts/exemplo_com_llm.py "proposta comercial" docx
python scripts/exemplo_com_llm.py "ata de reuniêo" docx
```

---

## Gerar Apresentaçêo PowerPoint

```bash
python scripts/exemplo_com_llm.py "seu assunto" pptx
```

**Exemplos:**
```bash
python scripts/exemplo_com_llm.py "resultados Q4" pptx
python scripts/exemplo_com_llm.py "pitch de vendas" pptx
python scripts/exemplo_com_llm.py "treinamento equipe" pptx
```

---

## Gerar Imagem

```bash
python scripts/gerar_imagem.py "descriçêo da imagem"
```

**Exemplos:**
```bash
python scripts/gerar_imagem.py "logo minimalista tech"
python scripts/gerar_imagem.py "gráfico de barras 3D"
python scripts/gerar_imagem.py "paisagem corporativa"
```

Com nome do arquivo:
```bash
python scripts/gerar_imagem.py "logo azul" out/logo.png
```

---

## Assunto Detalhado

Use aspas para assuntos longos:

```bash
python scripts/exemplo_com_llm.py "Planilha de controle de incêndios no Brasil dos últimos 5 anos, com dados por bioma e por estado, incluindo gráficos comparativos" xlsx
```

---

## Usar Arquivo de Referência

Crie um arquivo `.txt` com as instruções:

**briefing.txt:**
```
Criar relatório de vendas contendo:
- Resumo executivo
- Vendas por regiêo
- Top 10 produtos
- Comparativo com ano anterior
- Recomendações
```

**Executar:**
```bash
python scripts/exemplo_com_llm.py briefing.txt docx
```

---

## Formatos Disponíveis

| Comando | Gera |
|---------|------|
| `xlsx` | Excel |
| `docx` | Word |
| `pptx` | PowerPoint |

---

## Onde Ficam os Arquivos

Todos os arquivos sêo salvos na pasta `out/`

---

## Resumo

```bash
# Excel
python scripts/exemplo_com_llm.py "assunto" xlsx

# Word
python scripts/exemplo_com_llm.py "assunto" docx

# PowerPoint
python scripts/exemplo_com_llm.py "assunto" pptx

# Imagem
python scripts/gerar_imagem.py "descriçêo"

# Com arquivo de referência
python scripts/exemplo_com_llm.py arquivo.txt xlsx
```
