from fastapi import FastAPI
import random

app = FastAPI()

# Define a root `/` endpoint
@app.get('/')
def random_quote():
    quote_list = [
        "Comme le disait Maître Tong… euh qu’est-ce qu’il disait déjà ce cong ?!… Ah oui… Si la philosophie est l’air pur de l’esprit, ça ne peut t’empêcher de vivre parfois en paix…",
        "Comme le disait maître Tzing Fu : tandis que l’oreille du sage décèle l’élixir… l’oreille du singe ne recèle que de la cire !",
        "Comme le disait la marraine de la soeur du beau-frère de ma mère (euh… ) : entre la culture des perles fines et ceux qui perlent l’inculture, un point commun domine : c’est le QI de l’huître !",
        "Comme le disait feu Maître King Feu… et pas l'inverse, telle la petite feuille emportée par la brise, laisse-toi donc guider… sinon, ça me les brise !",
        "Comme le disais jadis le grand sage Freulix qui vivait tout en haut de la montagne sacrée… PUTAIN, ça pèle !",
        "Comme le disait Maître Tang… qui n’en buvait pas tang que ça, d’ailleurs… tang c’était de la poudre aux yeux… dans l’eau… Pour accéder au droit divin spirituel, il faut parfois céder aux vins spiritueux !",
        "Comme le disait naguère, à sa pauvre grand mère, le petit roi Dajis en tendant son majeur… tout en étant mineur… Quand la mana fuit, l’anti-magie va, mais quand mamie fuit, la magie s’en va…",
        "Comme le disait Firmin à son ami infirme : “L’important c’est le “R” !",
        "Comme le disaient Grishtor et Ilux ou Polgor et Caska : “C’est là un sacré don que de voir consacré le pouvoir de doubler son inutilité !”…",
        "Comme le disait Roger le tavernier : “Si la solution est un mélange homogène résultant de la dissolution d’un soluté dans un solvant… eh ben… c’est pas gagné… "
    ]
    quote = random.choices(quote_list)[0]
    return {'Kyo': quote}
