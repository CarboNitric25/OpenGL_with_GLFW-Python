
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
from config import *

def main():

    if not glfw.init(): #Initializes the GLFW library. If any errors it throws a runtime error
        raise RuntimeError("Failed to initialize GLFW library.")

    #Sets some of the properties of window before creating it
    glfw.window_hint(glfw.RESIZABLE, glfw.FALSE)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    
    #Creates the window where all graphics processing will be done.
    window1 = glfw.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE, None, None)
    if not window1: # If theres an error initializing the window it throws a runtime error
        raise RuntimeError("Failed to initialize the window.")

    #Makes the window current context so OpenGL knows what window are we talking about.
    glfw.make_context_current(window1) 

    #Creates the viewport of our window
    glViewport(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT);

    # Main loop of the window we created. It prevents from the window closing until close button is pressed.
    while not glfw.window_should_close(window1):
        glfw.swap_buffers(window1) #Swap backbuffer (which rendering is done) to front buffer (which you can see the final graphic).
        glfw.poll_events() #Processes events (such as mouse click) until close button is pressed.

    glfw.destroy_window(window1) #Destroys the window to free the memory when exiting the mainloop.
    glfw.terminate() #Terminates the GLFW library to free memory.

# A way to prevent the file opening more than once.
if __name__ == "__main__":
    main() #The main program
