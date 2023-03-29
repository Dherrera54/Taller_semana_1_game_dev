from multiprocessing.connection import wait
from src.ecs.components.c_enemy_spawner import CEnemySpawner

from src.ecs.create.prefab_creator import crear_cuadrado
import esper
import pygame
import json


enemy_config_file = json.load(open('./assets/cfg/enemies.json'))


def system_enemy_spawner(ecs_world:esper.World, time:float, enemy_type:str, pos: pygame.Vector2):
    components = ecs_world.get_components(CEnemySpawner)

    enemy = enemy_config_file[enemy_type]
    size = enemy['size']
    color = enemy['color']

    c_e_s:CEnemySpawner

   
    crear_cuadrado(ecs_world,
                                pygame.Vector2(size['x'],size['y']), 
                                pygame.Vector2(pos.x, pos.y),
                                pygame.Vector2(enemy['velocity_min'],enemy['velocity_max']),
                                pygame.Color(color['r'], color['g'], color['b']))
