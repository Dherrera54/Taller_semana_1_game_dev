from multiprocessing.connection import wait
from src.ecs.components.c_enemy_spawner import CEnemySpawner, SpawnEventData

from src.ecs.create.prefab_creator import crear_cuadrado
import esper
import pygame
import json


enemy_config_file = json.load(open('./assets/cfg/enemies.json'))


def system_enemy_spawner(ecs_world:esper.World, delta_time:float):
    components = ecs_world.get_components(CEnemySpawner)
    c_e_s:CEnemySpawner
    for entity, c_e_s in components:
        c_e_s.now+= delta_time
        enemy_spawn:SpawnEventData
        for enemy_spawn  in c_e_s.spawnEventData:

            enemy = enemy_spawn['enemy_type']
            size = enemy['size']
            color = enemy['color']
            pos = enemy_spawn['position']
            crear_cuadrado(ecs_world,
                                    pygame.Vector2(size['x'],size['y']), 
                                    pygame.Vector2(pos['x'], pos['y']),
                                    pygame.Vector2(enemy['velocity_min'],enemy['velocity_max']),
                                    pygame.Color(color['r'], color['g'], color['b']))
