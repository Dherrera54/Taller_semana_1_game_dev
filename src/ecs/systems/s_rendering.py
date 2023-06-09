from src.ecs.components.c_transform import CTransform
from src.ecs.components.c_surface import CSurface
import esper
import pygame

def system_rendering(world:esper.World, screen:pygame.Surface):
    components = world.get_components(CTransform, CSurface)

    c_t:CTransform
    c_s:CSurface
    for entity, ( c_t, c_s) in components:
        screen.blit(c_s.surf, c_t.pos)

