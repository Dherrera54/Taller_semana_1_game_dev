import pygame
class CEnemySpawner:
    def __init__(self, level_config:list) -> None:
       self.now  = 0.0
       self.enemies= []
       self.spawned=False
       for enemy in level_config:
            print(enemy)
            self.enemies.append([enemy['time'],
            enemy['enemy_type'],
            pygame.Vector2(enemy['position']['x'],enemy['position']['y']), 
            False])

        
        
        