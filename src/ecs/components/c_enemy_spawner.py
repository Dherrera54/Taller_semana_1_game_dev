
import pygame
from sqlalchemy import false


class CEnemySpawner:
    def __init__(self, level_config:list) -> None:
       self.now  = 0.0
       self.spawnEventData= []
       for enemy in level_config:
            print(enemy)
            self.spawnEventData.append(SpawnEventData(enemy['time'],
            enemy['enemy_type'],
            pygame.Vector2(enemy['position']['x'],enemy['position']['y'])
            ))
        

class SpawnEventData:
    def __init__(self, time: float, enemy_type:str, pos:pygame.Vector2) -> None:
        self.spawned=False
        self.time=time
        self.enemy_type =  enemy_type
        self.pos = pos
        
        