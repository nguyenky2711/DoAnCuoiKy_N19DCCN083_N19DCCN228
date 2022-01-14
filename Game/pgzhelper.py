import math
import pygame
from pgzero.actor import Actor, POS_TOPLEFT, ANCHOR_CENTER, transform_anchor
from pgzero import game, loaders
import types
import sys
import time
class Actor(Actor):
  @property
  def images(self):
    return self._images

  @images.setter
  def images(self, images):
    self._images = images
    if len(self._images) != 0:
      self.image = self._images[0]

  def next_image(self):
    if self.image in self._images:
      current = self._images.index(self.image)
      if current == len(self._images) - 1:
        self.image = self._images[0]
      else:
        self.image = self._images[current + 1]
    else:
      self.image = self._images[0]

  def draw(self):
    game.screen.blit(self._surf, self.topleft)

