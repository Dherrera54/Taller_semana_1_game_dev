from src.ecs.create.prefab_creator import crear_spawner, crear_cuadrado
from src.ecs.systems.s_enemy_spawner import system_enemy_spawner
from src.ecs.systems.s_screen_bounce import system_screen_bounce
from src.ecs.systems.s_rendering import system_rendering
from src.ecs.systems.s_movement import system_movement
import esper
import pygame
import json

window_config_file = json.load(open('./assets/cfg/window.json'))
level_config_file = json.load(open('./assets/cfg/level_01.json'))
window_size = window_config_file['window']['size']
framerate = window_config_file['window']['framerate']
bg_color = window_config_file['window']['bg_color']

class GameEngine:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((window_size['w'],window_size['h']),pygame.SCALED)
        pygame.display.set_caption(window_config_file['window']['title'])
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.framerate = framerate
        self.delta_time = 0

        self.ecs_world = esper.World()

    def run(self) -> None:
        self._create()
        self.is_running = True
        while self.is_running:
            self._calculate_time()
            self._process_events()
            self._update()
            self._draw()
        self._clean()

    def _create(self):

        crear_spawner(self.ecs_world, level_config_file['enemy_spawn_events'])
        
        """ for enemy in level_config_file['enemy_spawn_events']:            
            system_enemy_spawner(self.ecs_world,
                                    enemy['time'],
                                    enemy['enemy_type'],
                                    pygame.Vector2(enemy['position']['x'],enemy['position']['y'])) """

    def _calculate_time(self):
        self.clock.tick(self.framerate)
        self.delta_time = self.clock.get_time()/1000.0

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running=False
            

    def _update(self):
        system_enemy_spawner(self.ecs_world, self.delta_time)
        system_movement(self.ecs_world, self.delta_time)
        system_screen_bounce(self.ecs_world, self.screen)

    def _draw(self):
        self.screen.fill((bg_color['r'],
                          bg_color['g'],
                          bg_color['b']))

        system_rendering(self.ecs_world, self.screen)
        

        pygame.display.flip()

    def _clean(self):
        pygame.quit()
