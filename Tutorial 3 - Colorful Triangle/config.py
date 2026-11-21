import numpy

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_TITLE = "OpenGL with GLFW"

VERTICES1 = numpy.array([
    # Vertex Positions  Vertex Color
    # x,    y,    z,    r,    g,    b
    -0.5, -0.5,  0.0,  1.0,  0.0,  0.0, #Lower left
     0.5, -0.5,  0.0,  0.0,  1.0,  0.0, #Lower right
     0.0,  0.5,  0.0,  0.0,  0.0,  1.0  #Upper middle
], dtype=numpy.float32)

INDICES1 = numpy.array([
    0, 1, 2, #0 means the first element on the VERTICES1 array, 1 means the second and so on
], dtype=numpy.int32)
