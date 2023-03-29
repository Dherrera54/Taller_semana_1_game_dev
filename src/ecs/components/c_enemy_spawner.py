
import pygame


class CEnemySpawner:
    def __init__(self, level_config:list) -> None:
       self.now :float = 0
       self.spawnEventData:list[SpawnEventData] = []
       for enemy in level_config:
            self.spawnEventData.append(SpawnEventData(enemy['time'],
            enemy['enemy_type'],
            pygame.Vector2(enemy['position']['x'],enemy['position']['y'])
            ))
        

class SpawnEventData:
    def __init__(self, time: float, enemy_type:str, pos:pygame.Vector2) -> None:
        self.time:float = time
        self.enemy_type:str =  enemy_type
        self.pos:pygame.Vector2 = pos
        
        