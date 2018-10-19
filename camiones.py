
from numpy import *
from random import randrange
import pygame
import os
import pygameMenu
#LIBRERIA QUE DESCAERGUE PARA CREAR MENUS
from pygameMenu.locals import * 

ABOUT = ['Simulador de Camion','BY CARLOS A. ROBLES']

pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

jump = pygame.mixer.Sound('jump.wav')
mov_teclas = pygame.mixer.Sound('teclas_1.wav')
enter_menu = pygame.mixer.Sound('enter_1.wav')
pygame.mixer.music.load('jumper_original.mp3')
fondo_mapa = pygame.image.load("mapa.png")
   
#Menu info
COLOR_BACKGROUND = (128, 0, 128)
FPS = 60.0
MENU_BACKGROUND_COLOR = (228, 55, 36)

# Colores
flag = 0
NEGRO = (0, 0, 0) 
BLANCO = (255, 255, 255) 
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
BLANCO = (255, 255, 255)
 
# Dimensiones de la pantalla
LARGO_PANTALLA = 800
ALTO_PANTALLA = 600
CONF_PANTALLA = (800, 600)
pantalla = pygame.display.set_mode(CONF_PANTALLA)
DIFFICULTY = ['1']
clock = pygame.time.Clock()


def change_difficulty(d):
    """
    Change difficulty of the game.
    
    :return: 
    """
    print ('Selected difficulty bruh: {0}'.format(i))
    DIFFICULTY[0] = d


def play_function(difficulty, font):
    """
    Main game function
    
    :param difficulty: Difficulty of the game
    :param font: Pygame font
    :return: None
    """
    pygame.init()
    global flag
    flag = 1
    ruta = 0
    
    difficulty = difficulty[0]
    assert isinstance(difficulty, str)

    clock = pygame.time.Clock()

    class Player(object):

        x_ini = 66
        y_ini = 66
        step = 14
        gravity = -45 #va a causar la curvatura
        y_ini += 22

       
        def __init__(self,x,y):
            self.rect = pygame.draw.rect(pantalla, (0, 0, 128), (64, 54, 16, 16))
            self

        def update(self):
           
            self.rect.move(-1, 0)

            self.rect.move(1, 0)
           
            self.rect.move(0, -1)
           
            self.rect.move(0, 1)

        def draw(self, surface):
            self.x_ini += 40
            self.y_ini -= self.gravity
            pygame.draw.rect(pantalla, (255,0,0), (self.x_ini, self.y_ini, 16, 16))





    if difficulty == '1':
        ruta = 1
        
    elif difficulty == '2':
        ruta = 2
    elif difficulty == 'HARD':
        ruta = 3
    else:
        raise Exception('Unknown difficulty {0}'.format(difficulty))

    # Draw random color and text
    bg_color = random_color()
    #f_width = f.get_size()[0]

    # Reset main menu and disable
    # You also can set another menu, like a 'pause menu', or just use the same
    # main_menu as the menu that will check all your input.
    main_menu.disable()
    main_menu.reset(1)

    player = Player(100,100)
    clock = pygame.time.Clock()

    while True:

        # Clock tick
        clock.tick(3)

        player.draw(pantalla)
        player.update()
        pygame.display.update()





        # Application events
        playevents = pygame.event.get()
        for e in playevents:
            if e.type == quit:
                exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    if main_menu.is_disabled():
                        main_menu.enable()

                        # Quit this function, then skip to loop of main-menu on line 197
                        return

        # Pass events to main_menu
        main_menu.mainloop(playevents)

        # Continue playing
        pantalla.fill(bg_color)
        pantalla.blit(fondo_mapa, [0, 0])

        pygame.display.flip()

def main_background():
    """
    Function used by menus, draw on background while menu is active.
    
    :return: None
    """
    pantalla.fill(COLOR_BACKGROUND)

play_menu = pygameMenu.Menu(pantalla,
                            bgfun=main_background,
                            color_selected=BLANCO,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=NEGRO,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_height=int(CONF_PANTALLA[1] * 0.6),
                            menu_width=int(CONF_PANTALLA[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Jugar',
                            window_height=CONF_PANTALLA[1],
                            window_width=CONF_PANTALLA[0]
                            )
# When pressing return -> play(DIFFICULTY[0], font)
play_menu.add_option('Empieza', play_function, DIFFICULTY,
                     pygame.font.Font(pygameMenu.fonts.FONT_FRANCHISE, 30))
play_menu.add_selector('Selecciona Ruta', [('1', '1'),
                                             ('2', '2'),
                                             ('3', '3')],
                       onreturn=None,
                       onchange=change_difficulty)
play_menu.add_option('Regresar al menu', PYGAME_MENU_BACK)

# ABOUT MENU
about_menu = pygameMenu.TextMenu(pantalla,
                                 bgfun=main_background,
                                 color_selected=BLANCO,
                                 font=pygameMenu.fonts.FONT_BEBAS,
                                 font_color=NEGRO,
                                 font_size_title=30,
                                 font_title=pygameMenu.fonts.FONT_8BIT,
                                 menu_color=MENU_BACKGROUND_COLOR,
                                 menu_color_title=BLANCO,
                                 menu_height=int(CONF_PANTALLA[1] * 0.6),
                                 menu_width=int(CONF_PANTALLA[0] * 0.6),
                                 onclose=PYGAME_MENU_DISABLE_CLOSE,
                                 option_shadow=False,
                                 text_color=NEGRO,
                                 text_fontsize=20,
                                 title='Creditos',
                                 window_height=CONF_PANTALLA[1],
                                 window_width=CONF_PANTALLA[0]
                                 )
for m in ABOUT:
    about_menu.add_line(m)
about_menu.add_line(PYGAMEMENU_TEXT_NEWLINE)
about_menu.add_option('Regresar al menu', PYGAME_MENU_BACK)

# MAIN MENU

main_menu = pygameMenu.Menu(pantalla,
                            bgfun=main_background,
                            color_selected=BLANCO,
                            font=pygameMenu.fonts.FONT_BEBAS,
                            font_color=NEGRO,
                            font_size=30,
                            menu_alpha=100,
                            menu_color=MENU_BACKGROUND_COLOR,
                            menu_height=int(CONF_PANTALLA[1] * 0.6),
                            menu_width=int(CONF_PANTALLA[0] * 0.6),
                            onclose=PYGAME_MENU_DISABLE_CLOSE,
                            option_shadow=False,
                            title='Simulador de Rutas',
                            window_height=CONF_PANTALLA[1],
                            window_width=CONF_PANTALLA[0]
                            )

main_menu.add_option('Empezar', play_menu)
main_menu.add_option('About', about_menu)
main_menu.add_option('Quit', PYGAME_MENU_EXIT)










def random_color():
    """
    Return random color.
    
    :return: Color tuple
    """
    return randrange(0, 255), randrange(0, 255), randrange(0, 255)


class Protagonista(pygame.sprite.Sprite): 
    """ Esta clase representa la barra inferior que controla el protagonista """
   
    # -- Atributos 
    # Establecemos el vector velocidad del protagonista
    cambio_x = 0
    cambio_y = 0
     
    # Lista de todos los sprites contra los que podemos botar
    nivel = None
     
    # -- Métodos
    def __init__(self): 
        """ Función Constructor  """
         
        #  -- Llama al constructor padre 
        super().__init__() 
         
        # Crea una imagen del bloque y lo rellena con color rojo.
        # También podríamos usar una imagen guardada en disco   
        largo = 20
        alto = 40
        self.image = pygame.Surface([largo, alto])
        self.image.fill(random_color())        
   
        # Establecemos una referencia hacia la imagen rectangular
        self.rect = self.image.get_rect() 
       
    def update(self): 
        """ Desplazamos al protagonista. """
        # Gravedad
        self.calc_grav()
         
        # Desplazar izquierda/derecha
        self.rect.x += self.cambio_x
         
        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        for bloque in lista_impactos_bloques:
            # Si nos estamos desplazando hacia la derecha, hacemos que nuestro lado derecho sea el lado izquierdo del objeto que hemos tocado-
            if self.cambio_x > 0:
                self.rect.right = bloque.rect.left
            elif self.cambio_x < 0:
                # En caso contrario, si nos desplazamos hacia la izquierda, hacemos lo opuesto.
                self.rect.left = bloque.rect.right
                
          
 
        # Desplazar arriba/abajo
        self.rect.y += self.cambio_y
         
        # Comprobamos si hemos chocado contra algo
        lista_impactos_bloques = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False) 
        for bloque in lista_impactos_bloques:
 
            # Restablecemos nuestra posición basándonos en la parte superior/inferior del objeto.
            if self.cambio_y > 0:
                self.rect.bottom = bloque.rect.top 
            elif self.cambio_y < 0:
                self.rect.top = bloque.rect.bottom
 
            # Detenemos nuestro movimiento vertical
            self.cambio_y = 0
 
    def calc_grav(self):
        """ Calculamos el efecto de la gravedad. """
        if self.cambio_y == 0:
            self.cambio_y = 1
        else:
            self.cambio_y += .35
 
        # Observamos si nos encontramos sobre el suelo. 
        if self.rect.y >= ALTO_PANTALLA - self.rect.height and self.cambio_y >= 0:
            self.cambio_y = 0
            self.rect.y = ALTO_PANTALLA - self.rect.height
 
    def saltar(self):

        jump.play()
      
        """ Llamado cuando el usuario pulsa el botón de 'saltar'. """
         
        # Descendemos un poco y observamos si hay una plataforma debajo nuestro.
        # Descendemos 2 píxels (con una plataforma que está  descendiendo, no funciona bien 
    # si solo descendemos uno).
        self.rect.y += 2
        lista_impactos_plataforma = pygame.sprite.spritecollide(self, self.nivel.listade_plataformas, False)
        self.rect.y -= 2
         
        # Si está listo para saltar, aumentamos nuestra velocidad hacia arriba
        if len(lista_impactos_plataforma) > 0 or self.rect.bottom >= ALTO_PANTALLA:
            self.cambio_y = -10
             
    # Movimiento controlado por el protagonista
    def ir_izquierda(self):
        """ Es llamado cuando el usuario pulsa la flecha izquierda """
        self.cambio_x = -6
 
    def ir_derecha(self):
        """ Es llamado cuando el usuario pulsa la flecha derecha """
        self.cambio_x = 6
 
    def stop(self):
        """ Es llamado cuando el usuario abandona el teclado """
        self.cambio_x = 0
    
    def turbo_derecha(self):
        """ Es llamado cuando se presiona la tecla a. Hace ir a la derecha con mas rapidez """
        self.cambio_x = 20
        
    
    def turbo_izquierda(self):
        """ Es llamado cuando se presiona la tecla a. Hace ir a la izquierda con mas rapidez"""
        self.cambio_x = -20
                    
class Plataforma(pygame.sprite.Sprite):
    """ Plataforma sobre la que el usuario puede saltar. """
 
    def __init__(self, largo, alto ):
        """  Constructor de plataforma. Asume su construcción cuando el usuario le haya pasado 
            un array de 5 números, tal como se ha definido al principio de este código. """
        super().__init__()
         
        self.image = pygame.Surface([largo, alto])
        self.image.fill(ROJO)    
                 
        self.rect = self.image.get_rect()
  
class Nivel(object):
    """ Esta es una súper clase genérica usada para definir un nivel.
        Crea una clase hija específica para cada nivel con una info específica. """
         
    def __init__(self, protagonista):
        """ Constructor. Requerido para cuando las plataformas móviles colisionan con el protagonista. """
        self.listade_plataformas = pygame.sprite.Group()
        self.listade_enemigos = pygame.sprite.Group()
        self.protagonista = protagonista
 
         
        # Imagen de fondo
        self.imagende_fondo = None
         
     
    # Actualizamos todo en este nivel
    def update(self):
        """ Actualizamos todo en este nivel."""
        self.listade_plataformas.update()
        self.listade_enemigos.update()
     
    def draw(self, pantalla):
        """ Dibujamos todo en este nivel. """
         
        # Dibujamos la imagen de fondo
        pantalla.fill(AZUL)
                   
        # Dibujamos todas las listas de sprites que tengamos
        self.listade_plataformas.draw(pantalla)
        self.listade_enemigos.draw(pantalla)
 
     
# Creamos las plataformas para el nivel
class Nivel_01(Nivel):
    """ Definición para el nivel 1. """
 
    def __init__(self, protagonista):
        """ Creamos el nivel 1. """
         
        # llamamos al constructor padre
        Nivel.__init__(self, protagonista)
         
        # Array con la información sobre el largo, alto, x, e y
        nivel = [ [random.randint(33,500), random.randint(22,340), 50, 500],
                  [210, 70, 200, 400],
                  [random.randint(100,500), 7, random.randint(30,250), 300],
                  ]
 
        # Iteramos sobre el array anterior y añadimos plataformas
        for plataforma in nivel:
            bloque = Plataforma(plataforma[0], plataforma[1])
            bloque.rect.x = plataforma[2]
            bloque.rect.y = plataforma[3]
            bloque.protagonista = self.protagonista
            self.listade_plataformas.add(bloque)        

 
def main():
    """ Programa Principal """
    pygame.init() 
    print(pygame.key.get_focused())
    
    print(pygame.mouse.get_pos())


    #musica de fondo del juego engineering jumper
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(.4)
  
   

    # Definimos el alto y largo de la pantalla 
    dimensiones = [LARGO_PANTALLA, ALTO_PANTALLA] 
    pantalla = pygame.display.set_mode(dimensiones) 
       
    pygame.display.set_caption("Saltador de Plataformas ") 
     
    # Creamos al protagonista
    protagonista = Protagonista()
    while flag == 0:

    # Tick
        clock.tick(60)

    # Application events
        events = pygame.event.get()
      

    # Main menu
        main_menu.mainloop(events)

    # Flip surface
        pygame.display.flip()
    # Creamos todos los niveles
    listade_niveles = []
    listade_niveles.append(Nivel_01(protagonista))
     
    # Establecemos el nivel actual
    nivel_actual_no = 0
    nivel_actual = listade_niveles[nivel_actual_no]
     
    lista_sprites_activos = pygame.sprite.Group()
    protagonista.nivel = nivel_actual
     
    protagonista.rect.x = 340
    protagonista.rect.y = protagonista.rect.height - ALTO_PANTALLA
    lista_sprites_activos.add(protagonista)
         
    #Iteramos hasta que el usuario pulse sobre el botón de salida 
    hecho = False
    game_over = False
       
    # Lo usamos para gestionar cuan rápido se actualiza la pantalla.
    reloj = pygame.time.Clock() 
       
    # -------- Bucle Principal del Programa ----------- 
    while not game_over: 
        for evento in pygame.event.get(): # El usuario realizó alguna acción 
            if evento.type == pygame.QUIT: # Si el usuario hizo click en salir
                hecho = True # Marcamos como hecho y salimos de este bucle

            if evento.type == pygame.MOUSEBUTTONDOWN:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    protagonista.ir_izquierda()
                if evento.key == pygame.K_RIGHT:
                    protagonista.ir_derecha()
                if evento.key == pygame.K_UP:
                    protagonista.saltar()
                if evento.key == pygame.K_a and evento.key == pygame.K_RIGHT:
                    protagonista.turbo_derecha()
                if evento.key == pygame.K_a and evento.key == pygame.K_LEFT:
                    protagonista.turbo_izquierda()
             
            #Si se deja de presionar el teclado el jugador no se movera
            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and protagonista.cambio_x < 0: 
                    protagonista.stop()
                if evento.key == pygame.K_RIGHT and protagonista.cambio_x > 0:
                    protagonista.stop()
                    
            if evento.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                clicked_sprites = [s for s in lista_sprites_activos if s.rect.collidepoint(pos)]
                    
 
        # Actualizamos al protagonista. 
        lista_sprites_activos.update()
         
        # Actualizamos los objetos en este nivel
        nivel_actual.update()
    
        # Si el protagonista se aproxima al lado derecho, desplazamos su mundo a la izquierda (-x)
        if protagonista.rect.right > LARGO_PANTALLA-1:
            protagonista.rect.right = 22
            
     
        # Si el protagonista se aproxima al lado izquierdo, desplazamos su mundo a la derecha (+x)
        if protagonista.rect.left < 0:
            protagonista.rect.right = LARGO_PANTALLA-1
             
        # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO 
        nivel_actual.draw(pantalla)
        lista_sprites_activos.draw(pantalla)
         
        # TODO EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO 
           
        # Limitamos a 60 fps 
        reloj.tick(60) 
       
        # Avanzamos y actualizamos la pantalla con todo lo que hemos dibujado. 
        pygame.display.flip() 
           
    # Pórtate bien con el IDLE. Si te olvidas de esta línea, el programa se 'colgará' al salir.
    pygame.quit()
 
if __name__ == "__main__":
    main()