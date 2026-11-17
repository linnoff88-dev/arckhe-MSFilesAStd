# Scripts de Geração de Documentos

Scripts Python standalone para gerar documentos Word, Excel, PowerPoint e PDF.
Compatíveis com qualquer LLM (Codex, GPT-4, Claude, etc).

## Instalação

```bash
pip install python-docx openpyxl python-pptx reportlab
```

## Scripts Disponíveis

| Script | Formato | Biblioteca |
|--------|---------|------------|
| `generate_docx.py` | Word (.docx) | python-docx |
| `generate_xlsx.py` | Excel (.xlsx) | openpyxl |
| `generate_pptx.py` | PowerPoint (.pptx) | python-pptx |
| `generate_pdf.py` | PDF (.pdf) | reportlab |

## Uso Básico

### Gerar documento de exemplo:

```bash
python generate_docx.py                    # Cria out/documento_exemplo.docx
python generate_xlsx.py                    # Cria out/planilha_exemplo.xlsx
python generate_pptx.py                    # Cria out/apresentacao_exemplo.pptx
python generate_pdf.py                     # Cria out/documento_exemplo.pdf
```

### Especificar arquivo de saída:

```bash
python generate_docx.py meu_arquivo.docx
python generate_xlsx.py relatorio.xlsx
python generate_pptx.py apresentacao.pptx
python generate_pdf.py relatorio.pdf
```

## Uso com LLMs (Codex, GPT-4, etc)

Cada script contém **funções auxiliares** que podem ser usadas programaticamente:

### Word (docx)

```python
from generate_docx import *

# Criar documento personalizado
criar_documento_personalizado(
    titulo="Meu Relatório",
    secoes=[
        {"titulo": "Introdução", "conteudo": "Texto da introdução..."},
        {"titulo": "Análise", "conteudo": "Texto da análise..."},
    ],
    caminho_saida="out/relatorio.docx"
)

# Ou usar funções granulares
from docx import Document
doc = Document()
adicionar_titulo(doc, "Título", nivel=0)
adicionar_paragrafo(doc, "Texto do parágrafo", negrito=True)
adicionar_tabela(doc, [["A", "B"], ["1", "2"]])
adicionar_lista(doc, ["Item 1", "Item 2"], numerada=False)
doc.save("out/arquivo.docx")
```

### Excel (xlsx)

```python
from generate_xlsx import *

# Criar workbook
wb = novo_workbook()
ws = wb.active

# Adicionar dados
adicionar_tabela(ws, [
    ["Produto", "Preço", "Qtd"],
    ["A", 100, 5],
    ["B", 200, 3],
], linha_inicio=1, com_cabecalho=True)

# Adicionar gráficos
from openpyxl.chart import Reference
dados = Reference(ws, min_col=2, min_row=1, max_row=3)
cats = Reference(ws, min_col=1, min_row=2, max_row=3)
adicionar_grafico_barras(ws, dados, cats, posicao="E2", titulo="Vendas")

salvar_workbook(wb, "out/planilha.xlsx")
```

### PowerPoint (pptx)

```python
from generate_pptx import *
from pptx.dml.color import RGBColor

# Criar apresentação
prs = nova_apresentacao()

# Slide de título
adicionar_slide_titulo(prs, "Título Principal", "Subtítulo", cor_fundo=RGBColor(31, 78, 121))

# Slide com bullets
adicionar_slide_conteudo(prs, "Agenda", [
    "Primeiro ponto",
    "Segundo ponto",
    "Terceiro ponto"
])

# Slide com gráfico
adicionar_slide_grafico(prs, "Resultados",
    categorias=['Jan', 'Fev', 'Mar'],
    series_dados={'2024': [100, 150, 200]}
)

salvar_apresentacao(prs, "out/apresentacao.pptx")
```

### PDF

```python
from generate_pdf import *

# Criar documento
doc = novo_documento("out/relatorio.pdf")
styles = criar_estilos()
elementos = []

# Adicionar conteúdo
elementos.append(criar_paragrafo("Título do Relatório", 'TituloPrincipal', styles))
elementos.append(Spacer(1, 20))
elementos.append(criar_paragrafo("Texto do parágrafo...", 'TextoNormal', styles))

# Adicionar tabela
elementos.append(criar_tabela([
    ["Col1", "Col2", "Col3"],
    ["A", "B", "C"],
    ["D", "E", "F"],
]))

# Adicionar gráfico
elementos.append(criar_grafico_barras(
    [[10, 20, 30], [15, 25, 35]],
    ['A', 'B', 'C'],
    'Meu Gráfico'
))

# Gerar PDF
construir_pdf(doc, elementos)
```

## Exemplos de Prompts para LLMs

### Codex / GPT-4:

```
Usando o script generate_xlsx.py, crie uma planilha com:
- Dados de vendas de Janeiro a Junho
- Fórmulas de total e média
- Gráfico de barras comparativo
- Salvar como out/vendas_2024.xlsx
```

### Prompt genérico:

```
Importe as funções do generate_docx.py e crie um documento Word com:
1. Título "Relatório Mensal"
2. Seção de introdução
3. Tabela com 3 colunas de dados
4. Lista de próximos passos
Salve em out/relatorio_mensal.docx
```

## Estrutura dos Arquivos

```
scripts/
├── generate_docx.py    # Gerador Word
├── generate_xlsx.py    # Gerador Excel
├── generate_pptx.py    # Gerador PowerPoint
├── generate_pdf.py     # Gerador PDF
└── README.md           # Este arquivo
```

## Dependências

```
python-docx>=0.8.11
openpyxl>=3.1.0
python-pptx>=0.6.21
reportlab>=4.0.0
```

## Compatibilidade

- Python 3.8+
- Windows, macOS, Linux
- Funciona com qualquer LLM que execute código Python
