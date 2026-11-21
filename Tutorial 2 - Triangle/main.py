import glfw
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

    #Creating the vertex and fragment shader that will tell GPU how it should process the vertex data
    #Creating the vertex shader
    vertex_shader = glCreateShader(GL_VERTEX_SHADER)
    #Showing the source of the vertex shader
    glShaderSource(vertex_shader, return_file_contents("shaders/vertex_sh.glsl"))
    #Compiling the vertex shader into binaries that OpenGL will understand
    glCompileShader(vertex_shader)

    #Creating the fragment shader
    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER);
    #Showing the source of the fragment shader
    glShaderSource(fragment_shader, return_file_contents("shaders/fragment_sh.glsl"))
    #Compiling the fragment shader into binaries that OpenGL will understand
    glCompileShader(fragment_shader)

    #Creating the shader program
    shader_program = glCreateProgram()
    #Attaching the vertex and fragment shader into the program
    glAttachShader(shader_program, vertex_shader)
    glAttachShader(shader_program, fragment_shader)
    #Links the program for usage
    glLinkProgram(shader_program)

    # Deleting the shaders because we wont need them any longer
    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    #Initializes the VAO that makes it easier to bind (if there will be) lots of VBO objects
    #Also core OpenGL needs a VAO object which makes VAO an mandatory object
    vao1 = glGenVertexArrays(1)
    #Binds the VAO object
    glBindVertexArray(vao1)

    #Initializes the VBO object that stores the vertices
    vbo1 = glGenBuffers(1)
    #Binding VBO objects and defining its data
    glBindBuffer(GL_ARRAY_BUFFER, vbo1)
    glBufferData(GL_ARRAY_BUFFER, VERTICES1.nbytes, VERTICES1, GL_STATIC_DRAW)

    #Setting the vertex attribute pointer (which in vertex shader the vertex positions are located in layout 0 so this pointer points to vertex coordinates)
    # and showing OpenGL how to interpret the vertex data - also this attribute needs to be enabled because it is disabled by default
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * ctypes.sizeof(ctypes.c_float), ctypes.c_void_p(0))
    #Enabling the vertex attribute pointer
    glEnableVertexAttribArray(0)

    #Initializes the EBO object that store the indices
    ebo1 = glGenBuffers(1)
    #Binding the EBO objects and defining its data
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo1)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, INDICES1.nbytes, INDICES1, GL_STATIC_DRAW)

    #Unbind the objects to not to accidentally assigning them later
    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, 0)
    glBindVertexArray(0)

    while not glfw.window_should_close(window1):
      
        glClearColor(0.1, 0.1, 0.1, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        #Activates the shader program
        glUseProgram(shader_program)

        #Rebinding VAO object to access vertices
        glBindVertexArray(vao1)

        #Drawing / rendering function
        glDrawElements(GL_TRIANGLES, 0, GL_UNSIGNED_INT, INDICES1)

        glfw.swap_buffers(window1)
        glfw.poll_events()

    #Destroys the VAO, VBO and EBO objects to free the memory
    glDeleteVertexArrays(1, [vao1])
    glDeleteBuffers(1, [vbo1])
    glDeleteBuffers(1, [ebo1])
  
    glfw.destroy_window(window1)
    glfw.terminate()

# A way to prevent the file opening more than once.
if __name__ == "__main__":
    main() #The main program
