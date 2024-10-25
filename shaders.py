vertex_shader = '''
#version 450 core

layout (location = 0) in vec3 position;
layout (location = 1) in vec2 texCoords;
layout (location = 2) in vec3 normala;

out vec2 outTexCoords;
out vec3 outNormals;

void main()
{
    gl_Position = vec4(position, 1.0);
    outColor = texCoords;
    outNormals = normals;
}
'''
fragment_shader ='''

#version 450 core
in vec3 outColor;
out vec4 fragColor;

void main()
{
    fragColor = vec4(outColor, 1.0);
}
'''