import pygame
from game import game
from player import player
pygame.init()


# generer la fenetre de notre jeu
pygame.display.set_caption("JulesGame") # Donne un nom à la fenêtre
screen = pygame.display.set_mode((1080,720)) # La résolution de la fenêtre

#importer l'arrière plan

background = pygame.image.load('assets/bg.jpg')

#charger notre jeu
game = game()

#charger notre joueur
player = player()

running = True

# boucle tant que cette condition est vraie

while running: 
    
    #appliquer l'arrière plan
    screen.blit(background, (0,-200))
    
    # appliquer l'image de mon joueur
    screen.blit(game.player.image, game.player.rect)
    
    # verifier si le joueur veut aller a gauche ou a droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x < 915:
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > -33:
        game.player.move_left()
    
    # maj de l'écran
    pygame.display.flip()
    
    # Si le joueur ferme cette fenetre
    for event in pygame.event.get():
        # verifie que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        #Detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
            
