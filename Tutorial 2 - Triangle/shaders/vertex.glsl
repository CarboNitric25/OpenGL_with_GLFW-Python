#version 330 core //Means were using the 3.3 core version of OpenGL

//Locating the vertex positions in location 1 layout
layout (location = 0) in vec3 aPos;

//The main function of the shader
void main(){
    gl_Position = vec4(aPos.x, aPos.y, aPos.z, 1.0); //Writing vertex positions
}
