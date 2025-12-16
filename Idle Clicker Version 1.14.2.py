import os 
import sys 
import time 
import math 
import random 
import string 
import uuid 
import traceback 
import colorsys 
import pygame 
import zlib 

pygame .init ()

try :
    PLAYER_SESSION_ID 
except NameError :
    import string 
    PLAYER_SESSION_ID =''.join (random .choice (string .ascii_letters )for _ in range (20 ))

try :
    PLAYER_UID 
except NameError :
    import uuid 
    PLAYER_UID =uuid .uuid4 ().hex 

pygame .key .set_repeat (350 ,35 )

CAPTCHA_QA =[
{"q":"Le soleil est une étoile.","ans":True },
{"q":"2 est un nombre impair.","ans":False },
{"q":"La France est un continent.","ans":False },
{"q":"L'eau gèle à 0°C (au niveau de la mer).","ans":True },
{"q":"7 + 5 = 13.","ans":False },
{"q":"Un carré a quatre côtés.","ans":True },
{"q":"La Tour Eiffel se trouve à Paris.","ans":True },
{"q":"Les oiseaux respirent sous l'eau sans remonter.","ans":False },
{"q":"Janvier est un mois de l'année.","ans":True },
{"q":"Les humains ont généralement 3 yeux.","ans":False },
{"q":"La Terre tourne autour du Soleil.","ans":True },
{"q":"Un triangle a 5 angles.","ans":False },
{"q":"Le feu est froid.","ans":False },
{"q":"Le chocolat est comestible.","ans":True },
{"q":"Le zèbre est un animal rayé.","ans":True },
{"q":"La Lune produit sa propre lumière.","ans":False },
{"q":"0 est un nombre pair.","ans":True },
{"q":"La capitale de l'Espagne est Madrid.","ans":True },
{"q":"Un litre contient 1000 millilitres.","ans":True },
{"q":"Les baleines sont des poissons.","ans":False },
{"q":"L'oxygène est nécessaire à la respiration humaine.","ans":True },
{"q":"Les araignées ont six pattes.","ans":False },
{"q":"L'eau bout à 100°C (au niveau de la mer).","ans":True },
{"q":"Le sable est bleu par nature.","ans":False },
{"q":"La lumière va plus vite que le son.","ans":True },
{"q":"Une année bissextile a 366 jours.","ans":True },
{"q":"Un rectangle a tous ses côtés égaux.","ans":False },
{"q":"Le pôle Nord est plus froid que l'équateur.","ans":True },
{"q":"Les humains peuvent respirer dans l'espace sans combinaison.","ans":False },
{"q":"Le Japon se trouve en Asie.","ans":True },
{"q":"Les saisons sont inversées entre l'hémisphère Nord et Sud.","ans":True },
{"q":"Le sang humain est toujours bleu dans le corps.","ans":False },
{"q":"Le Mont Everest est la plus haute montagne au-dessus du niveau de la mer.","ans":True },
{"q":"Le sucre est salé.","ans":False },
{"q":"Le pingouin peut voler comme un aigle.","ans":False },
{"q":"Venise est une ville avec des canaux.","ans":True },
{"q":"Les cactus stockent de l'eau.","ans":True },
{"q":"La banane est un légume.","ans":False },
{"q":"Les continents dérivent très lentement au fil du temps.","ans":True },
{"q":"Le Sahara est un désert.","ans":True },
{"q":"Pluton est officiellement classée planète depuis 2006.","ans":False },
{"q":"Un koala est un marsupial.","ans":True },
{"q":"L'électricité circule à travers le bois sec aussi facilement que dans le métal.","ans":False },
{"q":"Le corps humain est composé d'os, de muscles et d'organes.","ans":True },
{"q":"Le café contient de la caféine.","ans":True },
{"q":"Un papillon commence sa vie comme chenille.","ans":True },
{"q":"La mer Morte est très salée.","ans":True },
{"q":"Un octogone a huit côtés.","ans":True },
{"q":"La neige tombe en été au Sahara chaque année.","ans":False },
{"q":"Les volcans peuvent entrer en éruption.","ans":True },
{"q":"L’océan Pacifique est l’océan le plus vaste.","ans":True },
{"q":"La capitale de l’Australie est Canberra.","ans":True },
{"q":"Le zéro absolu est à -273,15°C.","ans":True },
{"q":"Les tortues sont des reptiles.","ans":True },
{"q":"La Grande Muraille de Chine est visible depuis la Lune à l’œil nu.","ans":False },
{"q":"Mars possède deux lunes.","ans":True },
{"q":"Un octet contient 8 bits.","ans":True },
{"q":"La Suisse possède un accès à la mer.","ans":False },
{"q":"La monnaie du Japon est le yen.","ans":True },
{"q":"Le diamant est moins dur que le talc.","ans":False },
{"q":"Les chauves-souris sont des mammifères.","ans":True },
{"q":"La péninsule ibérique comprend l’Espagne et le Portugal.","ans":True },
{"q":"Le mercure est un métal liquide à température ambiante.","ans":True },
{"q":"Pluton est une planète naine.","ans":True },
{"q":"Le pH 7 est neutre.","ans":True },
{"q":"Les pandas géants se nourrissent principalement de bambou.","ans":True },
{"q":"La capitale du Canada est Toronto.","ans":False },
{"q":"La Terre possède deux satellites naturels.","ans":False },
{"q":"Le Nil se jette dans l’océan Atlantique.","ans":False },
{"q":"L’hélium est plus léger que l’air.","ans":True },
{"q":"Les mitochondries réalisent la photosynthèse.","ans":False },
{"q":"Le bronze est un alliage de cuivre et d’étain.","ans":True },
{"q":"H2O est la formule de l’eau.","ans":True },
{"q":"L’atome ne contient que des électrons.","ans":False },
{"q":"Le Canada est plus grand que la Chine en superficie.","ans":True },
{"q":"L’intensité électrique se mesure en ampères.","ans":True },
{"q":"Saturne possède des anneaux.","ans":True },
{"q":"Un hexagone a sept côtés.","ans":False },
{"q":"La mer Morte est située entre Israël et la Jordanie.","ans":True },
{"q":"Le Sahara se trouve principalement en Afrique du Nord.","ans":True },
{"q":"Le mont Kilimandjaro se situe en Afrique.","ans":True },
{"q":"La capitale du Brésil est Rio de Janeiro.","ans":False },
{"q":"Les globules rouges transportent l’oxygène.","ans":True },
{"q":"Un photon a une masse au repos nulle.","ans":True },
{"q":"La foudre ne peut pas tomber deux fois au même endroit.","ans":False },
{"q":"La gravité sur la Lune est plus faible que sur la Terre.","ans":True },
{"q":"Le Gange se jette dans l’océan Indien.","ans":True },
{"q":"Le requin-baleine est le plus grand poisson connu.","ans":True },
{"q":"Le clavier AZERTY est standard en France.","ans":True },
{"q":"Le sel de table est principalement du chlorure de sodium.","ans":True },
{"q":"Le kiwi (fruit) pousse sous terre.","ans":False },
{"q":"L’Antarctique est le continent le plus sec.","ans":True },
{"q":"L’alcool gèle à 0°C.","ans":False },
{"q":"La vitesse du son est plus grande dans l’air que dans l’acier.","ans":False },
{"q":"Les céphalopodes incluent les poulpes.","ans":True },
{"q":"L’eau salée gèle exactement à 0°C.","ans":False },
{"q":"Les protéines sont composées d’acides aminés.","ans":True },
{"q":"Le Sahara recouvre la totalité de l’Afrique.","ans":False },
{"q":"Les pingouins vivent naturellement au pôle Nord.","ans":False },
{"q":"Le mètre est une unité de longueur.","ans":True }
]
captcha_attempts_left =3 
captcha_question_index =0 
captcha_last_question_index =None 
captcha_completed =False 

def pick_captcha_question_index ():
    """Tire une question différente de la précédente durant une même vérification."""
    global captcha_question_index ,captcha_last_question_index 
    n =len (CAPTCHA_QA )
    if n <=1 :

        captcha_question_index =0 if n ==1 else 0 
        captcha_last_question_index =captcha_question_index if n ==1 else None 
        return captcha_question_index 

    new_idx =random .randint (0 ,n -1 )
    if captcha_last_question_index is not None :
        tries =0 
        while new_idx ==captcha_last_question_index and tries <20 :
            new_idx =random .randint (0 ,n -1 )
            tries +=1 

    captcha_question_index =new_idx 
    captcha_last_question_index =new_idx 
    return captcha_question_index 

def reset_captcha_state ():
    global captcha_completed ,captcha_attempts_left ,captcha_question_index ,captcha_last_question_index 
    captcha_completed =False 
    captcha_attempts_left =3 
    captcha_last_question_index =None 
    captcha_question_index =pick_captcha_question_index ()

CURRENT_VERSION ="1.14.2"
_info =pygame .display .Info ()
_dw ,_dh =int (getattr (_info ,'current_w',1824 )),int (getattr (_info ,'current_h',1026 ))
WIDTH =max (960 ,min (1824 ,int (_dw *0.95 )))
HEIGHT =max (540 ,min (1026 ,int (_dh *0.90 )))
screen =pygame .display .set_mode ((WIDTH ,HEIGHT ))
pygame .display .set_caption (f"Idle Clicker Version {CURRENT_VERSION }")
clock =pygame .time .Clock ()
WHITE =(255 ,255 ,255 );BLACK =(0 ,0 ,0 )
BLUE =(50 ,150 ,255 );GREEN =(50 ,205 ,50 );RED =(255 ,50 ,50 )
GRAY =(200 ,200 ,200 );DARK_GRAY =(100 ,100 ,100 )
ORANGE =(255 ,140 ,0 );PURPLE =(128 ,0 ,128 )
REINCARNATION_COLOR =(255 ,200 ,100 );INFINITY_COLOR =(100 ,255 ,255 )
BAR_BG =(220 ,220 ,220 )
PANEL_BG_ALPHA =(0 ,0 ,0 ,140 )
PANEL_LIGHT =(245 ,245 ,245 )
YELLOW =(255 ,215 ,0 )
DARK_RED =(139 ,0 ,0 )
try :


    preferred =pygame .font .get_default_font ()
    try :
        font =pygame .font .SysFont ("Segoe UI",24 )
        big_font =pygame .font .SysFont ("Segoe UI",36 )
        secondary_font =pygame .font .SysFont ("Segoe UI",18 )
        small_font =pygame .font .SysFont ("Segoe UI",14 )
        notif_font =pygame .font .SysFont ("Segoe UI",18 )
    except Exception :
        font =pygame .font .SysFont ("Arial",24 )
        big_font =pygame .font .SysFont ("Arial",36 )
        secondary_font =pygame .font .SysFont ("Arial",18 )
        small_font =pygame .font .SysFont ("Arial",14 )
        notif_font =pygame .font .SysFont ("Arial",18 )
except Exception :
    font =pygame .font .Font (None ,24 )
    big_font =pygame .font .Font (None ,36 )
    secondary_font =pygame .font .Font (None ,18 )
    small_font =pygame .font .Font (None ,14 )
    notif_font =pygame .font .Font (None ,18 )


MAX_FPS_GRAPHICS =70 
MAX_FPS_PERFORMANCE =400 


low_fps_switched_to_performance =False 

DIFF_VERY_EASY =1 
DIFF_EASY =2 
DIFF_NORMAL =3 
DIFF_HARD =4 
DIFF_IMPOSSIBLE =5 

difficulty_selected =False 

show_version_popup =False 


_open_version_from_settings =False 


_version_popup_fired =False 
_welcome_fired =False 

_pending_click_after_popup =None 
difficulty =DIFF_NORMAL 

welcome_popup ={
"open":False ,
"rect_ok":None ,
"already_shown":False 
}

DIFF_LABELS ={
DIFF_VERY_EASY :"Très Facile",
DIFF_EASY :"Facile",
DIFF_NORMAL :"Normal",
DIFF_HARD :"Difficile",
DIFF_IMPOSSIBLE :"Impossible",
}

SETTINGS_SUBTITLES ={
None :"Paramètres",
"general":"Paramètres — Général",
"automation":"Paramètres — Automatisation",
"display":"Paramètres — Affichage",
"beta":"Paramètres — Fonctionnalités BETA",
"dev":"Paramètres — Développeur"
}

_diff_btn_rects ={}

BASE_SUFFIXES =[
"K","M","B","T"
]

NEG_INF =float ('-inf')
SCI_SWITCH_L =100.0 
LOG10_2 =math .log10 (2.0 )
LOG10_4 =2.0 *LOG10_2 
LOG10_15 =math .log10 (15.0 )

loading_step_index =0 
loading_step_start_ms =-1 

LOADING_STEPS =[
{"label":"Chargement des ressources…","duration":450 },
{"label":"Connexion au serveur…","duration":1200 },
{"label":"Chargement des données…","duration":250 },
{"label":"Optimisation des performances…","duration":550 },
{"label":"Lancement du jeu…","duration":650 },
]

LOG10_PI_BOOST =math .log10 (1.2 )

LOG10_PI_RP_BOOST =math .log10 (1.001 )

NOTIF_TOP_Y =85 
NOTIF_RIGHT_MARGIN =24 
NOTIF_GAP_Y =8 

PLAYER_SESSION_ID =''.join (random .choice (string .ascii_letters )for _ in range (20 ))


POPUP_MIN_W =560 
POPUP_MIN_H =300 
POPUP_MARGIN_X =60 
POPUP_MARGIN_Y =60 
POPUP_PADDING =28 
POPUP_LINE_SPACING =8 
POPUP_TITLE_SPACING =18 
POPUP_BTN_H =56 
POPUP_BTN_W =200 

def measure_wrapped_lines (lines ,font ,max_text_width ):
    """
    Wrap automatique de toutes les lignes (utilise wrap_lines_auto existant)
    et retourne:
      wrapped_lines: liste de lignes déjà wrapées
      max_w: largeur max mesurée
      total_h: hauteur totale (sans bouton OK, ni paddings)
    """
    wrapped_lines =[]
    max_w =0 
    total_h =0 
    for ln in lines :
        parts =wrap_lines_auto (ln ,font ,max_text_width )
        for p in parts :
            surf =font .render (p ,True ,(0 ,0 ,0 ))
            max_w =max (max_w ,surf .get_width ())
            total_h +=surf .get_height ()+POPUP_LINE_SPACING 
        wrapped_lines .extend (parts )

    if total_h >0 :
        total_h -=POPUP_LINE_SPACING 
    return wrapped_lines ,max_w ,total_h 

def compute_popup_rect_for_content (title_surf ,content_lines ,font ,screen_w ,screen_h ):
    """
    Calcule rect (x,y,w,h) centré pour la popup:
      - wrape le contenu selon une largeur théorique (on commence grand puis on réajuste)
      - applique min/max et clamp aux marges écran
      - retourne (rect, wrapped_lines, text_w, text_h, viewport_needed)
    """

    max_popup_w =screen_w -POPUP_MARGIN_X *2 
    max_popup_h =screen_h -POPUP_MARGIN_Y *2 

    tentative_text_w =max_popup_w -POPUP_PADDING *2 


    wrapped ,text_w ,text_h =measure_wrapped_lines (content_lines ,font ,tentative_text_w )


    w =max (POPUP_MIN_W ,text_w +POPUP_PADDING *2 )
    h_content_block =title_surf .get_height ()+POPUP_TITLE_SPACING +text_h 
    h =max (POPUP_MIN_H ,h_content_block +POPUP_PADDING *2 +POPUP_BTN_H +POPUP_TITLE_SPACING )


    w =min (w ,max_popup_w )
    h =min (h ,max_popup_h )


    viewport_needed =(h <h_content_block +POPUP_PADDING *2 +POPUP_BTN_H +POPUP_TITLE_SPACING )


    x =screen_w //2 -w //2 
    y =screen_h //2 -h //2 
    return (pygame .Rect (x ,y ,w ,h ),wrapped ,min (text_w ,w -POPUP_PADDING *2 ),text_h ,viewport_needed )

def draw_circular_progress (surface ,center ,radius ,ratio ,color ,thickness =6 ,back_color =(0 ,0 ,0 ,60 )):
    """
    Dessine un anneau de fond + un arc de progression autour d'un centre.
    - center: (x, y)
    - radius: rayon externe de l'anneau
    - ratio: 0.0 .. 1.0
    - color: couleur de l'arc
    - thickness: épaisseur du trait
    - back_color: couleur (RGBA) de l'anneau de fond (translucide recommandé)
    """
    ratio =max (0.0 ,min (1.0 ,float (ratio )))

    bg_surf =pygame .Surface ((radius *2 +4 ,radius *2 +4 ),pygame .SRCALPHA )
    pygame .draw .circle (bg_surf ,back_color ,(radius +2 ,radius +2 ),radius ,thickness )
    surface .blit (bg_surf ,(center [0 ]-radius -2 ,center [1 ]-radius -2 ))

    start =-math .pi /2 
    end =start +2 *math .pi *ratio 
    rect =pygame .Rect (center [0 ]-radius ,center [1 ]-radius ,radius *2 ,radius *2 )
    pygame .draw .arc (surface ,color ,rect ,start ,end ,thickness )

def draw_circular_progress_around_button (surface ,btn_rect ,ratio ,color ,pad =8 ,thickness =6 ):
    """
    Dessine un progress circulaire qui fait le tour du bouton.
    - pad: décalage pour que le cercle entoure légèrement le bouton
    """

    w ,h =btn_rect .width ,btn_rect .height 
    r_btn =min (w ,h )//2 
    radius =r_btn +pad 
    center =btn_rect .center 

    draw_circular_progress (surface ,center ,radius ,ratio ,color ,thickness ,back_color =(0 ,0 ,0 ,64 ))

def _format_exponent_compact (e :int )->str :
    if e <=0 :
        return "0"
    if e >=10 **10000 :
        e2 =int (math .floor (math .log10 (e )))
        e3 =int (math .floor (math .log10 (max (1 ,e2 ))))
        return f"eee{e3 }"
    if e >=10 **100 :
        e2 =int (math .floor (math .log10 (e )))
        return f"ee{e2 }{_format_plain_with_suffixes_from_log10 (math .log10 (max (1 ,e2 )))}"
    Le =math .log10 (max (1 ,e ))
    return _format_plain_with_suffixes_from_log10 (Le )

def _alpha_suffix_from_index (n :int )->str :
    """
    Convertit un index n>=0 en suffixe alphabétique infini sur 'a'..'z'.
    n=0 -> "aa", 1->"ab", ..., 25->"az", 26->"ba", etc.
    """
    if n <0 :
        return ""
    alpha =[]
    x =n 
    while True :
        x ,r =divmod (x ,26 )
        alpha .append (chr (ord ('a')+r ))
        if x ==0 :
            break 

        x -=1 
    s =''.join (reversed (alpha ))
    if len (s )==1 :
        s ='a'+s 
    return s 

def _suffix_for_group_index (g :int )->str :
    """
    g=0->K, 1->M, 2->B, 3->T, g>=4 -> aa, ab, ... (infini)
    """
    try :
        return BASE_SUFFIXES [g ]
    except Exception :
        return _alpha_suffix_from_index (g -4 )

def _format_plain_with_suffixes_from_log10 (L :float )->str :
    """
    Formate v avec :
      - K, M, B, T puis suffixes générés (aa, ab, ...),
      - 2 décimales sur la mantisse,
      - pas de fallback en notation scientifique (côté 'ee') tant qu'on peut suffixer.
    """
    if not math .isfinite (L )or L <3 :
        v =10.0 **max (0.0 ,L )
        return str (int (v ))
    idx =int (L //3 )-1 
    scaled_log =L -3 *(idx +1 )
    mant =10.0 **scaled_log 
    suf =_suffix_for_group_index (idx )
    return f"{mant :.2f}{suf }"

def format_from_log10 (L :float )->str :
    if not math .isfinite (L ):
        if L ==NEG_INF :return "0"
        return "∞"
    if L >=10000 :

        return "∞"
    elif L >=3 :

        return _format_plain_with_suffixes_from_log10 (L )
    else :
        val =10.0 **L 
        return str (int (val ))if val >=100 else f"{val :.2f}"

def format_points_integer (P_log10 :float )->str :
    if P_log10 ==NEG_INF or not math .isfinite (P_log10 ):
        return '0'
    if P_log10 <0 :return '0'
    if P_log10 >12 :
        e =int (P_log10 )
        mant =10 **(P_log10 -e )
        return f"~{mant :.3f}e{e }"
    n =int (10 **P_log10 )
    return f"{n :,}".replace (',',' ')

def format_points_pretty (P_log10 :float )->str :
    """Affiche un total de points (R/P/A/Re) avec suffixes/expo (comme le score)."""
    if P_log10 ==NEG_INF or not math .isfinite (P_log10 )or P_log10 <0 :
        return "0"
    return format_from_log10 (P_log10 )

def format_percent_from_multiplier_log10 (Lm_log10 :float )->str :
    """
    Convertit une contribution multiplicative log10 => pourcentage +X%.
    - Lm_log10 = log10(facteur) ; facteur = 10**Lm_log10
    - % = (facteur - 1) * 100
    - <= 1000% : rendu numérique classique
    - > 1000% : suffixes / notation scientifique (via format_from_log10)
    """
    if not math .isfinite (Lm_log10 ):
        return "0%"

    if Lm_log10 <math .log10 (11 ):
        pct =((10.0 **Lm_log10 )-1.0 )*100.0 
        if pct <0.005 :
            return "0%"
        return f"{pct :.2f}%"

    log10_percent_value =Lm_log10 +math .log10 (100.0 )
    return f"{format_from_log10 (log10_percent_value )}%"

def per_family_multiplier_log10 (fam :str ,pts :dict )->float :
    """
    Contribution log10 au multiplicateur de score d'UNE famille de points.
    Recalque la logique de total_points_multiplier_log10(), mais isolée par famille.
    """
    P_log10 =pts .get (fam ,NEG_INF )
    if fam =='R':
        r_rate =0.02 if have_challenge_buff (1 )else 0.01 
        L =log10_linear_bonus (r_rate ,P_log10 )
    elif fam =='P':
        L =log10_linear_bonus (0.05 ,P_log10 )
    elif fam =='A':
        L =log10_linear_bonus (0.20 ,P_log10 )
    elif fam =='Re':
        L =log10_linear_bonus (0.50 ,P_log10 )
    else :
        return 0.0 

    if P_log10 >NEG_INF :
        L +=math .floor (max (0.0 ,P_log10 )/3.0 )*LOG10_2 

    return L 

def log10_add (x :float ,y :float )->float :
    if x ==NEG_INF :return y 
    if y ==NEG_INF :return x 
    m =x if x >y else y 
    d =(y if x >y else x )-m 
    return m +math .log10 (1 +10.0 **d )

def log10_sub (x :float ,y :float )->float :
    if x <=y :return NEG_INF 
    d =10.0 **(y -x )
    if d ==0.0 :return x 
    val =1.0 -d 
    if val <=0.0 :return NEG_INF 
    return x +math .log10 (val )

class Button :
    def __init__ (self ,rect ,text ,bg_color ,text_color =BLACK ):
        self .rect =pygame .Rect (rect )
        self .text =text 
        self .bg =bg_color 
        self .text_color =text_color 
        self ._bounce_active =False 
        self ._bounce_start =0 
        self ._bounce_cooldown =0 
    def bounce (self ):
        if game_settings .get ("graphics_mode")=="performance":
            return 
        now =pygame .time .get_ticks ()
        if now -self ._bounce_cooldown <1000 :
            return 
        self ._bounce_active =True 
        self ._bounce_start =now 
        self ._bounce_cooldown =now 
    def draw (self ,surface ,mouse_pos ):

        label =getattr (self ,"label",getattr (self ,"text",""))

        bg =(getattr (self ,"color",None )or 
        getattr (self ,"bg",None )or 
        getattr (self ,"bg_color",None )or 
        getattr (self ,"base_color",None )or 
        getattr (self ,"fill_color",None )or 
        (200 ,200 ,200 ))

        fg =(getattr (self ,"text_color",None )or 
        getattr (self ,"fg",None )or 
        getattr (self ,"fg_color",None )or 
        getattr (self ,"color_text",None )or 
        (0 ,0 ,0 ))

        rr =getattr (self ,"border_radius",10 )
        if rr is None :rr =10 

        hovered =self .rect .collidepoint (mouse_pos )
        fancy =(game_settings .get ("graphics_mode")=="graphismes_travaillés")

        scale =1.0 
        if self ._bounce_active :
            t =(pygame .time .get_ticks ()-self ._bounce_start )/320.0 

            if t <1.0 :

                scale =0.93 +0.17 *abs (math .sin (3.6 *t )*math .exp (-2.2 *t ))
            else :
                self ._bounce_active =False 
                scale =1.0 
        elif fancy and hovered :
            t =pygame .time .get_ticks ()*0.001 
            pulse =0.02 *math .sin (2.0 *math .pi *1.0 *t )
            scale =1.03 +pulse 

        if fancy and hovered :
            t =pygame .time .get_ticks ()*0.001 
            pulse =0.02 *math .sin (2.0 *math .pi *1.0 *t )
            scale =1.03 +pulse 
            w ,h =self .rect .size 
            glow_pad =10 
            comp_w ,comp_h =w +glow_pad *2 ,h +glow_pad *2 
            comp =pygame .Surface ((comp_w ,comp_h ),pygame .SRCALPHA )

            glow_rgb =(min (255 ,bg [0 ]+40 ),min (255 ,bg [1 ]+40 ),min (255 ,bg [2 ]+40 ))
            layers =5 
            for i in range (layers ,0 ,-1 ):
                alpha =int (18 *i )
                grow =i *4 
                gr =pygame .Rect (
                (comp_w -(w +grow ))//2 ,
                (comp_h -(h +grow ))//2 ,
                w +grow ,
                h +grow 
                )
                pygame .draw .rect (comp ,(*glow_rgb ,alpha ),gr ,border_radius =max (rr ,rr +i *2 ))

            body =pygame .Rect (glow_pad ,glow_pad ,w ,h )
            pygame .draw .rect (comp ,bg ,body ,border_radius =rr )

            txt =font .render (str (label ),True ,fg )
            comp .blit (txt ,txt .get_rect (center =body .center ))

            sw =max (1 ,int (comp_w *scale ))
            sh =max (1 ,int (comp_h *scale ))
            comp_scaled =pygame .transform .smoothscale (comp ,(sw ,sh ))
            dest =comp_scaled .get_rect (center =self .rect .center )
            surface .blit (comp_scaled ,dest )
        else :

            pygame .draw .rect (surface ,bg ,self .rect ,border_radius =rr )
            txt =font .render (str (label ),True ,fg )
            surface .blit (txt ,txt .get_rect (center =self .rect .center ))

def draw_button_disabled (surface ,button :Button ):
    overlay =pygame .Surface ((button .rect .width ,button .rect .height ),pygame .SRCALPHA )
    overlay .fill ((160 ,160 ,160 ,150 ))
    surface .blit (overlay ,button .rect .topleft )
    pygame .draw .rect (surface ,(120 ,120 ,120 ),button .rect ,3 ,border_radius =8 )

TOOLTIP_BG =(0 ,0 ,0 ,200 )
TOOLTIP_PAD_X =10 
TOOLTIP_PAD_Y =8 

def draw_tooltip (surface ,lines ,mouse_pos ):

    if not game_settings .get ("show_tooltips_on_hover",True ):
        return 
    if not lines :
        return 
    text_surfs =[small_font .render (ln ,True ,(255 ,255 ,255 ))for ln in lines ]
    w =max (ts .get_width ()for ts in text_surfs )+TOOLTIP_PAD_X *2 
    h =sum (ts .get_height ()for ts in text_surfs )+TOOLTIP_PAD_Y *2 +(len (text_surfs )-1 )*2 
    x ,y =mouse_pos [0 ]+16 ,mouse_pos [1 ]+16 
    if x +w >WIDTH -10 :x =WIDTH -10 -w 
    if y +h >HEIGHT -10 :y =HEIGHT -10 -h 
    box =pygame .Surface ((w ,h ),pygame .SRCALPHA )
    box .fill (TOOLTIP_BG )
    surface .blit (box ,(x ,y ))
    ty =y +TOOLTIP_PAD_Y 
    for ts in text_surfs :
        surface .blit (ts ,(x +TOOLTIP_PAD_X ,ty ));ty +=ts .get_height ()+2 

def overlays_open ()->bool :
    """True si une modale/overlay est ouverte (quit, GR, reset, flow, pwd dev, saisie code)."""
    try :
        return (
        quit_confirm .get ("open",False )or 
        gr_confirm .get ("open",False )or 
        reset_confirm .get ("open",False )or 
        reset_flow .get ("state",0 )!=0 or 
        reset_flow .get ("in_progress",False )or 
        dev_password_mode or 
        (code_input_mode is not None )or 
        globals ().get ('show_version_popup',False )or 
        (isinstance (globals ().get ('welcome_popup',{}),dict )and globals ()['welcome_popup'].get ('open',False ))
        )
    except Exception :
        return False 

def _display_with_ellipsis (shown :str ,max_w :int ,fnt )->tuple [str ,int ]:
    """
    Retourne (disp, start) où disp est le texte affiché (avec '…' si tronqué à gauche),
    et start l’index de début visible dans 'shown'.
    """
    disp =shown 
    start =0 

    while fnt .size (disp )[0 ]>max_w and start <len (shown ):
        start +=1 
        disp =shown [start :]
    if start >0 :
        disp ="…"+disp 
    return disp ,start 

def _caret_from_click (shown :str ,start :int ,left_x :int ,mouse_x :int ,fnt )->int :
    """
    Calcule l’index de caret à partir d’un clic souris horizontal.
    'shown' = texte réellement affiché (masqué si nécessaire, sans ellipsis),
    'start' = index de début visible (tronquage gauche),
    'left_x' = x de départ du texte (hors bordure / padding),
    'mouse_x' = x du clic.
    """
    px =max (0 ,mouse_x -left_x )

    if start >0 :
        ell_w =fnt .size ("…")[0 ]
        if px <=ell_w //2 :
            return start 
        px -=ell_w 

    visible =shown [start :]
    acc =0 
    for i ,ch in enumerate (visible ):
        cw =fnt .size (ch )[0 ]
        if px <acc +cw /2 :
            return start +i 
        acc +=cw 
    return len (shown )

def draw_eye_icon (surface ,rect :pygame .Rect ,open :bool =True ):
    """
    Dessine une icône d'œil dans rect.
    - open=True : œil ouvert avec pupille (mot de passe visible)
    - open=False : œil barré (mot de passe masqué)
    """
    pygame .draw .ellipse (surface ,(0 ,0 ,0 ),rect ,2 )
    cx ,cy =rect .center 
    if open :

        r =max (2 ,rect .height //6 )
        pygame .draw .circle (surface ,(0 ,0 ,0 ),(cx ,cy ),r )
    else :

        pygame .draw .line (surface ,(0 ,0 ,0 ),
        (rect .left +2 ,rect .bottom -2 ),
        (rect .right -2 ,rect .top +2 ),2 )

def draw_welcome_popup (mouse_pos ):
    """v31.5.3 — Modale 'Bienvenue' affichée une fois après le choix de difficulté."""
    if not welcome_popup .get ("open",False ):
        return 

    overlay =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
    overlay .fill ((0 ,0 ,0 ,160 ))
    screen .blit (overlay ,(0 ,0 ))

    w ,h =900 ,320 
    x ,y =WIDTH //2 -w //2 ,HEIGHT //2 -h //2 
    pygame .draw .rect (screen ,(250 ,250 ,250 ),(x ,y ,w ,h ),border_radius =12 )
    pygame .draw .rect (screen ,(0 ,0 ,0 ),(x ,y ,w ,h ),2 ,border_radius =12 )

    title =big_font .render ("Bienvenue !",True ,(0 ,0 ,0 ))
    screen .blit (title ,(x +w //2 -title .get_width ()//2 ,y +18 ))

    lines =[
    "La personnalisation du jeu est maintenant disponible dans Paramètres.",
    "Vous pouvez changer les graphismes, le thème, les notifications,",
    "et d'autres options pour adapter l'expérience à vos préférences."
    ]
    ty =y +88 
    for ln in lines :
        surf =secondary_font .render (ln ,True ,(20 ,20 ,20 ))
        screen .blit (surf ,(x +24 ,ty ))
        ty +=28 

    btn_w ,btn_h =220 ,52 
    ok_rect =pygame .Rect (x +w -btn_w -24 ,y +h -btn_h -18 ,btn_w ,btn_h )
    btn =Button (ok_rect ,"OK",(90 ,180 ,220 ),(255 ,255 ,255 ))
    btn .draw (screen ,mouse_pos )

    welcome_popup ["rect_ok"]=ok_rect 

def draw_reset_overlays (mouse_pos ):
    global _reset_btn_rects 
    if reset_flow .get ('state',0 )==0 or reset_flow .get ('in_progress',False ):
        _reset_btn_rects ={"cont":None ,"back":None }
        return 

    overlay =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
    overlay .fill ((0 ,0 ,0 ,160 ))
    screen .blit (overlay ,(0 ,0 ))

    w ,h =900 ,260 
    x ,y =WIDTH //2 -w //2 ,HEIGHT //2 -h //2 
    pygame .draw .rect (screen ,(250 ,250 ,250 ),(x ,y ,w ,h ),border_radius =12 )
    pygame .draw .rect (screen ,(0 ,0 ,0 ),(x ,y ,w ,h ),2 ,border_radius =12 )

    state =reset_flow .get ('state',1 )
    title_txt ="Avertissement"
    body_lines =[]
    if state ==1 :
        title_txt ="Avertissement"
        body_lines =[
        "Vous êtes sur le point de réinitialiser VOTRE PROGRESSION.",
        "Cette action ne peut être annulée. Confirmez pour continuer.",
        ]
    elif state ==2 :
        title_txt ="Mise en garde"
        body_lines =[
        "La réinitialisation supprime : score, points, PI, challenges, achievements, codes utilisés...",
        "Vous reviendrez à l'écran de lancement avec le Captcha.",
        ]
    else :
        title_txt ="DERNIER AVERTISSEMENT"

        now =pygame .time .get_ticks ()
        start_ms =reset_flow .get ('start_ms',-1 )
        elapsed =0 if start_ms <0 else (now -start_ms )
        remaining =max (0 ,30000 -elapsed )
        secs =remaining //1000 
        body_lines =[
        "Confirmez votre décision : cliquez 10 fois en 30 secondes sur 'Continuer'.",
        f"Clics : {reset_flow .get ('clicks',0 )}/10 · Temps restant : {secs }s",
        ]

    ts =big_font .render (title_txt ,True ,(0 ,0 ,0 ))
    screen .blit (ts ,(x +w //2 -ts .get_width ()//2 ,y +18 ))

    yy =y +70 
    for ln in body_lines :
        ls =secondary_font .render (ln ,True ,(20 ,20 ,20 ))
        screen .blit (ls ,(x +24 ,yy ));yy +=28 

    btn_w ,btn_h =220 ,50 
    cont_rect =pygame .Rect (x +w -btn_w -24 ,y +h -btn_h -18 ,btn_w ,btn_h )
    back_rect =pygame .Rect (x +24 ,y +h -btn_h -18 ,btn_w ,btn_h )
    cont_btn =Button (cont_rect ,"Continuer",(90 ,200 ,120 ),(255 ,255 ,255 ))
    back_btn =Button (back_rect ,"Retour",(200 ,120 ,120 ),(255 ,255 ,255 ))
    cont_btn .draw (screen ,mouse_pos )
    back_btn .draw (screen ,mouse_pos )

    _reset_btn_rects ={"cont":cont_rect ,"back":back_rect }

def perform_full_data_reset ():
    global game_settings ,developer_mode_active ,dev_password_mode ,dev_password_text ,last_dev_command_ms ,dev_logs_page ,dev_password_visible ,dev_password_eye_rect 
    global game_data ,challenge_state ,notifications ,used_codes 
    global captcha_completed ,captcha_attempts_left ,captcha_question_index ,captcha_last_question_index 
    global mini_notifs ,last_pi_milestones_count 
    global tutorial_active ,tutorial_mode ,tutorial_step ,tutorial_auto_advance 
    global visited_achievements ,visited_settings ,visited_history ,visited_tutorial ,visited_milestones ,visited_menu ,visited_play 
    global clicks_done ,click_upgrades ,auto_upgrades ,mult_upgrades ,score_reached_100 ,score_reached_1000 ,renaissance_done 
    global code_input_mode ,code_input_text 

    try :
        GLOBAL_PROGRESS ["idx"]=1 
        GLOBAL_PROGRESS ["done"]=False 
    except Exception :
        pass 

    game_data ={
    "score_log10":NEG_INF ,"max_score_log10":NEG_INF ,
    "click_value":BASE_VALUES ["click"],
    "auto_value":BASE_VALUES ["auto"],
    "multiplier_log10":BASE_VALUES ["multiplier_log10"],
    "cost_auto_log10":BASE_COST_LOG10 ["auto"],
    "cost_click_log10":BASE_COST_LOG10 ["click"],
    "cost_mult_log10":BASE_COST_LOG10 ["mult"],
    "points_log10":{"R":NEG_INF ,"P":NEG_INF ,"A":NEG_INF ,"Re":NEG_INF },
    "PI":0 ,
    "points_max_log10":{"R":NEG_INF ,"P":NEG_INF ,"A":NEG_INF ,"Re":NEG_INF },
    "pi_max":0 ,"pi_spent_total":0 ,"grand_resets":0 ,
    "total_clicks":0 ,"max_sps":0.0 ,"total_play_time":0.0 ,"total_upgrades_bought":0 ,
    "max_auto_sps_log10":NEG_INF ,
    "perm_unlocks":{"mini_autoclicker":True ,"auto_buyers":True },
    "ever_unlocked_challenges":False ,
    }

    challenge_state ={"active":False ,"current":0 ,"completed":[False ,False ,False ,False ],"notified_ready":False }

    try :
        sync_challenges_with_difficulty ()
    except Exception :
        pass 

    try :
        achievements_unlocked .clear ()
    except Exception :
        pass 
    try :
        ach_page_index_by_cat .clear ()
    except Exception :
        pass 

    used_codes =set ()
    notifications .clear ()

    game_settings .clear ()
    game_settings .update ({
    "graphics_mode":"graphismes_travaillés",
    "purchase_mode":"single",
    "mini_autoclicker":False ,
    "auto_buyers":False ,
    "theme":"clair",
    "mini_notifications":True ,
    "ingame_notifications":True ,
    "show_reset_points":True ,
    "show_reset_boosts":True ,
    "show_tooltips_on_hover":True ,
    "auto_rebirth":False ,
    })

    developer_mode_active =False 
    dev_password_mode =False 
    dev_password_text =""
    last_dev_command_ms =0 
    dev_logs_page =0 

    reset_captcha_state ()

captcha_completed =False 
captcha_attempts_left =3 
captcha_last_question_index =None 
captcha_question_index =pick_captcha_question_index ()

tutorial_active =False 
tutorial_mode =None 
tutorial_step =0 
tutorial_auto_advance =False 
visited_achievements =visited_settings =visited_history =False 
visited_tutorial =visited_milestones =visited_menu =visited_play =False 
clicks_done =click_upgrades =auto_upgrades =mult_upgrades =0 
score_reached_100 =score_reached_1000 =False 
renaissance_done =False 

mini_notifs ={'tutorial':False ,'achievements':False ,'milestones':False ,'play':False }
last_pi_milestones_count =0 

LOADING_POST_HOLD_MS =1000 
LOADING_FADE_MS =800 

loading_transition ={
"active":False ,
"start":-1 ,
"from_snap":None ,
}

def gr_button_is_visible ()->bool :
    """Vérité unique de visibilité du bouton GR (rendu et input doivent l'utiliser)."""
    completed =challenge_state .get ('completed',[False ,False ,False ,False ])
    try :
        if difficulty ==DIFF_VERY_EASY :

            return milestone_currently_unlocked (20 )
        elif difficulty ==DIFF_EASY :

            return len (completed )>1 and completed [1 ]
        else :

            return len (completed )>3 and completed [3 ]
    except Exception :
        return False 

def start_loading_to_captcha_transition ():
    """Démarre la transition: 1s de pause puis fondu vers l'écran Captcha (idempotent)."""
    global loading_mode ,loading_transition 

    if loading_transition .get ("active",False ):
        return 

    loading_transition ["active"]=True 
    loading_transition ["start"]=pygame .time .get_ticks ()

    loading_transition ["from_snap"]=screen .copy ()

    loading_mode ="transition_to_captcha"

def draw_loading_to_captcha (mouse_pos ,dt ):

    global screen ,loading_transition ,loading_mode ,current_screen ,captcha_completed ,game_state 

    if not loading_transition .get ("active",False ):
        return 

    now =pygame .time .get_ticks ()
    t =now -loading_transition ["start"]

    if loading_transition .get ("from_snap")is None :
        loading_transition ["active"]=False 
        loading_transition ["from_snap"]=None 
        loading_mode =None 
        captcha_completed =False 
        try :
            set_game_state ('captcha')
        except NameError :
            game_state ='captcha'
        if 'current_screen'in globals ():
            current_screen ='captcha'
        return 

    if t <LOADING_POST_HOLD_MS :
        snap =loading_transition .get ("from_snap")
        if snap :
            screen .blit (snap ,(0 ,0 ))
        return 

    tau =t -LOADING_POST_HOLD_MS 
    r =max (0.0 ,min (1.0 ,tau /float (LOADING_FADE_MS )))

    captcha_frame =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
    as_screen_backup =screen 
    try :
        screen =captcha_frame 
        draw_captcha (mouse_pos ,dt )
    finally :
        screen =as_screen_backup 

    snap =loading_transition .get ("from_snap")
    if snap :
        snap_fade =snap .copy ()
        snap_fade .set_alpha (int (255 *(1.0 -r )))
        screen .blit (snap_fade ,(0 ,0 ))

    captcha_frame .set_alpha (int (255 *r ))
    screen .blit (captcha_frame ,(0 ,0 ))

    if r >=1.0 :
        loading_transition ["active"]=False 
        loading_transition ["from_snap"]=None 
        loading_mode =None 
        captcha_completed =False 
        try :
            set_game_state ('captcha')
        except NameError :
            game_state ='captcha'
        if 'current_screen'in globals ():
            current_screen ='captcha'

def handle_welcome_popup (event )->bool :
    """Renvoie True si l'event est consommé par la popup 'Bienvenue'."""
    if not welcome_popup .get ("open",False ):
        return False 
    if event .type ==pygame .MOUSEBUTTONDOWN and event .button ==1 :
        ro =welcome_popup .get ("rect_ok")
        if ro and ro .collidepoint (event .pos ):
            welcome_popup ["open"]=False 
            return True 
    if event .type ==pygame .KEYDOWN and event .key ==pygame .K_ESCAPE :
        welcome_popup ["open"]=False 
        return True 

    if event .type in (pygame .MOUSEBUTTONDOWN ,pygame .MOUSEBUTTONUP ,pygame .MOUSEWHEEL ,pygame .MOUSEMOTION ):
        return True 
    return False 

def _force_exit_loading_transition_if_stuck ():
    """Sécurité: si la transition dépasse un délai raisonnable, forcer la sortie vers Captcha."""

    global loading_transition ,loading_mode ,current_screen ,captcha_completed ,game_state 

    if loading_transition .get ("active",False ):
        now =pygame .time .get_ticks ()
        max_ms =LOADING_POST_HOLD_MS +LOADING_FADE_MS +1500 
        if now -loading_transition ["start"]>max_ms :
            loading_transition ["active"]=False 
            loading_transition ["from_snap"]=None 

            loading_mode =None 
            captcha_completed =False 
            try :
                set_game_state ('captcha')
            except NameError :
                game_state ='captcha'
            if 'current_screen'in globals ():
                current_screen ='captcha'
            try :
                log_event ("[LOADING] Transition forcée vers Captcha (fail-safe)")
            except Exception :
                pass 

KEEP_LOADING_BAR_DURING_FADE =True 
_loading_final_frame_armed =False 

code_input_mode =None 
code_input_text =""

settings_tab =None 
_settings_hub_rects ={}

SETTINGS_BACK_MENU_BTN =Button ((80 ,HEIGHT -70 ,280 ,48 ),"Retour au menu principal",GRAY )
SETTINGS_BACK_HUB_BTN =Button ((420 ,HEIGHT -70 ,360 ,48 ),"Retour au choix des paramètres",GRAY )

_milestones_page =0 
_milestones_nav ={"prev":None ,"next":None }

captcha_completed =False 
captcha_attempts_left =3 
pick_captcha_question_index ()

loading_last_check ={"time":None ,"kb":0 ,"speed":100.0 }

GR_BASE_COST_PI =1_000_000 

_last_version_btn_rect =None 


class FloatingShape :
    def __init__ (self ):

        self .shape =random .choice ([
        "circle","square","triangle",
        "pentagon","hexagon","octagon"

        ])
        self .size =random .randint (35 ,105 )
        self .x =random .uniform (0 ,WIDTH )
        self .y =random .uniform (0 ,HEIGHT )
        self .vx =random .uniform (-80 ,80 )
        self .vy =random .uniform (-80 ,80 )
        self .offset =random .random ()*10 

    def update (self ,dt ):
        self .x +=self .vx *dt /1000.0 
        self .y +=self .vy *dt /1000.0 
        if self .x <0 :self .x =WIDTH 
        elif self .x >WIDTH :self .x =0 
        if self .y <0 :self .y =HEIGHT 
        elif self .y >HEIGHT :self .y =0 

    def draw (self ,surface ):
        t =(pygame .time .get_ticks ()/1000.0 +self .offset )%10 
        hue =(t /10.0 )%1.0 
        r ,g ,b =colorsys .hsv_to_rgb (hue ,1 ,1 )
        color =(int (r *255 ),int (g *255 ),int (b *255 ))
        cx ,cy =int (self .x ),int (self .y )
        sz =self .size 

        if self .shape =="circle":
            pygame .draw .circle (surface ,color ,(cx ,cy ),sz //2 )

        elif self .shape =="square":
            rect =pygame .Rect (self .x -sz /2 ,self .y -sz /2 ,sz ,sz )
            pygame .draw .rect (surface ,color ,rect )

        elif self .shape =="triangle":
            pts =[
            (self .x ,self .y -sz /2 ),
            (self .x -sz /2 ,self .y +sz /2 ),
            (self .x +sz /2 ,self .y +sz /2 )
            ]
            pygame .draw .polygon (surface ,color ,pts )

        elif self .shape =="pentagon":
            pts =[]
            for i in range (5 ):
                ang =2 *math .pi *i /5 -math .pi /2 
                px =self .x +math .cos (ang )*sz /2 
                py =self .y +math .sin (ang )*sz /2 
                pts .append ((px ,py ))
            pygame .draw .polygon (surface ,color ,pts )

        elif self .shape =="hexagon":
            pts =[]
            for i in range (6 ):
                ang =2 *math .pi *i /6 -math .pi /2 
                px =self .x +math .cos (ang )*sz /2 
                py =self .y +math .sin (ang )*sz /2 
                pts .append ((px ,py ))
            pygame .draw .polygon (surface ,color ,pts )

        elif self .shape =="octagon":
            pts =[]
            for i in range (8 ):
                ang =2 *math .pi *i /8 -math .pi /2 
                px =self .x +math .cos (ang )*sz /2 
                py =self .y +math .sin (ang )*sz /2 
                pts .append ((px ,py ))
            pygame .draw .polygon (surface ,color ,pts )

        elif self .shape =="decagon":

            pts =[]
            for i in range (10 ):
                ang =2 *math .pi *i /10 -math .pi /2 
                px =self .x +math .cos (ang )*sz /2 
                py =self .y +math .sin (ang )*sz /2 
                pts .append ((px ,py ))
            pygame .draw .polygon (surface ,(255 ,215 ,0 ),pts )

        else :

            pygame .draw .circle (surface ,color ,(cx ,cy ),sz //2 )

floating_shapes =[FloatingShape ()for _ in range (13 )]

class ClickParticle :
    def __init__ (self ,x ,y ,color ,z =None ):
        """
        z = profondeur [0.0 .. 1.0] ; 0 = arrière-plan (petit/lent/faible alpha),
                                    1 = avant-plan (grand/rapide/alpha fort)
        """
        self .z =random .uniform (0.15 ,1.0 )if z is None else max (0.0 ,min (1.0 ,z ))
        ang =random .uniform (0 ,2 *math .pi )
        base_speed =random .uniform (140 ,300 )
        speed =base_speed *(0.55 +0.85 *self .z )

        self .vx =math .cos (ang )*speed 
        self .vy =math .sin (ang )*speed 

        self .x =float (x )
        self .y =float (y )

        self .life =0.0 
        self .max_life =random .uniform (0.40 ,0.85 )*(0.85 +0.3 *(1.0 -self .z ))

        base_size =random .randint (2 ,5 )
        self .size =int (base_size *(0.7 +1.6 *self .z ))
        self .color =color 

        self .glow =1.00 +0.20 *self .z +random .uniform (-0.05 ,0.05 )

        self .friction =0.98 -0.05 *(1.0 -self .z )
        self .gravity =220.0 *(0.6 +0.7 *self .z )

    def dead (self )->bool :
        return self .life >=self .max_life 

    def update (self ,dt ):
        dt_s =dt /1000.0 
        self .life +=dt_s 

        self .x +=self .vx *dt_s 
        self .y +=self .vy *dt_s 

        self .vy +=self .gravity *dt_s 
        self .vx *=self .friction 
        self .vy *=self .friction 

    def draw (self ,surface ):
        if self .dead ():
            return 

        t =self .life /self .max_life 
        base_alpha =255 *(0.5 +0.5 *self .z )
        alpha =max (0 ,int (base_alpha *(1.0 -t )))

        s =int (max (1 ,self .size *(1.0 -0.35 *t )))
        tmp =pygame .Surface ((s *2 ,s *2 ),pygame .SRCALPHA )

        r =g =b =int (255 *self .glow )
        r =min (255 ,r );g =min (255 ,g );b =min (255 ,b )
        pygame .draw .circle (tmp ,(r ,g ,b ,alpha ),(s ,s ),s )
        surface .blit (tmp ,(int (self .x )-s ,int (self .y )-s ))

def spawn_click_explosion (x ,y ,base_color =(80 ,180 ,255 )):
    """
    Crée une explosion parallax en 3 couches :
      - back  : petites particules, lentes, discrètes
      - mid   : intermédiaire
      - front : grandes particules, rapides, alpha fort
    """
    layers =[
    {"count":10 ,"zmin":0.15 ,"zmax":0.35 ,"mul":0.90 },
    {"count":16 ,"zmin":0.35 ,"zmax":0.70 ,"mul":1.00 },
    {"count":12 ,"zmin":0.70 ,"zmax":1.00 ,"mul":1.10 },
    ]
    for L in layers :
        for _ in range (L ["count"]):
            z =random .uniform (L ["zmin"],L ["zmax"])

            r ,g ,b =base_color 
            color =(min (255 ,int (r *L ["mul"])),
            min (255 ,int (g *L ["mul"])),
            min (255 ,int (b *L ["mul"])))
            particles .append (ClickParticle (x ,y ,color ,z =z ))

particles =[]

secret_shape_last_spawn =time .time ()
secret_shape_interval =180 
secret_shape_active =False 
secret_shape_obj =None 
secret_bonus_unlocked =False 

BASE_VALUES ={"click":1 ,"auto":0 ,"multiplier_log10":0.0 }
BASE_COST_LOG10 ={"auto":math .log10 (39.0 ),"click":math .log10 (25.0 ),"mult":math .log10 (49.0 )}
LOG10_UPG_INC ={"auto":math .log10 (1.25 ),"click":math .log10 (1.15 ),"mult":math .log10 (1.35 )}

game_settings ={
"graphics_mode":"graphismes_travaillés",
"purchase_mode":"single",
"mini_autoclicker":False ,
"auto_buyers":False ,
"theme":"clair",
"mini_notifications":True ,
"ingame_notifications":True ,
"auto_rebirth":False ,
"confirm_resets":True ,
}

game_data ={

"score_log10":NEG_INF ,
"max_score_log10":NEG_INF ,

"click_value":BASE_VALUES ["click"],
"auto_value":BASE_VALUES ["auto"],
"multiplier_log10":BASE_VALUES ["multiplier_log10"],
"cost_auto_log10":BASE_COST_LOG10 ["auto"],
"cost_click_log10":BASE_COST_LOG10 ["click"],
"cost_mult_log10":BASE_COST_LOG10 ["mult"],

"points_log10":{"R":NEG_INF ,"P":NEG_INF ,"A":NEG_INF ,"Re":NEG_INF },
"PI":0 ,

"points_max_log10":{"R":NEG_INF ,"P":NEG_INF ,"A":NEG_INF ,"Re":NEG_INF },
"pi_max":0 ,
"pi_spent_total":0 ,
"grand_resets":0 ,

"total_clicks":0 ,
"max_sps":0.0 ,
"total_play_time":0.0 ,
"total_upgrades_bought":0 ,
"max_auto_sps_log10":NEG_INF ,

"perm_unlocks":{"mini_autoclicker":True ,"auto_buyers":True },

"ever_unlocked_challenges":False ,
}

L_REN =3.0 
L_PRE =math .log10 (5.0 )+6.0 
L_ASC =13.0 
L_REINC =31.0 
L_INF =39.0 

def draw_modal_popups (mouse_pos ):

    if show_version_popup :
        draw_version_popup (mouse_pos )


PI_M_THRESH =[1 ,2 ,3 ,5 ,10 ,15 ,20 ,50 ,100 ,200 ,
500 ,1000 ,2000 ,5000 ,10000 ,
20000 ,50000 ,100000 ,200000 ,1000000 ]

def pi_m_count ()->int :
    pi =game_data .get ("PI",0 )
    cnt =0 
    for t in PI_M_THRESH :
        if pi >=t :cnt +=1 
        else :break 
    return cnt 

PI_M_LABELS =[
("M1","×1.2 score / milestone (M1+)"),
("M2","×1.1 pts réinit / milestone (M2+)"),
("M3","×1.01 PI / milestone (M3+)"),
("M4","×10 score"),
("M5","×1.5 pts réinit"),
("M6","×1.1 PI"),
("M7","×1K score"),
("M8","M1 passe à ×1.25 / milestone"),
("M9","M2 passe à ×1.15 / milestone"),
("M10","M3 passe à ×1.025 / milestone"),
("M11","Score ^1.01"),
("M12","Débloque Challenges"),
("M13","×1e10 score"),
("M14","×2 pts réinit"),
("M15","×1.5 PI"),
("M16","Score ^1.05"),
("M17","×5 pts réinit"),
("M18","×2 PI"),
("M19","Score ^1.1"),
("M20","Débloque Grand Reset"),
]

CHALLENGES_DEF =[
{
"id":1 ,
"name":"Challenge 1",
"objective":"Obtenir 1 point d’infinité",
"nerf":"Score obtenu divisé par 10",
"buff":"Score obtenu multiplié par 2",
},
{
"id":2 ,
"name":"Challenge 2",
"objective":"Obtenir 1^100 de score",
"nerf":"Pas de PI, points de réinitialisation ÷2",
"buff":"Bonus R : +2% (au lieu de +1%)",
},
{
"id":3 ,
"name":"Challenge 3",
"objective":"Obtenir la 18ème milestone d’infinité (100K PI)",
"nerf":"Aucun",
"buff":"Points de réinitialisation ×1.5 (PI ×1.1)",
},
{
"id":4 ,
"name":"Challenge 4",
"objective":"Obtenir 1 point d’ascension",
"nerf":"Améliorations de score indisponibles",
"buff":"Déblocage du Grand Reset",
},
]

challenge_state ={
"active":False ,
"current":0 ,
"completed":[False ,False ,False ,False ],
"notified_ready":False ,
}

def gr_count ():
    return int (game_data .get ("grand_resets",0 ))

def gr_gain_exponent ():
    """Exposant multiplié sur les gains de score (appliqué dans apply_gain_modifiers)."""
    g =gr_count ()
    if difficulty ==DIFF_VERY_EASY :
        return 3.0 if g <=0 else 3.0 +0.2 *(g -1 )
    if difficulty ==DIFF_IMPOSSIBLE :
        return 1.1 if g <=0 else 1.1 +0.01 *(g -1 )

    return 2.0 if g <=0 else 2.0 +0.1 *(g -1 )

def gr_points_gain_log10_bonus_log10 ():
    """
    Ajoute un bonus multiplicatif (log10) sur les gains R/P/A/Re par GR.
    v29: x100/GR => +2.0 log10 par GR. Difficulté modifie:
      - Très Facile: x1000/GR => +3.0 log10 par GR
      - Impossible : x5/GR    => +log10(5) par GR
    """
    g =gr_count ()
    if difficulty ==DIFF_VERY_EASY :return 3.0 *g 
    if difficulty ==DIFF_IMPOSSIBLE :return math .log10 (5.0 )*g 
    return 2.0 *g 

def gr_points_gain_bonus_log10 ():
    return gr_points_gain_log10_bonus_log10 ()

def gr_pi_gain_multiplier ():
    """
    Multiplicateur PI (Infinité) cumulé par GR :
      - v29: ×2^g
      - Très Facile: ×3^g
      - Impossible : ×1.1^g
    """
    g =gr_count ()
    if g <=0 :
        return 1.0 
    if difficulty ==DIFF_VERY_EASY :
        return 3.0 **g 
    if difficulty ==DIFF_IMPOSSIBLE :
        return (1.1 )**g 
    return float (1 <<g )

CHALLENGE_UNLOCK_PI =1000 

def challenges_unlocked ()->bool :

    if difficulty in (DIFF_VERY_EASY ,DIFF_EASY ):
        return True 
    return game_data .get ("PI",0 )>=CHALLENGE_UNLOCK_PI 

def challenges_menu_accessible ()->bool :
    if difficulty in (DIFF_VERY_EASY ,DIFF_EASY ):
        return True 
    return game_data .get ('ever_unlocked_challenges',False )or challenges_unlocked ()

def sync_challenges_with_difficulty ():
    """
    - Très Facile : C1..C4 considérés comme complétés, menu challenges accessible.
    - Facile      : C1 et C2 complétés; le joueur n'a plus qu'à faire C3 et C4.
    Appelée après sélection de la difficulté, après full reset et après Grand Reset.
    """
    global challenge_state ,game_data 
    try :
        completed =challenge_state .get ("completed",[False ,False ,False ,False ])
    except Exception :
        challenge_state ={"active":False ,"current":0 ,"completed":[False ,False ,False ,False ],"notified_ready":False }
        completed =challenge_state ["completed"]

    if difficulty ==DIFF_VERY_EASY :

        challenge_state ["active"]=False 
        challenge_state ["current"]=0 
        challenge_state ["completed"]=[True ,True ,True ,True ]
        game_data ["ever_unlocked_challenges"]=True 
    elif difficulty ==DIFF_EASY :

        completed [0 ]=True 
        completed [1 ]=True 
        challenge_state ["completed"]=completed 
        game_data ["ever_unlocked_challenges"]=True 
    else :

        pass 

def have_challenge_buff (idx :int )->bool :

    if difficulty ==DIFF_VERY_EASY :
        return True 

    if challenge_state ["active"]:
        return False 
    return bool (challenge_state ["completed"][idx ])

def objective_met (cid :int )->bool :
    if cid ==1 :
        return game_data .get ("PI",0 )>=1 
    if cid ==2 :
        return game_data .get ("score_log10",NEG_INF )>=100.0 
    if cid ==3 :
        return game_data .get ("PI",0 )>=100_000 
    if cid ==4 :
        return game_data .get ("points_log10",{}).get ("A",NEG_INF )>=0.0 
    return False 

def _test_infinity_guard ():
    cases =[
    (0 ,100 ,False ),
    (99.9 ,100 ,False ),
    (100 ,100 ,True ),
    (150 ,100 ,True ),
    ]
    for s ,r ,expected in cases :
        got =can_enter_infinity (s ,r )
        assert got ==expected ,f"can_enter_infinity({s },{r })={got } expected={expected }"
    print ("[OK] Infinity guard tests passed")

def can_enter_infinity (current_score :float ,required_score :float )->bool :
    try :
        return float (current_score )>=float (required_score )
    except Exception :
        return False 

def format_infinity_status (current_score ,required_score )->str :
    ok =can_enter_infinity (current_score ,required_score )
    return "Score suffisant"if ok else f"Score insuffisant : besoin de {required_score :,}"

def reset_progress_for_run ():

    game_data ["score_log10"]=NEG_INF 
    game_data ["click_value"]=BASE_VALUES ["click"]
    game_data ["auto_value"]=BASE_VALUES ["auto"]
    game_data ["multiplier_log10"]=BASE_VALUES ["multiplier_log10"]
    game_data ["cost_auto_log10"]=BASE_COST_LOG10 ["auto"]
    game_data ["cost_click_log10"]=BASE_COST_LOG10 ["click"]
    game_data ["cost_mult_log10"]=BASE_COST_LOG10 ["mult"]
    for k in ("R","P","A","Re"):
        game_data ["points_log10"][k ]=NEG_INF 
    game_data ["PI"]=0 

def start_challenge (cid :int ):

    if difficulty ==DIFF_VERY_EASY :
        add_notification ("En Très Facile, tous les challenges sont déjà complétés.",1800 )
        return False 

    if difficulty !=DIFF_VERY_EASY and not milestone_currently_unlocked (12 ):
        add_notification ("La 12e milestone d’infinité n’est pas débloquée actuellement.",2200 )
        return False 
    if cid <1 or cid >4 :return False 

    for i in range (cid -1 ):
        if not challenge_state ["completed"][i ]:
            add_notification ("Termine d'abord le challenge précédent.",1800 )
            return False 

    reset_progress_for_run ()
    challenge_state ["active"]=True 
    challenge_state ["current"]=cid 
    challenge_state ["notified_ready"]=False 
    add_notification (f"Challenge {cid } lancé !",1800 )
    return True 

def stop_challenge ():
    if not challenge_state ["active"]:return 
    reset_progress_for_run ()
    challenge_state ["active"]=False 
    prev =challenge_state ["current"]
    challenge_state ["current"]=0 
    challenge_state ["notified_ready"]=False 
    add_notification (f"Challenge {prev } arrêté. Progression réinitialisée.",2200 )

def complete_challenge ():
    if not challenge_state ["active"]:return False 
    cid =challenge_state ["current"]
    if not objective_met (cid ):
        add_notification ("Objectif non atteint.",1600 )
        return False 

    challenge_state ["completed"][cid -1 ]=True 

    reset_progress_for_run ()
    challenge_state ["active"]=False 
    challenge_state ["current"]=0 
    challenge_state ["notified_ready"]=False 
    add_notification (f"Challenge {cid } complété !",2400 )
    return True 

def unlocked_pi_milestones ():
    """
    Retourne une liste de tuples (thr, name, eff) comme avant,
    longueur = nombre de milestones PI débloquées.
    Les 'eff' sont vides (les calculs v29.9 sont ailleurs).
    """
    cnt =pi_m_count ()
    res =[]
    for i in range (cnt ):
        thr =PI_M_THRESH [i ]
        name =f"M{i +1 }"
        eff ={}
        res .append ((thr ,name ,eff ))
    return res 

def score_multiplier_from_milestones_log10 ()->float :
    """
    v29.9 — Nouveau M1 :
      - ×1.2 score par milestone > 2 (M3+)
      - passe à ×1.25 à partir de M8 (rétroactif)
    """
    cnt =pi_m_count ()
    if cnt <=2 :
        return 0.0 
    steps =cnt -2 
    per =1.25 if cnt >=8 else 1.2 
    return steps *math .log10 (per )
    return add 

def score_power_exponent_from_milestones ()->float :
    """v29.9 — exposant sur le gain de score (clic/auto)."""
    cnt =pi_m_count ()
    expo =1.0 
    if cnt >=11 :expo *=1.01 
    if cnt >=16 :expo *=1.05 
    if cnt >=19 :expo *=1.10 
    return expo 

def _debug_log_milestone_effects ():
    """
    Logge dans game_logs les effets calculés des milestones :
      - M1 (multiplicateur de score en log10 et en ×)
      - M2 (multiplicateur de points R/P/A/Re en log10 et ×)
      - M3 (multiplicateur de PI)
      - M11/M16/M19 : exposant total sur les gains de score
    """
    try :
        cnt =pi_m_count ()
        L_score_m1 =score_multiplier_from_milestones_log10 ()
        Pmul_R =points_gain_multiplier_log10_for ('R')-gr_points_gain_bonus_log10 ()-game_data .get ("PI",0 )*LOG10_PI_RP_BOOST if 'LOG10_PI_RP_BOOST'in globals ()else points_gain_multiplier_log10_for ('R')

        expo =score_power_exponent_from_milestones ()

        pi_mul =1.0 
        if cnt >3 :
            steps =cnt -3 
            per =1.025 if cnt >=10 else 1.01 
            pi_mul *=(per **steps )

        log_event (f"[DEBUG MILESTONES] cnt={cnt } · M1: +{L_score_m1 :.6f} log10 => ×{10 **L_score_m1 :.3f} · expo={expo :.4f} · PI_mul(M3)≈×{pi_mul :.4f}")
    except Exception as e :
        log_event (f"[DEBUG MILESTONES] ERREUR: {e }")

def milestone_tooltip_lines (i :int )->list [str ]:
    """
    Retourne des lignes expliquant le bonus appliqué à la milestone i (1..20),
    en se basant sur l'état courant (PI, GR, etc.).
    """
    lines =[]
    cnt =pi_m_count ()

    name ,desc =PI_M_LABELS [i -1 ]
    thr =PI_M_THRESH [i -1 ]
    unlocked =game_data .get ("PI",0 )>=thr 
    lines .append (f"{name } — seuil: {thr :,} PI".replace (","," "))
    lines .append ("État : "+("Débloquée"if unlocked else "Verrouillée"))

    if i ==1 :

        L =score_multiplier_from_milestones_log10 ()
        lines .append (f"Score global: ×{10 **L :.4f} (M1 cumulée)")
    elif i ==2 :

        addL =0.0 
        if cnt >2 :
            steps =cnt -2 
            per =1.15 if cnt >=9 else 1.10 
            addL +=steps *math .log10 (per )
        lines .append (f"Pts de réinit (R/P/A/Re): ×{10 **addL :.4f}")
    elif i ==3 :

        pi_mul =1.0 
        if cnt >3 :
            steps =cnt -3 
            per =1.025 if cnt >=10 else 1.01 
            pi_mul *=(per **steps )
        lines .append (f"PI: ×{pi_mul :.4f}")
    elif i in (11 ,16 ,19 ):
        expo =score_power_exponent_from_milestones ()
        lines .append (f"Exposant sur gains de score: ^{expo :.4f}")
    elif i ==12 :
        lines .append ("Débloque Challenges (accès au menu)")

    if i ==20 :
        lines .append ("Débloque Grand Reset (selon difficulté)")

    return lines 

def points_gain_multiplier_log10_for (family :str )->float :
    add =gr_points_gain_bonus_log10 ()
    cnt =pi_m_count ()

    if family in ("R","P","A","Re"):

        if cnt >2 :
            steps =cnt -2 
            per =1.15 if cnt >=9 else 1.1 
            add +=steps *math .log10 (per )

        add +=game_data .get ("PI",0 )*LOG10_PI_RP_BOOST 

        if have_challenge_buff (2 ):
            add +=math .log10 (1.5 )

        return add 

    return add 

def log10_linear_bonus (rate :float ,P_log10 :float )->float :
    if P_log10 ==NEG_INF or rate <=0 :return 0.0 
    if P_log10 >6.0 :return math .log10 (rate )+P_log10 
    P =10.0 **P_log10 
    return math .log10 (1.0 +rate *P )

def total_points_multiplier_log10 ()->float :
    pts =game_data .get ("points_log10",{})
    L =0.0 

    r_rate =0.02 if have_challenge_buff (1 )else 0.01 
    L +=log10_linear_bonus (r_rate ,pts .get ("R",NEG_INF ))
    if pts .get ("R",NEG_INF )>NEG_INF :
        L +=math .floor (max (0.0 ,pts .get ("R"))/3.0 )*LOG10_2 
    L +=log10_linear_bonus (0.05 ,pts .get ("P",NEG_INF ))
    if pts .get ("P",NEG_INF )>NEG_INF :
        L +=math .floor (max (0.0 ,pts .get ("P"))/3.0 )*LOG10_2 
    L +=log10_linear_bonus (0.20 ,pts .get ("A",NEG_INF ))
    if pts .get ("A",NEG_INF )>NEG_INF :
        L +=math .floor (max (0.0 ,pts .get ("A"))/3.0 )*LOG10_2 
    L +=log10_linear_bonus (0.50 ,pts .get ("Re",NEG_INF ))
    if pts .get ("Re",NEG_INF )>NEG_INF :
        L +=math .floor (max (0.0 ,pts .get ("Re"))/3.0 )*LOG10_2 
    L +=game_data .get ("PI",0 )*LOG10_PI_BOOST 
    L +=score_multiplier_from_milestones_log10 ()
    return L 

def log10_effective_click_value ()->float :
    cv =game_data ["click_value"]
    base =0.0 
    if cv >0 :base +=math .log10 (cv )
    base +=game_data .get ("multiplier_log10",0.0 )
    base +=total_points_multiplier_log10 ()
    return base 

def log10_effective_auto_value ()->float :
    av =game_data ["auto_value"]
    if av <=0 :return NEG_INF 
    base =math .log10 (av )
    base +=game_data .get ("multiplier_log10",0.0 )
    base +=total_points_multiplier_log10 ()
    return base 

def diff_score_gain_log10_bonus ()->float :
    """Bonus/nerf global sur les gains de score (log10)."""
    if difficulty ==DIFF_VERY_EASY :return math .log10 (5.0 )
    if difficulty ==DIFF_EASY :return math .log10 (3.0 )
    if difficulty ==DIFF_HARD :return -math .log10 (1.25 )
    if difficulty ==DIFF_IMPOSSIBLE :return -math .log10 (2.0 )
    return 0.0 

def diff_rp_gain_log10_bonus (family :str )->float :
    """
    Bonus/nerf sur points de réinit (R/P/A/Re). N'affecte PAS l'infinité (PI).
    """
    if family =='PI':return 0.0 
    if difficulty ==DIFF_VERY_EASY :return math .log10 (2.0 )
    if difficulty ==DIFF_EASY :return math .log10 (1.5 )
    if difficulty ==DIFF_HARD :return -math .log10 (1.5 )
    if difficulty ==DIFF_IMPOSSIBLE :return -math .log10 (2.0 )
    return 0.0 

def diff_pi_gain_multiplier ()->float :
    """Multiplicateur PI (seulement à l'infinité)."""
    if difficulty ==DIFF_VERY_EASY :return 1.5 
    if difficulty ==DIFF_EASY :return 1.25 
    if difficulty ==DIFF_HARD :return 1.0 /1.25 
    if difficulty ==DIFF_IMPOSSIBLE :return 1.0 /1.5 
    return 1.0 

def apply_gain_modifiers (addL :float )->float :

    if challenge_state ["active"]and challenge_state ["current"]==1 :
        addL -=math .log10 (10.0 )
    if have_challenge_buff (0 ):
        addL +=LOG10_2 

    addL +=diff_score_gain_log10_bonus ()

    if gr_count ()>0 :
        addL *=gr_gain_exponent ()
    sp =score_power_exponent_from_milestones ()
    if sp !=1.0 :
        addL *=sp 
    return addL 

def milestone_currently_unlocked (n :int )->bool :
    """
    True si la milestone n est débloquée.
    Ordre de priorité :
      1) Fonction dédiée milestone{n}_currently_unlocked()
      2) Milestones d'infinité (via PI_M_THRESH / PI)
      3) Compat: anciens achievements "MS.."
      4) Compat: niveaux externes (MILESTONE_UNLOCK_LEVELS / player.level)
    """

    fn =globals ().get (f"milestone{n }_currently_unlocked")
    if callable (fn ):
        try :
            return bool (fn ())
        except Exception :
            return False 

    try :
        if 1 <=n <=len (PI_M_THRESH ):
            return game_data .get ("PI",0 )>=PI_M_THRESH [n -1 ]
    except Exception :
        pass 

    achievements =globals ().get ('achievements')
    if isinstance (achievements ,dict ):
        keys =(f"MS{n }",f"MS{n :02d}",f"MS-{n :02d}")
        if any (achievements .get (k ,False )for k in keys ):
            return True 

    levels =globals ().get ('MILESTONE_UNLOCK_LEVELS')
    player =globals ().get ('player')
    if levels is not None and player is not None and hasattr (player ,'level'):
        try :
            req =levels [n ]if isinstance (levels ,dict )else levels [n -1 ]
            return player .level >=req 
        except Exception :
            pass 

    return False 

def reset_score_and_upgrades ():
    game_data ["score_log10"]=NEG_INF 
    game_data ["click_value"]=BASE_VALUES ["click"]
    game_data ["auto_value"]=BASE_VALUES ["auto"]
    game_data ["multiplier_log10"]=BASE_VALUES ["multiplier_log10"]
    game_data ["cost_auto_log10"]=BASE_COST_LOG10 ["auto"]
    game_data ["cost_click_log10"]=BASE_COST_LOG10 ["click"]
    game_data ["cost_mult_log10"]=BASE_COST_LOG10 ["mult"]

def _family_points_gain_log10 (L :float ,L0 :float ,band_factor_log10 :float )->float :
    if L <L0 :return NEG_INF 
    d =L -L0 
    b =int (math .floor (d /10.0 ))
    if b <0 :b =0 
    return d +b *band_factor_log10 

def estimate_points_gain_now_log10 (family :str ,L :float )->float :
    """v29.2.4: P = floor(log_b(S/T)) + 1 (si S >= T), renvoie log10(P).
    Bases: R=1.1 (T=1e3), P=1.125 (T=5e6), A=1.1625 (T=1e13), Re=1.2 (T=1e35)."""

    if family =='R':
        base =1.01 ;L0 =L_REN 
    elif family =='P':
        base =1.05 ;L0 =L_PRE 
    elif family =='A':
        base =1.10 ;L0 =L_ASC 
    elif family =='Re':
        base =1.15 ;L0 =L_REINC 
    else :
        return NEG_INF 
    if L <L0 :
        return NEG_INF 
    steps =int ((L -L0 )/math .log10 (base ))+1 
    if steps <=0 :
        return NEG_INF 
    return math .log10 (steps )

def do_reset_renaissance ()->bool :
    L =game_data ["score_log10"]
    if L <L_REN :return False 
    addL =estimate_points_gain_now_log10 ('R',L )+points_gain_multiplier_log10_for ('R')

    if challenge_state ["active"]and challenge_state ["current"]==2 :
        addL -=LOG10_2 

        addL +=diff_rp_gain_log10_bonus ('R')
    game_data ["points_log10"]["R"]=log10_add (game_data ["points_log10"]["R"],addL )
    reset_score_and_upgrades ()
    try :

        pretty =format_from_log10 (max (0.0 ,addL ))
        add_notification (f"Vous avez gagné ~{pretty } point(s) de Renaissance.",2200 )
    except Exception :
        pass 

    try :
        launch_reset_fx ("R",800 )
    except Exception as e :
        log_event (f"[FX] Renaissance error: {e }")

def do_reset_prestige ()->bool :
    L =game_data ["score_log10"]
    if L <L_PRE :return False 
    addL =estimate_points_gain_now_log10 ('P',L )+points_gain_multiplier_log10_for ('P')
    if challenge_state ["active"]and challenge_state ["current"]==2 :
        addL -=LOG10_2 

        addL +=diff_rp_gain_log10_bonus ('P')
    game_data ["points_log10"]["P"]=log10_add (game_data ["points_log10"]["P"],addL )
    game_data ["points_log10"]["R"]=NEG_INF 
    reset_score_and_upgrades ()
    try :
        pretty =format_from_log10 (max (0.0 ,addL ))
        add_notification (f"Vous avez gagné ~{pretty } point(s) de Prestige.",2200 )
    except Exception :
        pass 
    try :
        launch_reset_fx ("P",900 )
    except Exception as e :
        log_event (f"[FX] Prestige error: {e }")

def do_reset_ascension ()->bool :
    L =game_data ["score_log10"]
    if L <L_ASC :return False 
    addL =estimate_points_gain_now_log10 ('A',L )+points_gain_multiplier_log10_for ('A')
    if challenge_state ["active"]and challenge_state ["current"]==2 :
        addL -=LOG10_2 

        addL +=diff_rp_gain_log10_bonus ('A')
    game_data ["points_log10"]["A"]=log10_add (game_data ["points_log10"]["A"],addL )
    game_data ["points_log10"]["R"]=NEG_INF 
    game_data ["points_log10"]["P"]=NEG_INF 
    reset_score_and_upgrades ()
    try :
        pretty =format_from_log10 (max (0.0 ,addL ))
        add_notification (f"Vous avez gagné ~{pretty } point(s) d'Ascension.",2200 )
    except Exception :
        pass 
    try :
        launch_reset_fx ("A",1200 )
    except Exception as e :
        log_event (f"[FX] Ascension error: {e }")

def do_reset_reincarnation ()->bool :
    L =game_data ["score_log10"]
    if L <L_REINC :return False 
    addL =estimate_points_gain_now_log10 ('Re',L )+points_gain_multiplier_log10_for ('Re')
    if challenge_state ["active"]and challenge_state ["current"]==2 :
        addL -=LOG10_2 

        addL +=diff_rp_gain_log10_bonus ('Re')
    game_data ["points_log10"]["Re"]=log10_add (game_data ["points_log10"]["Re"],addL )
    game_data ["points_log10"]["R"]=NEG_INF 
    game_data ["points_log10"]["P"]=NEG_INF 
    game_data ["points_log10"]["A"]=NEG_INF 
    reset_score_and_upgrades ()
    try :
        pretty =format_from_log10 (max (0.0 ,addL ))
        add_notification (f"Vous avez gagné ~{pretty } point(s) de Réincarnation.",2200 )
    except Exception :
        pass 
    try :
        launch_reset_fx ("Re",1300 )
    except Exception as e :
        log_event (f"[FX] Reincarnation error: {e }")

def do_reset_infinity ()->bool :
    """
    v30.0 — Infinité
    - Si Challenge 2 actif : pas de PI (comportement déjà existant).
    - Gains de PI de base : floor( 1 + floor((L - L_INF)/3) ).
    - Multiplicateurs :
        1) GR : gr_pi_gain_multiplier()    (modifié par difficulté en v30.0)
        2) Milestones PI (M3 dynamique)    (existant)
        3) Difficulté : diff_pi_gain_multiplier()
    """
    L =game_data ["score_log10"]

    if L <L_INF :
        return False 

    if challenge_state ["active"]and challenge_state ["current"]==2 :
        reset_score_and_upgrades ()
        return True 


    gain_base =int (1 +math .floor ((L -L_INF )/LOG10_15 ))
    gain_base =max (0 ,gain_base )

    gr_mul =gr_pi_gain_multiplier ()

    cnt =pi_m_count ()
    pi_mul =1.0 
    if cnt >3 :
        steps =cnt -3 
        per =1.025 if cnt >=10 else 1.01 
        pi_mul *=(per **steps )

    diff_mul =diff_pi_gain_multiplier ()

    gain =int (math .floor (gain_base *gr_mul *pi_mul *diff_mul ))

    if gain >0 :
        game_data ["PI"]=game_data .get ("PI",0 )+gain 
        game_data ["pi_max"]=max (game_data .get ("pi_max",0 ),game_data ["PI"])

    if gain >0 :
        try :
            pretty =format_from_log10 (math .log10 (gain ))
            add_notification (f"Vous avez gagné {pretty } point(s) d'Infinité.",2400 )
        except Exception :
            add_notification (f"Vous avez gagné {gain } point(s) d'Infinité.",2400 )

    if challenges_unlocked ():
        game_data ["ever_unlocked_challenges"]=True 

    reset_score_and_upgrades ()
    try :
        launch_reset_fx ("Inf",1400 )
    except Exception as e :
        log_event (f"[FX] Infinity error: {e }")
    return True 

def next_gr_cost_pi ():
    """Coût en PI pour le prochain GR : base 1M, multiplié par 10 à chaque GR déjà effectué."""
    base =1_000_000 
    g =gr_count ()
    return base *(10 **g )

def do_grand_reset_if_confirm (now_ms :int )->bool :
    """
    v30.0 — Conditions d'accès au GR selon difficulté :
      - Très Facile : M20 INFINITÉ requise + 100K PI (pas de challenges requis)
      - Facile      : Challenge 2 complété (C2)
      - Normal/++   : Challenge 4 complété (comme avant)
    """

    completed =challenge_state .get ('completed',[False ,False ,False ,False ])
    if difficulty ==DIFF_VERY_EASY :
        if not milestone_currently_unlocked (20 ):
            return False 
        cost =next_gr_cost_pi ()
    elif difficulty ==DIFF_EASY :
        if not (len (completed )>1 and completed [1 ]):
            return False 
        cost =next_gr_cost_pi ()
    else :

        if not (len (completed )>3 and completed [3 ]):
            return False 
        cost =next_gr_cost_pi ()

    if game_data .get ("PI",0 )<cost :
        return False 

    game_data ["pi_spent_total"]+=cost 
    game_data ["PI"]=0 
    game_data ["grand_resets"]=gr_count ()+1 
    for k in ("R","P","A","Re"):
        game_data ["points_log10"][k ]=NEG_INF 
    reset_score_and_upgrades ()

    challenge_state ["completed"]=[False ,False ,False ,False ]
    if challenge_state ["active"]:
        challenge_state ["active"]=False 
        challenge_state ["current"]=0 

    try :
        sync_challenges_with_difficulty ()
    except Exception :
        pass 
    return True 

def perform_grand_reset_now ()->bool :
    log_event ("[GR] Trying to perform GR...")
    ok =do_grand_reset_if_confirm (pygame .time .get_ticks ())
    log_event (f"[GR] Result ok={ok }, PI={game_data .get ('PI',0 )}, cost={next_gr_cost_pi ()}, g={gr_count ()}")
    if ok :
        add_notification ("GRAND RESET effectué !",2800 )
        try :
            launch_reset_fx ("GR",1600 )
        except Exception as e :
            log_event (f"[FX] GR error: {e }")
    else :
        add_notification ("Conditions non remplies pour le Grand Reset.",2000 )
    return ok 

_milestones_row_rects =[]

notifications =[]

game_settings .setdefault ("global_progress",False )

GLOBAL_PROGRESS ={
"idx":1 ,
"done":False ,
}

def _gp_clamp01 (x :float )->float :
    return 0.0 if x <=0 else (1.0 if x >=1.0 else float (x ))

def _gp_ratio_log10 (curL :float ,needL :float )->float :
    """Progression de 0..1 vers un seuil log10 `needL` (gère NEG_INF)."""
    if not math .isfinite (needL )or needL <=0 :
        return 1.0 
    if curL ==NEG_INF or not math .isfinite (curL ):
        return 0.0 

    try :
        return _gp_clamp01 (10.0 **(curL -needL ))
    except Exception :
        return 0.0 

def _gp_points_L (fam :str )->float :
    return game_data .get ("points_log10",{}).get (fam ,NEG_INF )

def _gp_score_max_L ():

    return game_data .get ("score_log10",NEG_INF )

def _gp_counter (name :str )->int :
    """Lit un compteur avec alias robustes (ne dépend pas du tutoriel)."""

    if name =="clicks_done":

        return int (game_data .get ("total_clicks",0 ))

    if name in globals ():
        try :
            return int (globals ()[name ])
        except Exception :
            return 0 

    return 0 

def _gp_ch_active (cid :int )->bool :
    return bool (challenge_state .get ("active",False )and challenge_state .get ("current",0 )==cid )

def _gp_ch_done (cid :int )->bool :
    comp =challenge_state .get ("completed",[False ,False ,False ,False ])
    return bool (len (comp )>=cid and comp [cid -1 ])

def _gp_ms (n :int )->bool :
    try :
        return milestone_currently_unlocked (n )
    except Exception :
        return False 

def _gp_gr_count ()->int :
    try :
        return gr_count ()
    except Exception :
        return int (game_data .get ("grand_resets",0 ))

GP_DEFS =[
{"label":"Obtenir 25 de score","type":"score_L","L":math .log10 (25.0 )},
{"label":"Acheter une amélioration Clic","type":"counter","field":"click_upgrades","target":1 },
{"label":"Acheter un total de 10 améliorations clics","type":"counter","field":"click_upgrades","target":10 },
{"label":"Acheter 10 améliorations Auto","type":"counter","field":"auto_upgrades","target":10 },
{"label":"Acheter 5 améliorations Mult","type":"counter","field":"mult_upgrades","target":5 },

{"label":"Obtenir 1K de score","type":"score_L","L":3.0 },

{"label":"Faire une Renaissance","type":"has_points","fam":"R"},
{"label":"Obtenir un total de 10 points de Renaissance","type":"points_L","fam":"R","L":math .log10 (10.0 )},
{"label":"Obtenir 1K points de Renaissance","type":"points_L","fam":"R","L":3.0 },

{"label":"Obtenir 5M de score","type":"score_L","L":math .log10 (5.0 )+6.0 },

{"label":"Faire un Prestige","type":"has_points","fam":"P"},
{"label":"Obtenir 10 points de Prestige","type":"points_L","fam":"P","L":math .log10 (10.0 )},
{"label":"Obtenir 1K points de Prestige","type":"points_L","fam":"P","L":3.0 },

{"label":"Obtenir 10B de score","type":"score_L","L":10.0 },
{"label":"Obtenir 10T de score","type":"score_L","L":13.0 },

{"label":"Faire une Ascension","type":"has_points","fam":"A"},
{"label":"Obtenir 10 points d’Ascension","type":"points_L","fam":"A","L":math .log10 (10.0 )},
{"label":"Obtenir 1K points d’Ascension","type":"points_L","fam":"A","L":3.0 },

{"label":"Obtenir 1Qd de score","type":"score_L","L":15.0 },
{"label":"Obtenir 1Qn de score","type":"score_L","L":18.0 },
{"label":"Obtenir 1Sx de score","type":"score_L","L":21.0 },
{"label":"Obtenir 1Sp de score","type":"score_L","L":24.0 },
{"label":"Obtenir 1No de score","type":"score_L","L":30.0 },
{"label":"Obtenir 1De de score","type":"score_L","L":33.0 },
{"label":"Obtenir 100De de score","type":"score_L","L":35.0 },

{"label":"Faire une Réincarnation","type":"has_points","fam":"Re"},
{"label":"Obtenir 10 points de Réincarnation","type":"points_L","fam":"Re","L":math .log10 (10.0 )},
{"label":"Obtenir 1K points de Réincarnation","type":"points_L","fam":"Re","L":3.0 },

{"label":"Obtenir 1UDe de score","type":"score_L","L":36.0 },
{"label":"Obtenir 1DDe de score","type":"score_L","L":39.0 },
{"label":"Obtenir 1QdDe de score","type":"score_L","L":45.0 },
{"label":"Obtenir 1SxDe de score","type":"score_L","L":51.0 },
{"label":"Obtenir 1OcDe de score","type":"score_L","L":57.0 },
{"label":"Obtenir 1Vt de score","type":"score_L","L":63.0 },

{"label":"Faire une Infinité","type":"pi_amount","target":1 },

*[{"label":f"Obtenir la milestone d’infinité {i }","type":"ms","M":i }for i in range (1 ,13 )],

{"label":"Lancer le challenge 1","type":"chal_act","cid":1 },
{"label":"Terminer le challenge 1","type":"chal_done","cid":1 },
{"label":"Obtenir à nouveau la milestone d’infinité 12","type":"ms","M":12 },

{"label":"Lancer le challenge 2","type":"chal_act","cid":2 },
{"label":"Terminer le challenge 2","type":"chal_done","cid":2 },
{"label":"Obtenir à nouveau la milestone d’infinité 12","type":"ms","M":12 },

{"label":"Lancer le challenge 3","type":"chal_act","cid":3 },
{"label":"Terminer le challenge 3","type":"chal_done","cid":3 },
{"label":"Obtenir à nouveau la milestone d’infinité 12","type":"ms","M":12 },

{"label":"Lancer le challenge 4","type":"chal_act","cid":4 },
{"label":"Terminer le challenge 4","type":"chal_done","cid":4 },

*[{"label":f"Obtenir la milestone d’infinité {i }","type":"ms","M":i }for i in range (13 ,21 )],

{"label":"Obtenir 1M de points d’infinité","type":"pi_amount","target":1_000_000 },

{"label":"Effectuer un Grand Reset","type":"gr","target":1 },
{"label":"Effectuer un deuxième Grand Reset","type":"gr","target":2 },
{"label":"Effectuer un troisième Grand Reset","type":"gr","target":3 },
{"label":"Effectuer un total de 5 Grand Resets","type":"gr","target":5 },
{"label":"Effectuer un total de 10 Grand Resets","type":"gr","target":10 },
]

def gp_step_count ()->int :
    return len (GP_DEFS )

def gp_current_def ():
    i =GLOBAL_PROGRESS ["idx"]
    if GLOBAL_PROGRESS ["done"]or i <1 or i >gp_step_count ():
        return None 
    return GP_DEFS [i -1 ]

def gp_eval_ratio (defn :dict )->float :
    """Renvoie un ratio 0..1 pour l'étape `defn`."""
    typ =defn .get ("type","")

    if typ =="counter":
        field =defn .get ("field","")
        tgt =max (1 ,int (defn .get ("target",1 )))
        if field =="clicks_done":
            cur =int (game_data .get ("total_clicks",0 ))
        else :
            cur =_gp_counter (field )
        return _gp_clamp01 (cur /tgt )

    if typ =="score_L":
        return _gp_ratio_log10 (_gp_score_max_L (),float (defn ["L"]))

    if typ =="has_points":
        L =_gp_points_L (defn ["fam"])
        return 1.0 if L >NEG_INF else 0.0 

    if typ =="points_L":
        needL =float (defn ["L"])
        curL =_gp_points_L (defn ["fam"])
        return _gp_ratio_log10 (curL ,needL )

    if typ =="ms":
        return 1.0 if _gp_ms (int (defn ["M"]))else 0.0 

    if typ =="chal_act":
        return 1.0 if _gp_ch_active (int (defn ["cid"]))else 0.0 

    if typ =="chal_done":
        return 1.0 if _gp_ch_done (int (defn ["cid"]))else 0.0 

    if typ =="pi_amount":
        pi =int (game_data .get ("PI",0 ))
        tgt =max (1 ,int (defn .get ("target",1 )))
        return _gp_clamp01 (pi /tgt )

    if typ =="gr":
        g =_gp_gr_count ()
        tgt =max (1 ,int (defn .get ("target",1 )))
        return _gp_clamp01 (g /tgt )

    return 0.0 

def update_global_progress ():
    """Avance automatiquement tant que les étapes sont remplies + notifications."""
    if not game_settings .get ("global_progress",True ):
        return 
    if GLOBAL_PROGRESS ["done"]:
        return 

    advanced =0 
    N =gp_step_count ()

    while True :
        d =gp_current_def ()
        if not d :
            break 

        ratio =gp_eval_ratio (d )
        if ratio >=1.0 :

            cur_idx =GLOBAL_PROGRESS ["idx"]
            label =d .get ("label",f"Étape {cur_idx }")

            try :
                add_notification (f"Etape {cur_idx } terminée !",1800 )
            except Exception :
                pass 
            try :
                add_notification (f"✓ {label }",1400 )
            except Exception :
                pass 

            GLOBAL_PROGRESS ["idx"]+=1 
            advanced +=1 

            if GLOBAL_PROGRESS ["idx"]>N :
                GLOBAL_PROGRESS ["done"]=True 
                GLOBAL_PROGRESS ["idx"]=N 
                try :
                    add_notification ("Progression globale : 100% — Félicitations !",2600 )
                except Exception :
                    pass 
                break 

        else :
            break 

    if advanced >=3 :
        try :
            log_event (f"[GP] Auto-avancé de {advanced } étapes")
        except Exception :
            pass 

def global_progress_overall_ratio ()->float :
    """Ratio global = (étapes précédentes + progression de l'étape courante) / N."""
    N =gp_step_count ()
    if N <=0 :
        return 1.0 
    if GLOBAL_PROGRESS ["done"]:
        return 1.0 
    i =max (1 ,min (GLOBAL_PROGRESS ["idx"],N ))
    current_ratio =gp_eval_ratio (GP_DEFS [i -1 ])
    return _gp_clamp01 (((i -1 )+current_ratio )/N )

def wrap_lines_auto (text ,font ,max_width ):
    """
    Découpe automatiquement le texte en lignes qui ne dépassent pas max_width.
    Retourne une liste de lignes à afficher.
    """
    words =text .split (' ')
    lines =[]
    current =""
    for word in words :
        test =(current +" "+word ).strip ()
        if font .size (test )[0 ]>max_width and current :
            lines .append (current )
            current =word 
        else :
            current =test 
    if current :
        lines .append (current )
    return lines 

game_logs =[]

def log_event (msg :str ):
    try :
        ts =time .strftime ("%H:%M:%S")
    except Exception :
        ts ="--:--:--"
    entry =f"[{ts }] {msg }"
    game_logs .append (entry )

    if len (game_logs )>1000 :
        del game_logs [:len (game_logs )-1000 ]

developer_mode_active =False 
dev_password_mode =False 
dev_password_text =""
DEV_PASSWORD_SECRET ="devpass"
last_dev_command_ms =0 
DEV_CMD_COOLDOWN_MS =250 
dev_logs_page =0 
dev_cmd_rects ={}
dev_view_logs_rect =None 
dev_deactivate_rect =None 
dev_logs_nav_rects ={"prev":None ,"next":None }

dev_password_visible =False 
dev_password_eye_rect =None 

dev_ui_tab =None 
_dev_hub_rects ={}

DEV_BACK_MENU_BTN =Button ((80 ,HEIGHT -70 ,280 ,48 ),"Retour au menu principal",GRAY )
DEV_BACK_SETTINGS_BTN =Button ((380 ,HEIGHT -70 ,360 ,48 ),"Retour au choix des paramètres",GRAY )
DEV_BACK_COMMANDS_BTN =Button ((760 ,HEIGHT -70 ,360 ,48 ),"Retour commandes développeur",GRAY )

dev_score_input_text =""
dev_score_input_box_rect =None 
dev_score_input_left_x =0 
dev_score_input_max_w =0 
dev_score_caret =0 
dev_score_caret_visible =True 
dev_score_last_blink_ms =0 

DEV_SCORE_APPLY_BTN =None 

dev_pi_input_text =""
dev_pi_input_box_rect =None 
dev_pi_input_left_x =0 
dev_pi_input_max_w =0 
dev_pi_caret =0 
dev_pi_caret_visible =True 
dev_pi_last_blink_ms =0 


anti_cheat_offenses =0 

click_block_until_ms =0 

last_anticheat_trigger_ms =0 
DEV_PI_APPLY_BTN =None 

_dev_chal_rects ={
("c1","act"):None ,("c1","done"):None ,
("c2","act"):None ,("c2","done"):None ,
("c3","act"):None ,("c3","done"):None ,
("c4","act"):None ,("c4","done"):None ,
}

dev_deactivate_confirm ={"open":False ,"yes":None ,"no":None }

DEV_CARET_BLINK_MS =650 

dev_password_caret =0 
dev_password_caret_visible =True 
dev_password_last_blink_ms =0 
dev_password_box_rect =None 
dev_password_text_left_x =0 
dev_password_text_max_w =0 

code_input_caret =0 
code_input_caret_visible =True 
code_input_last_blink_ms =0 
code_input_box_rect =None 
code_input_text_left_x =0 
code_input_text_max_w =0 

def draw_dev_indicator ():
    """Small 'DEV' badge at bottom-right when developer mode is active."""
    if not developer_mode_active :
        return 
    tag =small_font .render ("DEV",True ,(255 ,255 ,255 ))
    pad =8 
    w ,h =tag .get_width ()+pad *2 ,tag .get_height ()+pad *2 
    box =pygame .Surface ((w ,h ),pygame .SRCALPHA )
    box .fill ((0 ,0 ,0 ,160 ))
    x =WIDTH -w -12 
    y =HEIGHT -h -12 
    screen .blit (box ,(x ,y ))
    screen .blit (tag ,(x +pad ,y +pad ))

def draw_difficulty_badge ():
    try :
        label =DIFF_LABELS .get (difficulty ,"?")
    except Exception :
        label ="?"

    if difficulty ==DIFF_VERY_EASY :bg =BLUE ;fg =WHITE 
    elif difficulty ==DIFF_EASY :bg =GREEN ;fg =WHITE 
    elif difficulty ==DIFF_NORMAL :bg =YELLOW ;fg =BLACK 
    elif difficulty ==DIFF_HARD :bg =RED ;fg =WHITE 
    else :bg =DARK_RED ;fg =WHITE 

    txt =small_font .render (f"Difficulté : {label }",True ,fg )
    pad =8 
    w ,h =txt .get_width ()+pad *2 ,txt .get_height ()+pad *2 

    margin =12 
    x =WIDTH -w -margin 
    y =HEIGHT -h -margin 

    if developer_mode_active :
        dev_tag =small_font .render ("DEV",True ,(255 ,255 ,255 ))
        dev_pad =8 
        dev_w ,dev_h =dev_tag .get_width ()+dev_pad *2 ,dev_tag .get_height ()+dev_pad *2 
        dev_x =WIDTH -dev_w -margin 
        dev_y =HEIGHT -dev_h -margin 

        gap =10 
        x =dev_x -gap -w 
        y =dev_y 

    box =pygame .Surface ((w ,h ),pygame .SRCALPHA )
    pygame .draw .rect (box ,(*bg ,220 ),(0 ,0 ,w ,h ),border_radius =10 )
    screen .blit (box ,(x ,y ))
    screen .blit (txt ,(x +pad ,y +pad ))

def draw_fps_badge ():
    fps =clock .get_fps ()
    txt =small_font .render (f"{fps :.1f} FPS",True ,(0 ,0 ,0 ))
    pad =7 
    w ,h =txt .get_width ()+pad *2 ,txt .get_height ()+pad *2 
    margin =12 

    y =HEIGHT -h -margin -42 
    x =WIDTH -w -margin 
    box =pygame .Surface ((w ,h ),pygame .SRCALPHA )
    box .fill ((220 ,240 ,255 ,220 ))
    pygame .draw .rect (box ,(180 ,220 ,255 ),(0 ,0 ,w ,h ),border_radius =8 )
    pygame .draw .rect (box ,(0 ,0 ,0 ),(0 ,0 ,w ,h ),2 ,border_radius =8 )
    box .blit (txt ,(pad ,pad ))
    screen .blit (box ,(x ,y ))

def draw_version_badge_bottom_right_above_fps ():
    """
    Affiche 'v<CURRENT_VERSION>' en bas-droite, juste au-dessus du badge FPS.
    """
    txt =small_font .render (f"v{CURRENT_VERSION }",True ,(0 ,0 ,0 ))
    pad =7 
    w ,h =txt .get_width ()+pad *2 ,txt .get_height ()+pad *2 

    margin =12 

    fps_txt =small_font .render (f"{clock .get_fps ():.1f} FPS",True ,(0 ,0 ,0 ))
    fps_pad =7 
    fps_w ,fps_h =fps_txt .get_width ()+fps_pad *2 ,fps_txt .get_height ()+fps_pad *2 
    fps_x =WIDTH -fps_w -margin 
    fps_y =HEIGHT -fps_h -margin -42 

    x =WIDTH -w -margin 
    y =fps_y -h -8 

    box =pygame .Surface ((w ,h ),pygame .SRCALPHA )
    box .fill ((220 ,240 ,255 ,220 ))
    pygame .draw .rect (box ,(180 ,220 ,255 ),(0 ,0 ,w ,h ),border_radius =8 )
    pygame .draw .rect (box ,(0 ,0 ,0 ),(0 ,0 ,w ,h ),2 ,border_radius =8 )
    box .blit (txt ,(pad ,pad ))
    screen .blit (box ,(x ,y ))

def execute_dev_command (code_name :str ):
    """Wrapper around existing dev code logic with cooldown and logging."""
    global last_dev_command_ms 
    now =pygame .time .get_ticks ()
    elapsed =now -last_dev_command_ms 
    if elapsed <DEV_CMD_COOLDOWN_MS :
        remain =int ((DEV_CMD_COOLDOWN_MS -elapsed )/1000 )+1 
        add_notification (f"Veuillez patienter {remain }s avant la prochaine commande.",1600 )
        return False 
    ok =apply_dev_code (code_name )
    if ok :
        last_dev_command_ms =now 
        log_event (f"Dev cmd exécutée: {code_name }")
    else :
        log_event (f"Dev cmd ÉCHEC: {code_name }")
    return ok 

FUSE_WINDOW_MS =5000 

def draw_global_progress_hud (mouse_pos ):
    """
    HUD de progression globale — affiché UNIQUEMENT pendant le jeu (écran 'play').
    - Barre verte, % basé sur l'étape courante (ex : 18/25 => 72%).
    - Cache automatiquement si overlay/modale ouverte.
    - N'apparaît ni pendant le chargement, ni pendant le Captcha, ni sur les autres écrans.
    - Efface une petite zone locale (autour de la barre) pour recouvrir une éventuelle barre dessinée avant,
      sans masquer le reste de l'UI.
    """

    try :
        if 'current_screen'in globals ()and current_screen !='play':
            return 
    except Exception :
        pass 

    if bool (loading_mode ):
        return 

    if not captcha_completed :
        return 

    overlay_open =(
    quit_confirm .get ("open",False )or 
    gr_confirm .get ("open",False )or 
    reset_confirm .get ("open",False )or 
    reset_flow .get ("state",0 )!=0 or 
    reset_flow .get ("in_progress",False )or 
    dev_password_mode or 
    (code_input_mode is not None )
    )
    if overlay_open :
        return 

    if not game_settings .get ("global_progress",True ):
        return 

    update_global_progress ()
    if GLOBAL_PROGRESS .get ("done",False ):
        return 

    N =gp_step_count ()
    idx =max (1 ,min (GLOBAL_PROGRESS .get ("idx",1 ),N ))
    step =gp_current_def ()

    def _step_ratio (defn ):
        if not defn :
            return 0.0 
        typ =defn .get ("type","")

        if typ =="score_L":
            needL =float (defn .get ("L",0.0 ))
            curL =game_data .get ("score_log10",NEG_INF )
            if curL ==NEG_INF or not math .isfinite (curL ):
                return 0.0 
            try :
                r =10.0 **(curL -needL )
                return 0.0 if r <0.0 else (1.0 if r >1.0 else r )
            except Exception :
                return 0.0 

        try :
            r =gp_eval_ratio (defn )or 0.0 
            r =float (r )
            return 0.0 if r <0.0 else (1.0 if r >1.0 else r )
        except Exception :
            return 0.0 

    ratio =_step_ratio (step )

    bg ,fg ,panel ,_bar_unused =theme_colors ()
    bar_w ,bar_h =int (WIDTH *0.45 ),18 
    x =WIDTH //2 -bar_w //2 
    y =30 

    pad_left ,pad_right ,pad_top ,pad_bottom =120 ,180 ,26 ,14 
    clear_rect =pygame .Rect (
    max (0 ,x -pad_left ),
    max (0 ,y -pad_top ),
    min (WIDTH -(x -pad_left ),bar_w +pad_left +pad_right ),
    min (HEIGHT -(y -pad_top ),bar_h +pad_top +pad_bottom )
    )
    pygame .draw .rect (screen ,bg ,clear_rect )

    label_txt =f"Étape {idx }/{N }"
    if step :
        label_txt +=f" — {step .get ('label','')}"
    title =small_font .render (label_txt ,True ,fg )
    screen .blit (title ,(x ,y -22 ))

    pygame .draw .rect (screen ,BAR_BG ,(x ,y ,bar_w ,bar_h ),border_radius =6 )

    fill_w =int (bar_w *ratio )
    if fill_w >0 :
        pygame .draw .rect (screen ,GREEN ,(x ,y ,fill_w ,bar_h ),border_radius =6 )

    pygame .draw .rect (screen ,(0 ,0 ,0 ),(x ,y ,bar_w ,bar_h ),2 ,border_radius =6 )

    pct_surf =small_font .render (f"{int (ratio *100 )}%",True ,fg )
    screen .blit (pct_surf ,(x +bar_w +10 ,y +bar_h //2 -pct_surf .get_height ()//2 ))

def render_hud_layer (mouse_pos ):
    """Couche HUD commune (barre de progression globale) avec protection des erreurs."""
    try :
        draw_global_progress_hud (mouse_pos )
    except Exception as e :
        try :
            log_event (f"[HUD] error: {e }")
        except Exception :
            pass 

    try :
        if 'current_screen'in globals ()and current_screen =='play':
            draw_version_badge_bottom_right_above_fps ()
    except Exception :
        pass 

loading_start_ms =-1 
loading_duration_ms =0 
loading_mode =None 

reset_white_start_ms =-1 
reset_white_duration_ms =1000 

KB_PER_SEC =100.0 
KB_STEP =0.1 
LOADING_STEP_MS =2 

loading_total_kb =268 
loaded_kb_display =0.0 
loading_step_accum_ms =0 

__DRAWING_PLAY =False 

RESET_FX ={
"active":False ,
"kind":None ,
"start":0 ,
"duration":1200 ,
"snap":None ,
"rng_seed":0 ,
"particles":[],
"tiles":[],
}

global _GP_HUD_DRAWN ,_GP_HUD_CALLERS 

_GP_HUD_DRAWN =False 
_GP_HUD_CALLERS =[]

def _fx_ease_out (t :float )->float :

    return 1.0 -(1.0 -t )**2.0 

def _fx_ease_in (t :float )->float :

    return t **2.0 

def launch_reset_fx (kind :str ,duration_ms :int =1200 ):
    """Démarre un FX. Ne fait rien en mode performance."""
    if game_settings .get ("graphics_mode")!="graphismes_travaillés":
        return 
    RESET_FX ["active"]=True 
    RESET_FX ["kind"]=kind 
    RESET_FX ["start"]=pygame .time .get_ticks ()
    RESET_FX ["duration"]=duration_ms 
    RESET_FX ["snap"]=screen .copy ()
    RESET_FX ["rng_seed"]=RESET_FX ["start"]
    RESET_FX ["particles"]=[]
    RESET_FX ["tiles"]=[]

    rnd =random .Random (RESET_FX ["rng_seed"])
    cx ,cy =WIDTH //2 ,HEIGHT //2 

    if kind =="P":
        for _ in range (160 ):
            RESET_FX ["particles"].append ({
            "x":rnd .uniform (0 ,WIDTH ),
            "y":rnd .uniform (0 ,HEIGHT ),
            "r":rnd .uniform (1.5 ,2.8 ),
            "phase":rnd .uniform (0 ,2 *math .pi ),
            "speed":rnd .uniform (2.0 ,3.8 ),
            })

    elif kind =="Inf":
        for _ in range (220 ):
            ang =rnd .uniform (0 ,2 *math .pi )
            sp =rnd .uniform (180 ,520 )
            size =rnd .uniform (1.2 ,2.8 )
            col =(rnd .randint (200 ,255 ),rnd .randint (200 ,255 ),255 )
            RESET_FX ["particles"].append ({"ang":ang ,"dist":sp ,"size":size ,"col":col })

    elif kind =="GR":
        grid_x ,grid_y =12 ,7 
        tw =WIDTH //grid_x 
        th =HEIGHT //grid_y 
        snap =RESET_FX ["snap"]
        for gy in range (grid_y ):
            for gx in range (grid_x ):
                rect =pygame .Rect (gx *tw ,gy *th ,tw ,th )
                tile =snap .subsurface (rect ).copy ()
                cx0 =rect .centerx -cx 
                cy0 =rect .centery -cy 
                ang =rnd .uniform (-20 ,20 )
                RESET_FX ["tiles"].append ({
                "surf":tile ,
                "rect":rect .copy (),
                "dx":-cx0 ,
                "dy":-cy0 ,
                "rot":ang ,
                })

def draw_reset_fx_overlay ():
    """Dessine l'overlay si un FX est actif. À appeler APRÈS le rendu normal."""
    if not RESET_FX ["active"]:
        return 
    now =pygame .time .get_ticks ()
    t =(now -RESET_FX ["start"])/max (1 ,RESET_FX ["duration"])
    if t >=1.0 :
        RESET_FX ["active"]=False 
        return 

    kind =RESET_FX ["kind"]
    snap =RESET_FX ["snap"]
    cx ,cy =WIDTH //2 ,HEIGHT //2 

    if kind =="R":
        overlay =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
        radius =int (max (WIDTH ,HEIGHT )*(0.15 +1.1 *_fx_ease_out (t )))

        for i in range (6 ):
            a =int (140 *(1.0 -t )*(1.0 -i /6 ))
            pygame .draw .circle (overlay ,(50 ,205 ,50 ,a ),(cx ,cy ),max (1 ,radius -i *60 ),60 )

        tint =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
        tint .fill ((50 ,140 ,80 ,int (70 *(1.0 -t ))))
        screen .blit (overlay ,(0 ,0 ))
        screen .blit (tint ,(0 ,0 ))

    elif kind =="P":

        gold =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
        gold .fill ((255 ,215 ,0 ,int (40 +100 *(1.0 -t ))))
        screen .blit (gold ,(0 ,0 ),special_flags =pygame .BLEND_ADD )

        rnd =random .Random (RESET_FX ["rng_seed"])
        for p in RESET_FX ["particles"]:
            x ,y ,r =p ["x"],p ["y"],p ["r"]

            a =0.5 +0.5 *math .sin (p ["phase"]+now /1000.0 *p ["speed"])
            alpha =int (220 *a *(1.0 -t ))
            if alpha <=0 :continue 
            s =pygame .Surface ((int (r *4 ),int (r *4 )),pygame .SRCALPHA )
            pygame .draw .circle (s ,(255 ,240 ,180 ,alpha ),(s .get_width ()//2 ,s .get_height ()//2 ),int (r *2 ))
            screen .blit (s ,(int (x -s .get_width ()/2 ),int (y -s .get_height ()/2 )),special_flags =pygame .BLEND_ADD )

    elif kind =="A":
        y_off =int (-_fx_ease_out (t )*(HEIGHT *0.6 ))
        if snap :
            screen .blit (snap ,(0 ,y_off ))
        white =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
        white .fill ((255 ,255 ,255 ,int (255 *t )))
        screen .blit (white ,(0 ,0 ))

    elif kind =="Re":

        ang =360.0 *t *2.0 
        scale =max (0.3 ,1.0 -0.6 *t )
        if snap :
            rot =pygame .transform .rotozoom (snap ,ang ,scale )
            screen .blit (rot ,rot .get_rect (center =(cx ,cy )))

        overlay =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
        R =int (math .hypot (WIDTH ,HEIGHT )*0.55 )
        rings =7 
        for i in range (rings ):
            hue =(t +i /rings )%1.0 
            r ,g ,b =colorsys .hsv_to_rgb (hue ,0.9 ,1.0 )
            col =(int (r *255 ),int (g *255 ),int (b *255 ),int (110 *(1.0 -t )))
            pygame .draw .circle (overlay ,col ,(cx ,cy ),int (R *(i +1 )/rings ),8 )
        screen .blit (overlay ,(0 ,0 ))

    elif kind =="Inf":

        overlay =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
        e =_fx_ease_out (t )
        for s in RESET_FX ["particles"]:
            dist =s ["dist"]*e 
            x =cx +math .cos (s ["ang"])*dist 
            y =cy +math .sin (s ["ang"])*dist 
            alpha =int (255 *(1.0 -t ))
            pygame .draw .circle (overlay ,(*s ["col"],alpha ),(int (x ),int (y )),int (s ["size"]))
        screen .blit (overlay ,(0 ,0 ))

        if snap :
            for i in range (4 ):
                sc =max (0.15 ,1.0 -t *(0.6 +i *0.1 ))
                rot =pygame .transform .rotozoom (snap ,0 ,sc )
                a =int (140 *(1.0 -t )*(1.0 -i /4 ))
                mask =pygame .Surface (rot .get_size (),pygame .SRCALPHA )
                mask .fill ((255 ,255 ,255 ,a ))
                rot .blit (mask ,(0 ,0 ),special_flags =pygame .BLEND_MULT )
                screen .blit (rot ,rot .get_rect (center =(cx ,cy )))

    elif kind =="GR":
        e =_fx_ease_in (t )

        for tile in RESET_FX ["tiles"]:
            x =tile ["rect"].x +tile ["dx"]*e 
            y =tile ["rect"].y +tile ["dy"]*e 
            angle =tile ["rot"]*(1.0 -e )
            surf =pygame .transform .rotozoom (tile ["surf"],angle ,max (0.2 ,1.0 -0.6 *e ))
            screen .blit (surf ,(x ,y ))

        hole =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
        radius =int (max (WIDTH ,HEIGHT )*0.05 +e *max (WIDTH ,HEIGHT )*0.45 )
        pygame .draw .circle (hole ,(0 ,0 ,0 ,255 ),(cx ,cy ),radius )

        for i in range (4 ):
            a =int (90 *(1.0 -i /4 ))
            pygame .draw .circle (hole ,(0 ,0 ,0 ,a ),(cx ,cy ),radius +30 +i *36 ,36 )
        screen .blit (hole ,(0 ,0 ))

def compute_loading_total_kb ()->int :
    """
    Essaie d'estimer automatiquement la taille à charger (en Ko).
    Par défaut: taille du script courant (~KiB). Fallback: 199 Ko.
    """
    try :
        sz_bytes =os .path .getsize (__file__ )

        return max (1 ,int (math .ceil (sz_bytes /1024.0 )))
    except Exception :
        return 199 

def get_game_file_size_kb ()->int :
    """Retourne une estimation en Ko de la taille du script de jeu."""
    try :
        sz_bytes =os .path .getsize (__file__ )
        return int (math .ceil (sz_bytes /1024.0 ))
    except Exception :
        return 0 

def add_notification (message :str ,timer :int =2000 ):

    log_event (f"NOTIF: {message }")

    if not game_settings .get ("ingame_notifications",True ):
        return 
    now =pygame .time .get_ticks ()
    for n in notifications :
        if n .get ("message")==message and now -n .get ("created",now )<=FUSE_WINDOW_MS :
            n ["count"]=n .get ("count",1 )+1 
            n ["timer"]=max (n .get ("timer",timer ),timer )
            return 
    notifications .append ({"message":message ,"timer":timer ,"created":now ,"count":1 })

click_button =Button ((WIDTH //2 -100 ,HEIGHT //2 -120 ,220 ,220 ),"CLICK",BLUE ,WHITE )
upgrade_auto_button =Button ((50 ,HEIGHT -220 ,300 ,60 ),"",ORANGE )
upgrade_click_button =Button ((370 ,HEIGHT -220 ,300 ,60 ),"",BLUE )
upgrade_mult_button =Button ((690 ,HEIGHT -220 ,300 ,60 ),"",PURPLE )

captcha_true_button =Button ((WIDTH //2 -210 ,HEIGHT //2 +120 ,180 ,60 ),"Vrai",(90 ,200 ,120 ),(255 ,255 ,255 ))
captcha_false_button =Button ((WIDTH //2 +30 ,HEIGHT //2 +120 ,180 ,60 ),"Faux",(220 ,120 ,120 ),(255 ,255 ,255 ))

renaissance_button =Button ((WIDTH -320 ,40 ,300 ,74 ),"Renaissance",(120 ,220 ,120 ),BLACK )
prestige_button =Button ((WIDTH -320 ,160 ,300 ,74 ),"Prestige",(220 ,120 ,120 ),WHITE )
ascension_button =Button ((WIDTH -320 ,280 ,300 ,74 ),"Ascension",(240 ,220 ,120 ),BLACK )
reinc_button =Button ((WIDTH -320 ,400 ,300 ,74 ),"Réincarnation",REINCARNATION_COLOR ,BLACK )
infinity_button =Button ((WIDTH -320 ,520 ,300 ,74 ),"Infinité",INFINITY_COLOR ,BLACK )

actions_base_y =250 
STEP =80 
MENU_X =WIDTH //2 -200 
MENU_W ,MENU_H =400 ,60 
labels =[
("play","Jouer",GREEN ,WHITE ),
("milestones","Milestones (PI)",GREEN ,WHITE ),
("challenges","Challenges",GREEN ,WHITE ),
("achievements","Achievements",GREEN ,WHITE ),
("settings","Paramètres",GREEN ,WHITE ),
("history","Statistiques",GREEN ,WHITE ),
("tutorial","Tutoriel",GREEN ,WHITE ),
("quit","Quitter",RED ,WHITE ),
]
menu_buttons ={key :Button ((MENU_X ,actions_base_y +i *STEP ,MENU_W ,MENU_H ),text ,bg ,fg )for i ,(key ,text ,bg ,fg )in enumerate (labels )}

mini_notifs ={'tutorial':False ,'achievements':False ,'milestones':False ,'play':False }
last_pi_milestones_count =0 

def draw_mini_badge (surface ,btn_rect ):
    """Dessine un petit badge de notification (rond rouge avec !) en haut à droite d'un bouton."""
    r =12 
    cx =btn_rect .right -10 
    cy =btn_rect .top +10 
    try :
        pygame .draw .circle (surface ,(235 ,70 ,70 ),(cx ,cy ),r )
        exclam =small_font .render ('!',True ,(255 ,255 ,255 ))
        surface .blit (exclam ,exclam .get_rect (center =(cx ,cy )))
    except Exception :

        pass 

back_button =Button ((20 ,HEIGHT -60 ,140 ,44 ),"Retour",GRAY ,BLACK )

dev_code_button =Button ((WIDTH -120 -280 ,HEIGHT -100 ,280 ,50 ),"Codes développeurs",(200 ,140 ,90 ),WHITE )
code_input_mode =None 
code_input_text =""

reset_progress_button =Button ((WIDTH //2 -260 ,HEIGHT -100 ,520 ,50 ),"Réinitialiser la progression",(200 ,80 ,80 ),WHITE )
reset_flow ={"state":0 ,"clicks":0 ,"start_ms":-1 ,"in_progress":False ,"progress_start_ms":-1 }
_reset_btn_rects ={"cont":None ,"back":None }

gr_confirm ={"open":False ,"rect_yes":None ,"rect_no":None }

quit_confirm ={"open":False ,"rect_yes":None ,"rect_no":None }

reset_confirm ={"open":False ,"kind":None ,"rect_yes":None ,"rect_no":None }

def handle_version_and_snapshot_popups (event )->bool :
    """Renvoie True si l'event est consommé par une popup modale."""
    global show_version_popup 

    if show_version_popup :
        if event .type ==pygame .MOUSEBUTTONDOWN and event .button ==1 :
            rect_ok =globals ().get ('_version_popup_ok_btn_rect')
            if rect_ok and rect_ok .collidepoint (event .pos ):

                show_version_popup =False 
                globals ().pop ('_version_popup_ok_btn_rect',None )

                if globals ().get ('_open_version_from_settings',False ):
                    globals ()['_open_version_from_settings']=False 
                return True 

        if event .type ==pygame .KEYDOWN and event .key ==pygame .K_ESCAPE :

            show_version_popup =False 
            globals ().pop ('_version_popup_ok_btn_rect',None )
            if globals ().get ('_open_version_from_settings',False ):
                globals ()['_open_version_from_settings']=False 
            return True 


        if event .type ==pygame .MOUSEWHEEL :

            step =(secondary_font .get_height ()+POPUP_LINE_SPACING )*3 

            delta =-event .y *step 
            globals ()['version_popup_scroll']=globals ().get ('version_popup_scroll',0 )+delta 
            return True 


        if event .type in (pygame .MOUSEBUTTONDOWN ,pygame .MOUSEBUTTONUP ,pygame .MOUSEWHEEL ,pygame .MOUSEMOTION ):
            return True 


        if event .type ==pygame .KEYDOWN and event .key ==pygame .K_ESCAPE :
            show_version_popup =False 
            globals ().pop ('_version_popup_ok_btn_rect',None )
            return True 


        if event .type in (pygame .MOUSEBUTTONDOWN ,pygame .MOUSEBUTTONUP ,pygame .MOUSEWHEEL ,pygame .MOUSEMOTION ):
            return True 


    return False 

def draw_reset_confirm_overlay (mouse_pos ):
    """v30.1 — Modale de confirmation pour resets R/P/A/Re/Inf."""
    if not reset_confirm .get ("open",False ):
        return 
    overlay =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
    overlay .fill ((0 ,0 ,0 ,160 ))
    screen .blit (overlay ,(0 ,0 ))
    w ,h =920 ,280 
    x ,y =WIDTH //2 -w //2 ,HEIGHT //2 -h //2 
    pygame .draw .rect (screen ,(250 ,250 ,250 ),(x ,y ,w ,h ),border_radius =12 )
    pygame .draw .rect (screen ,(0 ,0 ,0 ),(x ,y ,w ,h ),2 ,border_radius =12 )
    kind =reset_confirm .get ("kind","?")
    title =big_font .render (f"Confirmer le reset : {kind }",True ,(0 ,0 ,0 ))
    screen .blit (title ,(x +w //2 -title .get_width ()//2 ,y +18 ))
    lines =[
    "Cette action effectue le reset correspondant et applique les gains.",
    "Souhaitez-vous continuer ?",
    ]
    yy =y +88 
    for ln in lines :
        ls =secondary_font .render (ln ,True ,(20 ,20 ,20 ))
        screen .blit (ls ,(x +24 ,yy ));yy +=28 
    btn_w ,btn_h =280 ,50 
    yes_rect =pygame .Rect (x +w -btn_w -24 ,y +h -btn_h -18 ,btn_w ,btn_h )
    no_rect =pygame .Rect (x +24 ,y +h -btn_h -18 ,btn_w ,btn_h )
    yes_btn =Button (yes_rect ,"Oui, continuer",(140 ,200 ,120 ),(255 ,255 ,255 ))
    no_btn =Button (no_rect ,"Annuler",(200 ,120 ,120 ),(255 ,255 ,255 ))
    yes_btn .draw (screen ,mouse_pos )
    no_btn .draw (screen ,mouse_pos )
    reset_confirm ["rect_yes"]=yes_rect 
    reset_confirm ["rect_no"]=no_rect 

def have_enough_score (cost_log10 :float )->bool :
    return game_data ["score_log10"]>=cost_log10 

def can_reset_now (kind :str )->bool :
    """
    True si le score actuel est suffisant pour déclencher le reset demandé.
    kind accepte soit un code {'R','P','A','Re','Inf'}, soit un libellé
    {'Renaissance','Prestige','Ascension','Réincarnation','Infinité'}.
    """

    alias ={
    'Renaissance':'R',
    'Prestige':'P',
    'Ascension':'A',
    'Réincarnation':'Re',
    'Reincarnation':'Re',
    'Infinité':'Inf',
    'Infinite':'Inf',
    }
    kind =alias .get (kind ,kind )

    L_cur =game_data .get ("score_log10",NEG_INF )
    thresholds ={
    'R':L_REN ,
    'P':L_PRE ,
    'A':L_ASC ,
    'Re':L_REINC ,
    'Inf':L_INF ,
    }
    need =thresholds .get (kind ,float ('inf'))
    return L_cur >=need 

def gr_progress_ratio ()->float :
    have =max (0 ,int (game_data .get ("PI",0 )))
    cost =int (next_gr_cost_pi ())
    if cost <=0 :
        return 1.0 
    return max (0.0 ,min (1.0 ,have /float (cost )))

def open_reset_or_notify (kind :str ):
    """
    Ouvre la fenêtre de confirmation uniquement si le score est suffisant.
    Sinon : notification 'score insuffisant' immédiate, sans modale.
    Respecte l'option 'confirm_resets'.
    """

    labels ={
    'Renaissance':"Renaissance",
    'Prestige':"Prestige",
    'Ascension':"Ascension",
    'Réincarnation':"Réincarnation",
    'Infinité':"Infinité",
    }
    label =labels .get (kind ,"Reset")

    if not can_reset_now (kind ):
        add_notification (f"Score insuffisant pour {label }.",1600 )
        return 

    if game_settings .get ("confirm_resets",True ):

        reset_confirm .update ({"open":True ,"kind":kind ,"rect_yes":None ,"rect_no":None })
    else :

        actions ={
        'Renaissance':do_reset_renaissance ,
        'Prestige':do_reset_prestige ,
        'Ascension':do_reset_ascension ,
        'Réincarnation':do_reset_reincarnation ,
        'Infinité':do_reset_infinity ,
        }
        fn =actions .get (kind )
        if callable (fn ):
            fn ()

def pay_score (cost_log10 :float )->bool :
    if not have_enough_score (cost_log10 ):return False 
    game_data ["score_log10"]=log10_sub (game_data ["score_log10"],cost_log10 )
    return True 

def _get_cost_log10 (kind :str )->float :
    return game_data [f"cost_{kind }_log10"]

def _increase_cost (kind :str ):
    game_data [f"cost_{kind }_log10"]+=LOG10_UPG_INC [kind ]

def buy_upgrade (kind :str ,notify :bool =True ):
    if challenge_state ["active"]and challenge_state ["current"]==4 :
        add_notification ("Améliorations indisponibles dans le Challenge 4.",1600 )
        return False 
    costL =_get_cost_log10 (kind )
    if pay_score (costL ):
        if kind =="auto":
            game_data ["auto_value"]+=1 
            globals ()["auto_upgrades"]=globals ().get ("auto_upgrades",0 )+1 

        elif kind =="click":
            game_data ["click_value"]+=1.0 
            globals ()["click_upgrades"]=globals ().get ("click_upgrades",0 )+1 

        elif kind =="mult":
            game_data ["multiplier_log10"]=game_data .get ("multiplier_log10",0.0 )+math .log10 (1.2 )
            globals ()["mult_upgrades"]=globals ().get ("mult_upgrades",0 )+1 

        _increase_cost (kind )
        game_data ["total_upgrades_bought"]+=1 
        if notify :
            add_notification ({"auto":"Auto +1 acheté !",
            "click":"Clic +1 acheté !",
            "mult":"Multiplicateur x1.2 acheté !"}[kind ],2000 )
        return True 
    else :
        if notify :
            add_notification ("Score insuffisant pour l'upgrade.",1500 )
        return False 

def buy_upgrade_max (kind :str ):
    n =0 
    while have_enough_score (_get_cost_log10 (kind )):
        if not buy_upgrade (kind ,notify =False ):break 
        n +=1 

        try :
            gm =game_settings .get ("graphics_mode","graphismes_travaillés")
        except Exception :
            gm ="graphismes_travaillés"
        cap =50000 if gm =="graphismes_travaillés"else 100000 
        if n >=cap :
            break 
    if n >0 :add_notification (f"{kind .capitalize ()} x{n } acheté(s) !",2000 )

SUFFIX_TO_EXP ={"K":3 ,"M":6 ,"B":9 ,"T":12 ,"Qd":15 ,"Qn":18 ,"Sx":21 ,"Sp":24 ,"Oc":27 ,"No":30 ,"De":33 ,"UDe":36 ,"DDe":39 ,"TDe":42 ,"QdDe":45 ,"QnDe":48 ,"SxDe":51 ,"SpDe":54 ,"OcDe":57 ,"NoDe":60 ,"Vt":63 ,"UVt":66 ,"DVt":69 ,"TVt":72 ,"QdVt":75 ,"QnVt":78 ,"SxVt":81 ,"SpVt":84 ,"OcVt":87 ,"NoVt":90 ,"Tg":93 ,"UTg":96 ,"DTg":99 ,"TTg":102 ,"QdTg":105 ,"QnTg":108 ,"SxTg":111 ,"SpTg":114 ,"OcTg":117 ,"NoTg":120 }
SUFFIX_TO_EXP_CASELESS ={k .lower ():v for k ,v in SUFFIX_TO_EXP .items ()}

def parse_amount_to_log10 (s :str )->float :
    s =s .strip ().replace (' ','')
    if not s :return NEG_INF 
    if 'e'in s or 'E'in s :
        try :
            base ,exp =s .lower ().split ('e')
            base =float (base );exp =float (exp )
            if base <=0 :return NEG_INF 
            return math .log10 (base )+exp 
        except Exception :
            return NEG_INF 
    num ,suf ='',''
    for ch in s :
        if (ch .isdigit ()or ch =='.'):num +=ch 
        else :suf +=ch 
    try :
        val =float (num )if num else 0.0 
    except :
        val =0.0 
    if suf :
        suf_l =suf .lower ()
        exp =SUFFIX_TO_EXP_CASELESS .get (suf_l ,None )
        if exp is None :


            if suf_l .isalpha ():

                def alpha_suffix_to_index (target :str )->int |None :


                    max_try =max (26 ,26 **len (target ))
                    for n in range (max_try ):
                        try :
                            if _alpha_suffix_from_index (n )==target :
                                return n 
                        except Exception :
                            continue 
                    return None 

                ai =alpha_suffix_to_index (suf_l )
                if ai is not None and val >0 :
                    idx =4 +ai 
                    exp =3 *(idx +1 )
                else :
                    return NEG_INF 
            else :
                return NEG_INF 
        if exp is None or val <=0 :return NEG_INF 
        return math .log10 (val )+exp 
    else :
        if val <=0 :return NEG_INF 
        return math .log10 (val )

def validate_dev_input (user_input :str )->float :
    """
    Valide la saisie en mode développeur :
    - applique le système de suffixes via parse_amount_to_log10
    - interdit la saisie de mots 'infini', 'infinity', '∞' ou contenant ces mots
    """
    if not user_input :
        return NEG_INF 
    s =user_input .strip ().lower ()

    if s in ("infini","infinity","∞")or "infini"in s or "infinity"in s :
        return NEG_INF 

    return parse_amount_to_log10 (user_input )


def apply_dev_code (code :str )->bool :
    if not developer_mode_active :
        add_notification ("Commandes développeur désactivées.",1600 )
        return False 
    c =code .lower ()
    if c =='testrebirth':
        L =parse_amount_to_log10 ('15K')
        if L >NEG_INF :game_data ['score_log10']=log10_add (game_data ['score_log10'],L )
        add_notification ('+15K score (dev)',1600 );return True 
    if c =='testprestige':
        L =parse_amount_to_log10 ('50M')
        if L >NEG_INF :game_data ['score_log10']=log10_add (game_data ['score_log10'],L )
        add_notification ('+50M score (dev)',1600 );return True 
    if c =='testascension':
        L =parse_amount_to_log10 ('500T')
        if L >NEG_INF :game_data ['score_log10']=log10_add (game_data ['score_log10'],L )
        add_notification ('+500T score (dev)',1600 );return True 
    if c =='testreincarnation':
        L =parse_amount_to_log10 ('100DDe')
        if L >NEG_INF :game_data ['score_log10']=log10_add (game_data ['score_log10'],L )
        add_notification ('+100DDe score (dev)',1600 );return True 
    if c =='testinfinity':
        L =parse_amount_to_log10 ('1UVt')
        if L >NEG_INF :
            game_data ['score_log10']=log10_add (game_data ['score_log10'],L )
            add_notification ('+1UVt score (dev)',1600 )
            return True 
    if c =='testgrandreset':
        game_data ['PI']=game_data .get ('PI',0 )+1_000_000 
        add_notification ('+1M PI (dev)',1800 );return True 

    if c =='testchallenge1':
        game_data ['PI']+=10 
        add_notification ('Dev: +10 PI',1600 );return True 
    if c =='finishchallenge1':
        start_challenge (1 )
        game_data ['PI']=max (game_data .get ('PI',0 ),1 )
        add_notification ('Dev: Challenge 1 prêt à être complété',1800 );return True 
    if c =='testchallenge2':
        challenge_state ['completed'][0 ]=True 
        game_data ['PI']+=10 
        add_notification ('Dev: C1 marqué comme complété, +10 PI',1800 );return True 
    if c =='finishchallenge2':
        challenge_state ['completed'][0 ]=True 
        start_challenge (2 )
        game_data ['score_log10']=max (game_data .get ('score_log10',NEG_INF ),100.0 )
        add_notification ('Dev: Challenge 2 prêt à être complété',1800 );return True 
    if c =='testchallenge3':
        challenge_state ['completed'][0 ]=True 
        challenge_state ['completed'][1 ]=True 
        game_data ['PI']+=10 
        add_notification ('Dev: C1 & C2 complétés, +10 PI',1800 );return True 
    if c =='finishchallenge3':
        challenge_state ['completed'][0 ]=True 
        challenge_state ['completed'][1 ]=True 
        start_challenge (3 )
        game_data ['PI']=max (game_data .get ('PI',0 ),20_000 )
        add_notification ('Dev: Challenge 3 prêt à être complété',1800 );return True 
    if c =='testchallenge4':
        challenge_state ['completed'][0 ]=True 
        challenge_state ['completed'][1 ]=True 
        challenge_state ['completed'][2 ]=True 
        game_data ['PI']+=10 
        add_notification ('Dev: C1, C2 & C3 complétés, +10 PI',1800 );return True 
    if c =='finishchallenge4':
        challenge_state ['completed'][0 ]=True 
        challenge_state ['completed'][1 ]=True 
        challenge_state ['completed'][2 ]=True 
        start_challenge (4 )
        game_data ['points_log10']['A']=max (game_data ['points_log10']['A'],0.0 )
        add_notification ('Dev: Challenge 4 prêt à être complété',1800 );return True 

    return False 

achievements_unlocked =set ()
selected_ach_category ='score'

def _score_thresholds_log10 ():
    exps =[3 +3 *i for i in range (31 )]
    exps .append (100.0 )
    return exps 

SCORE_THRESH_L =_score_thresholds_log10 ()
AUTO_THRESH_L =list (SCORE_THRESH_L )
CLICKS_THRESH =[1 ,2 ,5 ,10 ,20 ,50 ,100 ,200 ,500 ,1000 ,2000 ,5000 ,10000 ,20000 ,50000 ,100000 ]
GR_THRESH =[1 ,2 ,3 ,5 ,10 ]
ALL_POINTS_EXPS =[3.0 ,6.0 ,9.0 ,12.0 ,15.0 ]

ACH_CATEGORIES ={'score':[],'clicks':[],'reset_points':[],'autoclick':[],'grand_reset':[],'milestones':[]}

def _label_from_L (L ,suffix =''):
    txt =format_from_log10 (L )
    return f"≥ {txt }{suffix }"

for i ,L in enumerate (SCORE_THRESH_L ,1 ):
    ACH_CATEGORIES ['score'].append ({'id':f'score_{i }','name':f'Score — {_label_from_L (L )}','desc':'Atteindre un score maximal donné.','kind':'score','L':L })
for i ,L in enumerate (AUTO_THRESH_L ,1 ):
    ACH_CATEGORIES ['autoclick'].append ({'id':f'auto_{i }','name':f'Auto/s — {_label_from_L (L ,"/s")}','desc':'Atteindre un maximum de score/seconde automatique.','kind':'autoclick','L':L })
for i ,v in enumerate (CLICKS_THRESH ,1 ):
    ACH_CATEGORIES ['clicks'].append ({'id':f'clicks_{i }','name':f'Clicks — {v :,}'.replace (',',' '),'desc':'Clics manuels cumulés.','kind':'clicks','N':v })
firsts =[('R','Renaissance'),('P','Prestige'),('A','Ascension'),('Re','Réincarnation')]
for fam ,label in firsts :
    ACH_CATEGORIES ['reset_points'].append ({'id':f'rp_first_{fam }','name':f'Premier point de {label }','desc':f'Obtenir votre premier point de {label }.','kind':'rp_first','fam':fam })
ACH_CATEGORIES ['reset_points'].append ({'id':'rp_first_PI','name':"Premier point d'Infinité",'desc':'Obtenir votre premier PI.','kind':'rp_first','fam':'PI'})
for exp ,tag in zip (ALL_POINTS_EXPS ,['1K','1M','1B','1T','1Qd']):
    ACH_CATEGORIES ['reset_points'].append ({'id':f'rp_all_{int (exp )}','name':f'≥ {tag } points pour R, P, A, Réinc','desc':'Avoir simultanément au moins ce total pour chaque famille (hors PI).','kind':'rp_all','L':exp })
for v in GR_THRESH :
    ACH_CATEGORIES ['grand_reset'].append ({'id':f'gr_{v }','name':f'Grand Reset — {v }','desc':'Atteindre ce nombre de GR.','kind':'gr','N':v })
for i in range (1 ,21 ):
    ACH_CATEGORIES ['milestones'].append ({'id':f'ms_{i }','name':f"Milestone d'Infinité — M{i }",'desc':'Débloquer cette milestone.','kind':'ms','N':i })

TOTAL_ACHIEVEMENTS =sum (len (v )for v in ACH_CATEGORIES .values ())

def _points_log10 (fam ):
    return game_data .get ('points_log10',{}).get (fam ,NEG_INF )

def _has_first_point (fam ):
    if fam =='PI':
        return game_data .get ('PI',0 )>=1 
    return _points_log10 (fam )>NEG_INF 

def _all_points_at_least (expL ):
    return (_points_log10 ('R')>=expL and _points_log10 ('P')>=expL and _points_log10 ('A')>=expL and _points_log10 ('Re')>=expL )

def update_achievements_v293 ():
    global achievements_unlocked ,mini_notifs 
    newly =0 
    maxL =game_data .get ('max_score_log10',NEG_INF )
    for it in ACH_CATEGORIES ['score']:
        if it ['id']not in achievements_unlocked and maxL >=it ['L']:
            achievements_unlocked .add (it ['id']);newly +=1 
    autoL =game_data .get ('max_auto_sps_log10',NEG_INF )
    for it in ACH_CATEGORIES ['autoclick']:
        if it ['id']not in achievements_unlocked and autoL >=it ['L']:
            achievements_unlocked .add (it ['id']);newly +=1 
    clicks =game_data .get ('total_clicks',0 )
    for it in ACH_CATEGORIES ['clicks']:
        if it ['id']not in achievements_unlocked and clicks >=it ['N']:
            achievements_unlocked .add (it ['id']);newly +=1 
    for it in ACH_CATEGORIES ['reset_points']:
        if it ['id']in achievements_unlocked :continue 
        if it ['kind']=='rp_first':
            if _has_first_point (it ['fam']):
                achievements_unlocked .add (it ['id']);newly +=1 
        elif it ['kind']=='rp_all':
            if _all_points_at_least (it ['L']):
                achievements_unlocked .add (it ['id']);newly +=1 
    grc =gr_count ()
    for it in ACH_CATEGORIES ['grand_reset']:
        if it ['id']not in achievements_unlocked and grc >=it ['N']:
            achievements_unlocked .add (it ['id']);newly +=1 
    ms_count =len (unlocked_pi_milestones ())
    for it in ACH_CATEGORIES ['milestones']:
        if it ['id']not in achievements_unlocked and ms_count >=it ['N']:
            achievements_unlocked .add (it ['id']);newly +=1 
    if newly >0 :
        try :
            mini_notifs ['achievements']=True 
        except Exception :
            pass 
        add_notification (f"Nouveaux succès : +{newly }",2000 )

_ach_cat_btns ={}

_ach_nav_btns ={}
ach_page_index_by_cat ={}

def ensure_achievements_v293_init ():
    global achievements_unlocked ,selected_ach_category ,_ach_cat_btns ,_ach_nav_btns ,ach_page_index_by_cat 
    try :
        achievements_unlocked 
    except NameError :
        achievements_unlocked =set ()
    try :
        selected_ach_category 
    except NameError :
        selected_ach_category ='score'
    try :
        _ach_cat_btns 
    except NameError :
        _ach_cat_btns ={}
    try :
        _ach_nav_btns 
    except NameError :
        _ach_nav_btns ={}
    try :
        ach_page_index_by_cat 
    except NameError :
        ach_page_index_by_cat ={}

def draw_achievements (mouse_pos ,dt ):
    global selected_ach_category 
    bg ,fg ,panel ,bar =theme_colors ()
    screen .fill (bg )
    if game_settings .get ("graphics_mode")=="graphismes_travaillés":
        for sh in floating_shapes :
            sh .update (dt );sh .draw (screen )

    unlocked_cnt =len (achievements_unlocked )
    title =big_font .render (f"Achievements — {unlocked_cnt }/{TOTAL_ACHIEVEMENTS }",True ,fg )
    screen .blit (title ,(WIDTH //2 -title .get_width ()//2 ,40 ))

    cats =[('score','Score'),('clicks','Clicks'),('reset_points','Pts réinit.'),('autoclick','Autoclic'),('grand_reset','Grand Reset'),('milestones','Milestones')]
    _ach_cat_btns .clear ()
    bx ,by =80 ,96 
    bw ,bh ,gap =180 ,40 ,8 
    for key ,label in cats :
        btn =Button ((bx ,by ,bw ,bh ),label ,(220 ,220 ,220 ))
        btn .draw (screen ,mouse_pos )
        if selected_ach_category ==key :
            pygame .draw .rect (screen ,GREEN ,btn .rect ,4 ,border_radius =8 )
        _ach_cat_btns [key ]=btn .rect 
        bx +=bw +gap 

    items =ACH_CATEGORIES .get (selected_ach_category ,[])
    cols =2 
    col_x =[80 ,WIDTH //2 +40 ]
    card_w =WIDTH //2 -140 
    card_h =84 
    gap_y =10 

    top_y =150 
    bottom_reserved =120 
    avail_h =max (0 ,HEIGHT -top_y -bottom_reserved )
    rows_per_col =max (1 ,avail_h //(card_h +gap_y ))
    items_per_page =rows_per_col *cols 

    cur_page =ach_page_index_by_cat .get (selected_ach_category ,0 )
    total_pages =max (1 ,(len (items )+items_per_page -1 )//items_per_page )
    if cur_page >=total_pages :
        cur_page =total_pages -1 
        ach_page_index_by_cat [selected_ach_category ]=cur_page 

    start_idx =cur_page *items_per_page 
    end_idx =min (len (items ),start_idx +items_per_page )
    subset =items [start_idx :end_idx ]

    i =0 
    for it in subset :
        col =i %cols ;row =i //cols 
        x =col_x [col ];y =top_y +row *(card_h +gap_y )
        pygame .draw .rect (screen ,panel ,(x ,y ,card_w ,card_h ),border_radius =10 )
        pygame .draw .rect (screen ,(0 ,0 ,0 ),(x ,y ,card_w ,card_h ),2 ,border_radius =10 )
        name =font .render (it ['name'],True ,fg )
        screen .blit (name ,(x +12 ,y +10 ))
        desc =small_font .render (it .get ('desc',''),True ,DARK_GRAY )
        screen .blit (desc ,(x +12 ,y +42 ))
        ok =it ['id']in achievements_unlocked 
        status =small_font .render ('Débloqué'if ok else 'Verrouillé',True ,(0 ,160 ,60 )if ok else (160 ,0 ,0 ))
        screen .blit (status ,(x +card_w -140 ,y +card_h -28 ))
        i +=1 

    _ach_nav_btns .clear ()
    if total_pages >1 :
        nav_y =HEIGHT -90 
        prev_btn =Button ((WIDTH //2 -220 ,nav_y ,160 ,44 ),'← Précédent',(210 ,210 ,210 ))
        next_btn =Button ((WIDTH //2 +60 ,nav_y ,160 ,44 ),'Suivant →',(210 ,210 ,210 ))
        prev_btn .draw (screen ,mouse_pos )
        next_btn .draw (screen ,mouse_pos )
        if cur_page <=0 :
            draw_button_disabled (screen ,prev_btn )
        if cur_page >=total_pages -1 :
            draw_button_disabled (screen ,next_btn )
        _ach_nav_btns ['prev']=prev_btn .rect 
        _ach_nav_btns ['next']=next_btn .rect 
        pi =small_font .render (f"Page {cur_page +1 }/{total_pages }",True ,fg )
        screen .blit (pi ,(WIDTH //2 -pi .get_width ()//2 ,nav_y -28 ))

    back_button .draw (screen ,mouse_pos )

    draw_modal_popups (mouse_pos )


    overlays_open =(
    quit_confirm .get ("open",False )or 
    gr_confirm .get ("open",False )or 
    reset_confirm .get ("open",False )or 
    reset_flow .get ("state",0 )!=0 or 
    reset_flow .get ("in_progress",False )or 
    dev_password_mode or 
    (code_input_mode is not None )
    )
    if not overlays_open :
        draw_version_badge_bottom_right_above_fps ()
        draw_fps_badge ()

def draw_captcha (mouse_pos ,dt ):
    bg ,fg ,panel ,bar =theme_colors ()
    screen .fill (bg )
    if game_settings .get ("graphics_mode")=="graphismes_travaillés":
        for sh in floating_shapes :
            sh .update (dt );sh .draw (screen )
    title =big_font .render ("Vérification anti-robot",True ,fg )
    screen .blit (title ,(WIDTH //2 -title .get_width ()//2 ,140 ))
    sub =secondary_font .render ("Répondez Vrai ou Faux. Vous avez 3 tentatives.",True ,DARK_GRAY )
    screen .blit (sub ,(WIDTH //2 -sub .get_width ()//2 ,180 ))
    qa =CAPTCHA_QA [captcha_question_index ]
    q_text =qa ["q"]
    lines =[]
    words =q_text .split (" ")
    cur =""
    for w in words :
        test =(cur +" "+w ).strip ()
        surf =font .render (test ,True ,fg )
        if surf .get_width ()>WIDTH -240 and cur :
            lines .append (cur )
            cur =w 
        else :
            cur =test 
    if cur :lines .append (cur )
    yq =240 
    for ln in lines :
        t =font .render (ln ,True ,fg )
        screen .blit (t ,(WIDTH //2 -t .get_width ()//2 ,yq ));yq +=36 
    att =font .render (f"Tentatives restantes : {captcha_attempts_left }",True ,(120 ,0 ,0 )if captcha_attempts_left <=1 else DARK_GRAY )
    screen .blit (att ,(WIDTH //2 -att .get_width ()//2 ,yq +10 ))
    captcha_true_button .draw (screen ,mouse_pos )
    captcha_false_button .draw (screen ,mouse_pos )
    draw_modal_popups (mouse_pos )

def theme_colors ():
    if game_settings .get ("theme","clair")=="sombre":
        return (18 ,18 ,22 ),(235 ,235 ,240 ),(30 ,30 ,36 ),(60 ,60 ,70 )
    return WHITE ,BLACK ,PANEL_LIGHT ,BAR_BG 

LEFT_X =120 
RIGHT_X =WIDTH //2 +40 
COL_W =WIDTH //2 -160 
ROW_H =56 
PANEL_Y =220 
PANEL_H =420 
BTN_W =120 
BTN_GAP =20 

settings_buttons ={
"graphics_mode":{
"performance":Button ((LEFT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +10 ,BTN_W ,ROW_H ),"Perf",GRAY ),
"graphismes":Button ((LEFT_X +COL_W -BTN_W ,PANEL_Y +10 ,BTN_W ,ROW_H ),"Graph",GRAY ),
},
"purchase_mode":{
"single":Button ((LEFT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +90 ,BTN_W ,ROW_H ),"Single",GRAY ),
"multi":Button ((LEFT_X +COL_W -BTN_W ,PANEL_Y +90 ,BTN_W ,ROW_H ),"Multi",GRAY ),
},
"theme":{
"clair":Button ((LEFT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +170 ,BTN_W ,ROW_H ),"Clair",GRAY ),
"sombre":Button ((LEFT_X +COL_W -BTN_W ,PANEL_Y +170 ,BTN_W ,ROW_H ),"Sombre",GRAY ),
},
"global_progress":{
"off":Button ((0 ,0 ,BTN_W ,ROW_H ),"Off",GRAY ),
"on":Button ((0 ,0 ,BTN_W ,ROW_H ),"On",GRAY ),
},
"mini_autoclicker":{
"off":Button ((RIGHT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +80 ,BTN_W ,ROW_H ),"Off",GRAY ),
"on":Button ((RIGHT_X +COL_W -BTN_W ,PANEL_Y +80 ,BTN_W ,ROW_H ),"On",GRAY ),
},
"auto_buyers":{
"off":Button ((RIGHT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +160 ,BTN_W ,ROW_H ),"Off",GRAY ),
"on":Button ((RIGHT_X +COL_W -BTN_W ,PANEL_Y +160 ,BTN_W ,ROW_H ),"On",GRAY ),
},
"auto_rebirth":{
"off":Button ((RIGHT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +240 ,BTN_W ,ROW_H ),"Off",GRAY ),
"on":Button ((RIGHT_X +COL_W -BTN_W ,PANEL_Y +240 ,BTN_W ,ROW_H ),"On",GRAY ),
},
"mini_notifications":{
"off":Button ((RIGHT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +240 ,BTN_W ,ROW_H ),"Off",GRAY ),
"on":Button ((RIGHT_X +COL_W -BTN_W ,PANEL_Y +240 ,BTN_W ,ROW_H ),"On",GRAY ),
},
"ingame_notifications":{
"off":Button ((RIGHT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +320 ,BTN_W ,ROW_H ),"Off",GRAY ),
"on":Button ((RIGHT_X +COL_W -BTN_W ,PANEL_Y +320 ,BTN_W ,ROW_H ),"On",GRAY ),
},
"show_reset_points":{
"off":Button ((RIGHT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +240 ,BTN_W ,ROW_H ),"Off",GRAY ),
"on":Button ((RIGHT_X +COL_W -BTN_W ,PANEL_Y +240 ,BTN_W ,ROW_H ),"On",GRAY ),
},
"show_reset_boosts":{
"off":Button ((RIGHT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +300 ,BTN_W ,ROW_H ),"Off",GRAY ),
"on":Button ((RIGHT_X +COL_W -BTN_W ,PANEL_Y +300 ,BTN_W ,ROW_H ),"On",GRAY ),
},
"show_tooltips_on_hover":{
"off":Button ((RIGHT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +360 ,BTN_W ,ROW_H ),"Off",GRAY ),
"on":Button ((RIGHT_X +COL_W -BTN_W ,PANEL_Y +360 ,BTN_W ,ROW_H ),"On",GRAY ),
},
"confirm_resets":{
"off":Button ((RIGHT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +420 ,BTN_W ,ROW_H ),"Off",GRAY ),
"on":Button ((RIGHT_X +COL_W -BTN_W ,PANEL_Y +420 ,BTN_W ,ROW_H ),"On",GRAY ),
},}

_chal_btn_rects ={}

def draw_milestones (mouse_pos ,dt ):
    """v30.0.1 — Milestones : pagination + tooltips au premier plan (sans décalage)."""
    global _milestones_page ,_milestones_nav 
    bg ,fg ,panel ,bar =theme_colors ()
    screen .fill (bg )

    if game_settings .get ("graphics_mode")=="graphismes_travaillés":
        for sh in floating_shapes :
            sh .update (dt )
            sh .draw (screen )

    title =big_font .render ("Milestones d'Infinité (PI)",True ,fg )
    screen .blit (title ,(WIDTH //2 -title .get_width ()//2 ,60 ))

    page =max (0 ,min (1 ,_milestones_page ))
    start_idx =page *10 
    end_idx =min (len (PI_M_THRESH ),start_idx +10 )

    tip_lines =None 
    tip_pos =None 

    y =140 
    row_h =64 
    for idx in range (start_idx ,end_idx ):
        m_idx =idx +1 

        thr =PI_M_THRESH [idx ]
        name ,desc =PI_M_LABELS [idx ]
        unlocked =game_data .get ("PI",0 )>=thr 

        row_rect =pygame .Rect (80 ,y ,WIDTH -160 ,row_h )

        pygame .draw .rect (screen ,panel ,row_rect ,border_radius =10 )
        pygame .draw .rect (screen ,(0 ,180 ,80 )if unlocked else (0 ,0 ,0 ),row_rect ,2 ,border_radius =10 )

        txt =font .render (f"{name } — {thr :,} PI".replace (","," "),True ,fg )
        screen .blit (txt ,(row_rect .x +20 ,row_rect .y +8 ))

        d =small_font .render (desc ,True ,(0 ,120 ,50 )if unlocked else DARK_GRAY )
        screen .blit (d ,(row_rect .x +20 ,row_rect .y +34 ))

        status =small_font .render ("Débloqué"if unlocked else "Verrouillé",
        True ,(0 ,160 ,60 )if unlocked else (160 ,0 ,0 ))
        screen .blit (status ,(row_rect .right -180 ,row_rect .y +20 ))

        if row_rect .collidepoint (mouse_pos ):

            if "milestone_tooltip_lines"in globals ()and callable (milestone_tooltip_lines ):
                tip_lines =milestone_tooltip_lines (m_idx )
            else :

                tip_lines =[
                f"{name }",
                f"Seuil : {thr :,} PI".replace (","," "),
                "État : "+("Débloquée ✅"if unlocked else "Verrouillée 🔒"),
                ]
            tip_pos =mouse_pos 

        y +=row_h +10 

    _milestones_nav ={"prev":None ,"next":None }
    nav_y =HEIGHT -90 

    prev_btn =Button ((WIDTH //2 -220 ,nav_y ,160 ,44 ),"← Page 1",(210 ,210 ,210 ))
    next_btn =Button ((WIDTH //2 +60 ,nav_y ,160 ,44 ),"Page 2 →",(210 ,210 ,210 ))
    prev_btn .draw (screen ,mouse_pos )
    next_btn .draw (screen ,mouse_pos )

    if page ==0 :
        draw_button_disabled (screen ,prev_btn )
    if page ==1 :
        draw_button_disabled (screen ,next_btn )

    _milestones_nav ["prev"]=prev_btn .rect 
    _milestones_nav ["next"]=next_btn .rect 

    pi =small_font .render (f"Page {page +1 }/2",True ,fg )
    screen .blit (pi ,(WIDTH //2 -pi .get_width ()//2 ,nav_y -28 ))

    back_button .draw (screen ,mouse_pos )
    try :

        draw_interactive_tip_if_any (mouse_pos ,context ='milestones')
    except Exception :
        pass 

    if tip_lines :
        draw_tooltip (screen ,tip_lines ,tip_pos )

    draw_modal_popups (mouse_pos )

def draw_points_panel_top_right ():
    return 0 

def draw_difficulty_select (mouse_pos ,dt ):
    """v30.1 — Sélection de difficulté verticale + description à côté de chaque bouton."""
    global _diff_btn_rects 
    bg ,fg ,panel ,bar =theme_colors ()
    screen .fill (bg )

    if game_settings .get ("graphics_mode")=="graphismes_travaillés":
        for sh in floating_shapes :
            sh .update (dt );sh .draw (screen )

    title =big_font .render ("Choisissez la difficulté",True ,fg )
    screen .blit (title ,(WIDTH //2 -title .get_width ()//2 ,80 ))
    info =small_font .render (
    "Le choix est définitif jusqu'à la relance du jeu.",
    True ,DARK_GRAY 
    )
    screen .blit (info ,(WIDTH //2 -info .get_width ()//2 ,118 ))

    entries =[
    (DIFF_VERY_EASY ,"Très Facile",BLUE ,WHITE ),
    (DIFF_EASY ,"Facile",GREEN ,WHITE ),
    (DIFF_NORMAL ,"Normal",YELLOW ,BLACK ),
    (DIFF_HARD ,"Difficile",RED ,WHITE ),
    (DIFF_IMPOSSIBLE ,"Impossible",DARK_RED ,WHITE ),
    ]

    desc_by_diff ={
    DIFF_VERY_EASY :[
    "Buffs challenges actifs",
    "GR : M20 requis, coût de base 1M PI (prix ×10 par GR)",
    "Score ×5, R/P/A/Re ×2, PI ×1.5",
    "GR score: ^3 (+0.2/GR), Points ×1K/GR, PI ×3^g",
    ],
    DIFF_EASY :[
    "C1 & C2 complétés d'emblée",
    "Score ×3, R/P/A/Re ×1.5, PI ×1.25",
    "GR: standard",
    ],
    DIFF_NORMAL :[
    "Jeu inchangé",
    ],
    DIFF_HARD :[
    "Score ÷1.25, R/P/A/Re ÷1.5, PI ÷1.25",
    "GR: standard",
    ],
    DIFF_IMPOSSIBLE :[
    "Score ÷2, R/P/A/Re ÷2, PI ÷1.5",
    "GR score: ^1.1 (+0.01/GR), Points ×5/GR, PI ×1.1^g",
    ],
    }

    _diff_btn_rects .clear ()
    left_margin =140 
    top_y =170 
    btn_w ,btn_h =420 ,56 
    gap_block =16 
    right_gap =20 
    max_right_w =WIDTH -(left_margin +btn_w +right_gap )-100 

    y =top_y 
    for key ,label ,bgc ,txtc in entries :

        btn_rect =pygame .Rect (left_margin ,y ,btn_w ,btn_h )
        btn =Button (btn_rect ,label ,bgc ,txtc )
        btn .draw (screen ,mouse_pos )
        _diff_btn_rects [key ]=btn_rect 

        lines =desc_by_diff .get (key ,[])

        line_h =small_font .get_height ()
        text_block_h =len (lines )*line_h +max (0 ,(len (lines )-1 ))*2 
        text_x =btn_rect .right +right_gap 
        text_y =btn_rect .y +(btn_rect .height -text_block_h )//2 

        text_w =0 
        for ln in lines :
            w =small_font .size (ln )[0 ]
            text_w =max (text_w ,w )
        text_w =min (text_w ,max_right_w )
        pad =10 
        panel_rect =pygame .Rect (text_x -pad ,text_y -pad ,text_w +pad *2 ,text_block_h +pad *2 )
        pygame .draw .rect (screen ,panel ,panel_rect ,border_radius =10 )
        pygame .draw .rect (screen ,(0 ,0 ,0 ),panel_rect ,2 ,border_radius =10 )

        ty =text_y 
        for ln in lines :

            ts =small_font .render (ln ,True ,fg )
            screen .blit (ts ,(text_x ,ty ))
            ty +=line_h +2 

        block_h =max (btn_h ,text_block_h +pad *2 )
        y +=block_h +gap_block 

    hint =small_font .render ("Astuce: vous pouvez survoler chaque bouton pour relire les effets dans le panneau.",True ,DARK_GRAY )
    screen .blit (hint ,(left_margin ,min (y +10 ,HEIGHT -60 )))
    draw_modal_popups (mouse_pos )

def draw_version_popup (mouse_pos ):
    bg ,fg ,panel ,bar =theme_colors ()
    overlay =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
    overlay .fill ((0 ,0 ,0 ,160 ))
    screen .blit (overlay ,(0 ,0 ))


    title =big_font .render (f"Dernière version — {CURRENT_VERSION }",True ,fg )

    lines =[
    f"Nouveautés et corrections — Version {CURRENT_VERSION }:",
    "- Passage de la version en 1.14.2.",
    "- Ajout de la catégorie Paramètres : Fonctionnalités BETA (vide pour le moment).",
    "- Réinitialisation des données : affichage d'un pourcentage pendant le traitement.",
    "- Amélioration de l'écran d'erreur : gel visuel + type d'erreur + code d'erreur.",
    "- Mode développeur : ajout d'une catégorie Tests (test écran d'erreur).",
    "- Taille de la fenêtre : auto-adaptation à la taille de l'écran.",
    "- Agrandissement automatique de la popup changelog pour mieux utiliser l'espace horizontal.",
    "- Correction du scroll dans la popup changelog (molette désormais prise en charge).",
    "- Mise à jour du contenu du changelog avec les modifications de la version.",
    "- Diverses améliorations UI et corrections mineures.",
    "",
    "Merci de jouer à Idle Clicker !",
    ]


    rect ,wrapped ,text_w ,text_h ,viewport_needed =compute_popup_rect_for_content (
    title ,lines ,secondary_font ,WIDTH ,HEIGHT 
    )


    pygame .draw .rect (screen ,(245 ,245 ,245 ),rect ,border_radius =12 )
    pygame .draw .rect (screen ,(0 ,0 ,0 ),rect ,3 ,border_radius =12 )


    screen .blit (title ,(rect .x +rect .w //2 -title .get_width ()//2 ,rect .y +POPUP_PADDING ))


    text_area_x =rect .x +POPUP_PADDING 
    text_area_y =rect .y +POPUP_PADDING +title .get_height ()+POPUP_TITLE_SPACING 
    text_area_w =rect .w -POPUP_PADDING *2 

    available_h =rect .h -(text_area_y -rect .y )-POPUP_TITLE_SPACING -POPUP_BTN_H -POPUP_PADDING 

    if viewport_needed :

        viewport =pygame .Surface ((text_area_w ,available_h ),pygame .SRCALPHA )
        viewport .fill ((0 ,0 ,0 ,0 ))

        scroll_px =max (0 ,globals ().get ('version_popup_scroll',0 ))

        max_scroll =max (0 ,text_h -available_h )

        scroll_px =max (0 ,min (scroll_px ,max_scroll ))
        globals ()['version_popup_scroll']=scroll_px 


        ycur =-scroll_px 
        for ln in wrapped :
            surf =secondary_font .render (ln ,True ,fg )
            viewport .blit (surf ,(0 ,ycur ))
            ycur +=surf .get_height ()+POPUP_LINE_SPACING 


        screen .blit (viewport ,(text_area_x ,text_area_y ))


        if max_scroll >0 :
            bar_w =6 
            track_x =rect .x +rect .w -POPUP_PADDING -bar_w 
            track_y =text_area_y 
            track_h =available_h 
            pygame .draw .rect (screen ,(220 ,220 ,220 ),(track_x ,track_y ,bar_w ,track_h ),border_radius =3 )

            knob_h =max (32 ,int (track_h *(available_h /(text_h +1 ))))
            knob_y =track_y +int ((track_h -knob_h )*(scroll_px /max_scroll ))
            pygame .draw .rect (screen ,(120 ,120 ,120 ),(track_x ,knob_y ,bar_w ,knob_h ),border_radius =3 )
    else :

        ycur =text_area_y 
        for ln in wrapped :
            surf =secondary_font .render (ln ,True ,fg )
            screen .blit (surf ,(text_area_x ,ycur ))
            ycur +=surf .get_height ()+POPUP_LINE_SPACING 


    ok_btn_rect =pygame .Rect (rect .x +rect .w //2 -POPUP_BTN_W //2 ,
    rect .y +rect .h -POPUP_PADDING -POPUP_BTN_H ,
    POPUP_BTN_W ,POPUP_BTN_H )
    Button (ok_btn_rect ,"OK",(90 ,200 ,120 ),WHITE ).draw (screen ,mouse_pos )
    globals ()['_version_popup_ok_btn_rect']=ok_btn_rect 


tutorial_active =False 
tutorial_mode =None 
tutorial_step =0 

tutorial_auto_advance =False 

TUTO_CHOICE_STATIC_BTN =Button ((WIDTH //2 -360 ,180 ,320 ,64 ),"Tutoriel statique",(110 ,170 ,110 ),WHITE )
TUTO_CHOICE_INTER_BTN =Button ((WIDTH //2 +40 ,180 ,320 ,64 ),"Tutoriel interactif",(110 ,140 ,210 ),WHITE )

TUTO_START_AUTO_BTN =Button ((WIDTH //2 -320 ,240 ,280 ,56 ),"Lancer (Auto)",(90 ,200 ,120 ),WHITE )
TUTO_START_MANUAL_BTN =Button ((WIDTH //2 +40 ,240 ,280 ,56 ),"Lancer (Manuel)",(90 ,140 ,210 ),WHITE )

TUTO_BACK_MENU_BTN =Button ((80 ,HEIGHT -70 ,280 ,48 ),"Retour au menu principal",GRAY )
TUTO_BACK_CHOICE_BTN =Button ((380 ,HEIGHT -70 ,360 ,48 ),"Retour au choix du type de tutoriel",GRAY )

_tut_prev_rect =None 
_tut_next_rect =None 
_tut_skip_rect =None 

visited_achievements =False 
visited_settings =False 
visited_history =False 
visited_tutorial =False 
visited_milestones =False 
visited_menu =False 
visited_play =False 
clicks_done =0 
click_upgrades =0 
auto_upgrades =0 
mult_upgrades =0 
score_reached_100 =False 
score_reached_1000 =False 
renaissance_done =False 

TUTORIAL_TEXT ={
1 :"Étape 1/19 · Ouvrir Achievements",
2 :"Étape 2/19 · Ouvrir Paramètres",
3 :"Étape 3/19 · Ouvrir Statistiques",
4 :"Étape 4/19 · Ouvrir l'onglet Tutoriel",
5 :"Étape 5/19 · Ouvrir Milestones (PI)",
6 :"Étape 6/19 · Revenir au menu principal",
7 :"Étape 7/19 · Cliquer sur 'Jouer'",
8 :"Étape 8/19 · Cliquer sur CLICK ×10",
9 :"Étape 9/19 · Acheter Clic (+0.75)",
10 :"Étape 10/19 · Acheter Clic à nouveau",
11 :"Étape 11/19 · Acheter Auto (+1/s)",
12 :"Étape 12/19 · Acheter Auto à nouveau",
13 :"Étape 13/19 · Acheter Auto à nouveau",
14 :"Étape 14/19 · Acheter Mult (x1.15)",
15 :"Étape 15/19 · Acheter Mult à nouveau",
16 :"Étape 16/19 · Atteindre 100 de score",
17 :"Étape 17/19 · Atteindre 1 000 de score",
18 :"Étape 18/19 · Lancer Renaissance",
19 :"Étape 19/19 · Cliquez sur 'Terminer le tutoriel' pour recevoir une compensation vers 10 points de Renaissance au total",
}
TUTORIAL_LAST_STEP =max (TUTORIAL_TEXT .keys ())
TUTOR_CLICKS_TARGET =10 

def start_interactive_tutorial (auto :bool ):
    global tutorial_auto_advance 
    tutorial_auto_advance =bool (auto )
    reset_interactive_tutorial ()

def reset_interactive_tutorial ():
    global tutorial_active ,tutorial_mode ,tutorial_step 
    global visited_achievements ,visited_settings ,visited_history ,visited_tutorial ,visited_milestones ,visited_menu ,visited_play 
    global clicks_done ,click_upgrades ,auto_upgrades ,mult_upgrades ,score_reached_100 ,score_reached_1000 ,renaissance_done 
    tutorial_active =True 
    tutorial_mode ='interactive'
    tutorial_step =1 
    visited_achievements =visited_settings =visited_history =False 
    visited_tutorial =visited_milestones =visited_menu =visited_play =False 
    clicks_done =0 
    click_upgrades =0 
    auto_upgrades =0 
    mult_upgrades =0 
    score_reached_100 =False 
    score_reached_1000 =False 
    renaissance_done =False 

def is_step_condition_met (step :int )->bool :
    if step ==1 :return visited_achievements 
    if step ==2 :return visited_settings 
    if step ==3 :return visited_history 
    if step ==4 :return visited_tutorial 
    if step ==5 :return visited_milestones 
    if step ==6 :return visited_menu 
    if step ==7 :return visited_play 
    if step ==8 :return clicks_done >=TUTOR_CLICKS_TARGET 
    if step ==9 :return click_upgrades >=1 
    if step ==10 :return click_upgrades >=2 
    if step ==11 :return auto_upgrades >=1 
    if step ==12 :return auto_upgrades >=2 
    if step ==13 :return auto_upgrades >=3 
    if step ==14 :return mult_upgrades >=1 
    if step ==15 :return mult_upgrades >=2 
    if step ==16 :return score_reached_100 
    if step ==17 :return score_reached_1000 
    if step ==18 :return renaissance_done 
    if step ==19 :return True 
    return False 

def draw_interactive_tip_if_any (mouse_pos ,context :str ,sy_after_stats :int =0 ):
    global _tut_prev_rect ,_tut_next_rect ,_tut_skip_rect 
    if not (tutorial_active and tutorial_mode =='interactive'and 1 <=tutorial_step <=TUTORIAL_LAST_STEP ):
        _tut_prev_rect =_tut_next_rect =_tut_skip_rect =None 
        return 
    text =TUTORIAL_TEXT .get (tutorial_step ,f"Étape {tutorial_step }")
    if context =='main':
        panel_w ,panel_h =800 ,120 
        px ,py =40 ,max (sy_after_stats +12 ,340 )
    else :
        panel_w ,panel_h =980 ,110 
        px ,py =WIDTH //2 -panel_w //2 ,HEIGHT -160 
    pygame .draw .rect (screen ,(255 ,255 ,255 ),(px ,py ,panel_w ,panel_h ),border_radius =12 )
    pygame .draw .rect (screen ,(0 ,0 ,0 ),(px ,py ,panel_w ,panel_h ),2 ,border_radius =12 )
    ts =secondary_font .render (text ,True ,(0 ,0 ,0 ))
    screen .blit (ts ,(px +16 ,py +14 ))
    btn_w ,btn_h =180 ,44 
    prev_rect =pygame .Rect (px +16 ,py +panel_h -btn_h -14 ,btn_w ,btn_h )
    skip_rect =pygame .Rect (px +panel_w //2 -90 ,py +panel_h -btn_h -14 ,180 ,btn_h )
    next_rect =pygame .Rect (px +panel_w -btn_w -16 ,py +panel_h -btn_h -14 ,btn_w ,btn_h )
    prev_btn =Button (prev_rect ,"Étape précédente",GRAY )
    skip_btn =Button (skip_rect ,"Passer le tutoriel",(220 ,120 ,120 ),WHITE )
    next_label ="Terminer le tutoriel"if tutorial_step ==TUTORIAL_LAST_STEP else "Étape suivante"
    next_btn =Button (next_rect ,next_label ,(90 ,200 ,120 ),WHITE )
    prev_btn .draw (screen ,mouse_pos )
    skip_btn .draw (screen ,mouse_pos )
    next_btn .draw (screen ,mouse_pos )
    if tutorial_step <=1 :
        draw_button_disabled (screen ,prev_btn )
    if tutorial_step !=TUTORIAL_LAST_STEP and not is_step_condition_met (tutorial_step ):
        draw_button_disabled (screen ,next_btn )
    _tut_prev_rect =prev_rect 
    _tut_next_rect =next_rect 
    _tut_skip_rect =skip_rect 

def draw_main_menu (mouse_pos ,dt ):
    bg ,fg ,panel ,bar =theme_colors ()
    screen .fill (bg )
    if game_settings ["graphics_mode"]=="graphismes_travaillés":
        for sh in floating_shapes :
            sh .update (dt );sh .draw (screen )
    title =big_font .render (f"Idle Clicker Version {CURRENT_VERSION }",True ,fg )
    screen .blit (title ,(WIDTH //2 -title .get_width ()//2 ,120 ))
    for key ,b in menu_buttons .items ():
        b .draw (screen ,mouse_pos )
        if game_settings .get ("mini_notifications",True )and key in mini_notifs and mini_notifs .get (key ,False ):
            draw_mini_badge (screen ,b .rect )
    draw_interactive_tip_if_any (mouse_pos ,context ='menu')

    global _welcome_fired ,_version_popup_fired ,show_version_popup 

    if not _welcome_fired and not welcome_popup .get ("already_shown",False ):
        welcome_popup ["open"]=True 
        welcome_popup ["already_shown"]=True 
        _welcome_fired =True 

    if not _version_popup_fired and not welcome_popup .get ("open",False ):
        show_version_popup =True 
        _version_popup_fired =True 


    draw_welcome_popup (mouse_pos )
    draw_modal_popups (mouse_pos )

    draw_quit_confirm_overlay (mouse_pos )
    draw_version_badge_bottom_right_above_fps ()
    draw_fps_badge ()

def _draw_progress_bar (x ,y ,w ,h ,ratio ,color =(100 ,200 ,255 )):
    ratio =max (0.0 ,min (1.0 ,ratio ))
    pygame .draw .rect (screen ,BAR_BG ,(x ,y ,w ,h ),border_radius =5 )
    fillw =int (w *ratio )
    pygame .draw .rect (screen ,color ,(x ,y ,fillw ,h ),border_radius =5 )
    pygame .draw .rect (screen ,(0 ,0 ,0 ),(x ,y ,w ,h ),2 ,border_radius =5 )

def human_time (seconds :float )->str :
    s =int (seconds )
    h =s //3600 ;m =(s %3600 )//60 ;sec =s %60 
    if h >0 :return f"{h }h {m }m {sec }s"
    if m >0 :return f"{m }m {sec }s"
    return f"{sec }s"

def _draw_setting_label_aligned (text ,target_rect ):
    bg ,fg ,panel ,bar =theme_colors ()
    t =font .render (text ,True ,fg )
    ty =target_rect .centery -t .get_height ()//2 
    screen .blit (t ,(LEFT_X ,ty ))

def _draw_settings_group_buttons (group ,surface ,mouse_pos ):
    for btn in group .values ():
        btn .draw (surface ,mouse_pos )

def draw_settings (mouse_pos ,dt ):
    global settings_tab ,_settings_hub_rects 
    bg ,fg ,panel ,bar =theme_colors ()
    screen .fill (bg )
    if game_settings ["graphics_mode"]=="graphismes_travaillés":
        for sh in floating_shapes :
            sh .update (dt );sh .draw (screen )

    subtitle =SETTINGS_SUBTITLES .get (settings_tab ,"Paramètres")
    title =big_font .render (subtitle ,True ,fg )
    screen .blit (title ,(WIDTH //2 -title .get_width ()//2 ,60 ))


    def _highlight_btn (btn ):
        try :
            s =pygame .Surface ((btn .rect .width ,btn .rect .height ),pygame .SRCALPHA )
            s .fill ((80 ,200 ,120 ,44 ))
            screen .blit (s ,btn .rect .topleft )
            pygame .draw .rect (screen ,GREEN ,btn .rect ,3 ,border_radius =8 )
        except Exception :
            pygame .draw .rect (screen ,GREEN ,btn .rect ,3 ,border_radius =8 )

    def _draw_panel (rect :pygame .Rect ,title :str |None =None ,accent :tuple [int ,int ,int ]|None =None ):
        """Draw the original simple panel: background + border (no shadow/header)."""
        try :

            pygame .draw .rect (screen ,panel ,rect ,border_radius =12 )
            pygame .draw .rect (screen ,(0 ,0 ,0 ),rect ,2 ,border_radius =12 )

        except Exception :
            try :
                pygame .draw .rect (screen ,(245 ,245 ,245 ),rect )
            except Exception :
                pass 

    if settings_tab is None :
        _settings_hub_rects ={}
        info =secondary_font .render ("Choisissez une catégorie :",True ,fg )
        info_y =60 +title .get_height ()+16 
        screen .blit (info ,(WIDTH //2 -info .get_width ()//2 ,info_y ))

        btn_w ,btn_h =520 ,92 
        gap_x ,gap_y =36 ,28 
        start_x =WIDTH //2 -(btn_w +gap_x //2 )
        start_y =180 


        try :
            dev_label =("Commandes développeur"if developer_mode_active else "Mode développeur")
        except Exception :
            dev_label ="Mode développeur"

        labels =[
        ("general","Paramètres généraux"),
        ("automation","Automatisation"),
        ("display","Affichage"),
        ("dev",dev_label ),
        ("beta","Fonctionnalités BETA"),
        ("about","À propos"),
        ("rules","Règles et fonctionnement"),
        ]

        def grid_positions (count ,cols ,start_x ,start_y ,btn_w ,btn_h ,gap_x ,gap_y ):
            positions =[]
            for idx in range (count ):
                col =idx %cols 
                row =idx //cols 
                x =start_x +col *(btn_w +gap_x )
                y =start_y +row *(btn_h +gap_y )
                positions .append ((x ,y ))
            return positions 

        positions =grid_positions (len (labels ),2 ,start_x ,start_y ,btn_w ,btn_h ,gap_x ,gap_y )
        palette =[(120 ,180 ,255 ),(180 ,220 ,140 ),(255 ,200 ,140 ),(200 ,160 ,255 ),(255 ,160 ,180 ),(200 ,200 ,240 )]
        for i ,((key ,txt ),(x ,y ))in enumerate (zip (labels ,positions )):

            card_color =tuple (min (255 ,c +18 )for c in palette [i %len (palette )])
            pygame .draw .rect (screen ,card_color ,(x -6 ,y -6 ,btn_w +12 ,btn_h +12 ),border_radius =12 )
            acc_rect =pygame .Rect (x -6 ,y -6 ,12 ,btn_h +12 )
            pygame .draw .rect (screen ,palette [i %len (palette )],acc_rect ,border_radius =8 )

            b =Button ((x ,y ,btn_w ,btn_h ),txt ,(245 ,245 ,250 ),(30 ,30 ,30 ))
            b .draw (screen ,mouse_pos )

            try :
                pygame .draw .circle (screen ,palette [i %len (palette )],(x +36 ,y +btn_h //2 ),18 )
            except Exception :
                pass 


            _settings_hub_rects [key ]=b .rect 


        try :
            SETTINGS_BACK_MENU_BTN .draw (screen ,mouse_pos )
        except Exception :
            pass 

        return 

    if settings_tab =='beta':
        bg ,fg ,panel ,bar =theme_colors ()
        screen .fill (bg )
        if game_settings .get ('graphics_mode')=='graphismes_travaillés':
            for sh in floating_shapes :
                sh .update (dt );sh .draw (screen )
        title =big_font .render ('Fonctionnalités BETA',True ,fg )
        screen .blit (title ,(WIDTH //2 -title .get_width ()//2 ,120 ))
        msg =secondary_font .render ("Aucune fonctionnalité BETA n'est disponible pour le moment",True ,(60 ,60 ,60 ))
        screen .blit (msg ,(WIDTH //2 -msg .get_width ()//2 ,190 ))
        SETTINGS_BACK_HUB_BTN .draw (screen ,mouse_pos )
        SETTINGS_BACK_MENU_BTN .draw (screen ,mouse_pos )
        return 

    draw_panels =(settings_tab =='general')
    if draw_panels :
        left_rect =pygame .Rect (LEFT_X -30 ,PANEL_Y ,COL_W +60 ,PANEL_H )
        right_rect =pygame .Rect (RIGHT_X -30 ,PANEL_Y ,COL_W +60 ,PANEL_H )
        _draw_panel (left_rect ,title ="Paramètres")
        _draw_panel (right_rect ,title ="Options")
        settings_buttons ["graphics_mode"]["graphismes"].rect .topleft =(LEFT_X +COL_W -BTN_W ,PANEL_Y +10 )
        _draw_settings_group_buttons (settings_buttons ["graphics_mode"],screen ,mouse_pos )
        _draw_setting_label_aligned ("Mode d'affichage",settings_buttons ["graphics_mode"]["graphismes"].rect )
        hint =small_font .render ("Performance / Graphismes",True ,DARK_GRAY )
        screen .blit (hint ,(LEFT_X ,settings_buttons ["graphics_mode"]["graphismes"].rect .bottom +4 ))


        gm =game_settings .get ("graphics_mode")
        hi_btn ="performance"if gm =="performance"else "graphismes"
        if gm =="graphismes_travaillés":
            hi_btn ="graphismes"
        _highlight_btn (settings_buttons ["graphics_mode"][hi_btn ])
        _draw_settings_group_buttons (settings_buttons ["purchase_mode"],screen ,mouse_pos )
        _draw_setting_label_aligned ("Mode d'achat",settings_buttons ["purchase_mode"]["multi"].rect )
        hint =small_font .render ("Single / Multi",True ,DARK_GRAY )
        screen .blit (hint ,(LEFT_X ,settings_buttons ["purchase_mode"]["multi"].rect .bottom +4 ))
        hi_btn =game_settings .get ("purchase_mode","single")
        _highlight_btn (settings_buttons ["purchase_mode"][hi_btn ])

        settings_buttons ["theme"]["clair"].rect .topleft =(LEFT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +170 )
        settings_buttons ["theme"]["sombre"].rect .topleft =(LEFT_X +COL_W -BTN_W ,PANEL_Y +170 )
        _draw_settings_group_buttons (settings_buttons ["theme"],screen ,mouse_pos )
        _draw_setting_label_aligned ("Thème",settings_buttons ["theme"]["sombre"].rect )
        hint =small_font .render ("Clair / Sombre",True ,DARK_GRAY )
        screen .blit (hint ,(LEFT_X ,settings_buttons ["theme"]["sombre"].rect .bottom +4 ))
        hi_btn =game_settings .get ("theme","clair")
        _highlight_btn (settings_buttons ["theme"][hi_btn ])
        settings_buttons ["theme"]["sombre"].rect .topleft =(LEFT_X +COL_W -BTN_W ,PANEL_Y +170 )
        for btn in settings_buttons ["theme"].values ():btn .draw (screen ,mouse_pos )
        _draw_setting_label_aligned ("Thème",settings_buttons ["theme"]["sombre"].rect )
        hint =small_font .render ("Clair / Sombre",True ,DARK_GRAY )
        screen .blit (hint ,(LEFT_X ,settings_buttons ["theme"]["sombre"].rect .bottom +4 ))
        hi_btn =game_settings .get ("theme","clair")
        _highlight_btn (settings_buttons ["theme"][hi_btn ])

        settings_buttons ["global_progress"]["off"].rect .topleft =(LEFT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +250 )
        settings_buttons ["global_progress"]["on"].rect .topleft =(LEFT_X +COL_W -BTN_W ,PANEL_Y +250 )
        for btn in settings_buttons ["global_progress"].values ():
            btn .draw (screen ,mouse_pos )
        _draw_setting_label_aligned ("Progression globale",settings_buttons ["global_progress"]["on"].rect )
        st ="on"if game_settings .get ("global_progress",True )else "off"
        _highlight_btn (settings_buttons ["global_progress"][st ])

        reset_w ,reset_h =360 ,50 
        reset_x =right_rect .centerx -reset_w //2 
        reset_y =right_rect .y +100 
        reset_progress_button .rect =pygame .Rect (reset_x ,reset_y ,reset_w ,reset_h )
        reset_progress_button .text ="Réinitialisation données"

        reset_progress_button .draw (screen ,mouse_pos )

        if code_input_mode is not None :


            global code_input_box_rect 
            global code_input_text_left_x 
            global code_input_text_max_w 


            global code_input_caret_visible 
            global code_input_last_blink_ms 

            overlay =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
            overlay .fill ((0 ,0 ,0 ,160 ))
            screen .blit (overlay ,(0 ,0 ))
            w ,h =700 ,220 
            rx ,ry =WIDTH //2 -w //2 ,HEIGHT //2 -h //2 
            pygame .draw .rect (screen ,(250 ,250 ,250 ),(rx ,ry ,w ,h ),border_radius =12 )
            pygame .draw .rect (screen ,(0 ,0 ,0 ),(rx ,ry ,w ,h ),2 ,border_radius =12 )
            title ="Entrer un code DÉV"
            ts =big_font .render (title ,True ,(0 ,0 ,0 ))
            screen .blit (ts ,(rx +w //2 -ts .get_width ()//2 ,ry +16 ))

            text_max_w =max (10 ,text_right_limit -text_left_x )
            code_input_text_left_x =text_left_x 
            code_input_text_max_w =text_max_w 

            shown =code_input_text 
            disp ,vis_start =_display_with_ellipsis (shown ,text_max_w ,font )

            cur_txt =font .render (disp ,True ,(0 ,0 ,0 ))
            screen .blit (cur_txt ,(text_left_x ,box .y +box .height //2 -cur_txt .get_height ()//2 ))


            code_input_caret =max (0 ,min (len (shown ),code_input_caret ))

            now_ms =pygame .time .get_ticks ()
            if now_ms -code_input_last_blink_ms >=DEV_CARET_BLINK_MS :
                code_input_caret_visible =not code_input_caret_visible 
                code_input_last_blink_ms =now_ms 

            if code_input_caret_visible :
                caret_x =text_left_x 
                if vis_start >0 :
                    caret_x +=font .size ("…")[0 ]
                clamped =max (vis_start ,min (len (shown ),code_input_caret ))
                if clamped >vis_start :
                    caret_x +=font .size (shown [vis_start :clamped ])[0 ]
                pygame .draw .line (screen ,(0 ,0 ,0 ),(caret_x ,box .y +8 ),(caret_x ,box .bottom -8 ),2 )
                caret_x =text_left_x 
                if vis_start >0 :
                    caret_x +=font .size ("…")[0 ]
                clamped =max (vis_start ,min (len (shown ),code_input_caret ))
                if clamped >vis_start :
                    caret_x +=font .size (shown [vis_start :clamped ])[0 ]
                pygame .draw .line (screen ,(0 ,0 ,0 ),(caret_x ,box .y +8 ),(caret_x ,box .bottom -8 ),2 )

            hint =small_font .render ("Entrée = valider · Échap = fermer",True ,DARK_GRAY )
            screen .blit (hint ,(rx +w //2 -hint .get_width ()//2 ,ry +h -36 ))

    elif settings_tab =='automation':
        center_x =WIDTH //2 
        y1 =PANEL_Y +130 
        y2 =y1 +100 
        y3 =y2 +100 
        settings_buttons ["mini_autoclicker"]["off"].rect =pygame .Rect (center_x -(BTN_W +BTN_GAP //2 ),y1 ,BTN_W ,ROW_H )
        settings_buttons ["mini_autoclicker"]["on"].rect =pygame .Rect (center_x +(BTN_GAP //2 ),y1 ,BTN_W ,ROW_H )
        for btn in settings_buttons ["mini_autoclicker"].values ():btn .draw (screen ,mouse_pos )
        t =font .render ("Mini auto-clicker",True ,fg )
        screen .blit (t ,(center_x -t .get_width ()//2 ,y1 -40 ))
        state ="on"if game_settings .get ("mini_autoclicker")else "off"
        _highlight_btn (settings_buttons ["mini_autoclicker"][state ])

        if settings_buttons ["mini_autoclicker"]["off"].rect .collidepoint (mouse_pos )or settings_buttons ["mini_autoclicker"]["on"].rect .collidepoint (mouse_pos ):
            draw_tooltip (screen ,[
            "Mini auto-clicker :",
            "Active un clic automatique toutes les secondes.",
            "Permet de progresser sans cliquer manuellement."
            ],mouse_pos )
        screen .blit (t ,(center_x -t .get_width ()//2 ,y1 -40 ))
        state ="on"if game_settings .get ("mini_autoclicker")else "off"
        _highlight_btn (settings_buttons ["mini_autoclicker"][state ])

        settings_buttons ["auto_buyers"]["off"].rect =pygame .Rect (center_x -(BTN_W +BTN_GAP //2 ),y2 ,BTN_W ,ROW_H )
        settings_buttons ["auto_buyers"]["on"].rect =pygame .Rect (center_x +(BTN_GAP //2 ),y2 ,BTN_W ,ROW_H )
        for btn in settings_buttons ["auto_buyers"].values ():btn .draw (screen ,mouse_pos )
        t =font .render ("Auto-acheteurs",True ,fg )
        screen .blit (t ,(center_x -t .get_width ()//2 ,y2 -40 ))
        state ="on"if game_settings .get ("auto_buyers")else "off"
        _highlight_btn (settings_buttons ["auto_buyers"][state ])

        settings_buttons ["auto_rebirth"]["off"].rect =pygame .Rect (center_x -(BTN_W +BTN_GAP //2 ),y3 ,BTN_W ,ROW_H )
        completed_list =challenge_state .get ("completed",[])
        unlocked =(isinstance (completed_list ,list )and len (completed_list )>0 and completed_list [0 ])
        if not unlocked :
            for btn in settings_buttons ["auto_rebirth"].values ():
                draw_button_disabled (screen ,btn )
            hint =small_font .render ("Débloqué en complétant le Challenge 1",True ,DARK_GRAY )
            screen .blit (hint ,(center_x -hint .get_width ()//2 ,y3 +ROW_H +10 ))

        unlocked =(len (challenge_state .get ("completed",[]))>0 and challenge_state ["completed"][0 ])
        if not unlocked :
            for btn in settings_buttons ["auto_rebirth"].values ():
                draw_button_disabled (screen ,btn )
            hint =small_font .render ("Débloqué en complétant le Challenge 1",True ,DARK_GRAY )
            screen .blit (hint ,(center_x -hint .get_width ()//2 ,y3 +ROW_H +10 ))

        if settings_buttons ["auto_rebirth"]["off"].rect .collidepoint (mouse_pos )or settings_buttons ["auto_rebirth"]["on"].rect .collidepoint (mouse_pos ):
            draw_tooltip (screen ,["Débloqué en complétant le Challenge 1"],mouse_pos )

    elif settings_tab =='display':
        left_rect =pygame .Rect (LEFT_X -30 ,PANEL_Y ,COL_W +60 ,PANEL_H )
        right_rect =pygame .Rect (RIGHT_X -30 ,PANEL_Y ,COL_W +60 ,PANEL_H )
        _draw_panel (left_rect ,title ="Affichage")
        _draw_panel (right_rect ,title ="Options affichage")

        settings_buttons ["mini_notifications"]["off"].rect .topleft =(RIGHT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +80 )
        settings_buttons ["mini_notifications"]["on"].rect .topleft =(RIGHT_X +COL_W -BTN_W ,PANEL_Y +80 )
        for btn in settings_buttons ["mini_notifications"].values ():btn .draw (screen ,mouse_pos )
        t =font .render ("Mini notifications",True ,fg )
        screen .blit (t ,(RIGHT_X ,settings_buttons ["mini_notifications"]["on"].rect .centery -t .get_height ()//2 ))
        st ="Affiche les badges sur le menu"
        screen .blit (small_font .render (st ,True ,DARK_GRAY ),(RIGHT_X ,settings_buttons ["mini_notifications"]["on"].rect .bottom +4 ))
        state ="on"if game_settings .get ("mini_notifications")else "off"
        _highlight_btn (settings_buttons ["mini_notifications"][state ])

        settings_buttons ["ingame_notifications"]["off"].rect .topleft =(RIGHT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +160 )
        settings_buttons ["ingame_notifications"]["on"].rect .topleft =(RIGHT_X +COL_W -BTN_W ,PANEL_Y +160 )
        for btn in settings_buttons ["ingame_notifications"].values ():btn .draw (screen ,mouse_pos )
        t =font .render ("Notifications in-game",True ,fg )
        screen .blit (t ,(RIGHT_X ,settings_buttons ["ingame_notifications"]["on"].rect .centery -t .get_height ()//2 ))
        st ="Affiche les toasts d'information"
        screen .blit (small_font .render (st ,True ,DARK_GRAY ),(RIGHT_X ,settings_buttons ["ingame_notifications"]["on"].rect .bottom +4 ))
        state ="on"if game_settings .get ("ingame_notifications")else "off"
        _highlight_btn (settings_buttons ["ingame_notifications"][state ])

        global _last_version_btn_rect 
        try :
            _last_version_btn_rect 
        except NameError :
            pass 
        _last_version_btn_rect =None 

        btn_w ,btn_h =360 ,50 

        right_rect =pygame .Rect (RIGHT_X -30 ,PANEL_Y ,COL_W +60 ,PANEL_H )
        btn_x =right_rect .centerx -btn_w //2 


        btn_y =PANEL_Y +240 
        _last_version_btn_rect =pygame .Rect (btn_x ,btn_y ,btn_w ,btn_h )
        Button (_last_version_btn_rect ,"Dernière version",(90 ,160 ,230 ),WHITE ).draw (screen ,mouse_pos )

        hint =small_font .render ("Affiche le changelog et retourne au menu.",True ,DARK_GRAY )
        screen .blit (hint ,(right_rect .centerx -hint .get_width ()//2 ,btn_y +btn_h +10 ))


        settings_buttons ["show_reset_points"]["off"].rect .topleft =(LEFT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +80 )
        settings_buttons ["show_reset_points"]["on"].rect .topleft =(LEFT_X +COL_W -BTN_W ,PANEL_Y +80 )

        settings_buttons ["show_reset_boosts"]["off"].rect .topleft =(LEFT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +140 )
        settings_buttons ["show_reset_boosts"]["on"].rect .topleft =(LEFT_X +COL_W -BTN_W ,PANEL_Y +140 )

        settings_buttons ["show_tooltips_on_hover"]["off"].rect .topleft =(LEFT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +200 )
        settings_buttons ["show_tooltips_on_hover"]["on"].rect .topleft =(LEFT_X +COL_W -BTN_W ,PANEL_Y +200 )

        t =font .render ("Afficher points possédés (R/P/A/Réinc)",True ,fg )
        screen .blit (t ,(LEFT_X ,PANEL_Y +80 ))
        for btn in settings_buttons ["show_reset_points"].values ():btn .draw (screen ,mouse_pos )
        state ="on"if game_settings .get ("show_reset_points",True )else "off"
        _highlight_btn (settings_buttons ["show_reset_points"][state ])

        t =font .render ("Afficher boosts des points",True ,fg )
        screen .blit (t ,(LEFT_X ,PANEL_Y +140 ))
        for btn in settings_buttons ["show_reset_boosts"].values ():btn .draw (screen ,mouse_pos )
        state ="on"if game_settings .get ("show_reset_boosts",True )else "off"
        _highlight_btn (settings_buttons ["show_reset_boosts"][state ])

        t =font .render ("Afficher infobulles au survol",True ,fg )
        screen .blit (t ,(LEFT_X ,PANEL_Y +200 ))
        for btn in settings_buttons ["show_tooltips_on_hover"].values ():btn .draw (screen ,mouse_pos )
        state ="on"if game_settings .get ("show_tooltips_on_hover",True )else "off"
        _highlight_btn (settings_buttons ["show_tooltips_on_hover"][state ])

        settings_buttons ["confirm_resets"]["off"].rect .topleft =(LEFT_X +COL_W -(BTN_W *2 +BTN_GAP ),PANEL_Y +260 )
        settings_buttons ["confirm_resets"]["on"].rect .topleft =(LEFT_X +COL_W -BTN_W ,PANEL_Y +260 )
        t =font .render ("Confirmer avant les resets (R/P/A/Re/Inf)",True ,fg )
        screen .blit (t ,(LEFT_X ,PANEL_Y +260 ))
        for btn in settings_buttons ["confirm_resets"].values ():btn .draw (screen ,mouse_pos )
        state ="on"if game_settings .get ("confirm_resets",True )else "off"
        _highlight_btn (settings_buttons ["confirm_resets"][state ])

    elif settings_tab =='dev':

        center_w ,center_h =600 ,80 
        cx =WIDTH //2 -center_w //2 
        cy =HEIGHT //2 -center_h //2 
        dev_code_button .rect =pygame .Rect (cx ,cy ,center_w ,center_h )
        dev_code_button .text =("Commandes développeur"if developer_mode_active else "Activer le mode développeur")
        dev_code_button .draw (screen ,mouse_pos )

        if dev_password_mode :
            overlay =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
            overlay .fill ((0 ,0 ,0 ,160 ))
            screen .blit (overlay ,(0 ,0 ))
            w ,h =700 ,220 
            rx ,ry =WIDTH //2 -w //2 ,HEIGHT //2 -h //2 
            pygame .draw .rect (screen ,(250 ,250 ,250 ),(rx ,ry ,w ,h ),border_radius =12 )
            pygame .draw .rect (screen ,(0 ,0 ,0 ),(rx ,ry ,w ,h ),2 ,border_radius =12 )
            ts =big_font .render ("Mot de passe développeur",True ,(0 ,0 ,0 ))
            screen .blit (ts ,(rx +w //2 -ts .get_width ()//2 ,ry +16 ))
            box =pygame .Rect (rx +40 ,ry +90 ,w -80 ,44 )
            pygame .draw .rect (screen ,WHITE ,box ,border_radius =8 )
            pygame .draw .rect (screen ,(0 ,0 ,0 ),box ,2 ,border_radius =8 )

            global dev_password_eye_rect ,dev_password_box_rect 
            global dev_password_text_left_x ,dev_password_text_max_w 
            global dev_password_caret_visible ,dev_password_last_blink_ms 

            box =pygame .Rect (rx +40 ,ry +90 ,w -80 ,44 )
            pygame .draw .rect (screen ,WHITE ,box ,border_radius =8 )
            pygame .draw .rect (screen ,(0 ,0 ,0 ),box ,2 ,border_radius =8 )
            dev_password_box_rect =box 

            eye_w ,eye_h =36 ,24 
            eye_rect =pygame .Rect (
            box .right -10 -eye_w ,
            box .y +(box .height -eye_h )//2 ,
            eye_w ,eye_h 
            )
            dev_password_eye_rect =eye_rect 

            text_left_x =box .x +12 
            text_right_limit =eye_rect .left -6 
            text_max_w =max (10 ,text_right_limit -text_left_x )
            dev_password_text_left_x =text_left_x 
            dev_password_text_max_w =text_max_w 

            shown =dev_password_text if dev_password_visible else ("*"*len (dev_password_text ))

            disp ,vis_start =_display_with_ellipsis (shown ,text_max_w ,font )

            cur_txt =font .render (disp ,True ,(0 ,0 ,0 ))
            screen .blit (cur_txt ,(text_left_x ,box .y +box .height //2 -cur_txt .get_height ()//2 ))

            draw_eye_icon (screen ,eye_rect ,open =dev_password_visible )

            now_ms =pygame .time .get_ticks ()
            if now_ms -dev_password_last_blink_ms >=DEV_CARET_BLINK_MS :
                dev_password_caret_visible =not dev_password_caret_visible 
                dev_password_last_blink_ms =now_ms 

            if dev_password_caret_visible :

                caret_x =text_left_x 
                if vis_start >0 :
                    caret_x +=font .size ("…")[0 ]
                clamped =max (vis_start ,min (len (shown ),dev_password_caret ))
                if clamped >vis_start :
                    caret_x +=font .size (shown [vis_start :clamped ])[0 ]

                caret_y1 =box .y +8 
                caret_y2 =box .bottom -8 
                pygame .draw .line (screen ,(0 ,0 ,0 ),(caret_x ,caret_y1 ),(caret_x ,caret_y2 ),2 )

            hint =small_font .render (
            "Entrée = valider · Échap = fermer · Clic sur l’œil = afficher/masquer",
            True ,DARK_GRAY 
            )
            screen .blit (hint ,(rx +w //2 -hint .get_width ()//2 ,ry +h -36 ))

    elif settings_tab =='about':

        left_rect =pygame .Rect (LEFT_X -30 ,PANEL_Y ,COL_W +60 ,PANEL_H )
        right_rect =pygame .Rect (RIGHT_X -30 ,PANEL_Y ,COL_W +60 ,PANEL_H )
        for r in (left_rect ,right_rect ):
            pygame .draw .rect (screen ,panel ,r ,border_radius =12 )
            pygame .draw .rect (screen ,(0 ,0 ,0 ),r ,2 ,border_radius =12 )

        x =left_rect .x +24 
        y =left_rect .y +24 
        line_gap =34 

        ver =f"Version actuelle : v{CURRENT_VERSION }"
        screen .blit (font .render (ver ,True ,fg ),(x ,y ));y +=line_gap 


        try :
            size_kb =get_game_file_size_kb ()
            size_txt =f"Taille du fichier : {size_kb } Ko"
        except Exception :
            size_txt ="Taille du fichier : (indisponible)"
        screen .blit (font .render (size_txt ,True ,fg ),(x ,y ));y +=line_gap 

        sid_txt =f"Identifiant du joueur : {PLAYER_SESSION_ID }"
        screen .blit (font .render (sid_txt ,True ,fg ),(x ,y ));y +=line_gap 

        uid_txt =f"UID du joueur : {PLAYER_UID }"
        screen .blit (font .render (uid_txt ,True ,fg ),(x ,y ));y +=line_gap 

        warn_lines =[
        "Avertissement :",
        "Cet UID permet aux développeurs d’apporter des modifications à votre compte.",
        "Ne partagez cet UID avec personne. Toute personne autre qu’un développeur",
        "pourrait apporter des modifications irréversibles à votre compte.",
        "Si quelqu'un apporte des modifications quelconques à votre compte avec",
        "cet UID, merci de contacter les développeurs rapidement."
        ]
        wy =y +8 
        for ln in warn_lines :
            screen .blit (small_font .render (ln ,True ,(140 ,0 ,0 )),(x ,wy ));wy +=small_font .get_height ()+2 

        SETTINGS_BACK_HUB_BTN .draw (screen ,mouse_pos )

    elif settings_tab =='rules':

        left_rect =pygame .Rect (LEFT_X -30 ,PANEL_Y ,COL_W +60 ,PANEL_H )
        right_rect =pygame .Rect (RIGHT_X -30 ,PANEL_Y ,COL_W +60 ,PANEL_H )
        for r in (left_rect ,right_rect ):
            pygame .draw .rect (screen ,panel ,r ,border_radius =12 )
            pygame .draw .rect (screen ,(0 ,0 ,0 ),r ,2 ,border_radius =12 )

        note =small_font .render (
        "Certaines règles mentionnent des fonctions non disponibles actuellement ; ne pas en tenir compte.",
        True ,DARK_GRAY 
        )
        screen .blit (note ,(WIDTH //2 -note .get_width ()//2 ,96 ))

        RULES_DEF =[
        (
        "Interdiction de modifier le code du jeu : des vérifications sont effectuées à chaque lancement.",
        "Sanction : bannissement définitif et suppression immédiate des sauvegardes si une modification est détectée."
        ),
        (
        "Interdiction d’utiliser le mode développeur sans autorisation.",
        "Sanction : bannissement définitif et suppression immédiate des sauvegardes existantes."
        ),
        (
        "Interdiction de choisir un nom offensant.",
        "Sanctions progressives : 1) suppression du nom d’utilisateur ; 2) bannissement 7 jours ; 3) bannissement définitif."
        ),
        (
        "Interdiction d’exploiter des failles (ex. score illimité, mode dev activé sans raison...). "
        "Merci de les signaler aux développeurs.",
        "Sanction : bannissement définitif et suppression immédiate des sauvegardes existantes."
        ),
        ]
        CONTACT ="Pour contester un bannissement ou une sanction, merci de contacter les développeurs."

        x =left_rect .x +24 
        y =left_rect .y +20 
        max_w =left_rect .width -48 
        gap_y =10 

        def _wrap (text :str ,fnt ,width :int ):
            try :
                return wrap_lines_auto (text ,fnt ,width )
            except Exception :

                return [text ]

        bullet_color =fg 
        sanction_color =(160 ,0 ,0 )

        for rule_text ,sanction_text in RULES_DEF :

            for ln in _wrap ("• "+rule_text ,font ,max_w ):
                screen .blit (font .render (ln ,True ,bullet_color ),(x ,y ))
                y +=font .get_height ()+2 

            for ln in _wrap (sanction_text ,small_font ,max_w ):
                screen .blit (small_font .render (ln ,True ,sanction_color ),(x ,y ))
                y +=small_font .get_height ()+2 

            y +=gap_y 

        for ln in _wrap (CONTACT ,small_font ,max_w ):
            screen .blit (small_font .render (ln ,True ,fg ),(x ,y ))
            y +=small_font .get_height ()+2 

        SETTINGS_BACK_MENU_BTN .draw (screen ,mouse_pos )
        SETTINGS_BACK_HUB_BTN .draw (screen ,mouse_pos )

    if settings_tab is not None :
        SETTINGS_BACK_HUB_BTN .draw (screen ,mouse_pos )
    SETTINGS_BACK_MENU_BTN .draw (screen ,mouse_pos )

    draw_reset_overlays (mouse_pos )
    draw_version_badge_bottom_right_above_fps ()
    draw_fps_badge ()

def draw_quit_confirm_overlay (mouse_pos ):
    """v29.7.5 — Modale de confirmation avant de quitter le jeu."""
    if not quit_confirm .get ("open",False ):
        return 

    overlay =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
    overlay .fill ((0 ,0 ,0 ,160 ))
    screen .blit (overlay ,(0 ,0 ))

    w ,h =900 ,260 
    x ,y =WIDTH //2 -w //2 ,HEIGHT //2 -h //2 
    pygame .draw .rect (screen ,(250 ,250 ,250 ),(x ,y ,w ,h ),border_radius =12 )
    pygame .draw .rect (screen ,(0 ,0 ,0 ),(x ,y ,w ,h ),2 ,border_radius =12 )

    ts =big_font .render ("Quitter le jeu ?",True ,(0 ,0 ,0 ))
    screen .blit (ts ,(x +w //2 -ts .get_width ()//2 ,y +18 ))
    lines =[
    "Êtes-vous sûr de vouloir quitter le jeu ?",
    "Il n'y a pas encore de sauvegarde, votre progression actuelle sera donc perdue."
    ]
    yy =y +80 
    for ln in lines :
        ls =secondary_font .render (ln ,True ,(20 ,20 ,20 ))
        screen .blit (ls ,(x +24 ,yy ))
        yy +=28 

    btn_w ,btn_h =260 ,50 
    yes_rect =pygame .Rect (x +w -btn_w -24 ,y +h -btn_h -18 ,btn_w ,btn_h )
    no_rect =pygame .Rect (x +24 ,y +h -btn_h -18 ,btn_w ,btn_h )
    yes_btn =Button (yes_rect ,"Quitter quand même",(200 ,80 ,80 ),(255 ,255 ,255 ))
    no_btn =Button (no_rect ,"Annuler",(140 ,140 ,140 ),(255 ,255 ,255 ))
    yes_btn .draw (screen ,mouse_pos )
    no_btn .draw (screen ,mouse_pos )

    quit_confirm ["rect_yes"]=yes_rect 
    quit_confirm ["rect_no"]=no_rect 

def _draw_dev_deactivate_modal (mouse_pos ):
    """v29.9 — Modale de confirmation pour désactiver le mode développeur."""
    if not dev_deactivate_confirm .get ("open",False ):
        return 
    overlay =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
    overlay .fill ((0 ,0 ,0 ,160 ))
    screen .blit (overlay ,(0 ,0 ))

    w ,h =920 ,240 
    x ,y =WIDTH //2 -w //2 ,HEIGHT //2 -h //2 
    pygame .draw .rect (screen ,(250 ,250 ,250 ),(x ,y ,w ,h ),border_radius =12 )
    pygame .draw .rect (screen ,(0 ,0 ,0 ),(x ,y ,w ,h ),2 ,border_radius =12 )

    ts =big_font .render ("Désactiver le mode développeur ?",True ,(0 ,0 ,0 ))
    screen .blit (ts ,(x +w //2 -ts .get_width ()//2 ,y +16 ))
    lines =[
    "Vous perdrez l'accès aux commandes développeur.",
    "Vous pourrez le réactiver avec le mot de passe.",
    ]
    yy =y +80 
    for ln in lines :
        ls =secondary_font .render (ln ,True ,(20 ,20 ,20 ))
        screen .blit (ls ,(x +24 ,yy ));yy +=28 

    btn_w ,btn_h =260 ,50 
    yes_rect =pygame .Rect (x +w -btn_w -24 ,y +h -btn_h -18 ,btn_w ,btn_h )
    no_rect =pygame .Rect (x +24 ,y +h -btn_h -18 ,btn_w ,btn_h )
    yes_btn =Button (yes_rect ,"Désactiver maintenant",(200 ,120 ,120 ),WHITE )
    no_btn =Button (no_rect ,"Annuler",(140 ,140 ,140 ),WHITE )
    yes_btn .draw (screen ,mouse_pos )
    no_btn .draw (screen ,mouse_pos )
    dev_deactivate_confirm ["yes"]=yes_rect 
    dev_deactivate_confirm ["no"]=no_rect 

def draw_gr_confirm_overlay (mouse_pos ):
    """v29.8 — Modale de confirmation avant Grand Reset."""
    if not gr_confirm .get ("open",False ):
        return 

    overlay =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
    overlay .fill ((0 ,0 ,0 ,160 ))
    screen .blit (overlay ,(0 ,0 ))

    w ,h =940 ,300 
    x ,y =WIDTH //2 -w //2 ,HEIGHT //2 -h //2 
    pygame .draw .rect (screen ,(250 ,250 ,250 ),(x ,y ,w ,h ),border_radius =12 )
    pygame .draw .rect (screen ,(0 ,0 ,0 ),(x ,y ,w ,h ),2 ,border_radius =12 )

    ts =big_font .render ("Grand Reset — Confirmation",True ,(0 ,0 ,0 ))
    screen .blit (ts ,(x +w //2 -ts .get_width ()//2 ,y +18 ))
    lines =[
    "Cette action est irréversible et réinitialise TOUT en échange de boosts OP.",
    "Cliquez sur « Confirmer le Grand Reset » pour lancer l'opération.",
    ]
    yy =y +88 
    for ln in lines :
        ls =secondary_font .render (ln ,True ,(20 ,20 ,20 ))
        screen .blit (ls ,(x +24 ,yy ))
        yy +=28 

    btn_w ,btn_h =280 ,50 
    yes_rect =pygame .Rect (x +w -btn_w -24 ,y +h -btn_h -18 ,btn_w ,btn_h )
    no_rect =pygame .Rect (x +24 ,y +h -btn_h -18 ,btn_w ,btn_h )
    yes_btn =Button (yes_rect ,"Compris, continuer",(140 ,200 ,120 ),(255 ,255 ,255 ))
    no_btn =Button (no_rect ,"Annuler",(200 ,120 ,120 ),(255 ,255 ,255 ))
    yes_btn .draw (screen ,mouse_pos )
    no_btn .draw (screen ,mouse_pos )

    gr_confirm ["rect_yes"]=yes_rect 
    gr_confirm ["rect_no"]=no_rect 

def draw_history (mouse_pos ,dt ):
    bg ,fg ,panel ,bar =theme_colors ()
    screen .fill (bg )
    if game_settings ["graphics_mode"]=="graphismes_travaillés":
        for sh in floating_shapes :
            sh .update (dt );sh .draw (screen )
    title =big_font .render ("Statistiques",True ,fg )
    screen .blit (title ,(WIDTH //2 -title .get_width ()//2 ,60 ))
    stats ={
    "Score max":format_from_log10 (game_data ["max_score_log10"])if game_data ["max_score_log10"]>NEG_INF else "0",
    "Points R max":format_from_log10 (game_data ["points_max_log10"]["R"])if game_data ["points_max_log10"]["R"]>NEG_INF else "0",
    "Points P max":format_from_log10 (game_data ["points_max_log10"]["P"])if game_data ["points_max_log10"]["P"]>NEG_INF else "0",
    "Points A max":format_from_log10 (game_data ["points_max_log10"]["A"])if game_data ["points_max_log10"]["A"]>NEG_INF else "0",
    "Points Réinc max":format_from_log10 (game_data ["points_max_log10"]["Re"])if game_data ["points_max_log10"]["Re"]>NEG_INF else "0",
    "PI max":f"{game_data ['pi_max']}",
    "PI dépensés":f"{game_data ['pi_spent_total']}",
    "Grand Resets":f"{game_data ['grand_resets']}",
    "Clics totaux (manuels)":f"{game_data ['total_clicks']}",
    "Max Clicks/s":f"{game_data ['max_sps']:.2f}",
    "Upgrades achetés":f"{game_data ['total_upgrades_bought']}",
    "Temps de jeu":f"{int (game_data ['total_play_time']//3600 )}h {int ((game_data ['total_play_time']%3600 )//60 )}m {int (game_data ['total_play_time']%60 )}s",
    }
    y =140 
    for k ,v in stats .items ():
        t =font .render (f"{k }: {v }",True ,fg )
        screen .blit (t ,(WIDTH //2 -t .get_width ()//2 ,y ));y +=40 
    back_button .draw (screen ,mouse_pos )
    draw_interactive_tip_if_any (mouse_pos ,context ='history')

def draw_tutorial (mouse_pos ,dt ):
    bg ,fg ,panel ,bar =theme_colors ()
    screen .fill (bg )
    if game_settings ["graphics_mode"]=="graphismes_travaillés":
        for sh in floating_shapes :
            sh .update (dt );sh .draw (screen )
    title =big_font .render ("Tutoriel",True ,fg )
    screen .blit (title ,(WIDTH //2 -title .get_width ()//2 ,60 ))


    if tutorial_mode is None :
        info =secondary_font .render ("Choisissez un type de tutoriel :",True ,fg )
        screen .blit (info ,(WIDTH //2 -info .get_width ()//2 ,130 ))
        TUTO_CHOICE_STATIC_BTN .draw (screen ,mouse_pos )
        TUTO_CHOICE_INTER_BTN .draw (screen ,mouse_pos )

        TUTO_BACK_MENU_BTN .draw (screen ,mouse_pos )

    elif tutorial_mode =='static':
        lines =[
        "Bienvenue dans Idle Clicker !",
        "Objectif: accumuler le plus de score possible.",
        "Cliquez sur CLICK pour gagner du score manuellement.",
        "Améliorations:",
        "- Auto : ajoute des clics automatiques/s.",
        "- Clic : augmente la valeur du clic manuel.",
        "- Mult : multiplie tous les gains.",
        "Resets (progression):",
        "- Renaissance/Prestige/Ascension/Réincarnation donnent des points spéciaux.",
        "- Infinité : reset global, donne des PI (points d'infinité) et milestones PI.",
        "Milestones d'infinité (PI) — donnent des boosts OP",
        "",
        "Difficultés : donnent des boosts ou des nerfs selon la difficulté",
        "",
        "Astuce : utilisez l'onglet Milestones pour voir le bonus exact appliqué.",
        "",
        "Modifications dernière Version :",
        "Idle Clicker Version 31 - UI Update",
        "Ajout de la progression globale",
        "Ajout d'un nouveau paramètre",
        "Ajout d'effets spéciaux pour les resets",
        "Ajout d'animations diverses",
        "Augmentation du nombre de fps du jeu, passant de 60 à 72.",
        "Augmentation de la vitesse de chargement de 50 à 100Ko/s",
        "Correction de bugs mineurs",
        ]

        y =140 
        for ln in lines :
            t =secondary_font .render (ln ,True ,fg )
            screen .blit (t ,(80 ,y ));y +=28 

        TUTO_BACK_MENU_BTN .draw (screen ,mouse_pos )
        TUTO_BACK_CHOICE_BTN .draw (screen ,mouse_pos )
        globals ()['_tuto_static_back_menu_rect']=TUTO_BACK_MENU_BTN .rect 
        globals ()['_tuto_static_back_choice_rect']=TUTO_BACK_CHOICE_BTN .rect 

    elif tutorial_mode =='interactive':

        if not tutorial_active :
            TUTO_START_AUTO_BTN .draw (screen ,mouse_pos )
            TUTO_START_MANUAL_BTN .draw (screen ,mouse_pos )
            TUTO_BACK_MENU_BTN .draw (screen ,mouse_pos )
            TUTO_BACK_CHOICE_BTN .draw (screen ,mouse_pos )

    if tutorial_active and tutorial_mode =='interactive':
        draw_interactive_tip_if_any (mouse_pos ,context ='tutorial')

def draw_challenges (mouse_pos ,dt ):
    bg ,fg ,panel ,bar =theme_colors ()
    screen .fill (bg )
    if game_settings ["graphics_mode"]=="graphismes_travaillés":
        for sh in floating_shapes :
            sh .update (dt );sh .draw (screen )
    title =big_font .render ("Challenges",True ,fg )
    screen .blit (title ,(WIDTH //2 -title .get_width ()//2 ,60 ))

    _chal_btn_rects .clear ()

    if not challenges_menu_accessible ():
        info =secondary_font .render ("Débloqués à la milestone d’infinité 5.",True ,(160 ,0 ,0 ))
        screen .blit (info ,(WIDTH //2 -info .get_width ()//2 ,110 ))
    elif not milestone_currently_unlocked (12 ):
        info =secondary_font .render ("Milestone 12 non débloquée actuellement : consultation possible, lancement impossible.",True ,(160 ,80 ,0 ))
        screen .blit (info ,(WIDTH //2 -info .get_width ()//2 ,110 ))

    card_w =WIDTH -160 
    card_h =120 
    x =80 
    y =150 
    for i ,ch in enumerate (CHALLENGES_DEF ):
        cid =ch ["id"]
        pygame .draw .rect (screen ,panel ,(x ,y ,card_w ,card_h ),border_radius =12 )
        pygame .draw .rect (screen ,(0 ,0 ,0 ),(x ,y ,card_w ,card_h ),2 ,border_radius =12 )
        name =font .render (f"{ch ['name']}",True ,fg )
        screen .blit (name ,(x +16 ,y +12 ))
        objective =small_font .render (f"Objectif : {ch ['objective']}",True ,fg )
        nerf =small_font .render (f"Nerf : {ch ['nerf']}",True ,(160 ,40 ,40 ))
        buff =small_font .render (f"Buff : {ch ['buff']}",True ,(40 ,120 ,40 ))
        screen .blit (objective ,(x +16 ,y +42 ))
        screen .blit (nerf ,(x +16 ,y +66 ))
        screen .blit (buff ,(x +16 ,y +90 ))

        completed =challenge_state ["completed"][cid -1 ]
        active =challenge_state ["active"]and challenge_state ["current"]==cid 
        prev_done =True if cid ==1 else challenge_state ["completed"][cid -2 ]
        available =milestone_currently_unlocked (12 )and prev_done 
        status_txt ="Terminé"if completed else ("En cours"if active else ("Disponible"if available else "Verrouillé"))
        status_color =(0 ,160 ,60 )if completed else ((40 ,120 ,200 )if active else ((0 ,120 ,60 )if available else (160 ,0 ,0 )))
        status =small_font .render (status_txt ,True ,status_color )
        screen .blit (status ,(x +card_w -180 ,y +14 ))

        if difficulty ==DIFF_VERY_EASY :
            completed =True 
            active =False 
            available =False 

        btn_w ,btn_h =160 ,44 
        start_btn =Button ((x +card_w -520 ,y +card_h -btn_h -12 ,btn_w ,btn_h ),"Démarrer",(90 ,200 ,120 ),WHITE )
        stop_btn =Button ((x +card_w -350 ,y +card_h -btn_h -12 ,btn_w ,btn_h ),"Arrêter",(200 ,120 ,110 ),WHITE )
        comp_btn =Button ((x +card_w -180 ,y +card_h -btn_h -12 ,btn_w ,btn_h ),"Compléter",(120 ,160 ,240 ),WHITE )

        start_btn .draw (screen ,mouse_pos )
        stop_btn .draw (screen ,mouse_pos )
        comp_btn .draw (screen ,mouse_pos )

        if not available or completed or active :
            draw_button_disabled (screen ,start_btn )
        if not active :
            draw_button_disabled (screen ,stop_btn )
        can_complete =active and objective_met (cid )
        if not can_complete :
            draw_button_disabled (screen ,comp_btn )

        _chal_btn_rects [(cid ,'start')]=start_btn .rect 
        _chal_btn_rects [(cid ,'stop')]=stop_btn .rect 
        _chal_btn_rects [(cid ,'complete')]=comp_btn .rect 

        if active and can_complete and not challenge_state ["notified_ready"]:
            add_notification (f"Challenge {cid } complétable !",1800 )
            challenge_state ["notified_ready"]=True 

        y +=card_h +10 

    back_button .draw (screen ,mouse_pos )

def draw_loading (mouse_pos ,dt ):

    _force_exit_loading_transition_if_stuck ()
    if loading_mode =="transition_to_captcha":

        draw_loading_to_captcha (mouse_pos ,dt )
        return 

    global loading_start_ms ,loading_step_index ,loading_step_start_ms 

    screen .fill ((0 ,0 ,0 ))

    LOADING_STEPS =[
    {"label":"Chargement des ressources…","duration":300 },
    {"label":"Connexion au serveur…","duration":300 },
    {"label":"Chargement des données…","duration":300 },
    {"label":"Optimisation des performances…","duration":300 },
    {"label":"Lancement du jeu…","duration":300 },
    ]

    if "loading_step_index"not in globals ():
        loading_step_index =0 
        loading_step_start_ms =pygame .time .get_ticks ()

    ver =small_font .render (f"Idle Clicker Version {CURRENT_VERSION }",True ,(220 ,220 ,220 ))
    screen .blit (ver ,ver .get_rect (center =(WIDTH //2 ,HEIGHT //2 -110 )))

    if loading_step_index <len (LOADING_STEPS ):
        step =LOADING_STEPS [loading_step_index ]
        now =pygame .time .get_ticks ()
        elapsed =now -loading_step_start_ms 
        ratio =max (0.0 ,min (1.0 ,elapsed /step ["duration"]))

        bar_w ,bar_h =int (WIDTH *0.5 ),24 
        x =(WIDTH -bar_w )//2 
        y =HEIGHT //2 

        pygame .draw .rect (screen ,(60 ,60 ,60 ),(x ,y ,bar_w ,bar_h ),border_radius =8 )
        fill_w =int (bar_w *ratio )
        pygame .draw .rect (screen ,(180 ,180 ,180 ),(x ,y ,fill_w ,bar_h ),border_radius =8 )
        pygame .draw .rect (screen ,(220 ,220 ,220 ),(x ,y ,bar_w ,bar_h ),2 ,border_radius =8 )

        progress_label =small_font .render (f"Étape {loading_step_index +1 }/{len (LOADING_STEPS )}",True ,(220 ,220 ,220 ))
        screen .blit (progress_label ,progress_label .get_rect (center =(WIDTH //2 ,y -70 )))

        txt =small_font .render (step ["label"],True ,(220 ,220 ,220 ))
        screen .blit (txt ,txt .get_rect (center =(WIDTH //2 ,y -36 )))

        pct_txt =font .render (f"{int (ratio *100 )}%",True ,(220 ,220 ,220 ))
        screen .blit (pct_txt ,pct_txt .get_rect (center =(WIDTH //2 ,y +44 )))

        if elapsed >=step ["duration"]:

            try :
                lbl =step .get ("label","Étape")
                log_event (f"[Loading] {lbl } — OK en {elapsed } ms (étape {loading_step_index +1 }/{len (LOADING_STEPS )})")
            except Exception :
                pass 

            if loading_step_index ==1 :
                try :
                    log_event ("Connexion au serveur réussie.")
                except Exception :
                    pass 

            loading_step_index +=1 
            loading_step_start_ms =now 

    else :

        bar_w ,bar_h =int (WIDTH *0.5 ),24 
        x =(WIDTH -bar_w )//2 
        y =HEIGHT //2 

        final_label =LOADING_STEPS [-1 ]["label"]
        pygame .draw .rect (screen ,(60 ,60 ,60 ),(x ,y ,bar_w ,bar_h ),border_radius =8 )
        pygame .draw .rect (screen ,(180 ,180 ,180 ),(x ,y ,bar_w ,bar_h ),border_radius =8 )
        pygame .draw .rect (screen ,(220 ,220 ,220 ),(x ,y ,bar_w ,bar_h ),2 ,border_radius =8 )

        progress_label =small_font .render (f"Étape {len (LOADING_STEPS )}/{len (LOADING_STEPS )}",True ,(220 ,220 ,220 ))
        screen .blit (progress_label ,progress_label .get_rect (center =(WIDTH //2 ,y -70 )))

        txt =small_font .render (final_label ,True ,(220 ,220 ,220 ))
        screen .blit (txt ,txt .get_rect (center =(WIDTH //2 ,y -36 )))

        pct_txt =font .render ("100%",True ,(220 ,220 ,220 ))
        screen .blit (pct_txt ,pct_txt .get_rect (center =(WIDTH //2 ,y +44 )))

        if not loading_transition .get ("active",False ):

            try :
                log_event ("[Loading] Toutes les étapes terminées — démarrage de la transition vers le CAPTCHA.")
            except Exception :
                pass 
            start_loading_to_captcha_transition ()
            return 

def draw_reset_white (mouse_pos ,dt ):
    global reset_white_start_ms ,loading_start_ms ,loading_mode 
    screen .fill ((255 ,255 ,255 ))
    now =pygame .time .get_ticks ()
    elapsed =0 if reset_white_start_ms <0 else (now -reset_white_start_ms )
    if elapsed >=reset_white_duration_ms :

        loading_mode ='reset'
        loading_start_ms =now 

        loading_total_kb =compute_loading_total_kb ()
        loading_duration_ms =int (math .ceil (1000.0 *(loading_total_kb /KB_PER_SEC )))
        loaded_kb_display =0.0 
        loading_step_accum_ms =0 
        set_game_state ('loading')

def set_game_state (state ):
    globals ()['game_state']=state 

def set_to_captcha ():

    global loading_start_ms ,loading_mode 
    loading_start_ms =-1 
    loading_mode =None 
    set_game_state ('captcha')

    try :
        if not captcha_completed :
            pick_captcha_question_index ()
    except Exception :
        pass 

def draw_dev_commands (mouse_pos ,dt ):
    global dev_score_input_box_rect ,dev_score_input_left_x ,dev_score_input_max_w 
    global dev_score_caret_visible ,dev_score_last_blink_ms 
    global dev_score_input_text ,dev_score_caret 
    global DEV_SCORE_APPLY_BTN ,dev_ui_tab ,_dev_hub_rects ,_dev_chal_rects 
    global _dev_hub_rects ,DEV_SCORE_APPLY_BTN 
    bg ,fg ,panel ,bar =theme_colors ()
    screen .fill (bg )
    if game_settings ["graphics_mode"]=="graphismes_travaillés":
        for sh in floating_shapes :
            sh .update (dt );sh .draw (screen )

    title =big_font .render ("Commandes développeur",True ,fg )
    screen .blit (title ,(WIDTH //2 -title .get_width ()//2 ,60 ))

    if dev_ui_tab is None :
        _dev_hub_rects ={}
        info =secondary_font .render ("Choisissez une catégorie :",True ,fg )
        screen .blit (info ,(WIDTH //2 -info .get_width ()//2 ,120 ))

        btn_w ,btn_h =520 ,92 
        gap_x ,gap_y =36 ,28 
        start_x =WIDTH //2 -(btn_w +gap_x //2 )
        start_y =180 
        labels =[
        ("score","Score (saisie)"),
        ("pi","PI (saisie)"),
        ("challenges","Challenges"),
        ("tests","Tests"),
        ("logs","Logs du jeu"),
        ("deactivate","Désactivation du mode développeur"),
        ]
        for i ,(key ,txt )in enumerate (labels ):
            col =i %2 
            row =i //2 
            x =start_x +col *(btn_w +gap_x )
            y =start_y +row *(btn_h +gap_y )
            b =Button ((x ,y ,btn_w ,btn_h ),txt ,(210 ,210 ,210 ))
            b .draw (screen ,mouse_pos )
            _dev_hub_rects [key ]=b .rect 

        DEV_BACK_MENU_BTN .draw (screen ,mouse_pos )
        DEV_BACK_SETTINGS_BTN .draw (screen ,mouse_pos )
        return 

    if dev_ui_tab =="tests":
        w ,h =900 ,260 
        x ,y =WIDTH //2 -w //2 ,180 
        pygame .draw .rect (screen ,panel ,(x ,y ,w ,h ),border_radius =12 )
        pygame .draw .rect (screen ,(0 ,0 ,0 ),(x ,y ,w ,h ),2 ,border_radius =12 )
        t =font .render ("Tests",True ,fg )
        screen .blit (t ,(x +20 ,y +18 ))
        btn =Button ((x +20 ,y +90 ,360 ,56 ),"Test écran d'erreur",(200 ,140 ,90 ),(255 ,255 ,255 ))
        btn .draw (screen ,mouse_pos )
        globals ()['_dev_tests_error_rect']=btn .rect 
        DEV_BACK_COMMANDS_BTN .draw (screen ,mouse_pos )
        DEV_BACK_SETTINGS_BTN .draw (screen ,mouse_pos )
        DEV_BACK_MENU_BTN .draw (screen ,mouse_pos )
        return 

    if dev_ui_tab =="score":
        if dev_score_last_blink_ms ==0 :
            dev_score_caret =len (dev_score_input_text )
            dev_score_caret_visible =True 
            dev_score_last_blink_ms =pygame .time .get_ticks ()

        w ,h =900 ,260 
        x ,y =WIDTH //2 -w //2 ,180 
        pygame .draw .rect (screen ,panel ,(x ,y ,w ,h ),border_radius =12 )
        pygame .draw .rect (screen ,(0 ,0 ,0 ),(x ,y ,w ,h ),2 ,border_radius =12 )

        subt =font .render ("Donner du score (suffixes/scientifique acceptés)",True ,fg )
        screen .blit (subt ,(x +24 ,y +16 ))

        box =pygame .Rect (x +24 ,y +70 ,w -48 ,48 )
        pygame .draw .rect (screen ,WHITE ,box ,border_radius =8 )
        pygame .draw .rect (screen ,(0 ,0 ,0 ),box ,2 ,border_radius =8 )

        global dev_score_input_box_rect ,dev_score_input_left_x ,dev_score_input_max_w 
        dev_score_input_box_rect =box 
        dev_score_input_left_x =box .x +12 
        dev_score_input_max_w =box .width -24 

        now_ms =pygame .time .get_ticks ()
        if now_ms -dev_score_last_blink_ms >=DEV_CARET_BLINK_MS :
            dev_score_caret_visible =not dev_score_caret_visible 
            dev_score_last_blink_ms =now_ms 

        shown =dev_score_input_text 
        disp ,vis_start =_display_with_ellipsis (shown ,dev_score_input_max_w ,font )
        cur_txt =font .render (disp ,True ,(0 ,0 ,0 ))
        screen .blit (cur_txt ,(dev_score_input_left_x ,box .y +box .height //2 -cur_txt .get_height ()//2 ))
        if dev_score_caret_visible :
            cx =dev_score_input_left_x +(font .size ("…")[0 ]if vis_start >0 else 0 )
            clamp =max (vis_start ,min (len (shown ),dev_score_caret ))
            if clamp >vis_start :
                cx +=font .size (shown [vis_start :clamp ])[0 ]
            pygame .draw .line (screen ,(0 ,0 ,0 ),(cx ,box .y +8 ),(cx ,box .bottom -8 ),2 )

        apply_btn =Button ((x +w -240 ,y +h -70 ,220 ,50 ),"Valider",(90 ,200 ,120 ),WHITE )
        apply_btn .draw (screen ,mouse_pos )
        DEV_SCORE_APPLY_BTN =apply_btn .rect 

        hint =small_font .render ("Entrée = valider · Échap = effacer la saisie",True ,DARK_GRAY )
        screen .blit (hint ,(x +24 ,y +h -58 ))

        DEV_BACK_MENU_BTN .draw (screen ,mouse_pos )
        DEV_BACK_SETTINGS_BTN .draw (screen ,mouse_pos )
        DEV_BACK_COMMANDS_BTN .draw (screen ,mouse_pos )
        return 

    if dev_ui_tab =="pi":
        global dev_pi_input_text ,dev_pi_input_box_rect ,dev_pi_input_left_x ,dev_pi_input_max_w 
        global dev_pi_caret ,dev_pi_caret_visible ,dev_pi_last_blink_ms ,DEV_PI_APPLY_BTN 
        if dev_pi_last_blink_ms ==0 :
            dev_pi_caret =len (dev_pi_input_text )
            dev_pi_caret_visible =True 
            dev_pi_last_blink_ms =pygame .time .get_ticks ()

        w ,h =900 ,260 
        x ,y =WIDTH //2 -w //2 ,180 
        pygame .draw .rect (screen ,panel ,(x ,y ,w ,h ),border_radius =12 )
        pygame .draw .rect (screen ,(0 ,0 ,0 ),(x ,y ,w ,h ),2 ,border_radius =12 )

        subt =font .render ("Donner du PI (suffixes/scientifique acceptés)",True ,fg )
        screen .blit (subt ,(x +24 ,y +16 ))

        box =pygame .Rect (x +24 ,y +70 ,w -48 ,48 )
        pygame .draw .rect (screen ,WHITE ,box ,border_radius =8 )
        pygame .draw .rect (screen ,(0 ,0 ,0 ),box ,2 ,border_radius =8 )

        global dev_pi_input_box_rect ,dev_pi_input_left_x ,dev_pi_input_max_w 
        dev_pi_input_box_rect =box 
        dev_pi_input_left_x =box .x +12 
        dev_pi_input_max_w =box .width -24 

        now_ms =pygame .time .get_ticks ()
        if now_ms -dev_pi_last_blink_ms >=DEV_CARET_BLINK_MS :
            dev_pi_caret_visible =not dev_pi_caret_visible 
            dev_pi_last_blink_ms =now_ms 

        shown =dev_pi_input_text 
        disp ,vis_start =_display_with_ellipsis (shown ,dev_pi_input_max_w ,font )
        cur_txt =font .render (disp ,True ,(0 ,0 ,0 ))
        screen .blit (cur_txt ,(dev_pi_input_left_x ,box .y +box .height //2 -cur_txt .get_height ()//2 ))
        if dev_pi_caret_visible :
            cx =dev_pi_input_left_x +(font .size ("…")[0 ]if vis_start >0 else 0 )
            clamp =max (vis_start ,min (len (shown ),dev_pi_caret ))
            if clamp >vis_start :
                cx +=font .size (shown [vis_start :clamp ])[0 ]
            pygame .draw .line (screen ,(0 ,0 ,0 ),(cx ,box .y +8 ),(cx ,box .bottom -8 ),2 )

        apply_btn =Button ((x +w -240 ,y +h -70 ,220 ,50 ),"Valider",(90 ,200 ,120 ),WHITE )
        apply_btn .draw (screen ,mouse_pos )
        DEV_PI_APPLY_BTN =apply_btn .rect 

        hint =small_font .render ("Entrée = valider · Échap = effacer la saisie",True ,DARK_GRAY )
        screen .blit (hint ,(x +24 ,y +h -58 ))

        DEV_BACK_MENU_BTN .draw (screen ,mouse_pos )
        DEV_BACK_SETTINGS_BTN .draw (screen ,mouse_pos )
        DEV_BACK_COMMANDS_BTN .draw (screen ,mouse_pos )
        return 

    if dev_ui_tab =="challenges":

        lbl =secondary_font .render ("Raccourcis Challenges (Activation / Complétion)",True ,fg )
        screen .blit (lbl ,(WIDTH //2 -lbl .get_width ()//2 ,130 ))

        btn_w ,btn_h =360 ,50 
        start_x ,start_y =120 ,180 
        gap_x ,gap_y =40 ,24 
        pairs =[
        ("c1","Challenge 1","Activation (+1K PI)","Complétion (lance C1 +1 PI)"),
        ("c2","Challenge 2","Activation (C1 terminé +1K PI)","Complétion (lance C2 +1e100 score)"),
        ("c3","Challenge 3","Activation (C1-2 terminés +1K PI)","Complétion (lance C3 +100K PI)"),
        ("c4","Challenge 4","Activation (C1-3 terminés +1K PI)","Complétion (lance C4 +1 pt Ascension)"),
        ]
        row =0 
        for key ,title ,a_txt ,d_txt in pairs :
            t =font .render (title ,True ,fg )
            screen .blit (t ,(start_x ,start_y +row *(btn_h +60 )))

            act_btn =Button ((start_x ,start_y +28 +row *(btn_h +60 ),btn_w ,btn_h ),a_txt ,(110 ,150 ,210 ),WHITE )
            don_btn =Button ((start_x +btn_w +gap_x ,start_y +28 +row *(btn_h +60 ),btn_w ,btn_h ),d_txt ,(120 ,160 ,240 ),WHITE )
            act_btn .draw (screen ,mouse_pos )
            don_btn .draw (screen ,mouse_pos )
            _dev_chal_rects [(key ,"act")]=act_btn .rect 
            _dev_chal_rects [(key ,"done")]=don_btn .rect 
            row +=1 

        DEV_BACK_MENU_BTN .draw (screen ,mouse_pos )
        DEV_BACK_SETTINGS_BTN .draw (screen ,mouse_pos )
        DEV_BACK_COMMANDS_BTN .draw (screen ,mouse_pos )
        return 

    if dev_ui_tab =="logs":

        info =small_font .render ("Redirection vers l'écran Logs...",True ,fg )
        screen .blit (info ,(WIDTH //2 -info .get_width ()//2 ,HEIGHT //2 ))

        DEV_BACK_MENU_BTN .draw (screen ,mouse_pos )
        DEV_BACK_SETTINGS_BTN .draw (screen ,mouse_pos )
        DEV_BACK_COMMANDS_BTN .draw (screen ,mouse_pos )
        return 

    if dev_ui_tab =="deactivate":

        w ,h =1000 ,220 
        x ,y =WIDTH //2 -w //2 ,180 
        pygame .draw .rect (screen ,panel ,(x ,y ,w ,h ),border_radius =12 )
        pygame .draw .rect (screen ,(0 ,0 ,0 ),(x ,y ,w ,h ),2 ,border_radius =12 )

        txt1 =font .render ("Désactiver le mode développeur ?",True ,fg )
        txt2 =small_font .render ("Une confirmation sera demandée. Vous pourrez réactiver plus tard avec le mot de passe.",True ,DARK_GRAY )
        screen .blit (txt1 ,(x +24 ,y +18 ))
        screen .blit (txt2 ,(x +24 ,y +64 ))

        open_btn =Button ((x +w -300 ,y +h -60 ,280 ,46 ),"Ouvrir la confirmation",(200 ,120 ,120 ),WHITE )
        open_btn .draw (screen ,mouse_pos )

        DEV_BACK_MENU_BTN .draw (screen ,mouse_pos )
        DEV_BACK_SETTINGS_BTN .draw (screen ,mouse_pos )
        DEV_BACK_COMMANDS_BTN .draw (screen ,mouse_pos )

        if dev_deactivate_confirm .get ("open",False ):
            _draw_dev_deactivate_modal (mouse_pos )
        return 

def draw_dev_logs (mouse_pos ,dt ):
    bg ,fg ,panel ,bar =theme_colors ()
    screen .fill (bg )
    if game_settings ["graphics_mode"]=="graphismes_travaillés":
        for sh in floating_shapes :
            sh .update (dt );sh .draw (screen )
    title =big_font .render ("Logs du jeu",True ,fg )
    screen .blit (title ,(WIDTH //2 -title .get_width ()//2 ,60 ))

    lines_per_page =20 
    total_pages =max (1 ,(len (game_logs )+lines_per_page -1 )//lines_per_page )
    global dev_logs_page 
    if dev_logs_page >=total_pages :
        dev_logs_page =total_pages -1 
    start =max (0 ,len (game_logs )-(dev_logs_page +1 )*lines_per_page )
    end =len (game_logs )-dev_logs_page *lines_per_page 
    subset =game_logs [start :end ]
    y =120 
    for ln in subset :
        t =small_font .render (ln ,True ,fg )
        screen .blit (t ,(80 ,y ))
        y +=24 

    dev_logs_nav_rects ["prev"]=None 
    dev_logs_nav_rects ["next"]=None 
    nav_y =HEIGHT -80 
    prev_btn =Button ((WIDTH //2 -220 ,nav_y ,160 ,44 ),'← Précédent',(210 ,210 ,210 ))
    next_btn =Button ((WIDTH //2 +60 ,nav_y ,160 ,44 ),'Suivant →',(210 ,210 ,210 ))
    prev_btn .draw (screen ,mouse_pos )
    next_btn .draw (screen ,mouse_pos )
    if dev_logs_page >=total_pages -1 :
        draw_button_disabled (screen ,prev_btn )
    if dev_logs_page <=0 :
        draw_button_disabled (screen ,next_btn )
    dev_logs_nav_rects ['prev']=prev_btn .rect 
    dev_logs_nav_rects ['next']=next_btn .rect 
    pi =small_font .render (f"Page {total_pages -dev_logs_page }/{total_pages }",True ,fg )
    screen .blit (pi ,(WIDTH //2 -pi .get_width ()//2 ,nav_y -28 ))

    back_button .draw (screen ,mouse_pos )

def draw_main_game (mouse_pos ,dt ):
    bg ,fg ,panel ,bar =theme_colors ()
    screen .fill (bg )
    if game_settings ["graphics_mode"]=="graphismes_travaillés":
        for sh in floating_shapes :
            sh .update (dt );sh .draw (screen )
        if secret_shape_active and secret_shape_obj :
            secret_shape_obj .update (dt )
            secret_shape_obj .draw (screen )

    btn_rect =click_button .rect 
    btn_w ,btn_h =btn_rect .width ,btn_rect .height 
    radius =min (btn_w ,btn_h )//2 

    comp =pygame .Surface ((btn_w ,btn_h ),pygame .SRCALPHA )

    pygame .draw .circle (comp ,(120 ,200 ,255 ),(btn_w //2 ,btn_h //2 ),radius )
    pygame .draw .circle (comp ,(255 ,255 ,255 ),(btn_w //2 ,btn_h //2 ),radius -3 ,3 )

    ts =big_font .render ("Click",True ,(255 ,255 ,255 ))
    shadow =big_font .render ("Click",True ,(60 ,130 ,200 ))
    comp .blit (shadow ,shadow .get_rect (center =(btn_w //2 +3 ,btn_h //2 +6 )))
    comp .blit (ts ,ts .get_rect (center =(btn_w //2 ,btn_h //2 )))

    scale =1.0 
    if hasattr (click_button ,'_bounce_active')and click_button ._bounce_active :
        t_b =(pygame .time .get_ticks ()-click_button ._bounce_start )/320.0 
        if t_b <1.0 :
            scale =0.96 +0.18 *abs (math .sin (3.6 *t_b )*math .exp (-2.2 *t_b ))
    comp_scaled =pygame .transform .smoothscale (comp ,(int (btn_w *scale ),int (btn_h *scale )))
    dest =comp_scaled .get_rect (center =btn_rect .center )
    screen .blit (comp_scaled ,dest )

    if game_settings .get ("graphics_mode")=="graphismes_travaillés":

        for p in list (particles ):
            p .update (dt )

            if hasattr (p ,"dead"):
                if p .dead ():
                    particles .remove (p )
            else :
                if p .life >=p .max_life :
                    particles .remove (p )

        for p in sorted (particles ,key =lambda q :getattr (q ,"z",1.0 )):
            p .draw (screen )

    sx ,sy =20 ,20 
    def bl (line ,color =fg ):
        nonlocal sy 
        t =font .render (line ,True ,color );screen .blit (t ,(sx ,sy ));sy +=30 
    bl (f"Score : {format_from_log10 (game_data ['score_log10'])if game_data ['score_log10']>NEG_INF else '0'}")
    cvL =log10_effective_click_value ()
    cvL_disp =apply_gain_modifiers (cvL )
    if game_data .get ('score_multiplier_secret',1.0 )>1.0 :
        cvL_disp +=math .log10 (game_data ['score_multiplier_secret'])
    bl (f"Valeur du clic : ~{format_from_log10 (cvL_disp )}")
    av_log =log10_effective_auto_value ()
    av_log_disp =apply_gain_modifiers (av_log )if av_log >NEG_INF else NEG_INF 
    bl (f"Autoclics/s : ~{format_from_log10 (av_log_disp )if av_log_disp >NEG_INF else '0'}")
    Lm =game_data .get ('multiplier_log10',0.0 )
    bl (f"Multiplicateur (upgrade) : x{format_from_log10 (Lm )}")
    bl ('')
    pts =game_data .get ('points_log10',{})

    if game_settings .get ("show_reset_points",True ):
        bl ('Points :')
        bl (f" Renaissance : {format_points_pretty (pts .get ('R',NEG_INF ))}")
        bl (f" Prestige : {format_points_pretty (pts .get ('P',NEG_INF ))}")
        bl (f" Ascension : {format_points_pretty (pts .get ('A',NEG_INF ))}")
        bl (f" Réincarnation : {format_points_pretty (pts .get ('Re',NEG_INF ))}")

        pi_L =NEG_INF if game_data .get ('PI',0 )<=0 else math .log10 (game_data ['PI'])
        bl (f" Infinité : {format_points_pretty (pi_L )}")

    if game_settings .get ("show_reset_boosts",True ):
        boost_R =per_family_multiplier_log10 ('R',pts )
        boost_P =per_family_multiplier_log10 ('P',pts )
        boost_A =per_family_multiplier_log10 ('A',pts )
        boost_Re =per_family_multiplier_log10 ('Re',pts )
        bl ("")
        bl (" Boosts :")
        bl (f"  R : +{format_percent_from_multiplier_log10 (boost_R )}")
        bl (f"  P : +{format_percent_from_multiplier_log10 (boost_P )}")
        bl (f"  A : +{format_percent_from_multiplier_log10 (boost_A )}")
        bl (f"  Réinc : +{format_percent_from_multiplier_log10 (boost_Re )}")

        boost_PI =game_data .get ('PI',0 )*LOG10_PI_BOOST 
        bl (f" PI : +{format_percent_from_multiplier_log10 (boost_PI )}")

    if tutorial_active and tutorial_mode =='interactive':
        draw_interactive_tip_if_any (mouse_pos ,context ='main',sy_after_stats =sy )

    draw_difficulty_badge ()
    draw_version_badge_bottom_right_above_fps ()
    draw_fps_badge ()

    caL =game_data ['cost_auto_log10']
    ccL =game_data ['cost_click_log10']
    cmL =game_data ['cost_mult_log10']
    upgrade_auto_button .text =f"Auto (+1) (score {format_from_log10 (caL )})"
    upgrade_click_button .text =f"Clic (+1) (score {format_from_log10 (ccL )})"
    upgrade_mult_button .text =f"Mult (x1.20) (score {format_from_log10 (cmL )})"

    for b in (upgrade_auto_button ,upgrade_click_button ,upgrade_mult_button ,renaissance_button ,prestige_button ,ascension_button ,reinc_button ,infinity_button ):
        b .draw (screen ,mouse_pos )

    if challenge_state ["active"]and challenge_state ["current"]==4 :
        for b in (upgrade_auto_button ,upgrade_click_button ,upgrade_mult_button ):
            draw_button_disabled (screen ,b )

        if (upgrade_auto_button .rect .collidepoint (mouse_pos )
        or upgrade_click_button .rect .collidepoint (mouse_pos )
        or upgrade_mult_button .rect .collidepoint (mouse_pos )):
            draw_tooltip (screen ,["Améliorations indisponibles dans le Challenge 4."],mouse_pos )

    haveL =game_data ["score_log10"]

    if not (challenge_state ["active"]and challenge_state ["current"]==4 ):
        if haveL <caL :draw_button_disabled (screen ,upgrade_auto_button )
        if haveL <ccL :draw_button_disabled (screen ,upgrade_click_button )
        if haveL <cmL :draw_button_disabled (screen ,upgrade_mult_button )

    def draw_score_bar (btn ,needL ,have_log10 ,label_prefix ="Score"):
        bar_h =16 
        yb =btn .rect .bottom +6 
        rect_bg =pygame .Rect (btn .rect .x ,yb ,btn .rect .width ,bar_h )
        diff =(have_log10 if have_log10 >NEG_INF else -999999 )-needL 
        ratio =10.0 **max (-6.0 ,min (0.0 ,diff ))
        w =int (btn .rect .width *min (1.0 ,ratio ))
        pygame .draw .rect (screen ,bar ,rect_bg ,border_radius =5 )
        pygame .draw .rect (screen ,(150 ,255 ,150 ),(rect_bg .x ,rect_bg .y ,w ,rect_bg .height ),border_radius =5 )
        txt =small_font .render (f"{label_prefix } : {format_from_log10 (have_log10 )if have_log10 >NEG_INF else '0'} / {format_from_log10 (needL )}",True ,fg )
        screen .blit (txt ,txt .get_rect (center =rect_bg .center ))

    for btn ,thr in ((renaissance_button ,L_REN ),
    (prestige_button ,L_PRE ),
    (ascension_button ,L_ASC ),
    (reinc_button ,L_REINC ),
    (infinity_button ,L_INF )):
        if haveL <thr :
            draw_button_disabled (screen ,btn )
        draw_score_bar (btn ,thr ,haveL )
        if btn .rect .collidepoint (mouse_pos ):
            if btn is infinity_button :

                if haveL >=L_INF :
                    base =int (1 +math .floor (max (0.0 ,haveL -L_INF )/LOG10_15 ))
                else :
                    base =0 
                pi_gain =int (math .floor (base *gr_pi_gain_multiplier ()))if base >0 else 0 
                if have_challenge_buff (2 )and pi_gain >0 :
                    pi_gain =int (math .floor (pi_gain *1.1 ))
                if challenge_state ["active"]and challenge_state ["current"]==2 :
                    pi_gain =0 
                draw_tooltip (screen ,[
                "Score insuffisant"if haveL <L_INF else f"Gains PI si reset: +{pi_gain }",
                f"Seuil: {format_from_log10 (L_INF )}"if haveL <L_INF else ""
                ],mouse_pos )
            else :
                fam ='R'if btn is renaissance_button else ('P'if btn is prestige_button else ('A'if btn is ascension_button else 'Re'))
                gainL =estimate_points_gain_now_log10 (fam ,haveL )
                needL =L_REN if fam =='R'else L_PRE if fam =='P'else L_ASC if fam =='A'else L_REINC 
                if haveL <needL :
                    draw_tooltip (screen ,[
                    "Score insuffisant",
                    f"Seuil: {format_from_log10 (needL )}"
                    ],mouse_pos )
                else :
                    if gainL >NEG_INF :
                        gainL +=points_gain_multiplier_log10_for (fam )
                        if challenge_state ["active"]and challenge_state ["current"]==2 :
                            gainL -=LOG10_2 
                        draw_tooltip (screen ,[
                        f"Gains pts {fam } si reset: ~{format_from_log10 (gainL )}"
                        ],mouse_pos )

    gr_tip_lines =None 
    have_pi_chk =game_data .get ('PI',0 )
    if difficulty ==DIFF_VERY_EASY :
        show_gr =milestone_currently_unlocked (20 )
    elif difficulty ==DIFF_EASY :
        show_gr =(len (challenge_state .get ('completed',[]))>1 and challenge_state ['completed'][1 ])
    else :
        show_gr =(len (challenge_state .get ('completed',[]))>3 and challenge_state ['completed'][3 ])
    if show_gr :
        gr_cost =next_gr_cost_pi ()
        gr_btn =Button ((WIDTH -320 ,620 ,300 ,74 ),f"Grand Reset ({gr_count ()})",(140 ,120 ,220 ),WHITE )
        gr_btn .draw (screen ,mouse_pos )
        gr_button_rect =gr_btn .rect 
        have_pi =game_data .get ('PI',0 )
        if have_pi <gr_cost :
            draw_button_disabled (screen ,gr_btn )

        bar_h =16 
        rect_bg =pygame .Rect (gr_btn .rect .x ,gr_btn .rect .bottom +8 ,gr_btn .rect .width ,18 )
        pygame .draw .rect (screen ,panel ,rect_bg ,border_radius =5 )
        pygame .draw .rect (screen ,(0 ,0 ,0 ),rect_bg ,2 ,border_radius =5 )

        ratio_GR =gr_progress_ratio ()
        pygame .draw .rect (screen ,bar ,(rect_bg .x ,rect_bg .y ,int (rect_bg .width *ratio_GR ),rect_bg .height ),border_radius =5 )

        txt =small_font .render (f"PI : {format_points_pretty (math .log10 (have_pi )if have_pi >0 else NEG_INF )} / {format_points_pretty (math .log10 (gr_cost )if gr_cost >0 else NEG_INF )}",True ,fg )
        screen .blit (txt ,txt .get_rect (center =rect_bg .center ))

        if gr_button_rect .collidepoint (mouse_pos )and not overlays_open ():
            if have_pi >=gr_cost :
                draw_tooltip (screen ,[
                "Grand Reset",
                f"Coût: {gr_cost :,} PI".replace (","," "),
                "Cliquez pour confirmer"
                ],mouse_pos )
            else :
                draw_tooltip (screen ,[
                "PI insuffisants",
                f"Coût: {gr_cost :,} PI".replace (","," ")
                ],mouse_pos )

    draw_gr_confirm_overlay (mouse_pos )

    draw_reset_confirm_overlay (mouse_pos )

    draw_reset_fx_overlay ()

    curL =game_data .get ("score_log10",NEG_INF )
    if curL >game_data .get ("max_score_log10",NEG_INF ):
        game_data ["max_score_log10"]=curL 

    update_global_progress ()
    if game_settings .get ("global_progress",True )and not GLOBAL_PROGRESS ["done"]:
        bg ,fg ,panel ,bar =theme_colors ()
        N =gp_step_count ()
        step =gp_current_def ()
        ratio =global_progress_overall_ratio ()

        bar_w ,bar_h =int (WIDTH *0.45 ),18 
        x =WIDTH //2 -bar_w //2 
        y =16 +22 

        if step :
            label =f"Étape {GLOBAL_PROGRESS ['idx']}/{N } — {step ['label']}"
        else :
            label =f"Étape {GLOBAL_PROGRESS ['idx']}/{N }"
        title =small_font .render (label ,True ,fg )
        screen .blit (title ,(x ,y -22 ))

        pygame .draw .rect (screen ,BAR_BG ,(x ,y ,bar_w ,bar_h ),border_radius =6 )
        fillw =int (bar_w *ratio )
        pygame .draw .rect (screen ,bar ,(x ,y ,fillw ,bar_h ),border_radius =6 )
        pygame .draw .rect (screen ,(0 ,0 ,0 ),(x ,y ,bar_w ,bar_h ),2 ,border_radius =6 )

        pct =small_font .render (f"{int (ratio *100 )}%",True ,fg )
        screen .blit (pct ,(x +bar_w +10 ,y +bar_h //2 -pct .get_height ()//2 ))

    game_menu_button =Button ((20 ,HEIGHT -60 ,140 ,44 ),"Menu",GRAY ,BLACK )
    game_menu_button .draw (screen ,mouse_pos )
    return game_menu_button 

def run_auto_buyers ():
    if (not game_settings .get ("auto_buyers",False ))or (not game_data .get ("perm_unlocks",{}).get ("auto_buyers",False )):
        return 
    order =("mult","click","auto")
    if game_settings .get ("purchase_mode")=="multi":
        for kind in order :buy_upgrade_max (kind )
    else :
        for _ in range (300 ):
            bought =False 
            for kind in order :
                c =_get_cost_log10 (kind )
                if have_enough_score (c )and buy_upgrade (kind ):
                    bought =True ;break 
            if not bought :break 

def run_mini_autoclicker ():
    if game_settings .get ("mini_autoclicker",False )and game_data .get ("perm_unlocks",{}).get ("mini_autoclicker",False ):
        addL =log10_effective_click_value ()
        addL =apply_gain_modifiers (addL )
        game_data ["score_log10"]=log10_add (game_data ["score_log10"],addL )

def run_auto_rebirth (secs :float ):
    """
    v29.7 : Ajoute automatiquement des points de Renaissance à hauteur de 10%/s
    des points R actuellement obtenables via un reset de Renaissance,
    sans effectuer le reset.
    Si le joueur reset ensuite, il reçoit les points complets du reset en plus.
    """

    if not game_settings .get ("auto_rebirth",False ):
        return 
    if not (len (challenge_state .get ("completed",[]))>0 and challenge_state ["completed"][0 ]):
        return 
    if secs <=0.0 :
        return 

    L =game_data ["score_log10"]

    gainL =estimate_points_gain_now_log10 ('R',L )
    if gainL ==NEG_INF :
        return 

    gainL +=points_gain_multiplier_log10_for ('R')

    if challenge_state ["active"]and challenge_state ["current"]==2 :
        gainL -=LOG10_2 

    addL =(gainL -1.0 )+(math .log10 (secs )if secs >0 else NEG_INF )

    if math .isfinite (addL ):
        game_data ["points_log10"]["R"]=log10_add (game_data ["points_log10"]["R"],addL )

def handle_click_settings (pos ):
    global code_input_mode ,game_state ,dev_password_mode ,dev_password_text 
    global settings_tab ,game_settings ,_last_version_btn_rect ,show_version_popup 

    if reset_flow .get ("state",0 )>0 and not reset_flow .get ("in_progress",False ):
        cont_r =_reset_btn_rects .get ("cont")
        back_r =_reset_btn_rects .get ("back")

        if back_r and back_r .collidepoint (pos ):
            reset_flow ["state"]=0 
            reset_flow ["clicks"]=0 
            reset_flow ["start_ms"]=-1 
            return 

        if cont_r and cont_r .collidepoint (pos ):
            st =reset_flow .get ("state",1 )
            if st ==1 :
                reset_flow ["state"]=2 
            elif st ==2 :
                reset_flow ["state"]=3 
                reset_flow ["clicks"]=0 
                reset_flow ["start_ms"]=pygame .time .get_ticks ()
            else :

                reset_flow ["clicks"]=reset_flow .get ("clicks",0 )+1 

                if reset_flow .get ("start_ms",-1 )<0 :
                    reset_flow ["start_ms"]=pygame .time .get_ticks ()

                if reset_flow ["clicks"]>=10 :
                    reset_flow ["in_progress"]=True 
                    reset_flow ["progress_start_ms"]=-1 
            return 

    if settings_tab is None :
        for key ,r in list (_settings_hub_rects .items ()):
            if r and r .collidepoint (pos ):
                settings_tab =key 
                return 

        if SETTINGS_BACK_MENU_BTN .rect .collidepoint (pos ):
            game_state ='captcha'if not captcha_completed else 'menu'
            return 
        return 

    if SETTINGS_BACK_HUB_BTN .rect .collidepoint (pos ):
        settings_tab =None 
        return 

    if SETTINGS_BACK_MENU_BTN .rect .collidepoint (pos ):
        game_state ='captcha'if not captcha_completed else 'menu'
        return 

    if settings_tab =='general':

        for group ,buttons in settings_buttons .items ():
            for key ,btn in buttons .items ():
                if btn .rect .collidepoint (pos ):
                    if group =="purchase_mode":
                        game_settings ["purchase_mode"]=key 
                    elif group =="graphics_mode":
                        game_settings ["graphics_mode"]="performance"if key =="performance"else "graphismes_travaillés"
                    elif group =="theme":
                        game_settings ["theme"]=key 
                    elif group =="auto_buyers":
                        game_settings ["auto_buyers"]=(key =="on")
                    elif group =="mini_autoclicker":
                        game_settings ["mini_autoclicker"]=(key =="on")
                    elif group =="mini_notifications":
                        game_settings ["mini_notifications"]=(key =="on")
                    elif group =="ingame_notifications":
                        game_settings ["ingame_notifications"]=(key =="on")

                    elif group =="global_progress":
                        game_settings ["global_progress"]=(key =="on")

                        add_notification (
                        "Progression globale : activée"if key =="on"else "Progression globale : désactivée",
                        1400 
                        )

        if reset_progress_button .rect .collidepoint (pos ):
            reset_flow ["state"]=1 
            reset_flow ["clicks"]=0 
            reset_flow ["start_ms"]=-1 
            return 
        return 

    if settings_tab =='automation':
        for group ,buttons in settings_buttons .items ():
            for key ,btn in buttons .items ():
                if btn .rect .collidepoint (pos ):
                    if group =="auto_buyers":
                        game_settings ["auto_buyers"]=(key =="on")
                    elif group =="mini_autoclicker":
                        game_settings ["mini_autoclicker"]=(key =="on")
                    elif group =="auto_rebirth":
                        unlocked =(len (challenge_state .get ("completed",[]))>0 and challenge_state ["completed"][0 ])
                        if not unlocked :
                            add_notification ("Auto-Renaissance verrouillée : terminez le Challenge 1.",1800 )
                        else :
                            game_settings ["auto_rebirth"]=(key =="on")
                    return 

    if settings_tab =='display':
        if _last_version_btn_rect and _last_version_btn_rect .collidepoint (pos ):
            show_version_popup =True 
            globals ()['_open_version_from_settings']=True 
            game_state ='menu'
            return True 


        for key ,btn in settings_buttons ["mini_notifications"].items ():
            if btn .rect .collidepoint (pos ):
                game_settings ["mini_notifications"]=(key =="on")
                return 
        for key ,btn in settings_buttons ["ingame_notifications"].items ():
            if btn .rect .collidepoint (pos ):
                game_settings ["ingame_notifications"]=(key =="on")
                return 
        for key ,btn in settings_buttons ["show_reset_points"].items ():
            if btn .rect .collidepoint (pos ):
                game_settings ["show_reset_points"]=(key =="on")
                return 
        for key ,btn in settings_buttons ["show_reset_boosts"].items ():
            if btn .rect .collidepoint (pos ):
                game_settings ["show_reset_boosts"]=(key =="on")
                return 
        for key ,btn in settings_buttons ["show_tooltips_on_hover"].items ():
            if btn .rect .collidepoint (pos ):
                game_settings ["show_tooltips_on_hover"]=(key =="on")
                return 
        for key ,btn in settings_buttons ["confirm_resets"].items ():
            if btn .rect .collidepoint (pos ):
                game_settings ["confirm_resets"]=(key =="on")
                return 
        return 

    if settings_tab =='dev':
        if dev_code_button .rect .collidepoint (pos ):
            if developer_mode_active :
                game_state ='dev_commands'
            else :
                dev_password_mode =True 
                dev_password_text =''
                dev_password_caret =0 
                dev_password_caret_visible =True 
                dev_password_last_blink_ms =pygame .time .get_ticks ()
        return False 


ERROR_FREEZE_MS =650 
_error_overlay ={'active':False ,'stage':'freeze','start_ms':0 ,'code':0 ,'etype':'','msg':'','trace':'','snap':None }
ERROR_CODE_MAP ={'NameError':164 ,'OverflowError':189 ,'ZeroDivisionError':170 ,'ValueError':140 ,'KeyError':141 ,'IndexError':142 ,'TypeError':143 ,'AttributeError':144 ,'FileNotFoundError':145 ,'OSError':146 ,'TestError':0 }
def _compute_error_code (etype :str ,msg :str ,trace :str )->int :
    if etype in ERROR_CODE_MAP :
        return int (ERROR_CODE_MAP [etype ])
    s =(etype +'|'+(msg or '')+'|'+(trace or '')).encode ('utf-8',errors ='ignore')
    return 100 +(zlib .crc32 (s )%900 )
def trigger_error_overlay (etype :str ,msg :str ,code =None ,trace :str =''):
    try :
        snap =screen .copy ()
    except Exception :
        snap =None 
    c =int (code )if code is not None else _compute_error_code (etype ,msg ,trace )
    _error_overlay .update ({'active':True ,'stage':'freeze','start_ms':pygame .time .get_ticks (),'code':c ,'etype':etype ,'msg':msg ,'trace':trace ,'snap':snap })
def draw_error_overlay_loop ():
    now =pygame .time .get_ticks ()
    if not _error_overlay .get ('active',False ):
        return False 
    if _error_overlay .get ('stage')=='freeze':
        snap =_error_overlay .get ('snap')
        if snap is not None :
            screen .blit (snap ,(0 ,0 ))
        else :
            screen .fill ((255 ,255 ,255 ))
        t =(now -_error_overlay .get ('start_ms',now ))/float (max (1 ,ERROR_FREEZE_MS ))
        t =0.0 if t <0 else (1.0 if t >1.0 else t )
        ov =pygame .Surface ((WIDTH ,HEIGHT ),pygame .SRCALPHA )
        ov .fill ((255 ,255 ,255 ,int (180 *t )))
        screen .blit (ov ,(0 ,0 ))
        if t >=1.0 :
            _error_overlay ['stage']='error'
        return True 
    screen .fill ((255 ,255 ,255 ))
    et =_error_overlay .get ('etype','Erreur')
    cd =_error_overlay .get ('code',0 )
    msg =_error_overlay .get ('msg','')
    title =big_font .render (f"Une erreur est survenue — {et } (Code {cd })",True ,(180 ,0 ,0 ))
    screen .blit (title ,(WIDTH //2 -title .get_width ()//2 ,HEIGHT //2 -120 ))
    sub =secondary_font .render ('Veuillez relancer le jeu. Si cela se reproduit, indiquez le type et le code.',True ,(40 ,40 ,40 ))
    screen .blit (sub ,(WIDTH //2 -sub .get_width ()//2 ,HEIGHT //2 -78 ))
    if msg :
        m1 =small_font .render (f"Message: {msg }",True ,(60 ,60 ,60 ))
        screen .blit (m1 ,(WIDTH //2 -m1 .get_width ()//2 ,HEIGHT //2 -45 ))
    btn_w ,btn_h =220 ,56 
    btn_x ,btn_y =WIDTH //2 -btn_w //2 ,HEIGHT //2 +10 
    quit_btn =Button ((btn_x ,btn_y ,btn_w ,btn_h ),'Quitter',(200 ,80 ,80 ),(255 ,255 ,255 ))
    quit_btn .draw (screen ,pygame .mouse .get_pos ())
    globals ()['_error_quit_rect']=quit_btn .rect 
    return True 

mouse_pos =(0 ,0 )
running =True 
_GP_HUD_DRAWN =False 
_GP_HUD_CALLERS =[]

if not captcha_completed :
    game_state ='loading'
    loading_start_ms =pygame .time .get_ticks ()
    loading_mode ='initial'

    loading_total_kb =compute_loading_total_kb ()
    loading_duration_ms =int (math .ceil (1000.0 *(loading_total_kb /KB_PER_SEC )))
    loaded_kb_display =0.0 
    loading_step_accum_ms =0 
else :
    game_state ='menu'
start_time =time .time ()
last_auto_tick =pygame .time .get_ticks ()
last_sps_tick =pygame .time .get_ticks ()
clicks_in_last_second =0 

try :
    if not captcha_completed :
        pick_captcha_question_index ()
    while running :

        try :
            gm =game_settings .get ("graphics_mode","graphismes_travaillés")
        except Exception :
            gm ="graphismes_travaillés"
        target_fps =MAX_FPS_GRAPHICS if gm =="graphismes_travaillés"else MAX_FPS_PERFORMANCE 
        dt =clock .tick (target_fps )

        if _error_overlay .get ("active",False ):
            draw_error_overlay_loop ()
            for event in pygame .event .get ():
                if event .type ==pygame .QUIT :
                    running =False 
                elif event .type ==pygame .MOUSEBUTTONDOWN and event .button ==1 :
                    r =globals ().get ("_error_quit_rect")
                    if r and r .collidepoint (event .pos ):
                        running =False 
            pygame .display .flip ()
            continue 


        try :
            fps_now =clock .get_fps ()if hasattr (clock ,'get_fps')else (1000.0 /dt if dt >0 else 0.0 )
        except Exception :
            fps_now =(1000.0 /dt )if dt >0 else 0.0 

        if (not low_fps_switched_to_performance )and gm =="graphismes_travaillés"and fps_now >0 and fps_now <45 :
            try :
                game_settings ["graphics_mode"]="performance"
                low_fps_switched_to_performance =True 
                log_event (f"Auto-switch graphique -> performance à cause du faible FPS: {fps_now :.1f}")
            except Exception :
                pass 
        for event in pygame .event .get ():

            if handle_version_and_snapshot_popups (event ):
                continue 

            if welcome_popup .get ("open",False ):
                if event .type ==pygame .MOUSEBUTTONDOWN and event .button ==1 :
                    rok =welcome_popup .get ("rect_ok")
                    if rok and rok .collidepoint (event .pos ):
                        welcome_popup ["open"]=False 

                        if globals ().get ('current_screen')=='menu':
                            globals ()['_open_version_from_settings']=True 
                            globals ()['show_version_popup']=True 
                        continue 
                if event .type ==pygame .KEYDOWN and event .key ==pygame .K_ESCAPE :
                    welcome_popup ["open"]=False 

                    continue 

                if event .type in (pygame .MOUSEBUTTONDOWN ,pygame .MOUSEBUTTONUP ,
                pygame .MOUSEWHEEL ,pygame .MOUSEMOTION ):
                    continue 


            if event .type ==pygame .KEYDOWN :

                if 'dev_password_mode'in globals ()and dev_password_mode :
                    now =pygame .time .get_ticks ()
                    if event .key ==pygame .K_ESCAPE :
                        dev_password_mode =False 
                        dev_password_text =''
                        dev_password_visible =False 
                        dev_password_caret =0 
                        dev_password_caret_visible =True 
                        dev_password_last_blink_ms =now 

                    elif event .key ==pygame .K_RETURN :
                        if dev_password_text =='speduZtas8#7apR!bipuq?fi':
                            developer_mode_active =True 
                            add_notification ('Mode développeur activé.',1600 )
                            log_event ('Mode développeur ACTIF')
                            dev_password_mode =False 
                            dev_password_text =''
                            dev_password_visible =False 
                            dev_password_caret =0 
                            dev_password_caret_visible =True 
                            dev_password_last_blink_ms =now 
                            game_state ='menu'
                        else :
                            add_notification ('Mot de passe incorrect.',1600 )
                            dev_password_text =''
                            dev_password_caret =0 
                            dev_password_caret_visible =True 
                            dev_password_last_blink_ms =now 

                    elif event .key ==pygame .K_DELETE :
                        dev_password_text =''
                        dev_password_caret =0 

                    elif event .key ==pygame .K_BACKSPACE :
                        if dev_password_caret >0 :
                            dev_password_text =(dev_password_text [:dev_password_caret -1 ]
                            +dev_password_text [dev_password_caret :])
                            dev_password_caret -=1 

                    elif event .key ==pygame .K_LEFT :
                        dev_password_caret =max (0 ,dev_password_caret -1 )

                    elif event .key ==pygame .K_RIGHT :
                        dev_password_caret =min (len (dev_password_text ),dev_password_caret +1 )

                    elif event .key ==pygame .K_HOME :
                        dev_password_caret =0 

                    elif event .key ==pygame .K_END :
                        dev_password_caret =len (dev_password_text )

                    else :
                        if event .unicode and len (dev_password_text )<40 and 31 <ord (event .unicode )!=127 :
                            dev_password_text =(dev_password_text [:dev_password_caret ]
                            +event .unicode 
                            +dev_password_text [dev_password_caret :])
                            dev_password_caret +=1 

                    dev_password_caret_visible =True 
                    dev_password_last_blink_ms =now 
                    continue 


                if 'code_input_mode'in globals ()and code_input_mode is not None :
                    now =pygame .time .get_ticks ()
                    if event .key ==pygame .K_ESCAPE :
                        code_input_mode =None 

                        code_input_caret =0 
                        code_input_caret_visible =True 
                        code_input_last_blink_ms =now 

                    elif event .key ==pygame .K_RETURN :
                        code =code_input_text .strip ()
                        if not code :
                            add_notification ("Entre un code.",1400 )
                        else :
                            lc =code .lower ()
                            if lc in used_codes :
                                add_notification ("Code déjà utilisé.",1600 )
                            else :
                                ok =apply_dev_code (lc )
                                if not ok :
                                    add_notification ("Code invalide.",1600 )
                                else :
                                    used_codes .add (lc )
                                    code_input_mode =None 
                                    code_input_text =""
                                    code_input_caret =0 
                                    code_input_caret_visible =True 
                                    code_input_last_blink_ms =now 

                    elif event .key ==pygame .K_DELETE :

                        code_input_text =""
                        code_input_caret =0 

                    elif event .key ==pygame .K_BACKSPACE :
                        if code_input_caret >0 :
                            code_input_text =(code_input_text [:code_input_caret -1 ]
                            +code_input_text [code_input_caret :])
                            code_input_caret -=1 

                    elif event .key ==pygame .K_LEFT :
                        code_input_caret =max (0 ,code_input_caret -1 )

                    elif event .key ==pygame .K_RIGHT :
                        code_input_caret =min (len (code_input_text ),code_input_caret +1 )

                    elif event .key ==pygame .K_HOME :
                        code_input_caret =0 

                    elif event .key ==pygame .K_END :
                        code_input_caret =len (code_input_text )

                    else :
                        if event .unicode and len (code_input_text )<40 and 31 <ord (event .unicode )!=127 :
                            code_input_text =(code_input_text [:code_input_caret ]
                            +event .unicode 
                            +code_input_text [code_input_caret :])
                            code_input_caret +=1 

                    code_input_caret_visible =True 
                    code_input_last_blink_ms =now 
                    continue 


                if 'reset_confirm'in globals ()and reset_confirm .get ("open",False ):
                    if event .key ==pygame .K_ESCAPE :
                        reset_confirm ["open"]=False 
                        reset_confirm ["kind"]=None 
                        reset_confirm ["rect_yes"]=None 
                        reset_confirm ["rect_no"]=None 
                        continue 


            if event .type ==pygame .MOUSEBUTTONDOWN and event .button ==1 :

                if 'reset_confirm'in globals ()and reset_confirm .get ("open",False ):
                    yes_r =reset_confirm .get ("rect_yes")
                    no_r =reset_confirm .get ("rect_no")
                    if yes_r and yes_r .collidepoint (event .pos ):
                        kind =reset_confirm .get ("kind","")
                        ok =False 
                        if kind =="Renaissance":
                            ok =do_reset_renaissance ()
                            if ok and tutorial_active and tutorial_mode =='interactive':
                                renaissance_done =True 
                            if ok :
                                add_notification ("Renaissance !",2000 )
                            else :
                                add_notification ("Score insuffisant.",1500 )
                        elif kind =="Prestige":
                            ok =do_reset_prestige ()
                            add_notification ("Prestige !"if ok else "Score insuffisant.",2000 if ok else 1500 )
                        elif kind =="Ascension":
                            ok =do_reset_ascension ()
                            add_notification ("Ascension !"if ok else "Score insuffisant.",2000 if ok else 1500 )
                        elif kind =="Réincarnation":
                            ok =do_reset_reincarnation ()
                            add_notification ("Réincarnation !"if ok else "Score insuffisant.",2000 if ok else 1500 )
                        elif kind =="Infinité":
                            ok =do_reset_infinity ()
                            add_notification ("INFINITÉ !"if ok else "Score insuffisant.",2400 if ok else 1500 )

                        reset_confirm ["open"]=False 
                        reset_confirm ["kind"]=None 
                        reset_confirm ["rect_yes"]=None 
                        reset_confirm ["rect_no"]=None 
                        continue 
                    elif no_r and no_r .collidepoint (event .pos ):
                        reset_confirm ["open"]=False 
                        reset_confirm ["kind"]=None 
                        reset_confirm ["rect_yes"]=None 
                        reset_confirm ["rect_no"]=None 
                        continue 

                if reset_flow .get ("state",0 )>0 and not reset_flow .get ("in_progress",False ):
                    cont_r =_reset_btn_rects .get ("cont")
                    back_r =_reset_btn_rects .get ("back")
                    if back_r and back_r .collidepoint (event .pos ):
                        reset_flow ["state"]=0 
                        reset_flow ["clicks"]=0 
                        reset_flow ["start_ms"]=-1 
                        continue 
                    if cont_r and cont_r .collidepoint (event .pos ):
                        st =reset_flow .get ("state",1 )
                        if st ==1 :
                            reset_flow ["state"]=2 
                        elif st ==2 :
                            reset_flow ["state"]=3 
                            reset_flow ["clicks"]=0 
                            reset_flow ["start_ms"]=pygame .time .get_ticks ()
                        else :
                            reset_flow ["clicks"]=reset_flow .get ("clicks",0 )+1 
                            if reset_flow .get ("start_ms",-1 )<0 :
                                reset_flow ["start_ms"]=pygame .time .get_ticks ()
                            if reset_flow ["clicks"]>=10 :
                                reset_flow ["in_progress"]=True 
                                reset_flow ["progress_start_ms"]=-1 
                        continue 

                if 'dev_password_mode'in globals ()and dev_password_mode :
                    if dev_password_eye_rect and dev_password_eye_rect .collidepoint (event .pos ):
                        dev_password_visible =not dev_password_visible 
                        continue 
                    if dev_password_box_rect and dev_password_box_rect .collidepoint (event .pos ):
                        shown =dev_password_text if dev_password_visible else ("*"*len (dev_password_text ))
                        disp ,vis_start =_display_with_ellipsis (shown ,dev_password_text_max_w ,font )
                        dev_password_caret =_caret_from_click (shown ,vis_start ,dev_password_text_left_x ,event .pos [0 ],font )
                        dev_password_caret_visible =True 
                        dev_password_last_blink_ms =pygame .time .get_ticks ()
                        continue 


                if 'code_input_mode'in globals ()and code_input_mode is not None :
                    if code_input_box_rect and code_input_box_rect .collidepoint (event .pos ):
                        shown =code_input_text 
                        disp ,vis_start =_display_with_ellipsis (shown ,code_input_text_max_w ,font )
                        code_input_caret =_caret_from_click (shown ,vis_start ,code_input_text_left_x ,event .pos [0 ],font )
                        code_input_caret_visible =True 
                        code_input_last_blink_ms =pygame .time .get_ticks ()
                        continue 


            if overlays_open ():
                continue 


            if event .type ==pygame .MOUSEBUTTONDOWN and event .button ==1 :

                if not secret_bonus_unlocked :
                    now =time .time ()
                    if (not secret_shape_active and 
                    now -secret_shape_last_spawn >secret_shape_interval ):
                        secret_shape_obj =FloatingShape ()
                        secret_shape_obj .shape ="decagon"
                        secret_shape_obj .size =random .randint (45 ,120 )
                        secret_shape_obj .x =random .uniform (80 ,WIDTH -80 )
                        secret_shape_obj .y =random .uniform (100 ,HEIGHT -100 )
                        secret_shape_obj .vx =random .uniform (-80 ,80 )
                        secret_shape_obj .vy =random .uniform (-80 ,80 )
                        secret_shape_active =True 
                        secret_shape_last_spawn =now 

                        if difficulty ==DIFF_VERY_EASY :
                            add_notification ("La forme secrète dorée vient d’apparaître !",2500 )


                if secret_shape_active and secret_shape_obj and not secret_bonus_unlocked :
                    mx ,my =pygame .mouse .get_pos ()
                    dx =mx -secret_shape_obj .x 
                    dy =my -secret_shape_obj .y 
                    dist =math .hypot (dx ,dy )
                    if dist <=secret_shape_obj .size *0.6 :
                        secret_shape_active =False 
                        secret_shape_obj =None 
                        secret_bonus_unlocked =True 
                        game_data ['score_multiplier_secret']=2.0 
                        add_notification ("Polygone secret cliqué ! Score x2 pour toujours !",2800 )

            if event .type ==pygame .QUIT :
                running =False 
            elif event .type ==pygame .KEYDOWN :
                if game_state =='dev_commands'and dev_ui_tab =='score':
                    now =pygame .time .get_ticks ()
                    if event .key ==pygame .K_ESCAPE :
                        dev_score_input_text =""
                        dev_score_caret =0 
                        dev_score_caret_visible =True 
                        dev_score_last_blink_ms =now 
                        continue 
                    elif event .key ==pygame .K_RETURN :
                        s =dev_score_input_text .strip ()
                        if not s :
                            add_notification ("Entrez un montant de score.",1600 )
                        else :
                            L =validate_dev_input (s )
                            if L ==NEG_INF :
                                add_notification ("Montant invalide.",1800 )
                            else :
                                game_data ["score_log10"]=log10_add (game_data ["score_log10"],L )
                                add_notification (f"+{s } score (dev)",1600 )
                                log_event (f"Dev Score +{s }")
                        continue 
                    elif event .key ==pygame .K_DELETE :
                        dev_score_input_text =""
                        dev_score_caret =0 
                    elif event .key ==pygame .K_BACKSPACE :
                        if dev_score_caret >0 :
                            dev_score_input_text =(dev_score_input_text [:dev_score_caret -1 ]
                            +dev_score_input_text [dev_score_caret :])
                            dev_score_caret -=1 
                    elif event .key ==pygame .K_LEFT :
                        dev_score_caret =max (0 ,dev_score_caret -1 )
                    elif event .key ==pygame .K_RIGHT :
                        dev_score_caret =min (len (dev_score_input_text ),dev_score_caret +1 )
                    elif event .key ==pygame .K_HOME :
                        dev_score_caret =0 
                    elif event .key ==pygame .K_END :
                        dev_score_caret =len (dev_score_input_text )
                    else :

                        if event .unicode and len (dev_score_input_text )<80 and 31 <ord (event .unicode )!=127 :
                            dev_score_input_text =(dev_score_input_text [:dev_score_caret ]
                            +event .unicode 
                            +dev_score_input_text [dev_score_caret :])
                            dev_score_caret +=1 

                    dev_score_caret_visible =True 
                    dev_score_last_blink_ms =now 
                    continue 

                if game_state =='dev_commands'and dev_ui_tab =='pi':
                    now =pygame .time .get_ticks ()
                    if event .key ==pygame .K_ESCAPE :
                        dev_pi_input_text =""
                        dev_pi_caret =0 
                        dev_pi_caret_visible =True 
                        dev_pi_last_blink_ms =now 
                        continue 
                    elif event .key ==pygame .K_RETURN :
                        s =dev_pi_input_text .strip ()
                        if not s :
                            add_notification ("Entrez un montant de PI.",1600 )
                        else :
                            L =parse_amount_to_log10 (s )
                            if L ==NEG_INF :
                                add_notification ("Montant invalide.",1800 )
                            else :
                                try :

                                    if L <300 :
                                        n =int (round (10 **L ))
                                        game_data ["PI"]=game_data .get ("PI",0 )+n 
                                        add_notification (f"+{format_points_pretty (math .log10 (n )if n >0 else NEG_INF )} PI (dev)",1600 )
                                        log_event (f"Dev PI +{n }")
                                    else :

                                        add_notification ("Valeur trop élevée, aucun PI ajouté (max ≈ 1e300).",2000 )
                                except OverflowError :
                                    add_notification ("Valeur trop élevée (overflow), aucun PI ajouté.",2000 )
                                except Exception :
                                    add_notification ("Erreur inattendue pendant l’ajout de PI.",2000 )
                        continue 
                    elif event .key ==pygame .K_DELETE :
                        dev_pi_input_text =""
                        dev_pi_caret =0 
                    elif event .key ==pygame .K_BACKSPACE :
                        if dev_pi_caret >0 :
                            dev_pi_input_text =(dev_pi_input_text [:dev_pi_caret -1 ]
                            +dev_pi_input_text [dev_pi_caret :])
                            dev_pi_caret -=1 
                    elif event .key ==pygame .K_LEFT :
                        dev_pi_caret =max (0 ,dev_pi_caret -1 )
                    elif event .key ==pygame .K_RIGHT :
                        dev_pi_caret =min (len (dev_pi_input_text ),dev_pi_caret +1 )
                    elif event .key ==pygame .K_HOME :
                        dev_pi_caret =0 
                    elif event .key ==pygame .K_END :
                        dev_pi_caret =len (dev_pi_input_text )
                    else :

                        if event .unicode and len (dev_pi_input_text )<80 and 31 <ord (event .unicode )!=127 :
                            dev_pi_input_text =(dev_pi_input_text [:dev_pi_caret ]
                            +event .unicode 
                            +dev_pi_input_text [dev_pi_caret :])
                            dev_pi_caret +=1 

                    dev_pi_caret_visible =True 
                    dev_pi_last_blink_ms =now 
                    continue 


                if dev_password_mode :
                    now =pygame .time .get_ticks ()

                    if event .key ==pygame .K_ESCAPE :
                        dev_password_mode =False 
                        dev_password_text =''
                        dev_password_visible =False 
                        dev_password_caret =0 
                        dev_password_caret_visible =True 
                        dev_password_last_blink_ms =now 

                    elif event .key ==pygame .K_RETURN :
                        if dev_password_text =='speduZtas8#7apR!bipuq?fi':
                            developer_mode_active =True 
                            add_notification ('Mode développeur activé.',1600 )
                            log_event ('Mode développeur ACTIF')
                            dev_password_mode =False 
                            dev_password_text =''
                            dev_password_visible =False 
                            dev_password_caret =0 
                            dev_password_caret_visible =True 
                            dev_password_last_blink_ms =now 
                            game_state ='menu'
                        else :
                            add_notification ('Mot de passe incorrect.',1600 )
                            dev_password_text =''
                            dev_password_caret =0 
                            dev_password_caret_visible =True 
                            dev_password_last_blink_ms =now 

                    elif event .key ==pygame .K_DELETE :
                        dev_password_text =''
                        dev_password_caret =0 

                    elif event .key ==pygame .K_BACKSPACE :
                        if dev_password_caret >0 :
                            dev_password_text =(dev_password_text [:dev_password_caret -1 ]
                            +dev_password_text [dev_password_caret :])
                            dev_password_caret -=1 

                    elif event .key ==pygame .K_LEFT :
                        dev_password_caret =max (0 ,dev_password_caret -1 )

                    elif event .key ==pygame .K_RIGHT :
                        dev_password_caret =min (len (dev_password_text ),dev_password_caret +1 )

                    elif event .key ==pygame .K_HOME :
                        dev_password_caret =0 

                    elif event .key ==pygame .K_END :
                        dev_password_caret =len (dev_password_text )

                    else :
                        if event .unicode and len (dev_password_text )<40 and 31 <ord (event .unicode )!=127 :
                            dev_password_text =(dev_password_text [:dev_password_caret ]
                            +event .unicode 
                            +dev_password_text [dev_password_caret :])
                            dev_password_caret +=1 

                    dev_password_caret_visible =True 
                    dev_password_last_blink_ms =now 

                    continue 

                now =pygame .time .get_ticks ()
                if event .key ==pygame .K_ESCAPE :
                    code_input_mode =None 

                    code_input_caret =0 
                    code_input_caret_visible =True 
                    code_input_last_blink_ms =now 

                elif event .key ==pygame .K_RETURN :
                    code =code_input_text .strip ()
                    if not code :
                        add_notification ("Entre un code.",1400 )
                    else :
                        lc =code .lower ()
                        if lc in used_codes :
                            add_notification ("Code déjà utilisé.",1600 )
                        else :
                            ok =False 
                            ok =apply_dev_code (lc )
                            if not ok :
                                add_notification ("Code invalide.",1600 )
                            else :
                                used_codes .add (lc )
                                code_input_mode =None 
                                code_input_text =""
                                code_input_caret =0 
                                code_input_caret_visible =True 
                                code_input_last_blink_ms =now 

                elif event .key ==pygame .K_DELETE :

                    code_input_text =""
                    code_input_caret =0 

                elif event .key ==pygame .K_BACKSPACE :
                    if code_input_caret >0 :
                        code_input_text =(code_input_text [:code_input_caret -1 ]
                        +code_input_text [code_input_caret :])
                        code_input_caret -=1 

                elif event .key ==pygame .K_LEFT :
                    code_input_caret =max (0 ,code_input_caret -1 )

                elif event .key ==pygame .K_RIGHT :
                    code_input_caret =min (len (code_input_text ),code_input_caret +1 )

                elif event .key ==pygame .K_HOME :
                    code_input_caret =0 

                elif event .key ==pygame .K_END :
                    code_input_caret =len (code_input_text )

                else :
                    if event .unicode and len (code_input_text )<40 and 31 <ord (event .unicode )!=127 :
                        code_input_text =(code_input_text [:code_input_caret ]
                        +event .unicode 
                        +code_input_text [code_input_caret :])
                        code_input_caret +=1 

                code_input_caret_visible =True 
                code_input_last_blink_ms =now 

            elif event .type ==pygame .MOUSEBUTTONDOWN and event .button ==1 :
                if dev_password_mode :
                    if dev_password_mode and dev_password_eye_rect and dev_password_eye_rect .collidepoint (event .pos ):
                        dev_password_visible =not dev_password_visible 
                        continue 

                    if dev_password_box_rect and dev_password_box_rect .collidepoint (event .pos ):
                        shown =dev_password_text if dev_password_visible else ("*"*len (dev_password_text ))
                        disp ,vis_start =_display_with_ellipsis (shown ,dev_password_text_max_w ,font )
                        dev_password_caret =_caret_from_click (shown ,vis_start ,dev_password_text_left_x ,event .pos [0 ],font )
                        dev_password_caret_visible =True 
                        dev_password_last_blink_ms =pygame .time .get_ticks ()
                        continue 

                if code_input_mode is not None and code_input_box_rect and code_input_box_rect .collidepoint (event .pos ):
                    shown =code_input_text 
                    disp ,vis_start =_display_with_ellipsis (shown ,code_input_text_max_w ,font )
                    code_input_caret =_caret_from_click (shown ,vis_start ,code_input_text_left_x ,event .pos [0 ],font )
                    code_input_caret_visible =True 
                    code_input_last_blink_ms =pygame .time .get_ticks ()

                if game_state =='captcha':
                    if captcha_true_button .rect .collidepoint (event .pos )or captcha_false_button .rect .collidepoint (event .pos ):
                        user_ans =True if captcha_true_button .rect .collidepoint (event .pos )else False 
                        qa =CAPTCHA_QA [captcha_question_index ]
                        if user_ans ==qa ['ans']:
                            add_notification ('Captcha réussi !',1600 )
                            globals ()['captcha_completed']=True 

                            globals ()['game_state']='difficulty_select'
                            mini_notifs ['tutorial']=True 
                        else :
                            globals ()['captcha_attempts_left']-=1 
                            if captcha_attempts_left <=0 :
                                add_notification ('Captcha échoué (3 tentatives). Fermeture...',2200 )
                                running =False 
                            else :
                                add_notification ('Mauvaise réponse. Nouvelle question.',1600 )
                                pick_captcha_question_index ()
                        continue 
                if game_state =='main':
                    if click_button .rect .collidepoint (event .pos ):
                        now_click =pygame .time .get_ticks ()

                        if now_click <globals ().get ('click_block_until_ms',0 ):
                            add_notification ("Cliquage temporairement désactivé (anticheat).",1400 )
                            continue 

                        click_button .bounce ()
                        game_data ["total_clicks"]=game_data .get ("total_clicks",0 )+1 
                        clicks_in_last_second +=1 
                        if tutorial_active and tutorial_mode =='interactive'and tutorial_step >=8 :
                            clicks_done +=1 
                        addL =log10_effective_click_value ()
                        addL =apply_gain_modifiers (addL )
                        if game_data .get ('score_multiplier_secret',1.0 )>1.0 :
                            addL +=math .log10 (game_data ['score_multiplier_secret'])
                        game_data ["score_log10"]=log10_add (game_data ["score_log10"],addL )
                        if game_settings ["graphics_mode"]=="graphismes_travaillés":
                            spawn_click_explosion (click_button .rect .centerx ,
                            click_button .rect .centery ,
                            (80 ,180 ,255 ))
                    if upgrade_auto_button .rect .collidepoint (event .pos ):
                        pre =game_data ['auto_value']
                        if game_settings ["purchase_mode"]=="single":ok =buy_upgrade ("auto")
                        else :
                            ok =False ;buy_upgrade_max ("auto");ok =game_data ['auto_value']>pre 
                        if tutorial_active and tutorial_mode =='interactive'and ok :
                            auto_upgrades +=(game_data ['auto_value']-pre )
                    if upgrade_click_button .rect .collidepoint (event .pos ):
                        pre =game_data ['click_value']
                        if game_settings ["purchase_mode"]=="single":ok =buy_upgrade ("click")
                        else :
                            ok =False ;old =game_data ['click_value'];buy_upgrade_max ("click");ok =game_data ['click_value']>old 
                        if tutorial_active and tutorial_mode =='interactive'and ok :
                            delta =max (1 ,int ((game_data ['click_value']-pre )//0.75 ))
                            click_upgrades +=delta 
                    if upgrade_mult_button .rect .collidepoint (event .pos ):
                        preL =game_data .get ("multiplier_log10",0.0 )
                        if game_settings ["purchase_mode"]=="single":ok =buy_upgrade ("mult")
                        else :
                            ok =False ;buy_upgrade_max ("mult");ok =game_data .get ("multiplier_log10",0.0 )>preL 
                        if tutorial_active and tutorial_mode =='interactive'and ok :
                            mult_upgrades +=1 

                    if reset_confirm .get ("open",False ):
                        yes_r =reset_confirm .get ("rect_yes")
                        no_r =reset_confirm .get ("rect_no")
                        if yes_r and yes_r .collidepoint (event .pos ):
                            kind =reset_confirm .get ("kind","")
                            ok =False 
                            if kind =="Renaissance":
                                ok =do_reset_renaissance ()
                                if ok and tutorial_active and tutorial_mode =='interactive':
                                    renaissance_done =True 
                                if ok :
                                    add_notification ("Renaissance !",2000 )
                                else :
                                    add_notification ("Score insuffisant.",1500 )
                            elif kind =="Prestige":
                                ok =do_reset_prestige ()
                                add_notification ("Prestige !"if ok else "Score insuffisant.",2000 if ok else 1500 )
                            elif kind =="Ascension":
                                ok =do_reset_ascension ()
                                add_notification ("Ascension !"if ok else "Score insuffisant.",2000 if ok else 1500 )
                            elif kind =="Réincarnation":
                                ok =do_reset_reincarnation ()
                                add_notification ("Réincarnation !"if ok else "Score insuffisant.",2000 if ok else 1500 )
                            elif kind =="Infinité":
                                ok =do_reset_infinity ()
                                add_notification ("INFINITÉ !"if ok else "Score insuffisant.",2400 if ok else 1500 )

                            reset_confirm ["open"]=False 
                            reset_confirm ["kind"]=None 
                            reset_confirm ["rect_yes"]=None 
                            reset_confirm ["rect_no"]=None 
                            continue 
                        elif no_r and no_r .collidepoint (event .pos ):
                            reset_confirm ["open"]=False 
                            reset_confirm ["kind"]=None 
                            reset_confirm ["rect_yes"]=None 
                            reset_confirm ["rect_no"]=None 
                            continue 

                    def _open_reset_confirm (kind_label :str ):
                        reset_confirm ["open"]=True 
                        reset_confirm ["kind"]=kind_label 
                        reset_confirm ["rect_yes"]=None 
                        reset_confirm ["rect_no"]=None 

                    if renaissance_button .rect .collidepoint (event .pos ):
                        if game_settings .get ("confirm_resets",True ):
                            open_reset_or_notify ('Renaissance')
                        else :
                            if do_reset_renaissance ():
                                add_notification ("Renaissance !",2000 )
                                if tutorial_active and tutorial_mode =='interactive':
                                    renaissance_done =True 
                            else :
                                add_notification ("Score insuffisant.",1500 )
                        continue 

                    if prestige_button .rect .collidepoint (event .pos ):
                        if game_settings .get ("confirm_resets",True ):
                            open_reset_or_notify ('Prestige')
                        else :
                            if do_reset_prestige ():
                                add_notification ("Prestige !",2000 )
                            else :
                                add_notification ("Score insuffisant.",1500 )
                        continue 

                    if ascension_button .rect .collidepoint (event .pos ):
                        if game_settings .get ("confirm_resets",True ):
                            open_reset_or_notify ('Ascension')
                        else :
                            if do_reset_ascension ():
                                add_notification ("Ascension !",2000 )
                            else :
                                add_notification ("Score insuffisant.",1500 )
                        continue 

                    if reinc_button .rect .collidepoint (event .pos ):
                        if game_settings .get ("confirm_resets",True ):
                            open_reset_or_notify ('Réincarnation')
                        else :
                            if do_reset_reincarnation ():
                                add_notification ("Réincarnation !",2000 )
                            else :
                                add_notification ("Score insuffisant.",1500 )
                        continue 

                    if infinity_button .rect .collidepoint (event .pos ):
                        if game_settings .get ("confirm_resets",True ):
                            open_reset_or_notify ('Infinité')
                        else :
                            if do_reset_infinity ():
                                add_notification ("INFINITÉ !",2400 )
                            else :
                                add_notification ("Score insuffisant.",1500 )
                        continue 

                    show_gr =gr_button_is_visible ()
                    gr_btn_rect =pygame .Rect (WIDTH -320 ,620 ,300 ,74 )

                    if show_gr :
                        if gr_btn_rect .collidepoint (event .pos )and not overlays_open ():
                            cost =next_gr_cost_pi ()
                            if game_data .get ('PI',0 )>=cost :
                                gr_confirm ["open"]=True 
                                gr_confirm ["rect_yes"]=None 
                                gr_confirm ["rect_no"]=None 
                            else :
                                add_notification ("PI insuffisants pour GR.",1800 )
                            continue 

                    if gr_confirm .get ("open",False ):
                        if gr_confirm .get ("rect_yes")and gr_confirm ["rect_yes"].collidepoint (event .pos ):
                            perform_grand_reset_now ()
                            gr_confirm ["open"]=False 
                            continue 
                        if gr_confirm .get ("rect_no")and gr_confirm ["rect_no"].collidepoint (event .pos ):
                            gr_confirm ["open"]=False 
                            continue 

                        if gr_btn_rect .collidepoint (event .pos ):
                            if game_data .get ('PI',0 )>=next_gr_cost_pi ():

                                gr_confirm ["open"]=True 
                                gr_confirm ["rect_yes"]=None 
                                gr_confirm ["rect_no"]=None 
                            else :
                                add_notification ("PI insuffisants pour GR.",1800 )

                    menu_btn =pygame .Rect (20 ,HEIGHT -60 ,140 ,44 )
                    if menu_btn .collidepoint (event .pos ):
                        game_state ='captcha'if not captcha_completed else 'menu'
                        if tutorial_active and tutorial_mode =='interactive':
                            visited_menu =True 

                    if tutorial_active and tutorial_mode =='interactive':
                        if _tut_prev_rect and _tut_prev_rect .collidepoint (event .pos ):
                            tutorial_step =max (1 ,tutorial_step -1 )
                        if _tut_skip_rect and _tut_skip_rect .collidepoint (event .pos ):
                            tutorial_active =False ;tutorial_mode =None 
                            add_notification ("Tutoriel ignoré.",1600 )
                        if _tut_next_rect and _tut_next_rect .collidepoint (event .pos ):
                            if tutorial_step ==TUTORIAL_LAST_STEP :
                                curL =game_data ['points_log10']['R']
                                cur =0 if curL ==NEG_INF else (10 **curL )
                                need =max (0.0 ,10.0 -cur )
                                if need >0 :
                                    game_data ['points_log10']['R']=log10_add (curL ,math .log10 (need ))
                                tutorial_active =False ;tutorial_mode =None 
                                add_notification ("Tutoriel terminé : total 10 pts R garanti !",2800 )
                                mini_notifs ['play']=True 
                            else :
                                if is_step_condition_met (tutorial_step ):
                                    tutorial_step =min (TUTORIAL_LAST_STEP ,tutorial_step +1 )

                elif game_state =='achievements':
                    changed =False 
                    for key ,r in list (_ach_cat_btns .items ()):
                        if r and r .collidepoint (event .pos ):
                            selected_ach_category =key 
                            ach_page_index_by_cat [key ]=0 
                            changed =True 
                            break 
                    if not changed :
                        prev_r =_ach_nav_btns .get ('prev')
                        next_r =_ach_nav_btns .get ('next')
                        cur_page =ach_page_index_by_cat .get (selected_ach_category ,0 )
                        items =ACH_CATEGORIES .get (selected_ach_category ,[])
                        cols =2 
                        card_h =84 
                        gap_y =10 
                        top_y =150 
                        bottom_reserved =120 
                        avail_h =max (0 ,HEIGHT -top_y -bottom_reserved )
                        rows_per_col =max (1 ,avail_h //(card_h +gap_y ))
                        items_per_page =rows_per_col *cols 
                        total_pages =max (1 ,(len (items )+items_per_page -1 )//items_per_page )
                        if prev_r and prev_r .collidepoint (event .pos )and cur_page >0 :
                            ach_page_index_by_cat [selected_ach_category ]=cur_page -1 
                        elif next_r and next_r .collidepoint (event .pos )and cur_page <total_pages -1 :
                            ach_page_index_by_cat [selected_ach_category ]=cur_page +1 
                    if back_button .rect .collidepoint (event .pos ):
                        game_state ='captcha'if not captcha_completed else 'menu'
                        if tutorial_active and tutorial_mode =='interactive':
                            visited_menu =True 
                elif game_state =='menu':

                    if quit_confirm .get ("open",False ):
                        if quit_confirm .get ("rect_yes")and quit_confirm ["rect_yes"].collidepoint (event .pos ):
                            running =False 
                        elif quit_confirm .get ("rect_no")and quit_confirm ["rect_no"].collidepoint (event .pos ):
                            quit_confirm ["open"]=False 

                        continue 
                    if menu_buttons ["play"].rect .collidepoint (event .pos ):
                        mini_notifs ['play']=False 
                        game_state ='main'
                        if tutorial_active and tutorial_mode =='interactive':
                            visited_play =True 
                    elif menu_buttons ["milestones"].rect .collidepoint (event .pos ):
                        mini_notifs ['milestones']=False 
                        game_state ='milestones'
                    elif menu_buttons ["challenges"].rect .collidepoint (event .pos ):
                        if challenges_menu_accessible ():
                            game_state ='challenges'
                        else :
                            add_notification ("Les challenges ne sont pas encore accessibles.",1800 )
                    elif menu_buttons ["achievements"].rect .collidepoint (event .pos ):
                        mini_notifs ['achievements']=False 
                        game_state ='achievements'
                    elif menu_buttons ["settings"].rect .collidepoint (event .pos ):game_state ='settings'
                    elif menu_buttons ["history"].rect .collidepoint (event .pos ):game_state ='history'
                    elif menu_buttons ["tutorial"].rect .collidepoint (event .pos ):
                        mini_notifs ['tutorial']=False 
                        game_state ='tutorial'
                    elif menu_buttons ["quit"].rect .collidepoint (event .pos ):

                        quit_confirm ["open"]=True 
                        quit_confirm ["rect_yes"]=None 
                        quit_confirm ["rect_no"]=None 

                    if tutorial_active and tutorial_mode =='interactive':
                        if _tut_prev_rect and _tut_prev_rect .collidepoint (event .pos ):
                            tutorial_step =max (1 ,tutorial_step -1 )
                        if _tut_skip_rect and _tut_skip_rect .collidepoint (event .pos ):
                            tutorial_active =False ;tutorial_mode =None 
                            add_notification ("Tutoriel ignoré.",1600 )
                        if _tut_next_rect and _tut_next_rect .collidepoint (event .pos ):
                            if tutorial_step ==TUTORIAL_LAST_STEP :
                                curL =game_data ['points_log10']['R']
                                cur =0 if curL ==NEG_INF else (10 **curL )
                                need =max (0.0 ,10.0 -cur )
                                if need >0 :
                                    game_data ['points_log10']['R']=log10_add (curL ,math .log10 (need ))
                                tutorial_active =False ;tutorial_mode =None 
                                add_notification ("Tutoriel terminé : total 10 pts R garanti !",2800 )
                            else :
                                if is_step_condition_met (tutorial_step ):
                                    tutorial_step =min (TUTORIAL_LAST_STEP ,tutorial_step +1 )
                elif game_state =='milestones':

                    prev_r =_milestones_nav .get ("prev")
                    next_r =_milestones_nav .get ("next")
                    if prev_r and prev_r .collidepoint (event .pos ):
                        _milestones_page =max (0 ,_milestones_page -1 )
                        continue 
                    elif next_r and next_r .collidepoint (event .pos ):
                        _milestones_page =min (1 ,_milestones_page +1 )
                        continue 

                    if back_button .rect .collidepoint (event .pos ):
                        game_state ='captcha'if not captcha_completed else 'menu'

                        if tutorial_active and tutorial_mode =='interactive':
                            visited_menu =True 
                    continue 

                elif game_state in ('achievements','settings','history','tutorial','milestones','challenges'):
                    if back_button .rect .collidepoint (event .pos ):
                        game_state ='captcha'if not captcha_completed else 'menu'
                        if tutorial_active and tutorial_mode =='interactive':
                            visited_menu =True 
                    if game_state =='settings':
                        handle_click_settings (event .pos )
                    if game_state =='tutorial':
                        if tutorial_mode is None :
                            if TUTO_CHOICE_STATIC_BTN .rect .collidepoint (event .pos ):
                                globals ()['tutorial_mode']='static'
                            if TUTO_CHOICE_INTER_BTN .rect .collidepoint (event .pos ):
                                globals ()['tutorial_mode']='interactive'
                            if TUTO_BACK_MENU_BTN .rect .collidepoint (event .pos ):
                                game_state ='captcha'if not captcha_completed else 'menu'
                        elif tutorial_mode =='static':
                            if globals ().get ('_tuto_static_back_menu_rect')and globals ()['_tuto_static_back_menu_rect'].collidepoint (event .pos ):
                                game_state ='captcha'if not captcha_completed else 'menu'
                            if globals ().get ('_tuto_static_back_choice_rect')and globals ()['_tuto_static_back_choice_rect'].collidepoint (event .pos ):
                                globals ()['tutorial_mode']=None 
                        elif tutorial_mode =='interactive':
                            if not tutorial_active :
                                if TUTO_START_AUTO_BTN .rect .collidepoint (event .pos ):
                                    start_interactive_tutorial (auto =True )
                                    game_state ='menu'
                                if TUTO_START_MANUAL_BTN .rect .collidepoint (event .pos ):
                                    start_interactive_tutorial (auto =False )
                                    game_state ='menu'

                                if TUTO_BACK_MENU_BTN .rect .collidepoint (event .pos ):
                                    game_state ='captcha'if not captcha_completed else 'menu'
                                if TUTO_BACK_CHOICE_BTN .rect .collidepoint (event .pos ):
                                    globals ()['tutorial_mode']=None 
                            if tutorial_active and tutorial_mode =='interactive':
                                if _tut_prev_rect and _tut_prev_rect .collidepoint (event .pos ):
                                    tutorial_step =max (1 ,tutorial_step -1 )
                                if _tut_skip_rect and _tut_skip_rect .collidepoint (event .pos ):
                                    tutorial_active =False ;tutorial_mode =None 
                                    add_notification ("Tutoriel ignoré.",1600 )
                                if _tut_next_rect and _tut_next_rect .collidepoint (event .pos ):
                                    if tutorial_step ==TUTORIAL_LAST_STEP :
                                        curL =game_data ['points_log10']['R']
                                        cur =0 if curL ==NEG_INF else (10 **curL )
                                        need =max (0.0 ,10.0 -cur )
                                        if need >0 :
                                            game_data ['points_log10']['R']=log10_add (curL ,math .log10 (need ))
                                        tutorial_active =False ;tutorial_mode =None 
                                        add_notification ("Tutoriel terminé : total 10 pts R garanti !",2800 )
                                    else :
                                        if is_step_condition_met (tutorial_step ):
                                            tutorial_step =min (TUTORIAL_LAST_STEP ,tutorial_step +1 )
                    if game_state =='challenges':

                        for (cid ,kind ),r in list (_chal_btn_rects .items ()):
                            if r .collidepoint (event .pos ):
                                if kind =='start':
                                    start_challenge (cid )
                                elif kind =='stop':
                                    stop_challenge ()
                                elif kind =='complete':
                                    complete_challenge ()

                elif game_state =='dev_commands':

                    if dev_ui_tab =="deactivate"and dev_deactivate_confirm .get ("open",False ):
                        if dev_deactivate_confirm .get ("yes")and dev_deactivate_confirm ["yes"].collidepoint (event .pos ):
                            developer_mode_active =False 
                            dev_deactivate_confirm ["open"]=False 
                            dev_ui_tab =None 
                            add_notification ("Mode développeur désactivé.",1600 )
                            log_event ("Mode développeur DÉSACTIVÉ")
                            game_state ='menu'
                            continue 
                        elif dev_deactivate_confirm .get ("no")and dev_deactivate_confirm ["no"].collidepoint (event .pos ):
                            dev_deactivate_confirm ["open"]=False 
                            continue 
                    if dev_ui_tab =="pi":

                        if dev_pi_input_box_rect and dev_pi_input_box_rect .collidepoint (event .pos ):
                            disp ,vis_start =_display_with_ellipsis (dev_pi_input_text ,dev_pi_input_max_w ,font )
                            dev_pi_caret =_caret_from_click (dev_pi_input_text ,vis_start ,dev_pi_input_left_x ,event .pos [0 ],font )
                            dev_pi_caret_visible =True 
                            dev_pi_last_blink_ms =pygame .time .get_ticks ()
                            continue 

                        if DEV_PI_APPLY_BTN and pygame .Rect (DEV_PI_APPLY_BTN ).collidepoint (event .pos ):
                            s =dev_pi_input_text .strip ()
                            if not s :
                                add_notification ("Entrez un montant de PI.",1600 )
                            else :
                                L =parse_amount_to_log10 (s )
                                if L ==NEG_INF :
                                    add_notification ("Montant invalide.",1800 )
                                else :
                                    n =int (round (10 **L ))
                                    game_data ["PI"]=game_data .get ("PI",0 )+n 
                                    add_notification (f"+{n } PI (dev)",1600 )
                                    log_event (f"Dev PI +{n }")
                            continue 

                        if DEV_BACK_MENU_BTN .rect .collidepoint (event .pos ):
                            game_state ='captcha'if not captcha_completed else 'menu'
                            continue 
                        if DEV_BACK_SETTINGS_BTN .rect .collidepoint (event .pos ):
                            game_state ='settings'
                            continue 
                        if DEV_BACK_COMMANDS_BTN .rect .collidepoint (event .pos ):
                            dev_ui_tab =None 
                            continue 
                        continue 

                    if dev_ui_tab is None :
                        for key ,r in list (_dev_hub_rects .items ()):
                            if r and r .collidepoint (event .pos ):
                                if key =="logs":

                                    game_state ='dev_logs'
                                else :
                                    globals ()['dev_ui_tab']=key 
                                break 

                        if DEV_BACK_MENU_BTN .rect .collidepoint (event .pos ):
                            game_state ='captcha'if not captcha_completed else 'menu'
                        elif DEV_BACK_SETTINGS_BTN .rect .collidepoint (event .pos ):
                            game_state ='settings'
                        continue 

                    if dev_ui_tab =="score":

                        if dev_score_input_box_rect and dev_score_input_box_rect .collidepoint (event .pos ):
                            disp ,vis_start =_display_with_ellipsis (dev_score_input_text ,dev_score_input_max_w ,font )
                            globals ()['dev_score_caret']=_caret_from_click (dev_score_input_text ,vis_start ,dev_score_input_left_x ,event .pos [0 ],font )
                            dev_score_caret_visible =True 
                            dev_score_last_blink_ms =pygame .time .get_ticks ()
                            continue 

                        if DEV_SCORE_APPLY_BTN and pygame .Rect (DEV_SCORE_APPLY_BTN ).collidepoint (event .pos ):
                            s =dev_score_input_text .strip ()
                            if not s :
                                add_notification ("Entrez un montant de score.",1600 )
                            else :
                                L =parse_amount_to_log10 (s )
                                if L ==NEG_INF :
                                    add_notification ("Montant invalide.",1800 )
                                else :
                                    game_data ["score_log10"]=log10_add (game_data ["score_log10"],L )
                                    add_notification (f"+{s } score (dev)",1600 )
                                    log_event (f"Dev Score +{s }")
                            continue 

                        if DEV_BACK_MENU_BTN .rect .collidepoint (event .pos ):
                            game_state ='captcha'if not captcha_completed else 'menu'
                            continue 
                        if DEV_BACK_SETTINGS_BTN .rect .collidepoint (event .pos ):
                            game_state ='settings';continue 
                        if DEV_BACK_COMMANDS_BTN .rect .collidepoint (event .pos ):
                            dev_ui_tab =None ;continue 
                        continue 

                    if dev_ui_tab =="challenges":
                        def _force_launch (cid ):

                            reset_progress_for_run ()
                            challenge_state ["active"]=True 
                            challenge_state ["current"]=cid 
                            challenge_state ["notified_ready"]=False 
                            add_notification (f"Dev: Challenge {cid } lancé (forcé)",1600 )

                        for (key ,kind ),r in list (_dev_chal_rects .items ()):
                            if r and r .collidepoint (event .pos ):
                                if key =="c1"and kind =="act":
                                    game_data ["PI"]=game_data .get ("PI",0 )+1000 
                                    add_notification ("Dev: +1K PI",1600 )
                                elif key =="c1"and kind =="done":
                                    _force_launch (1 )
                                    game_data ["PI"]=game_data .get ("PI",0 )+1 
                                    add_notification ("Dev: C1 prêt ( +1 PI )",1800 )

                                elif key =="c2"and kind =="act":
                                    challenge_state ["completed"][0 ]=True 
                                    game_data ["PI"]=game_data .get ("PI",0 )+1000 
                                    add_notification ("Dev: C1 marqué terminé, +1K PI",1800 )
                                elif key =="c2"and kind =="done":
                                    challenge_state ["completed"][0 ]=True 
                                    _force_launch (2 )
                                    L =parse_amount_to_log10 ("1e100")
                                    game_data ["score_log10"]=log10_add (game_data ["score_log10"],L )
                                    add_notification ("Dev: C2 prêt ( +1e100 score )",1800 )

                                elif key =="c3"and kind =="act":
                                    challenge_state ["completed"][0 ]=True 
                                    challenge_state ["completed"][1 ]=True 
                                    game_data ["PI"]=game_data .get ("PI",0 )+1000 
                                    add_notification ("Dev: C1-2 marqués terminés, +1K PI",1800 )
                                elif key =="c3"and kind =="done":
                                    challenge_state ["completed"][0 ]=True 
                                    challenge_state ["completed"][1 ]=True 
                                    _force_launch (3 )
                                    game_data ["PI"]=max (game_data .get ("PI",0 ),1_000_000 )
                                    add_notification ("Dev: C3 prêt ( PI=100K )",1800 )

                                elif key =="c4"and kind =="act":
                                    challenge_state ["completed"][0 ]=True 
                                    challenge_state ["completed"][1 ]=True 
                                    challenge_state ["completed"][2 ]=True 
                                    game_data ["PI"]=game_data .get ("PI",0 )+1000 
                                    add_notification ("Dev: C1-3 marqués terminés, +1K PI",1800 )
                                elif key =="c4"and kind =="done":
                                    challenge_state ["completed"][0 ]=True 
                                    challenge_state ["completed"][1 ]=True 
                                    challenge_state ["completed"][2 ]=True 
                                    _force_launch (4 )

                                    game_data ["points_log10"]["A"]=max (game_data ["points_log10"]["A"],0.0 )
                                    add_notification ("Dev: C4 prêt ( +1 pt Ascension )",1800 )
                                break 

                        if DEV_BACK_MENU_BTN .rect .collidepoint (event .pos ):
                            game_state ='captcha'if not captcha_completed else 'menu'
                            continue 
                        if DEV_BACK_SETTINGS_BTN .rect .collidepoint (event .pos ):
                            game_state ='settings';continue 
                        if DEV_BACK_COMMANDS_BTN .rect .collidepoint (event .pos ):
                            dev_ui_tab =None ;continue 
                        continue 

                    if dev_ui_tab =="tests":
                        r =globals ().get ("_dev_tests_error_rect")
                        if r and r .collidepoint (event .pos ):
                            try :
                                trigger_error_overlay ("TestError","Erreur de test",0 )
                            except Exception :
                                pass 
                            continue 
                        if DEV_BACK_COMMANDS_BTN .rect .collidepoint (event .pos ):
                            dev_ui_tab =None 
                            continue 
                        if DEV_BACK_SETTINGS_BTN .rect .collidepoint (event .pos ):
                            game_state ="settings"
                            continue 
                        if DEV_BACK_MENU_BTN .rect .collidepoint (event .pos ):
                            game_state ="captcha"if not captcha_completed else "menu"
                            continue 
                        continue 

                    if dev_ui_tab =="logs":

                        game_state ='dev_logs'
                        continue 

                    if dev_ui_tab =="deactivate":

                        dev_deactivate_confirm ["open"]=True 
                        dev_deactivate_confirm ["yes"]=None 
                        dev_deactivate_confirm ["no"]=None 

                        if DEV_BACK_MENU_BTN .rect .collidepoint (event .pos ):
                            game_state ='captcha'if not captcha_completed else 'menu'
                            continue 
                        if DEV_BACK_SETTINGS_BTN .rect .collidepoint (event .pos ):
                            game_state ='settings';continue 
                        if DEV_BACK_COMMANDS_BTN .rect .collidepoint (event .pos ):
                            dev_ui_tab =None ;continue 
                        continue 

                elif game_state =='dev_logs':
                    if back_button .rect .collidepoint (event .pos ):
                        game_state ='dev_commands'
                    else :
                        prev_r =dev_logs_nav_rects .get ('prev')
                        next_r =dev_logs_nav_rects .get ('next')
                        if prev_r and prev_r .collidepoint (event .pos ):
                            dev_logs_page =min (dev_logs_page +1 ,max (0 ,(len (game_logs )+19 )//20 -1 ))
                        elif next_r and next_r .collidepoint (event .pos ):
                            dev_logs_page =max (0 ,dev_logs_page -1 )

                if game_state =='difficulty_select':
                    for key ,r in list (_diff_btn_rects .items ()):
                        if r and r .collidepoint (event .pos ):
                            globals ()['difficulty']=key 
                            globals ()['difficulty_selected']=True 

                            if not welcome_popup .get ("already_shown",False ):
                                welcome_popup ["open"]=True 
                                welcome_popup ["already_shown"]=True 
                                globals ()['show_version_popup']=False 
                            sync_challenges_with_difficulty ()
                            add_notification (f"Difficulté sélectionnée : {DIFF_LABELS [key ]}",1800 )
                            globals ()['game_state']='menu'
                            break 
                    continue 

        now =pygame .time .get_ticks ()
        if now -last_auto_tick >=1000 :
            secs =(now -last_auto_tick )/1000.0 
            last_auto_tick =now 
            avL =log10_effective_auto_value ()
            if avL >NEG_INF and secs >0 :
                addL =avL +math .log10 (secs )
                addL =apply_gain_modifiers (addL )
                game_data ["score_log10"]=log10_add (game_data ["score_log10"],addL )

            total_per_sec =NEG_INF 
            if avL >NEG_INF :
                total_per_sec =apply_gain_modifiers (avL )
            if game_settings .get ("mini_autoclicker",False )and game_data .get ("perm_unlocks",{}).get ("mini_autoclicker",False ):
                cL =log10_effective_click_value ()
                if cL >NEG_INF :
                    cL =apply_gain_modifiers (cL )
                    total_per_sec =cL if total_per_sec ==NEG_INF else log10_add (total_per_sec ,cL )
            if total_per_sec >game_data .get ("max_auto_sps_log10",NEG_INF ):
                game_data ["max_auto_sps_log10"]=total_per_sec 
            run_mini_autoclicker ()
            run_auto_buyers ()
            run_auto_rebirth (secs )
        if now -last_sps_tick >=1000 :
            sps =clicks_in_last_second /(((now -last_sps_tick )/1000.0 )if (now -last_sps_tick )>0 else 1.0 )
            if sps >game_data ["max_sps"]:game_data ["max_sps"]=sps 
            clicks_in_last_second =0 
            last_sps_tick =now 


            try :
                if not globals ().get ('developer_mode_active',False ):
                    if sps >20.0 :
                        lac =globals ().get ('last_anticheat_trigger_ms',0 )

                        if now -lac >800 :
                            globals ()['last_anticheat_trigger_ms']=now 
                            offenses =globals ().get ('anti_cheat_offenses',0 )
                            if offenses ==0 :
                                globals ()['anti_cheat_offenses']=1 
                                add_notification ('Avertissement : CPS anormal détecté (anticheat).',2200 )
                                log_event ('AntiCheat: CPS > 20 — avertissement enregistré (mode dev suspect).')
                            elif offenses ==1 :
                                globals ()['anti_cheat_offenses']=2 
                                globals ()['click_block_until_ms']=now +10000 
                                add_notification ('Interdiction de cliquer pendant 10 secondes (anticheat).',2200 )
                                log_event ('AntiCheat: CPS > 20 — 2e infraction, clics désactivés 10s.')
                            else :
                                log_event ('AntiCheat: CPS > 20 — 3e infraction, fermeture du jeu.')
                                add_notification ('Fermeture du jeu : comportement interdit détecté.',2000 )
                                pygame .display .flip ()
                                time .sleep (0.6 )
                                sys .exit ('Erreur anti-cheat : trop d\'infractions (CPS)')
            except Exception :
                pass 

        if tutorial_active and tutorial_mode =='interactive':
            L =game_data ['score_log10']
            if L >NEG_INF :
                if L >=math .log10 (100 ):score_reached_100 =True 
                if L >=math .log10 (1000 ):score_reached_1000 =True 
            if tutorial_auto_advance and tutorial_step !=TUTORIAL_LAST_STEP and is_step_condition_met (tutorial_step ):
                tutorial_step =min (TUTORIAL_LAST_STEP ,tutorial_step +1 )

        if game_data ["score_log10"]>game_data ["max_score_log10"]:
            game_data ["max_score_log10"]=game_data ["score_log10"]
        for fam in ("R","P","A","Re"):
            if game_data ["points_log10"][fam ]>game_data ["points_max_log10"][fam ]:
                game_data ["points_max_log10"][fam ]=game_data ["points_log10"][fam ]
        if game_data .get ("PI",0 )>game_data .get ("pi_max",0 ):
            game_data ["pi_max"]=game_data ["PI"]

        if game_data .get ("pi_max",0 )>=CHALLENGE_UNLOCK_PI :
            game_data ['ever_unlocked_challenges']=True 

        if challenge_state ["active"]and objective_met (challenge_state ["current"])and not challenge_state ["notified_ready"]:
            add_notification (f"Challenge {challenge_state ['current']} complétable !",1800 )
            challenge_state ["notified_ready"]=True 

        if milestone_currently_unlocked (12 ):
            game_data ['ever_unlocked_challenges']=True 
            cur_ms =len (unlocked_pi_milestones ())
            if cur_ms >last_pi_milestones_count :
                mini_notifs ['milestones']=True 
            last_pi_milestones_count =cur_ms 
        game_data ["total_play_time"]=time .time ()-start_time 
        update_achievements_v293 ()
        if tutorial_active and tutorial_mode =='interactive':
            if game_state =='achievements':visited_achievements =True 
            if game_state =='settings':visited_settings =True 
            if game_state =='history':visited_history =True 
            if game_state =='tutorial':visited_tutorial =True 
            if game_state =='milestones':visited_milestones =True 
            if game_state =='menu':visited_menu =True 

        mouse_pos =pygame .mouse .get_pos ()

        if _pending_click_after_popup :
            pos =_pending_click_after_popup 
            _pending_click_after_popup =None 
            if game_state =="menu":
                for key ,btn in menu_buttons .items ():
                    if btn .rect .collidepoint (pos ):

                        if key =="play":
                            mini_notifs ['play']=False 
                            game_state ='main'
                            if tutorial_active and tutorial_mode =='interactive':
                                visited_play =True 
                        elif key =="milestones":
                            mini_notifs ['milestones']=False 
                            game_state ='milestones'
                        elif key =="challenges":
                            if challenges_menu_accessible ():
                                game_state ='challenges'
                            else :
                                add_notification ("Les challenges ne sont pas encore accessibles.",1800 )
                        elif key =="achievements":
                            mini_notifs ['achievements']=False 
                            game_state ='achievements'
                        elif key =="settings":
                            game_state ='settings'
                        elif key =="history":
                            game_state ='history'
                        elif key =="tutorial":
                            mini_notifs ['tutorial']=False 
                            game_state ='tutorial'
                        elif key =="quit":
                            quit_confirm ["open"]=True 
                            quit_confirm ["rect_yes"]=None 
                            quit_confirm ["rect_no"]=None 
                        break 

        if game_state =='captcha':
            if not captcha_completed :
                draw_captcha (mouse_pos ,dt )
            else :

                game_state ='menu'
                draw_main_menu (mouse_pos ,dt )

        elif game_state =='menu':
            draw_main_menu (mouse_pos ,dt )

        elif game_state =='achievements':
            ensure_achievements_v293_init ()
            draw_achievements (mouse_pos ,dt )

        elif game_state =='settings':
            draw_settings (mouse_pos ,dt )

        elif game_state =='history':
            draw_history (mouse_pos ,dt )

        elif game_state =='tutorial':
            draw_tutorial (mouse_pos ,dt )

        elif game_state =='milestones':
            draw_milestones (mouse_pos ,dt )

        elif game_state =='challenges':
            draw_challenges (mouse_pos ,dt )

        elif game_state =='loading':
            draw_loading (mouse_pos ,dt )

        elif game_state =='reset_white':
            draw_reset_white (mouse_pos ,dt )

        elif game_state =='dev_commands':
            draw_dev_commands (mouse_pos ,dt )

        elif game_state =='dev_logs':
            draw_dev_logs (mouse_pos ,dt )

        elif game_state =='difficulty_select':
            draw_difficulty_select (mouse_pos ,dt )

        else :
            game_menu_button =draw_main_game (mouse_pos ,dt )

        try :
            draw_global_progress_hud (mouse_pos )
        except Exception as e :
            try :
                log_event (f"[GP HUD] error: {e }")
            except Exception :
                pass 

        if reset_flow .get ('in_progress',False ):
            now =pygame .time .get_ticks ()
            if reset_flow .get ('progress_start_ms',-1 )<0 :
                reset_flow ['progress_start_ms']=now 
            elapsed =now -reset_flow ['progress_start_ms']
            screen .fill ((0 ,0 ,0 ))
            msg =big_font .render ("Réinitialisation des données en cours...",True ,(255 ,255 ,255 ))
            screen .blit (msg ,(WIDTH //2 -msg .get_width ()//2 ,HEIGHT //2 -msg .get_height ()//2 ))
            pct =int ((elapsed /8000.0 )*100 )
            pct =0 if pct <0 else (100 if pct >100 else pct )
            pct_s =secondary_font .render (f"{pct }%",True ,(220 ,220 ,220 ))
            screen .blit (pct_s ,(WIDTH //2 -pct_s .get_width ()//2 ,HEIGHT //2 +18 ))
            pygame .display .flip ()
            if elapsed >=8000 :
                perform_full_data_reset ()
                reset_flow ['in_progress']=False 
                reset_flow ['progress_start_ms']=-1 
                reset_flow ['state']=0 
                reset_flow ['clicks']=0 
                reset_flow ['start_ms']=-1 

                reset_white_start_ms =pygame .time .get_ticks ()
                set_game_state ('reset_white')
                continue 

        draw_dev_indicator ()

        y =NOTIF_TOP_Y 
        for n in list (notifications ):
            n .setdefault ("timer",2000 )
            n ["timer"]-=dt 
            if n ["timer"]<=0 :
                notifications .remove (n );continue 
            msg =n .get ("message","");cnt =n .get ("count",1 )
            if cnt >1 :msg =f"{msg } (x{cnt })"
            ns =notif_font .render (msg ,True ,(255 ,255 ,255 ))
            nb =pygame .Surface ((ns .get_width ()+20 ,ns .get_height ()+10 ),pygame .SRCALPHA )
            alpha =max (40 ,min (150 ,int (150 *(n ["timer"]/2000 ))))
            nb .fill ((0 ,0 ,0 ,alpha ))
            rect =nb .get_rect (center =(WIDTH //2 ,y +nb .get_height ()//2 ))
            screen .blit (nb ,rect )
            screen .blit (ns ,ns .get_rect (center =rect .center ))
            y +=nb .get_height ()+8 


        draw_welcome_popup (mouse_pos )
        draw_modal_popups (mouse_pos )
        if not overlays_open ():
            render_hud_layer (mouse_pos )
        draw_reset_confirm_overlay (mouse_pos )
        draw_gr_confirm_overlay (mouse_pos )
        draw_quit_confirm_overlay (mouse_pos )
        draw_reset_fx_overlay ()

        _force_exit_loading_transition_if_stuck ()

        pygame .display .flip ()

except Exception as _e :
    err =traceback .format_exc ()
    etype =type (_e ).__name__ 
    try :
        with open ('error.log','w',encoding ='utf-8')as f :
            f .write (err )
    except Exception :
        pass 
    try :
        trigger_error_overlay (etype ,str (_e ),None ,err )
        clock_err =pygame .time .Clock ()
        waiting =True 
        while waiting :
            draw_error_overlay_loop ()
            for event in pygame .event .get ():
                if event .type ==pygame .QUIT :
                    waiting =False 
                elif event .type ==pygame .MOUSEBUTTONDOWN and event .button ==1 :
                    r =globals ().get ('_error_quit_rect')
                    if r and r .collidepoint (event .pos ):
                        waiting =False 
            pygame .display .flip ()
            clock_err .tick (60 )
    except Exception :
        pass 
finally :
    pygame .quit ()
    sys .exit ()
