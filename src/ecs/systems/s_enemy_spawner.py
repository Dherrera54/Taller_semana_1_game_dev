from src.ecs.components.c_enemy_spawner import CEnemySpawner
from src.create.prefab_creator import crear_cuadrado
import esper
import pygame
import json


enemy_config_file = json.load(open('./assets/cfg/enemies.json'))

def system_enemy_spawner(ecs_world:esper.World, delta_time:float):

    components = ecs_world.get_components(CEnemySpawner)
    c_e_s:CEnemySpawner
    
    for entity, c_e_s in components:

        c_e_s[0].now+=delta_time
        
        for enemy  in c_e_s[0].enemies:

            enemy_type = enemy[1]
            enemy_pos = enemy[2]
            
            if enemy[3]==False and c_e_s[0].now>=enemy[0]:
                enemy[3]=True
                crear_cuadrado(ecs_world,
                                enemy_type, 
                                pygame.Vector2(enemy_pos[0], enemy_pos[1]),
                                enemy_config_file)
