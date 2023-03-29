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
        
        c_e_s[0].now+= delta_time
        enemy_spawn:SpawnEventData
        for enemy_spawn  in c_e_s[0].spawnEventData:
            
            enemy = enemy_spawn.enemy_type
            pos = enemy_spawn.pos

            if enemy_spawn.spawned==False and c_e_s[0].now>=enemy_spawn.time:
                enemy_spawn.spawned=True
                crear_cuadrado(ecs_world,
                                        enemy, 
                                        pygame.Vector2(pos[0], pos[1]),
                                        enemy_config_file
                                        )
