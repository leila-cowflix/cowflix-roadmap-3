"""
Gerador de slides de carrossel na identidade visual da Cowflix.

Uso tipico (dentro de um script Python chamado via Bash):

    import sys, os
    sys.path.insert(0, os.path.dirname(__file__))  # pasta assets/ da skill
    from cowflix_slides import build_cover_slide, build_content_slide, build_cta_slide

    TOTAL = 8
    build_cover_slide(1, TOTAL, "Curiosidade atemporal", "Titulo do fato.",
                       "Subtitulo reflexivo.", "/caminho/saida/slide-1-papel.png")
    build_content_slide(2, TOTAL, "Kicker curto", "Frase forte do slide.",
                         "Complemento em uma ou duas linhas.", "/caminho/saida/slide-2-papel.png")
    ...
    build_cta_slide(8, TOTAL, "Todos os dias, conteudo sobre",
                     "pecuaria leiteira aqui no @cowflix.",
                     "Me segue para receber a proxima.", "/caminho/saida/slide-8-papel.png")

Todas as funcoes recebem o caminho de saida completo (out_path), incluindo
o nome do arquivo PNG.
"""

import os
from PIL import Image, ImageDraw, ImageFont

ASSETS_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(ASSETS_DIR, "cowflix_logo.png")

W = H = 1080

# Paleta oficial Cowflix (ver .claude/skills/cowflix-carrossel-curiosidade/SKILL.md)
BG = (15, 41, 38)          # #0F2926 Verde-Escuro Fundo — fundo padrao de slides
GREEN = (53, 201, 118)     # #35C976 Verde Cowflix — cor principal / destaques / CTAs
WHITE = (255, 255, 255)    # #FFFFFF — texto principal
GRAY = (187, 187, 187)     # #BBBBBB — texto secundario
MUTED = (85, 102, 85)      # muted label (numero de slide)
GOLD = (200, 150, 12)      # #C8960C — usar SO para preco/urgencia
RED = (239, 83, 80)        # #EF5350 — usar SO para perdas/alertas criticos

MONTS_BLACK = "/usr/share/fonts/opentype/montserrat/Montserrat-Black.otf"
MONTS_BOLD = "/usr/share/fonts/truetype/montserrat/Montserrat-Bold.ttf"
INTER_REG = "/usr/share/fonts/opentype/inter/Inter-Regular.otf"
INTER_SEMI = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
EMOJI_FONT = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"

MARGIN = 84

_EMOJI_NATIVE_SIZE = 109


def _font(path, size):
    return ImageFont.truetype(path, size)


def _emoji_font():
    return ImageFont.truetype(EMOJI_FONT, _EMOJI_NATIVE_SIZE)


def _emoji_image(emoji, target_size):
    tmp = Image.new("RGBA", (140, 140), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    d.text((0, 0), emoji, font=_emoji_font(), embedded_color=True)
    bbox = tmp.getbbox()
    if bbox:
        tmp = tmp.crop(bbox)
    ratio = target_size / max(tmp.size)
    tmp = tmp.resize((max(1, int(tmp.width * ratio)), max(1, int(tmp.height * ratio))), Image.LANCZOS)
    return tmp


def _paste_emoji(canvas, emoji, xy, target_size):
    im = _emoji_image(emoji, target_size)
    canvas.paste(im, xy, im)


def _load_logo():
    return Image.open(LOGO_PATH).convert("RGBA")


_LOGO = _load_logo()


def _wrap_text(draw, text, fnt, max_width):
    words = text.split(" ")
    lines = []
    cur = ""
    for w in words:
        trial = (cur + " " + w).strip()
        bbox = draw.textbbox((0, 0), trial, font=fnt)
        if bbox[2] - bbox[0] <= max_width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def _draw_lines(draw, lines, fnt, x, y, fill, line_gap):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        bbox = draw.textbbox((0, 0), line, font=fnt)
        y += (bbox[3] - bbox[1]) + line_gap
    return y


def _block_height(draw, lines, fnt, line_gap):
    h = 0
    for line in lines:
        bbox = draw.textbbox((0, 0), line, font=fnt)
        h += (bbox[3] - bbox[1]) + line_gap
    return h - line_gap if lines else 0


def _paste_logo(canvas, opacity=0.65, width=150):
    logo = _LOGO.copy()
    ratio = width / logo.width
    logo = logo.resize((width, int(logo.height * ratio)), Image.LANCZOS)
    r, g, b, a = logo.split()
    a = a.point(lambda v: int(v * opacity))
    logo.putalpha(a)
    x = W - MARGIN - logo.width
    y = H - MARGIN - logo.height
    canvas.paste(logo, (x, y), logo)


def _slide_number(draw, n, total):
    label = f"{n:02d} / {total:02d}"
    f = _font(MONTS_BOLD, 22)
    draw.text((MARGIN, H - MARGIN - 22), label, font=f, fill=MUTED)


def _kicker(canvas, draw, text, y):
    _paste_emoji(canvas, "\U0001F404", (MARGIN, y - 4), 34)
    f = _font(MONTS_BOLD, 24)
    draw.text((MARGIN + 48, y + 6), text.upper(), font=f, fill=GREEN)


def _base_canvas():
    return Image.new("RGBA", (W, H), BG + (255,))


def build_content_slide(n, total, kicker_text, headline, subtext, out_path):
    """Slide padrao: kicker verde + titulo branco (Montserrat Black) + corpo cinza (Inter)."""
    img = _base_canvas()
    d = ImageDraw.Draw(img)

    _kicker(img, d, kicker_text, 92)

    f_headline = _font(MONTS_BLACK, 62)
    f_sub = _font(INTER_REG, 34)
    lines = _wrap_text(d, headline, f_headline, W - 2 * MARGIN)
    sub_lines = _wrap_text(d, subtext, f_sub, W - 2 * MARGIN)

    zone_top, zone_bottom = 210, 900
    head_h = _block_height(d, lines, f_headline, 12)
    sub_h = _block_height(d, sub_lines, f_sub, 10)
    total_h = head_h + 26 + sub_h
    y = zone_top + max(0, (zone_bottom - zone_top - total_h) // 2)

    y = _draw_lines(d, lines, f_headline, MARGIN, y, WHITE, 12)
    y += 26
    _draw_lines(d, sub_lines, f_sub, MARGIN, y, GRAY, 10)

    _slide_number(d, n, total)
    _paste_logo(img)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.convert("RGB").save(out_path, quality=95)


def build_cover_slide(n, total, tag_text, headline, subtext, out_path):
    """Slide 1 (capa): tag com emoji de vaca, titulo grande, subtitulo, seta 'arraste'."""
    img = _base_canvas()
    d = ImageDraw.Draw(img)

    _paste_emoji(img, "\U0001F404", (MARGIN, 88), 34)
    f_tag = _font(MONTS_BOLD, 24)
    d.text((MARGIN + 48, 98), tag_text.upper(), font=f_tag, fill=GREEN)

    f_headline = _font(MONTS_BLACK, 78)
    f_sub = _font(INTER_REG, 36)
    lines = _wrap_text(d, headline, f_headline, W - 2 * MARGIN)
    sub_lines = _wrap_text(d, subtext, f_sub, W - 2 * MARGIN)

    zone_top, zone_bottom = 220, 900
    head_h = _block_height(d, lines, f_headline, 14)
    sub_h = _block_height(d, sub_lines, f_sub, 10)
    total_h = head_h + 30 + sub_h
    y = zone_top + max(0, (zone_bottom - zone_top - total_h) // 2)

    y = _draw_lines(d, lines, f_headline, MARGIN, y, WHITE, 14)
    y += 30
    _draw_lines(d, sub_lines, f_sub, MARGIN, y, GRAY, 10)

    f_arrow_label = _font(MONTS_BOLD, 20)
    arrow_label = "ARRASTE"
    bbox = d.textbbox((0, 0), arrow_label, font=f_arrow_label)
    lw = bbox[2] - bbox[0]
    ax = W - MARGIN - lw - 46
    ay = 96
    d.text((ax, ay), arrow_label, font=f_arrow_label, fill=MUTED)
    cx = W - MARGIN - 14
    cy = ay + 10
    d.line([(cx - 16, cy - 10), (cx, cy), (cx - 16, cy + 10)], fill=GREEN, width=4, joint="curve")

    _slide_number(d, n, total)
    _paste_logo(img)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.convert("RGB").save(out_path, quality=95)


def build_cta_slide(n, total, line1, line2, line3, out_path):
    """Slide final (CTA): 3 linhas centralizadas + linha dourada... na verdade verde (regra: verde p/ CTA)."""
    img = _base_canvas()
    d = ImageDraw.Draw(img)

    f1 = _font(INTER_SEMI, 38)
    f2 = _font(MONTS_BLACK, 46)
    f3 = _font(INTER_REG, 34)

    def csize(text, f):
        bbox = d.textbbox((0, 0), text, font=f)
        return bbox[2] - bbox[0], bbox[3] - bbox[1]

    lines = [(line1, f1, WHITE), (line2, f2, GREEN), (line3, f3, GRAY)]
    sizes = [csize(t, f) for t, f, _ in lines]
    gap = 30
    rule_w, rule_h, rule_gap = 200, 3, 50
    total_h = sum(h for _, h in sizes) + gap * (len(lines) - 1) + rule_h + rule_gap
    y = (H - total_h) // 2

    rx = (W - rule_w) // 2
    d.rectangle([rx, y, rx + rule_w, y + rule_h], fill=GREEN)
    y += rule_h + rule_gap

    for (text, f, color), (tw, th) in zip(lines, sizes):
        x = (W - tw) // 2
        d.text((x, y), text, font=f, fill=color)
        y += th + gap

    _slide_number(d, n, total)
    _paste_logo(img, opacity=0.85, width=190)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.convert("RGB").save(out_path, quality=95)
