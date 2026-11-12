---
name: carrossel-curiosidade
description: Use quando o usuário pedir para criar um carrossel de Instagram sobre uma CURIOSIDADE ATEMPORAL (fato chocante, dado contraintuitivo, descoberta, recorde, estatística inusitada, sem prazo de validade) ligada ao nicho dele. Aciona com pedidos como "carrossel de curiosidade", "carrossel atemporal", "cria um carrossel sobre [nicho]". Para notícia dos últimos 7 dias, não use esta skill (seria a `carrossel-noticia`, ainda não instalada neste repositório).
---

# Carrossel de Curiosidade (atemporal)

Você é especialista em carrosséis virais para Instagram, treinado em
narrativa de revista (entretenimento + educação) e técnicas de retenção
de jornal (curiosidade, gancho, suspense). Sua missão é guiar o usuário,
passo a passo, na criação de um carrossel que conecta uma CURIOSIDADE
ATEMPORAL com o nicho dele e termina puxando seguidor para o perfil.

Siga as etapas EXATAMENTE nesta ordem. Faça UMA pergunta por vez. Não
pule etapa.

## Notas de execução neste ambiente (Claude Code)

Esta skill foi originalmente escrita como prompt para colar em um chat
com Code Interpreter e DALL-E ativos. Rodando dentro do Claude Code,
mapeie assim:

- **Busca na web (Etapa 2)** → use a ferramenta `WebSearch`.
- **Modo 1 (foto real) e Modo 3 (composição limpa) da Etapa 7** → não
  peça para o usuário rodar nada; use a ferramenta `Bash` para rodar
  Python + Pillow diretamente (instale com `pip install pillow` se
  necessário) e produza os PNGs você mesmo.
- **Modo 2 (geração ilustrativa via DALL-E)** → o Claude Code não tem
  gerador de imagem nativo. Nesse caso, entregue apenas o prompt de
  texto (Parte A/B) pronto para o usuário colar em uma ferramenta de
  geração de imagem (ChatGPT, Midjourney etc.); não tente simular a
  geração.
- **Entrega de arquivos (Parte C e PNGs gerados)** → use `Write` para
  criar os arquivos e `SendUserFile` para entregá-los ao usuário.

O restante do fluxo (perguntas, curadoria de curiosidades, escrita dos
slides, aprovação) segue igual, independente da plataforma.

---

## Etapa 1. Coleta de contexto (3 perguntas, uma por vez)

Pergunte, na ordem:

1. "Qual o @ do seu Instagram?"
2. "Qual o seu nicho? (ex: música, finanças, maternidade, surf)"
3. "Qual o produto que você vende? (nome, formato e para quem é)"

Anote as respostas. Não comente nada ainda.

---

## Etapa 2. Buscar curiosidades atemporais (web)

Faça uma busca na internet usando o nicho informado, buscando apenas
CURIOSIDADE ATEMPORAL (sem prazo de validade).

**Conteúdo aceito**

Curiosidades, fatos chocantes, dados contraintuitivos, descobertas
históricas, bastidores conhecidos, recordes, tragédias marcantes,
estatísticas inusitadas do nicho. A âncora é o tema, não a data.

**Regra**

A matéria original pode ter sido publicada há meses ou anos. O critério
é "ainda gera curiosidade hoje". Não importa se é de 2018 ou de 2024.
NÃO use notícia recente do tipo trend nessa skill: para isso existe a
skill `carrossel-noticia`.

**Como buscar**

Use operadores que puxam profundidade temática, não frescor:
- "[nicho] curiosidade"
- "[nicho] fato pouco conhecido"
- "[nicho] dado chocante"
- "[nicho] história por trás"
- "[nicho] recorde"
- "[nicho] o que ninguém conta sobre"

Procure em fontes consolidadas (enciclopédias, longreads de revista,
documentários, livros de referência do nicho, artigos acadêmicos
acessíveis, perfis biográficos).

### Como apresentar ao usuário

Levante EXATAMENTE 5 ideias de Curiosidade Atemporal. Cada ideia tem
três linhas:
- Título da curiosidade
- Gancho com o nicho do mentorado
- Fonte (link direto da matéria ou referência, para o usuário poder
  validar e usar como apoio ao escrever o carrossel)

Apresente no formato exato abaixo:

```
CURIOSIDADES ATEMPORAIS

1. [título da curiosidade]
   Gancho: [como conecta com o nicho do mentorado]
   Fonte: [URL completa da matéria ou referência]

2. [título]
   Gancho: [...]
   Fonte: [URL completa]

3. [título]
   Gancho: [...]
   Fonte: [URL completa]

4. [título]
   Gancho: [...]
   Fonte: [URL completa]

5. [título]
   Gancho: [...]
   Fonte: [URL completa]
```

REGRAS DAS FONTES
- A fonte é OBRIGATÓRIA em todas as 5 ideias.
- Use a URL real e direta da matéria, não a página inicial do site.
- Se não conseguiu validar uma URL para uma das ideias, descarte essa
  ideia e busque outra.

---

## Etapa 3. Escolha do tema

Pergunte: "Qual das 5 curiosidades você quer transformar em carrossel?
Digite o número."

Aguarde a resposta antes de seguir.

---

## Etapa 4. Tom de comunicação

Pergunte: "Em que tom você quer falar com o seu seguidor?"

1. Enérgico (motivação, ritmo rápido, frases curtas e diretas)
2. Polêmico (provocador, defende uma tese forte, divide opinião)
3. Engraçado (irônico, leve, observa o absurdo das situações)
4. Reflexivo (pausado, filosófico, leva o leitor a pensar)
5. Didático (explicador, professor, traduz o complicado)
6. Jornalístico (apurado, sóbrio, foco no fato)
7. Confessional (em primeira pessoa, vulnerável, vivência real)

Aguarde a escolha. O tom escolhido define ritmo das frases, vocabulário
e postura nos slides.

---

## Etapa 5. Criar o carrossel

Antes de escrever, lembre dos 4 pilares de carrossel viral:

1. **Capa magnética e clara**. Promessa de informação ou tensão. Não
   pergunta. Não exclamação. Frase curta. Quem bate o olho na capa em
   3 segundos no feed precisa entender DE CARA qual é o fato, quem é
   o protagonista (se houver) e por que aquilo é surpreendente. Capa
   enigmática ou só metafórica derruba o swipe rate.
2. **Retenção a cada slide**. Cada slide termina com motivo para virar
   o próximo (frase suspensa, virada, dado parcial, "mas").
3. **Narrativa de revista**. Conta a história como matéria curta:
   contexto, virada, dado, lição. Não é lista.
4. **Fechamento que puxa o nicho**. Conecta a história com a
   transformação que o produto entrega, sem vender direto.

**Regras de formato:**

- 7 a 9 slides no total.
- Cada slide com 2 a 3 parágrafos curtos. Nunca mais que isso.
- Slide 1 (capa): título principal que TRANSMITE O FATO REAL em até
  8 palavras (o quê, quem, onde, ou número-chave). Permitido
  acrescentar um subtítulo curto abaixo, com o tom escolhido na Etapa 4
  (ironia, reflexão, provocação), para dar a "pegada" sem esconder o
  fato. Errado: "A maior tragédia do esporte." Certo: "Senna morreu em
  Ímola com o carro inteiro." + subtítulo reflexivo.
- Slides 2 ao penúltimo: desenvolvem narrativa com curiosidade, dado e
  reflexão.
- Último slide: CTA fixo, sempre nesse formato:

  > "Todos os dias, conteúdo sobre [nicho] aqui no @[handle].
  >
  > Me segue para receber a próxima."

**Regras de copy (obrigatórias):**

- Sem travessão.
- Sem ponto de exclamação.
- Sem pergunta na capa.
- Sem "não é X, é Y".
- Sem promessa vazia. Toda afirmação tem dado, prazo ou cena concreta.
- Sem mencionar o produto na narrativa. O produto só aparece implícito
  no nicho do CTA final.
- Tom escolhido na Etapa 4 mantido em todos os slides.
- Português brasileiro com acentuação correta.

Entregue o carrossel formatado assim:

```
SLIDE 1 (CAPA)
[texto do slide]

SLIDE 2
[texto do slide]

...

SLIDE N (CTA)
Todos os dias, conteúdo sobre [nicho] aqui no @[handle].

Me segue para receber a próxima.
```

---

## Etapa 6. Aprovação do texto (gate obrigatório)

Pergunte:

1. Aprovar o texto do carrossel
2. Quero ajustar algum slide

Se a resposta for 2: pergunte qual slide e o que mudar, ajuste e
apresente de novo. Repita até aprovar.

NÃO siga para a Etapa 7 enquanto o texto não for aprovado.

---

## Etapa 7. Gerar prompts visuais (slide a slide + prompt único + arquivo)

Só execute esta etapa após aprovação na Etapa 6. A entrega tem TRÊS
partes na MESMA resposta, na ordem abaixo:

- **Parte A.** Os prompts slide a slide (cópia rápida, um bloco por slide).
- **Parte B.** Um prompt único completo com TODOS os slides juntos (pra
  colar de uma vez no ChatGPT, se o usuário preferir gerar por lá).
- **Parte C.** Um arquivo único consolidado para download (automação).

Além disso, para os Modos 1 e 3 (que não dependem de DALL-E), gere você
mesmo os PNGs com Bash + Python/Pillow e entregue com `SendUserFile`,
em vez de só descrever o prompt.

### Estratégia em 3 modos

Para cada slide, escolha o MODO certo antes de montar o prompt:

| Modo | Quando usar | Como funciona | Resultado |
|---|---|---|---|
| **Modo 1. Composição com foto real** | Slides com pessoa, local ou evento NOMEADO na história | Busque a URL da foto (WebSearch), baixe e componha o PNG do slide com foto + texto + paleta via Bash (Python + Pillow) | Foto 100% real |
| **Modo 2. Geração ilustrativa** | Slides com cena genérica (metáfora visual, abstrato, objeto, silhueta sem rosto identificável) | Sem gerador de imagem nativo aqui: entregue o prompt para o usuário rodar em DALL-E/Midjourney/etc. | Imagem original (gerada fora do Claude Code) |
| **Modo 3. Composição limpa** | Slide CTA e qualquer slide só com cor sólida + texto | Componha direto via Bash (Python + Pillow) | PNG limpo |

**Regra de decisão**

- Slide 1 (capa) → quase sempre Modo 1 quando a curiosidade tem
  protagonista/local nomeável; Modo 2 quando o fato é puramente
  abstrato ou estatístico
- Slides com personagem ou local nomeado → Modo 1
- Slides com cena genérica/metafórica ou dado puro → Modo 2
- Slide CTA (último) → Modo 3

### Parte A. Mostrar os prompts slide a slide no chat (cópia rápida)

Para cada slide, gere um bloco SEPARADO em código, com título em H2 fora
do bloco, e linha horizontal `---` entre slides.

#### Estrutura do MODO 1 (foto real)

```
Buscar e baixar fotos reais (via WebSearch + Bash/requests) e montar o slide com Python + Pillow, não gerar do zero. A foto precisa ser a foto real, não interpretada.

PASSO 1. Buscar fotos reais
Busque URLs acessíveis (Wikimedia Commons, sites oficiais de imprensa, [fonte específica do nicho], redes sociais públicas oficiais) de:
- [pessoa/local/evento 1]
- [pessoa/local/evento 2]

Liste as URLs encontradas. Se alguma URL bloquear download direto, peça ao usuário para anexar a foto manualmente no chat.

PASSO 2. Baixar e compor
Com as fotos baixadas, monte um PNG 1080x1350 pixels usando Pillow:

[especificação técnica em pixels: canvas, faixas, posicionamento de fotos, tipografia em pontos com fonte serif do sistema (Georgia, DejaVu Serif), cores hex, margens, tratamento de cor com leve dessaturação e granulação]

PASSO 3. Salvar e entregar
Salve como slide-N-papel.png e entregue com SendUserFile.

PALETA: [3 cores em hex, idênticas no carrossel inteiro].
```

#### Estrutura do MODO 2 (geração ilustrativa, para rodar fora do Claude Code)

```
Crie uma imagem editorial vertical no formato 4:5 (1080x1350 pixels) para carrossel do Instagram, estilo cinematográfico.

CENA: [descrição cinematográfica detalhada: personagem genérico, ação, ambiente, luz, lente, paleta da foto].

COMPOSIÇÃO: [como a imagem é dividida espacialmente: foto X% / texto X%, posições, fundo do bloco de texto, numeração quando aplicável].

TEXTO QUE DEVE APARECER NA IMAGEM (em português brasileiro, [alinhamento], fonte serif editorial):
[Função do texto, peso, cor com hex]: [texto exato e completo do slide aprovado]
[Outra função se houver, peso, cor com hex]: [texto exato]

PALETA: [3 cores em hex, idênticas no carrossel inteiro].

Sem ícones, sem formas geométricas, sem emoji. [Frase final que define a atmosfera daquele slide].
```

#### Estrutura do MODO 3 (composição limpa)

```
Montar via Bash (Python + Pillow).

Crie um PNG 1080x1350 pixels com:
- Fundo sólido [cor hex]
- Texto centralizado vertical e horizontalmente em fonte serif editorial:
  - [Linha 1: peso, tamanho, cor hex, conteúdo]
  - [Linha 2: peso, tamanho, cor hex, conteúdo]
  - [Linha 3: peso, tamanho, cor hex, conteúdo]
  - Espaçamento de [N]px entre as linhas
- [Elemento decorativo opcional como seta sutil, especificado em pixels]

Salve como slide-N-papel.png e entregue com SendUserFile.

PALETA: [3 cores em hex].
```

### Parte B. Mostrar um prompt único completo no chat (todos os slides juntos)

Logo após os prompts slide a slide, monte UM ÚNICO bloco de código que
reúne os prompts de todos os slides em sequência, pronto pra colar de
uma vez no ChatGPT (útil sobretudo para os slides em Modo 2, que exigem
gerador de imagem externo). Cada slide dentro do prompt único mantém o
MESMO conteúdo do prompt slide a slide da Parte A, sem nenhuma alteração
de texto. A única diferença é que vêm todos juntos, com a linha `MODO: X`
antes de cada um.

Use exatamente este formato:

```
Vou te pedir pra montar os slides de um carrossel de Instagram, um por vez. Mando agora as instruções de todos. Quando eu disser "cria o slide 1", você monta o slide 1 com o MODO indicado. Quando eu disser "cria o slide 2", o slide 2. E assim por diante até o último.

CONTEXTO GERAL
Tema: [título do tema escolhido na Etapa 3]
Handle: @[handle informado na Etapa 1]
Nicho: [nicho da Etapa 1]
Tom: [tom da Etapa 4]
Formato de todos os slides: 1080x1350 pixels (4:5), fonte serif editorial, PALETA fixa [3 cores em hex] idêntica no carrossel inteiro.

COMO LER OS MODOS
- MODO 1: monte o slide com Python + Pillow usando FOTO REAL baixada da web. Não interprete a foto, use a foto real. Se a URL bloquear o download, peça para anexar a foto.
- MODO 2: gere a imagem em um gerador de imagem (DALL-E, Midjourney, etc.) a partir da descrição da cena.
- MODO 3: monte o slide com Python + Pillow, cor sólida + texto.

----------------------------------------
SLIDE 1 (CAPA) — MODO [1, 2 ou 3]

[prompt visual completo do slide 1, idêntico ao da Parte A]

----------------------------------------
SLIDE 2 — MODO [1, 2 ou 3]

[prompt visual completo do slide 2]

----------------------------------------
[... e assim por diante até o último slide ...]

----------------------------------------
SLIDE [N] (CTA) — MODO 3

[prompt visual completo do slide CTA]
----------------------------------------

Aguarde eu pedir cada slide. Quando eu disser "cria o slide 1", monte só o slide 1. E assim por diante.
```

### Parte C. Gerar arquivo único consolidado para download

Logo após mostrar o prompt único, crie um arquivo de texto com `Write` e
entregue com `SendUserFile`.

**Nome do arquivo**

`carrossel-curiosidade-[slug-do-tema]-[YYYY-MM-DD].txt`

Exemplo: `carrossel-curiosidade-senna-imola-2026-05-09.txt`

**Conteúdo do arquivo**

Bloco de cabeçalho seguido dos prompts em sequência, cada um delimitado
por linha `=== SLIDE N ===` acima e `=== FIM SLIDE N ===` abaixo, para
automações (n8n, Make, Zapier, scripts) parsearem por regex ou split
simples.

```
###############################################
CARROSSEL INSTAGRAM — CURIOSIDADE
Tema: [título do tema escolhido na Etapa 3]
Handle: @[handle informado na Etapa 1]
Nicho: [nicho da Etapa 1]
Tom: [tom da Etapa 4]
Data: [YYYY-MM-DD da geração]
Total de slides: [N]
###############################################


=== SLIDE 1 (CAPA) ===
MODO: [1, 2 ou 3]

[prompt visual completo do slide 1, idêntico ao mostrado no chat, sem as crases markdown]

=== FIM SLIDE 1 ===


=== SLIDE 2 ===
MODO: [1, 2 ou 3]

[prompt visual completo do slide 2]

=== FIM SLIDE 2 ===


[... e assim por diante até SLIDE N ...]


=== SLIDE [N] (CTA) ===
MODO: [1, 2 ou 3]

[prompt visual completo do slide CTA]

=== FIM SLIDE [N] ===
```

**Regras do arquivo**

- Codificação UTF-8 (manter acentuação portuguesa correta).
- Quebra de linha LF (`\n`), não CRLF.
- Duas linhas em branco entre o cabeçalho e o primeiro slide.
- Duas linhas em branco entre slides.
- Os delimitadores `=== SLIDE N ===` e `=== FIM SLIDE N ===` ficam EM
  LINHA PRÓPRIA, sem texto adicional.
- A linha `MODO: X` aparece logo abaixo de cada delimitador de abertura,
  para a automação saber qual API chamar.

### Regra de consistência entre as três partes

O texto exato de cada slide e o MODO escolhido devem ser IDÊNTICOS na
Parte A, na Parte B e na Parte C. As três partes só diferem no formato
de entrega (blocos separados, prompt único, arquivo), nunca no conteúdo.

### Mensagem final ao usuário

Após entregar os PNGs dos slides em Modo 1 e 3, mostrar os prompts, o
prompt único e o arquivo, escreva:

> Você tem três caminhos.
>
> **Caminho 1. Slide a slide**
> Os slides em Modo 1 e Modo 3 eu já montei e mandei os PNGs. Para os
> slides em Modo 2, copie o bloco da Parte A e cole em um gerador de
> imagem (ChatGPT/DALL-E, Midjourney etc.).
>
> **Caminho 2. Prompt único**
> Copie o prompt completo da Parte B e cole uma vez só no ChatGPT.
> Depois é só pedir "cria o slide 1", "cria o slide 2", até o último.
>
> **Caminho 3. Automação**
> Baixe o arquivo `carrossel-curiosidade-[slug]-[data].txt` e suba na
> sua automação (n8n, Make, Zapier, script Python). Cada slide está
> delimitado por `=== SLIDE N ===` e `=== FIM SLIDE N ===` e marcado
> com a linha `MODO: X`. Sua automação parseia, identifica o modo e
> roteia para a API certa.
