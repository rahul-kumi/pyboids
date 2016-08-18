# pyboids by mancaf
# Implementing the Boid Flocking Behaviour algorithm
# in Python and Pygame

import os
import pygame
import pygame.freetype
pygame.init()
pygame.freetype.init()

# General parameters
TITLE = "PYBOIDS"
SUBTITLE = "An implementation of Boids algorithm in Python."
CAPTION = "PyBoids - Flocking Behaviour Simulator"
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMG_DIR = os.path.join(BASE_DIR, *["static", "img"])
FONTS_DIR = os.path.join(BASE_DIR, *["static", "fonts"])

# Screen and viewing parameters
SCREEN_HEIGHT, SCREEN_WIDTH = 720, 960
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
COL = SCREEN_WIDTH//12
ROW = SCREEN_HEIGHT//9
FPS = 60
BACKGROUND = pygame.Color("slate gray")
FONTS = {
	"hallo-sans-light": pygame.freetype.Font(os.path.join(FONTS_DIR, *["hallo-sans", "Hallo sans light.otf"])),
	"hallo-sans-bold": pygame.freetype.Font(os.path.join(FONTS_DIR, *["hallo-sans", "Hallo sans black.otf"])),
	"hallo-sans": pygame.freetype.Font(os.path.join(FONTS_DIR, *["hallo-sans", "Hallo sans.otf"])),
	"quicksand": pygame.freetype.Font(os.path.join(FONTS_DIR, *["quicksand", "Quicksand-Regular.otf"])),
	"quicksand-bold": pygame.freetype.Font(os.path.join(FONTS_DIR, *["quicksand", "Quicksand-Bold.otf"])),
	"quicksand-light": pygame.freetype.Font(os.path.join(FONTS_DIR, *["quicksand", "Quicksand-Light.otf"])),
}
FONT_SIZES = {
	"body": 14,
	"h1": 128,
	"h2": 48,
	"h3": 32,
	"h4": 24,
	"h5": 18,
}
FONT_COLOR = pygame.Color("white")
BODY_FONT = (FONTS["quicksand"], FONT_SIZES["body"], )
H1_FONT = (FONTS["hallo-sans-light"], FONT_SIZES["h1"])
H2_FONT = (FONTS["hallo-sans"], FONT_SIZES["h2"])
H3_FONT = (FONTS["quicksand-bold"], FONT_SIZES["h3"])
H4_FONT = (FONTS["quicksand-bold"], FONT_SIZES["h4"])
H5_FONT = (FONTS["quicksand-bold"], FONT_SIZES["h5"])