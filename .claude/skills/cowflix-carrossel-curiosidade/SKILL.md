---
name: cowflix-carrossel-curiosidade
description: Use quando o usuário (Cowflix) pedir um carrossel de Instagram sobre uma CURIOSIDADE ATEMPORAL (fato chocante, dado contraintuitivo, descoberta, recorde, estatística inusitada, sem prazo de validade) para o perfil @cowflix. Aciona com pedidos como "carrossel de curiosidade pra Cowflix", "carrossel atemporal da Cowflix", "cria um carrossel sobre [tema] pro nosso Instagram". Já vem com o contexto da conta (handle, nicho, produto) e a identidade visual oficial da Cowflix pré-carregados — não é preciso reanexar o kit de marca. Para notícia dos últimos 7 dias, seria a `carrossel-noticia` (ainda não instalada).
---

# Carrossel de Curiosidade — Cowflix

Esta skill é uma especialização da `carrossel-curiosidade` genérica, com o
contexto da conta Cowflix e a identidade visual oficial da marca já
embutidos. Sempre que possível, gere as artes finais diretamente (PNG),
sem depender de ferramentas externas de geração de imagem.

## Contexto fixo da conta (não perguntar de novo)

- **Handle:** @cowflix
- **Nicho:** streaming de pecuária leiteira
- **Produto:** assinatura da plataforma Cowflix

Pode pular a Etapa 1 do fluxo genérico (coleta de contexto) e ir direto
para a Etapa 2 (buscar curiosidades). Se o usuário mencionar um
sub-produto específico (ex: "Elite do Leite — Imersão"), use-o no lugar
do produto padrão apenas para aquele carrossel.

## Fluxo (igual à skill genérica `carrossel-curiosidade`)

1. ~~Coleta de contexto~~ (já preenchido acima).
2. Buscar 5 curiosidades atemporais do nicho via `WebSearch`, com fonte
   obrigatória e verificável em cada uma. Se um número/recorde parecer
   ambíguo entre fontes (ex: total de lactação vs. torneio de N dias),
   avise o usuário antes de escrever o carrossel — não estampe um dado
   que não bateu entre as fontes.
3. Usuário escolhe o tema.
4. Pergunte o tom de comunicação (mesma lista de 7 tons da skill genérica).
5. Escreva o carrossel: 7 a 9 slides, seguindo as regras de copy da
   skill genérica (sem travessão, sem exclamação, sem pergunta na capa,
   sem "não é X, é Y", produto só implícito no CTA final, etc.). Prefira
   frases curtas — a identidade visual da Cowflix pede bullets/linhas
   curtas, não parágrafos longos (ver "Regras de marca" abaixo).
6. Aprovação do texto (gate obrigatório, repita até aprovar).
7. Gerar as artes finais — ver seção "Como montar as artes" abaixo.

## Identidade visual oficial da Cowflix

Fonte: kit de identidade visual anexado pelo usuário em 2026-07-05
(`Cowflix_Kit_IdentidadeVisual_SocialMedia.html`). Resumo do que importa
para carrosséis:

### Paleta (usar no máximo estas cores por slide)

| Nome | Hex | Uso |
|---|---|---|
| Verde Cowflix | `#35C976` | Cor principal · títulos de destaque · CTAs · kicker/badge |
| Verde-Escuro Fundo | `#0F2926` | Fundo padrão de todos os slides |
| Verde Noturno | `#071a12` | Fundo alternativo (variação ocasional) |
| Branco Puro | `#FFFFFF` | Texto principal (títulos/headline) |
| Cinza Texto | `#BBBBBB` | Texto secundário / corpo |
| Dourado Urgência | `#C8960C` | SOMENTE preços, badges de lote, datas, urgência |
| Vermelho Impacto | `#EF5350` | SOMENTE perdas financeiras, alertas críticos (nunca em algo positivo) |

Curiosidades atemporais normalmente não usam dourado nem vermelho —
esses ficam reservados para conteúdo comercial/de alerta.

### Tipografia

- **Montserrat** (Black/900 para títulos, Bold/700 para kickers e labels
  em uppercase com letter-spacing).
- **Inter** (Regular/400 para corpo, SemiBold/600 para notas/CTA).
- Fontes já instaladas neste ambiente via apt (`fonts-montserrat`,
  `fonts-inter`, `fonts-noto-color-emoji` para o emoji 🐄 colorido). Se
  não estiverem disponíveis, rode:
  `apt-get install -y fonts-montserrat fonts-inter fonts-noto-color-emoji`

### Regras de marca (do kit oficial)

Sempre:
- Fundo escuro (`#0F2926` ou `#111`) como padrão.
- Montserrat em todos os títulos e destaques.
- Logo Cowflix presente em todos os slides, sempre.
- Verde para destaques positivos e CTAs.
- Hierarquia clara: título grande → badge/kicker → corpo.
- Número do slide discreto em todos (ex: `02/08`).
- Seta de deslize visível no slide 1 do carrossel.
- Emoji 🐄 como elemento visual recorrente.
- Formato de carrossel: **1:1 quadrado (1080x1080)**.

Nunca:
- Fundo branco ou cores pastéis.
- Fontes genéricas (Arial, Roboto) nos títulos.
- Texto menor que 28pt no celular.
- Mais de 3 cores diferentes no mesmo slide.
- Logo distorcida ou fora de proporção.
- Vermelho em elementos positivos.
- Texto corrido longo — usar bullets curtos.
- Estilos diferentes entre slides do mesmo carrossel.
- Gradientes coloridos (roxo, rosa).
- Publicar carrossel sem número de slide visível.

### Logo

- Arquivo pronto (já com fundo transparente, alpha derivado do fundo
  preto original): `assets/cowflix_logo.png` (relativo à pasta desta
  skill).
- Posicionamento em carrossel (1:1): canto inferior direito, opacidade
  60–70%.
- Nunca menor que 80px de largura.

## Como montar as artes (Etapa 7)

Como o próprio kit da Cowflix usa cards de texto (fundo sólido +
tipografia), não fotos, **monte todos os slides diretamente aqui**, sem
depender de DALL-E ou de o usuário rodar algo em outra ferramenta. Use o
módulo pronto `assets/cowflix_slides.py` desta skill:

```python
import sys, os
sys.path.insert(0, "<base_directory_da_skill>/assets")
from cowflix_slides import build_cover_slide, build_content_slide, build_cta_slide

TOTAL = 8  # ajuste ao número real de slides aprovados

build_cover_slide(
    1, TOTAL,
    "Curiosidade atemporal",   # tag/kicker do slide 1
    "Título forte de até ~8 palavras.",
    "Subtítulo reflexivo de uma linha.",
    "/caminho/de/saida/slide-1-papel.png",
)

build_content_slide(
    2, TOTAL,
    "Kicker curto",            # 2-3 palavras, vira uppercase automaticamente
    "Frase forte do slide (headline).",
    "Complemento em uma ou duas linhas curtas.",
    "/caminho/de/saida/slide-2-papel.png",
)

# ... repetir build_content_slide para os slides do meio ...

build_cta_slide(
    TOTAL, TOTAL,
    "Todos os dias, conteúdo sobre",
    "pecuária leiteira aqui no @cowflix.",   # linha em destaque, verde
    "Me segue para receber a próxima.",
    "/caminho/de/saida/slide-N-papel.png",
)
```

Depois de gerar, **sempre olhe o resultado com a ferramenta `Read`**
antes de entregar (para pegar overflow de texto, contraste ruim etc.), e
entregue os PNGs com `SendUserFile`.

Se algum slide precisar mesmo de foto real (ex: um evento/pessoa muito
específico e verificável), siga o modo "foto real" da skill genérica
`carrossel-curiosidade` (busca via `WebSearch`, download e composição
via Bash/Pillow) em vez do template de texto — mas isso deve ser exceção,
não a regra, para manter a consistência visual pedida pelo kit.

### Arquivo de automação (Parte C)

Mantenha o mesmo formato de arquivo consolidado (`=== SLIDE N ===` /
`=== FIM SLIDE N ===`, `MODO: 3` para todos já que são cards de texto)
descrito na skill genérica, caso o usuário quera integrar com automação.
Isso é opcional quando as artes já são entregues prontas em PNG.
