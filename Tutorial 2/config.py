import numpy

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_TITLE = "OpenGL with GLFW"

VERTICES1 = numpy.array([
    -0.5, -0.5,  0.0, #Lower left
     0.5, -0.5,  0.0, #Lower right
     0.5,  0.5,  0.0,  #
    -0.5,  0.5,  0.0
], dtype=numpy.float32)

INDICES1 = numpy.array([
    0, 1, 2,
    0, 2, 3
], dtype=numpy.int32)
