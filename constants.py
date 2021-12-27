import pygame
import random

FPS = 60  # Game FPS

WIN_WIDTH = 1200  # width
WIN_HEIGHT = 1000  # height

BUBBLE_SPACE = 40  # distance between bubbles
INIT_R = 10  # initial radius
DR = 4  # number increase due to number
NUMBER = 10  # number of bubbles

COLORS = {
    "bg": (240, 255, 255),  # background color
    "bubble": (135, 206, 235),  # bubble colors
    "select": (0, 139, 139),  # selected bubble color
    "text": (0, 0, 0),  # text color
}

font = pygame.font.SysFOnt("Arial", 23)

pygame.init()  

