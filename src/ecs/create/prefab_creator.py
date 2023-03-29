import esper
import pygame
import json
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_enemy_spawner import CEnemySpawner

def crear_cuadrado(ecs_world: esper.World,
                   enemy_type: str, 
                   pos: pygame.Vector2, 
                   enemy_config: dict):

    size=  enemy_config[enemy_type]['size'] 
    color=enemy_config[enemy_type]['color']
    vel=  pygame.Vector2(enemy_config[enemy_type]['velocity_min'],enemy_config[enemy_type]['velocity_max'])
     
    cuad_entity = ecs_world.create_entity()
    
    ecs_world.add_component(cuad_entity,
                            CSurface(pygame.Vector2(size['x'],size['y']), pygame.Color(color['r'], color['g'],color['b'])))
    ecs_world.add_component(cuad_entity,
                            CTransform(pos))
    ecs_world.add_component(cuad_entity,
                            CVelocity(vel))  
      

def crear_spawner(ecs_world: esper.World,
                   level_config:list):
    spawner_entity = ecs_world.create_entity()
    ecs_world.add_component(spawner_entity,
                         CEnemySpawner(level_config))