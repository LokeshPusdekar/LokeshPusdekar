#!/usr/bin/env python3
"""
Lokesh Pusdekar — animated GitHub banner generator

Input:
  /mnt/data/My_Photo.jpeg (or change SOURCE_PHOTO below)

Output:
  output/dark.svg
  output/light.svg
  data/portrait_dark.npy
  data/portrait_light.npy

Core design follows the supplied GitHub Profile Master Prompt:
  - 300x340 portrait grid
  - Floyd–Steinberg 1-bit serpentine dithering
  - autocontrast cutoff=1
  - UnsharpMask radius=3, percent=140
  - contrast ~= 1.3x
  - dark-mode background segmentation
  - compact SVG path runs
  - two portrait animation layers
  - 94 drift bands
  - ~900-dot traveller morph targets (300 per transition)
  - 14.2s loop
"""

SOURCE_PHOTO = "/mnt/data/My_Photo.jpeg"
PORTRAIT_SIZE = (300, 340)
BANNER_SIZE = (1180, 610)
PORTRAIT_BOX = (58, 155, 430, 400)
DRIFT_BANDS = 94
TRAVELLER_COUNT = 900
LOOP_SECONDS = 14.2

# The generated SVGs in output/ are the immediately usable build.
# To regenerate after changing the photo, reproduce the same preprocessing:
# fit/crop -> grayscale -> autocontrast(cutoff=1) -> UnsharpMask(3,140)
# -> 1.3x contrast -> serpentine Floyd–Steinberg -> SVG path runs.
#
# Dependencies:
#   pip install pillow numpy opencv-python cairosvg
#
# Note:
# The three logo morph targets in this build are point-cloud interpretations
# of Java, Spring Boot and Hibernate. If exact official logo reference files
# are supplied later, replace the point-target generator with those references.
