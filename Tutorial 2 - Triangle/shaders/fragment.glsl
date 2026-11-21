#version 330 core //Means were using the 3.3 core version of OpenGL

//Takes FragColor as an output
out vec4 FragColor;

//Main function of the shader
void main(){
    FragColor = vec4(1.0, 0.0, 0.0, 1.0); //Sets the color of the triangle with FragColor
}
