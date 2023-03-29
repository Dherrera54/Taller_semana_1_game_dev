import esper
import pygame
import json
from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_velocity import CVelocity
from src.ecs.components.c_surface import CSurface
from src.ecs.components.c_enemy_spawner import CEnemySpawner

def crear_cuadrado(ecs_world: esper.World,
                   size: pygame.Vector2, 
                   pos: pygame.Vector2, 
                   vel: pygame.Vector2, 
                   col: pygame.Vector2):
    cuad_entity = ecs_world.create_entity()
    
    ecs_world.add_component(cuad_entity,
                            CSurface(size,col))
    ecs_world.add_component(cuad_entity,
                            CTransform(pos))
    ecs_world.add_component(cuad_entity,
                            CVelocity(vel))  
      

def crear_spawner(ecs_world: esper.World,
                   level_config:list):
    spawner_entity = ecs_world.create_entity()
    ecs_world.add_component(spawner_entity,
                         CEnemySpawner(level_config))