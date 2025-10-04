import pygame
import sys
import random
import math
import colorsys
import string

pygame.init()

# -------------------- DIMENSIONS ET FENÊTRE --------------------
WIDTH, HEIGHT = 1824, 1026
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Idle Clicker version 20.1")
clock = pygame.time.Clock()

# -------------------- CHARGEMENT DU FOND --------------------
try:
    background_img = pygame.image.load("background.png").convert()
    background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
except:
    print("Fichier 'background.png' introuvable, fond uni utilisé.")
    background_img = None

# -------------------- COULEURS ET POLICES --------------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
GREEN = (50, 205, 50)
RED = (255, 50, 50)
GRAY = (200, 200, 200)
DARK_RED = (150, 0, 0)
YELLOW = (255, 255, 0)

font = pygame.font.SysFont("Arial", 24)
big_font = pygame.font.SysFont("Arial", 36)
secondary_font = pygame.font.SysFont("Arial", 18)

# -------------------- FONCTION DE FORMATAGE DES NOMBRES --------------------
# Suffixes personnalisés : "", "k", "m", "b", "t", "aa", "ab", … jusqu’à "az"
custom_suffixes = ["", "k", "m", "b", "t", "aa", "ab", "ac", "ad", "ae", "af", "ag", "ah", "ai", "aj", "ak", "al", "am", "an", "ao", "ap", "aq", "ar", "as", "at", "au", "av", "aw", "ax", "ay", "az", "c", "d", "e", "infinite"]

def format_number(n):
    try:
        n = float(n)
    except:
        return str(n)
    if n < 1000:
        return str(int(n))
    power = int(math.floor(math.log10(n) / 3))
    if power >= len(custom_suffixes):
        power = len(custom_suffixes) - 1
    value = n / (1000 ** power)
    return f"{value:.2f}{custom_suffixes[power]}"

def get_rainbow_color():
    t = pygame.time.get_ticks() / 1000.0
    hue = (t % 10) / 10.0
    rgb = colorsys.hsv_to_rgb(hue, 1, 1)
    return (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))

# -------------------- CLASSES --------------------
class Button:
    def __init__(self, rect, text, bg_color, text_color=BLACK, image=None):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.bg_color = bg_color
        self.text_color = text_color
        self.image = image

    def draw(self, surface):
        if self.image:
            surface.blit(self.image, self.rect)
        else:
            pygame.draw.rect(surface, self.bg_color, self.rect, border_radius=8)
        text_surf = font.render(self.text, True, self.text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def is_hovered(self, pos):
        return self.rect.collidepoint(pos)

class ClickAnimation:
    def __init__(self, pos):
        self.pos = pos
        self.timer = 0
        self.duration = 500
        self.max_radius = 50

    def update(self, dt):
        self.timer += dt

    def is_finished(self):
        return self.timer >= self.duration

    def draw(self, surface):
        progress = self.timer / self.duration
        radius = int(progress * self.max_radius)
        alpha = max(int(255 * (1 - progress)), 0)
        if radius > 0:
            temp_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(temp_surface, (255, 255, 255, alpha), (radius, radius), radius, width=3)
            surface.blit(temp_surface, (self.pos[0] - radius, self.pos[1] - radius))

class Particle:
    def __init__(self, pos, velocity, lifetime, color, size):
        self.pos = list(pos)
        self.velocity = velocity
        self.lifetime = lifetime
        self.max_lifetime = lifetime
        self.color = color
        self.size = size

    def update(self, dt):
        self.lifetime -= dt
        self.pos[0] += self.velocity[0] * dt / 1000.0
        self.pos[1] += self.velocity[1] * dt / 1000.0

    def is_dead(self):
        return self.lifetime <= 0

    def draw(self, surface):
        if self.lifetime > 0:
            progress = self.lifetime / self.max_lifetime
            alpha = int(255 * progress)
            s = pygame.Surface((self.size*2, self.size*2), pygame.SRCALPHA)
            pygame.draw.circle(s, self.color + (alpha,), (self.size, self.size), self.size)
            surface.blit(s, (int(self.pos[0]-self.size), int(self.pos[1]-self.size)))

class FloatingShape:
    def __init__(self):
        self.shape = random.choice(["circle", "square", "triangle"])
        self.size = random.randint(35, 105)
        self.x = random.uniform(0, WIDTH)
        self.y = random.uniform(0, HEIGHT)
        self.vx = random.uniform(-80, 80)
        self.vy = random.uniform(-80, 80)
        self.offset = random.random() * 10

    def update(self, dt):
        self.x += self.vx * dt / 1000.0
        self.y += self.vy * dt / 1000.0
        # Bouclage
        if self.x < 0:
            self.x = WIDTH
        elif self.x > WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = HEIGHT
        elif self.y > HEIGHT:
            self.y = 0

    def draw(self, surface):
        t = (pygame.time.get_ticks() / 1000.0 + self.offset) % 10
        hue = (t / 10.0) % 1.0
        rgb = colorsys.hsv_to_rgb(hue, 1, 1)
        color = (int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))
        if self.shape == "circle":
            pygame.draw.circle(surface, color, (int(self.x), int(self.y)), self.size // 2)
        elif self.shape == "square":
            rect = pygame.Rect(self.x - self.size/2, self.y - self.size/2, self.size, self.size)
            pygame.draw.rect(surface, color, rect)
        elif self.shape == "triangle":
            points = [
                (self.x, self.y - self.size/2),
                (self.x - self.size/2, self.y + self.size/2),
                (self.x + self.size/2, self.y + self.size/2)
            ]
            pygame.draw.polygon(surface, color, points)

# Créer des formes flottantes
floating_shapes = [FloatingShape() for _ in range(13)]

# -------------------- VARIABLES DU JEU & BOOSTS --------------------
game_state = "menu"

# Valeurs de base
BASE_CLICK_VALUE = 1
BASE_AUTO_VALUE = 0
BASE_MULTIPLIER = 1.0
BASE_COST_AUTO = 40
BASE_COST_CLICK = 25
BASE_COST_MULTIPLIER = 50

score = 0
click_value = BASE_CLICK_VALUE
auto_value = BASE_AUTO_VALUE
multiplier = BASE_MULTIPLIER

# Coûts d'upgrade initiaux
base_upgrade_auto_cost = BASE_COST_AUTO
base_upgrade_click_cost = BASE_COST_CLICK
base_upgrade_multiplier_cost = BASE_COST_MULTIPLIER

# Système de prestige
prestige_count = 0
base_prestige_threshold = int(1000 * (1.5 ** prestige_count))
prestige_for_ascension = 0
ascension_count = 0
ascension_threshold = 10

# Statistiques
total_clicks = 0
max_score = 0

# Boosts achievements
prestige_discount_bonus = 0
click_bonus_bonus = 0
upgrade_cost_discount_bonus = 0
auto_income_bonus_bonus = 0
ascender_discount = 0

# -------------------- SYSTEME D'ASCENSION --------------------
# (Variables déjà initialisées ci-dessus)

# -------------------- ACHIEVEMENTS --------------------
achievements = {
    "Clicker": {
        "name": "Clicker",
        "description": "Effectuer des clics pour rendre le prestige moins cher.",
        "type": "click",
        "thresholds": [1, 10, 50, 100, 200, 500, 1000, 5000, 10000, 100000],
        "boosts": [0.01, 0.02, 0.03, 0.05, 0.07, 0.10, 0.15, 0.20, 0.30, 0.50],
        "current_level": 0
    },
    "Scoreur": {
        "name": "Scoreur",
        "description": "Obtenir un score élevé pour booster les clics.",
        "type": "score",
        "thresholds": [1e3, 1e6, 1e9, 1e12, 1e15, 1e18, 1e21, 1e24, 1e27, 1e30],
        "boosts": [0.10, 0.20, 0.30, 0.50, 0.75, 1.00, 1.50, 2.00, 5.00, 10.00],
        "current_level": 0
    },
    "Prestige Man": {
        "name": "Prestige Man",
        "description": "Accumuler des prestiges pour rendre les upgrades moins chères.",
        "type": "prestige",
        "thresholds": [1, 2, 3, 5, 7, 10, 15, 20, 50, 100],
        "boosts": [0.01, 0.02, 0.03, 0.05, 0.07, 0.10, 0.15, 0.20, 0.30, 0.50],
        "current_level": 0
    },
    "Auto clicker": {
        "name": "Auto clicker",
        "description": "Accumuler de l'auto income pour augmenter l'autoclic.",
        "type": "auto",
        "thresholds": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
        "boosts": [1, 2, 3, 5, 7, 10, 15, 20, 35, 50],
        "current_level": 0
    },
    "Ascender": {
        "name": "Ascender",
        "description": "Accumuler des ascensions pour réduire le coût en prestiges requis.",
        "type": "ascension",
        "thresholds": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        "boosts": [-1, -2, -3, -5, -7, -10, -15, -25, -50, -100],
        "current_level": 0
    }
}

def check_achievements():
    global prestige_discount_bonus, click_bonus_bonus, upgrade_cost_discount_bonus, auto_income_bonus_bonus, ascender_discount
    for key, ach in achievements.items():
        if ach["type"] == "click":
            value = total_clicks
        elif ach["type"] == "score":
            value = max_score
        elif ach["type"] == "prestige":
            value = prestige_count
        elif ach["type"] == "auto":
            value = auto_value
        elif ach["type"] == "ascension":
            value = ascension_count
        else:
            value = 0

        # Vérifier si on peut augmenter le niveau
        while ach["current_level"] < len(ach["thresholds"]) and value >= ach["thresholds"][ach["current_level"]]:
            ach["current_level"] += 1
            notifications.append({"message": f"{ach['name']} niveau {ach['current_level']} débloqué!", "timer": 3000})
            spawn_particles((WIDTH//2, HEIGHT//2), 30, YELLOW)

    # Mettre à jour les boosts
    prestige_level = achievements["Clicker"]["current_level"]
    click_level = achievements["Scoreur"]["current_level"]
    prestige_bonus_level = achievements["Prestige Man"]["current_level"]
    auto_level = achievements["Auto clicker"]["current_level"]
    ascension_level = achievements["Ascender"]["current_level"]

    prestige_discount_bonus = achievements["Clicker"]["boosts"][prestige_level -1] if prestige_level >0 else 0
    click_bonus_bonus = achievements["Scoreur"]["boosts"][click_level -1] if click_level >0 else 0
    upgrade_cost_discount_bonus = achievements["Prestige Man"]["boosts"][prestige_bonus_level -1] if prestige_bonus_level >0 else 0
    auto_income_bonus_bonus = achievements["Auto clicker"]["boosts"][auto_level -1] if auto_level >0 else 0
    ascender_discount = achievements["Ascender"]["boosts"][ascension_level -1] if ascension_level >0 else 0

def update_notifications(dt):
    for n in notifications[:]:
        n["timer"] -= dt
        if n["timer"] <= 0:
            notifications.remove(n)

def spawn_particles(pos, count, color):
    for _ in range(count):
        vx = random.uniform(-150, 150)
        vy = random.uniform(-150, 150)
        lifetime = random.randint(500, 1000)
        size = random.randint(2, 4)
        particles.append(Particle(pos, (vx, vy), lifetime, color, size))

# -------------------- BOUTONS --------------------
click_button = Button((WIDTH//2 - 100, HEIGHT//2 - 100, 200, 200), "CLICK", BLUE, WHITE)
upgrade_auto_button = Button((50, HEIGHT - 100, 220, 50),
    f"Auto Upgrade ($ {format_number(base_upgrade_auto_cost)})", GREEN)
upgrade_click_button = Button((300, HEIGHT - 100, 220, 50),
    f"Click Upgrade ($ {format_number(base_upgrade_click_cost)})", GREEN)
upgrade_multiplier_button = Button((550, HEIGHT - 100, 220, 50),
    f"Multiplier Upgrade ($ {format_number(base_upgrade_multiplier_cost)})", GREEN)
prestige_button = Button((WIDTH - 200, 20, 180, 50),
    f"Prestige ({prestige_count})", RED, WHITE)
ascension_button = Button((WIDTH - 200, 150, 180, 50),
    f"Ascension ({ascension_count})", RED, WHITE)
game_menu_button = Button((20, HEIGHT - 60, 100, 40), "Menu", GRAY, BLACK)

# Menu principal
menu_buttons = {
    "play": Button((WIDTH//2 - 100, 200, 200, 50), "Jouer", GREEN, WHITE),
    "achievements": Button((WIDTH//2 - 100, 270, 200, 50), "Achievements", GREEN, WHITE),
    "settings": Button((WIDTH//2 - 100, 340, 200, 50), "Paramètres", GREEN, WHITE),
    "history": Button((WIDTH//2 - 100, 410, 200, 50), "Historique", GREEN, WHITE),
    "changelog": Button((WIDTH//2 - 100, 480, 200, 50), "Changelog", GREEN, WHITE),  # repositionné
    "quit": Button((WIDTH//2 - 100, 550, 200, 50), "Quitter", RED, WHITE)
}
back_button = Button((20, HEIGHT - 60, 100, 40), "Menu", GRAY, BLACK)

# -------------------- TIMERS & LISTES --------------------
last_auto_update = pygame.time.get_ticks()
animations = []
particles = []
notifications = []

# -------------------- FONCTION PRINCIPALE --------------------
running = True
while running:
    dt = clock.tick(60)
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if game_state == "menu":
                if menu_buttons["play"].is_hovered(mouse_pos):
                    game_state = "game"
                elif menu_buttons["achievements"].is_hovered(mouse_pos):
                    game_state = "achievements"
                elif menu_buttons["settings"].is_hovered(mouse_pos):
                    game_state = "settings"
                elif menu_buttons["history"].is_hovered(mouse_pos):
                    game_state = "history"
                elif menu_buttons["changelog"].is_hovered(mouse_pos):
                    game_state = "changelog"
                elif menu_buttons["quit"].is_hovered(mouse_pos):
                    running = False
            elif game_state == "game":
                if game_menu_button.is_hovered(mouse_pos):
                    game_state = "menu"
                elif click_button.is_hovered(mouse_pos):
                    total_clicks += 1
                    effective_click = (click_value * multiplier * (2 ** prestige_count) * (15 ** ascension_count) * (1 + click_bonus_bonus))
                    score += effective_click
                    animations.append(ClickAnimation(mouse_pos))
                elif upgrade_auto_button.is_hovered(mouse_pos):
                    effective_cost = max(1, int(base_upgrade_auto_cost * (1 - upgrade_cost_discount_bonus)))
                    if score >= effective_cost:
                        score -= effective_cost
                        auto_value += 1
                        base_upgrade_auto_cost = int(base_upgrade_auto_cost * 1.5)
                        upgrade_auto_button.text = f"Auto Upgrade ($ {format_number(base_upgrade_auto_cost)})"
                        spawn_particles(mouse_pos, 15, GREEN)
                elif upgrade_click_button.is_hovered(mouse_pos):
                    effective_cost = max(1, int(base_upgrade_click_cost * (1 - upgrade_cost_discount_bonus)))
                    if score >= effective_cost:
                        score -= effective_cost
                        click_value += 1
                        base_upgrade_click_cost = int(base_upgrade_click_cost * 1.5)
                        upgrade_click_button.text = f"Click Upgrade ($ {format_number(base_upgrade_click_cost)})"
                        spawn_particles(mouse_pos, 15, BLUE)
                elif upgrade_multiplier_button.is_hovered(mouse_pos):
                    effective_cost = max(1, int(base_upgrade_multiplier_cost * (1 - upgrade_cost_discount_bonus)))
                    if score >= effective_cost:
                        score -= effective_cost
                        multiplier += 0.50
                        base_upgrade_multiplier_cost = int(base_upgrade_multiplier_cost * 2)
                        upgrade_multiplier_button.text = f"Multiplier Upgrade ($ {format_number(base_upgrade_multiplier_cost)})"
                        spawn_particles(mouse_pos, 15, GREEN)
                elif prestige_button.is_hovered(mouse_pos):
                    effective_prestige_threshold = int(base_prestige_threshold * (1 - prestige_discount_bonus))
                    if score >= effective_prestige_threshold:
                        prestige_count += 1
                        prestige_for_ascension += 1
                        base_prestige_threshold = int(1000 * (2.5 ** prestige_count))
                        spawn_particles(prestige_button.rect.center, 40, RED)
                        # Reset tout sauf les boosts
                        score = 0
                        click_value = BASE_CLICK_VALUE
                        auto_value = BASE_AUTO_VALUE
                        multiplier = BASE_MULTIPLIER
                        base_upgrade_auto_cost = BASE_COST_AUTO
                        base_upgrade_click_cost = BASE_COST_CLICK
                        base_upgrade_multiplier_cost = BASE_COST_MULTIPLIER
                elif ascension_button.is_hovered(mouse_pos):
                    effective_asc_threshold = max(ascension_threshold + ascender_discount, 1)
                    if prestige_for_ascension >= effective_asc_threshold:
                        ascension_count += 1
                        ascension_threshold *= 3
                        prestige_for_ascension = 0
                        score = 0
                        click_value = BASE_CLICK_VALUE
                        auto_value = BASE_AUTO_VALUE
                        multiplier = BASE_MULTIPLIER
                        base_upgrade_auto_cost = BASE_COST_AUTO
                        base_upgrade_click_cost = BASE_COST_CLICK
                        base_upgrade_multiplier_cost = BASE_COST_MULTIPLIER
                        prestige_count = 0
                        base_prestige_threshold = int(1000 * (1.75 ** prestige_count))
                        spawn_particles(ascension_button.rect.center, 50, YELLOW)
                        notifications.append({"message": "Ascension effectuée ! Boost XP: {}x, Boost Prestige: {}x".format(15**ascension_count, 2**ascension_count), "timer": 3000})
            elif game_state in ["achievements", "settings", "history", "changelog"]:
                if back_button.is_hovered(mouse_pos):
                    game_state = "menu"

    # -------------------- MISE À JOUR --------------------
    if game_state == "game":
        if current_time - last_auto_update >= 1000:
            seconds_passed = (current_time - last_auto_update) // 1000
            score += (auto_value + auto_income_bonus_bonus) * multiplier * (3 ** ascension_count) * seconds_passed
            last_auto_update += 1000 * seconds_passed

        for anim in animations[:]:
            anim.update(dt)
            if anim.is_finished():
                animations.remove(anim)
        for p in particles[:]:
            p.update(dt)
            if p.is_dead():
                particles.remove(p)
        check_achievements()
        if score > max_score:
            max_score = score
        update_notifications(dt)

    # Si fond image nulle, animation fond
    if background_img is None:
        for shape in floating_shapes:
            shape.update(dt)

    # -------------------- RENDERING --------------------
    if background_img:
        screen.blit(background_img, (0, 0))
    else:
        screen.fill(GRAY)
        for shape in floating_shapes:
            shape.draw(screen)

    if game_state == "menu":
        title_surf = big_font.render("Idle Clicker Version 20.1",True, BLACK)
        title_rect = title_surf.get_rect(center=(WIDTH//2, 100))
        screen.blit(title_surf, title_rect)
        for btn in menu_buttons.values():
            btn.draw(screen)
    elif game_state == "game":
        game_menu_button.draw(screen)
        # Bouton clic avec ombre
        shadow_offset = 5
        shadow_rect = click_button.rect.copy()
        shadow_rect.x += shadow_offset
        shadow_rect.y += shadow_offset
        pygame.draw.rect(screen, BLACK, shadow_rect, border_radius=8)
        click_button.draw(screen)

        upgrade_auto_button.draw(screen)
        upgrade_click_button.draw(screen)
        upgrade_multiplier_button.draw(screen)

        # Prestige
        effective_prestige_threshold = int(base_prestige_threshold * (1 - prestige_discount_bonus))
        prestige_button.bg_color = RED if score >= effective_prestige_threshold else DARK_RED
        prestige_button.text = f"Prestige ({prestige_count})"
        prestige_button.draw(screen)

        # Ascension
        effective_asc_threshold = max(ascension_threshold + ascender_discount, 1)
        if prestige_for_ascension >= effective_asc_threshold:
            ascension_button.bg_color = get_rainbow_color()
        else:
            ascension_button.bg_color = GRAY
        ascension_button.text = f"Ascension ({ascension_count})"
        ascension_button.draw(screen)

        # Progression
        progress_bar_width = 180
        progress_bar_height = 20
        # Prestige progress
        progress_ratio = score / effective_prestige_threshold if effective_prestige_threshold > 0 else 0
        progress_ratio = min(progress_ratio, 1)
        fill_width = int(progress_bar_width * progress_ratio)
        pygame.draw.rect(screen, BLACK, (prestige_button.rect.x, prestige_button.rect.bottom + 10, progress_bar_width, progress_bar_height), 2)
        pygame.draw.rect(screen, GREEN, (prestige_button.rect.x, prestige_button.rect.bottom + 10, fill_width, progress_bar_height))
        progress_text = font.render(f"{format_number(score)}/{format_number(effective_prestige_threshold)}", True, BLACK)
        screen.blit(progress_text, (prestige_button.rect.x + progress_bar_width//2 - progress_text.get_width()//2,
                                    prestige_button.rect.bottom + 10 + progress_bar_height//2 - progress_text.get_height()//2))
        # Ascension progress
        asc_progress_ratio = prestige_for_ascension / max(effective_asc_threshold,1)
        asc_progress_ratio = min(asc_progress_ratio,1)
        asc_fill_width = int(progress_bar_width * asc_progress_ratio)
        
        # Barre d'ascension en vert
        pygame.draw.rect(screen, GREEN, (ascension_button.rect.x, ascension_button.rect.bottom + 10, asc_fill_width, progress_bar_height))
        pygame.draw.rect(screen, BLACK, (ascension_button.rect.x, ascension_button.rect.bottom + 10, progress_bar_width, progress_bar_height), 2)
        asc_progress_text = font.render(f"{prestige_for_ascension}/{effective_asc_threshold}", True, BLACK)
        screen.blit(asc_progress_text, (ascension_button.rect.x + progress_bar_width//2 - asc_progress_text.get_width()//2,
                                          ascension_button.rect.bottom + 10 + progress_bar_height//2 - asc_progress_text.get_height()//2))
        # Stats
        stats = [
            f"Score: {format_number(score)}",
            f"Auto Income: {auto_value} / sec",
            f"Click Value: {click_value}",
            f"Multiplier: {multiplier:.2f}x",
            f"Prestige Bonus: *{2 ** prestige_count}",
            f"Next Prestige: {format_number(effective_prestige_threshold)} pts"
        ]
        for i, s in enumerate(stats):
            stat_surf = font.render(s, True, BLACK)
            screen.blit(stat_surf, (20, 20 + i * 30))
        # Notifications
        for i, note in enumerate(notifications):
            note_surf = font.render(note["message"], True, YELLOW)
            screen.blit(note_surf, (WIDTH//2 - note_surf.get_width()//2, HEIGHT//2 - 100 - i*30))
        # Animations
        for anim in animations:
            anim.draw(screen)
    elif game_state == "achievements":
        title = big_font.render("Achievements", True, BLACK)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 30))
        y_offset = 100
        for key, ach in achievements.items():
            color = GREEN if ach["current_level"] > 0 else RED
            main_text = f"{ach['name']} ({ach['current_level']}/10) : {ach['description']}"
            main_surf = font.render(main_text, True, color)
            screen.blit(main_surf, (50, y_offset))
            # Valeur actuelle
            if ach["type"] == "click":
                current_value = total_clicks
            elif ach["type"] == "score":
                current_value = max_score
            elif ach["type"] == "prestige":
                current_value = prestige_count
            elif ach["type"] == "auto":
                current_value = auto_value
            elif ach["type"] == "ascension":
                current_value = ascension_count
            else:
                current_value = 0
            # Prochain niveau
            if ach["current_level"] < len(ach["thresholds"]):
                req_text = f"Prochain niveau : {format_number(current_value)}/{format_number(ach['thresholds'][ach['current_level']])}"
            else:
                req_text = "Niveau maximum atteint"
            req_surf = secondary_font.render(req_text, True, BLACK)
            screen.blit(req_surf, (50, y_offset + 22))
            y_offset += 60
        back_button.draw(screen)
    elif game_state == "settings":
        title = big_font.render("Paramètres", True, BLACK)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 30))
        options = ["Son: ON", "Graphismes: Haute", "Volume Musique: 70%"]
        y_offset = 150
        for opt in options:
            opt_text = font.render(opt, True, BLACK)
            screen.blit(opt_text, (50, y_offset))
            y_offset += 40
        back_button.draw(screen)
    elif game_state == "history":
        title = big_font.render("Historique", True, BLACK)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 30))
        stats_list = [
            f"Total Clics: {total_clicks}",
            f"Meilleur Score: {format_number(max_score)}",
            f"Prestige: {prestige_count}",
            f"Auto Income Achieved: {auto_value} / sec"
        ]
        y_offset = 100
        for st in stats_list:
            st_text = font.render(st, True, BLACK)
            screen.blit(st_text, (50, y_offset))
            y_offset += 40
        back_button.draw(screen)
    elif game_state == "changelog":
        title = font.render("Changelog", True, BLACK)
        screen.blit(title, (WIDTH//2 - title.get_width()//3, 30))
        changes = [
            "v20.1 - Corrections de bugs mineurs concernant l'affichage des boosts après l'ascension"
            "v20 - Changement taille écran et adaptation des entités du jeu à la taille de l'appareil & changement formule de clics",
            "v19.2 - Changement taille de l'écran & corrections de bugs mineurs",
            "v19.1 - Correction de bugs mineurs",
            "v19 - Ajout changelogs & refonte suffixes",
            "v18 - Correction des boosts",
            "v17 - Ajout des particules et formes flottantes",
            "v16 - Implémentation du système d'ascension",
            "v15 - Interface utilisateur refaite",
            "v14 - 2 nouveaux succès implémentés",
            "v13 - Correction upgrade click automatique",
            "v12 - 1 nouvelle upgrade implémentée",
            "v11 - Refonte interface utilisateur",
            "v10 - Système de notifications pour les succès",
            "v9  - Formatage amélioré des nombres",
            "v8  - Amélioration des performances",
            "v7  - Refonte interface utilisateur",
            "v6  - Système de succès",
            "v5  - Résolution des bugs de clic",
            "v4  - Barre de progression prestige",
            "v3  - Corrections menu et boutons",
            "v2  - Changement du bouton clic",
            "v1  - Lancement du jeu"
        ]
        y_offset = 100
        for c in changes:
            line = font.render(c, True, BLACK)
            screen.blit(line, (50, y_offset))
            y_offset += 30
        back_button.draw(screen)

    pygame.display.flip()

pygame.quit()
