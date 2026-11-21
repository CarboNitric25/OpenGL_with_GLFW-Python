mport glfw
import ctypes
from OpenGL.GL import *
from OpenGL.GLU import *
from config import *

def return_file_contents(filepath):
    open_file = open(filepath, "r", encoding="utf-8");
    return open_file.read();

def main():

    if not glfw.init():
        raise RuntimeError("Failed to initialize GLFW library.")

    glfw.window_hint(glfw.RESIZABLE, glfw.FALSE)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    window1 = glfw.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, None, None)
    if not window1:
        raise RuntimeError("Failed to initialize the window.")

    glfw.make_context_current(window1) 

    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)

    vertex_shader = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vertex_shader, return_file_contents("shaders/vertex_sh.glsl"))
    glCompileShader(vertex_shader)

    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragment_shader, return_file_contents("shaders/fragment_sh.glsl"))
    glCompileShader(fragment_shader)

    shader_program = glCreateProgram()
    glAttachShader(shader_program, vertex_shader)
    glAttachShader(shader_program, fragment_shader)
    glLinkProgram(shader_program)

    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    vao1 = glGenVertexArrays(1)
    glBindVertexArray(vao1)

    vbo1 = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo1)
    glBufferData(GL_ARRAY_BUFFER, VERTICES1.nbytes, VERTICES1, GL_STATIC_DRAW)

    #Changing some of the parameters(stride and pointer) because of the byte offset between different attributes 
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 6 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
    glEnableVertexAttribArray(0)

    #Setting the vertex attribute pointer of layout 1 (which in this case it is vertex color)
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 6 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(3 * ctypes.sizeof(ctypes.c_float)))
    glEnableVertexAttribArray(1)
  
    ebo1 = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo1)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, INDICES1.nbytes, INDICES1, GL_STATIC_DRAW)
    
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    
    while not glfw.window_should_close(window1):
      
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        glUseProgram(shader_program)

        glBindVertexArray(vao1)

        glDrawElements(GL_TRIANGLES, 0, GL_UNSIGNED_INT, INDICES1)

        glfw.swap_buffers(window1)
        glfw.poll_events()

    glDeleteVertexArrays(1, [vao1])
    glDeleteBuffers(1, [vbo1])
    glDeleteBuffers(1, [ebo1])
  
    glfw.destroy_window(window1)
    glfw.terminate()

if __name__ == "__main__":
    main()
