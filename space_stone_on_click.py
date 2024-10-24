import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

def load_texture(filename):
    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    image = pygame.image.load(filename)
    image_data = pygame.image.tostring(image, "RGBA", True)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.get_width(), image.get_height(), 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    return texture_id

def draw_background(texture_id):
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glEnd()

def draw_cube(texture_id, x, y, z, scale, rotation):
    vertices = (
        (1.0, -1.0, -1.0),
        (1.0, 1.0, -1.0),
        (-1.0, 1.0, -1.0),
        (-1.0, -1.0, -1.0),
        (1.0, -1.0, 1.0),
        (1.0, 1.0, 1.0),
        (-1.0, -1.0, 1.0),
        (-1.0, 1.0, 1.0)
    )
    faces = (
        (0, 1, 2, 3),
        (3, 2, 7, 6),
        (6, 7, 5, 4),
        (4, 5, 1, 0),
        (1, 5, 7, 2),
        (4, 0, 3, 6)
    )
    tex_coords = (
        (0.0, 0.0),
        (1.0, 0.0),
        (1.0, 1.0),
        (0.0, 1.0)
    )

    glBindTexture(GL_TEXTURE_2D, texture_id)

    glPushMatrix()
    glTranslatef(x, y, z)
    glScalef(scale, scale, scale)
    glRotatef(rotation[0], 1.0, 0.0, 0.0)
    glRotatef(rotation[1], 0.0, 1.0, 0.0)
    glRotatef(rotation[2], 0.0, 0.0, 1.0)
    
    glBegin(GL_QUADS)
    for face in faces:
        for i in range(4):
            glTexCoord2fv(tex_coords[i])
            glVertex3fv(vertices[face[i]])
    glEnd()
    
    glPopMatrix()

def draw_glow(x, y, z, scale, angle):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(angle, 0, 1, 0)
    glScalef(scale, scale * 2, scale)
    
    glDisable(GL_TEXTURE_2D)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE)
    
    glColor4f(0.1, 0.7, 0.5, 0.2)  # Light blue with alpha
    
    for i in range(20):  # Draw multiple layers for the glow effect
        glow_scale = 1.0 + (i * 0.05)
        glPushMatrix()
        glScalef(glow_scale, glow_scale, glow_scale)
        quadric = gluNewQuadric()
        gluSphere(quadric, 0.5, 10, 7)
        gluDeleteQuadric(quadric)
        glPopMatrix()
    
    glDisable(GL_BLEND)
    glEnable(GL_TEXTURE_2D)
    glPopMatrix()

def draw_oval_stone(x, y, z, scale, angle):
    # Draw the glow effect first
    draw_glow(x, y, z, scale, angle)  # Slightly larger scale for the glow
    
    # Then draw the stone as before
    glColor3f(1.0, 1.0, 1.0)  # Set color to white
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(angle, 0, 1, 0)  # Rotate around the y-axis
    glScalef(scale, scale * 2, scale)  # Make it oval vertically

    quadric = gluNewQuadric()
    gluQuadricTexture(quadric, GL_TRUE)
    gluSphere(quadric, 0.5, 10, 7)  # Draw a sphere (which will be scaled to an oval)
    gluDeleteQuadric(quadric)

    glPopMatrix()

def split_part(part):
    """Split a part into multiple smaller parts."""
    new_parts = []
    num_new_parts = random.randint(1, 2)  # Generate 1 to 2 new parts
    for _ in range(num_new_parts):
        new_part = part.copy()
        # Randomize the position slightly
        new_part[0] += random.uniform(-0.1, 0.1)
        new_part[1] += random.uniform(-0.1, 0.1)
        new_part[2] += random.uniform(-0.1, 0.1)
        # Randomize the velocity with higher speeds
        new_part[3] = random.uniform(-0.2, 0.2)
        new_part[4] = random.uniform(-0.2, 0.2)
        new_part[5] = random.uniform(-0.2, 0.2)
        # Randomize the rotation
        new_part[6] = [random.uniform(-5, 5) for _ in range(3)]
        # Reduce the scale more
        new_part[7] *= random.uniform(0.3, 0.7)
        new_parts.append(new_part)
    return new_parts

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)

    background_texture_id = load_texture("D:\\CG\\mini project\\code_project\\background.jpg")
    texture_id = load_texture("D:\\CG\\mini project\\code_project\\tesseract.png")

    angle = 0.0
    stone_angle = 0.0
    scale = 1.0

    parts = []
    for i in range(-1, 2, 2):
        for j in range(-1, 2):
            for k in range(-1, 2):
                parts.append([i / 2.0, j / 2.0, k / 2.0, 0.0, 0.0, 0.0, [0, 0, 0], 0.1])

    break_cube = False
    break_time = 0
    show_stone = False
    start_stone_rotation = False
    stone_z = -5.0

    start_time = pygame.time.get_ticks()

    size_decreased = False
    cube_broken = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if not size_decreased:
                    size_decreased = True
                elif size_decreased and not cube_broken:
                    break_cube = True
                    break_time = pygame.time.get_ticks()
                    cube_broken = True
                    for part in parts:
                        part[3] = random.uniform(-0.05, 0.05)
                        part[4] = random.uniform(-0.05, 0.05)
                        part[5] = random.uniform(-0.05, 0.05)
                        part[6] = [random.uniform(-5, 5) for _ in range(3)]

        current_time = pygame.time.get_ticks()

        if break_cube and (current_time - break_time >= 10000):
            pygame.quit()
            quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glClearColor(0.0, 0.0, 0.0, 1.0)

        glPushMatrix()
        glLoadIdentity()
        glDisable(GL_DEPTH_TEST)
        draw_background(background_texture_id)
        glEnable(GL_DEPTH_TEST)
        glPopMatrix()

        if not break_cube:
            glPushMatrix()
            glRotatef(angle, 1.0, 1.0, 1.0)
            glScalef(scale, scale, scale)
            draw_cube(texture_id, 0.0, 0.0, 0.0, 1.0 if not size_decreased else scale, [0, 0, 0])
            glPopMatrix()

            if size_decreased and scale > 0.5:
                scale -= 0.01

        else:
            if current_time - break_time < 2000:
                new_parts = []
                for part in parts:
                    if part[7] > 0.01:
                        draw_cube(texture_id, part[0], part[1], part[2], part[7], part[6])
                        part[0] += part[3]
                        part[1] += part[4]
                        part[2] += part[5]
                        part[4] -= 0.001  # Gravity effect
                        part[7] *= 0.98   # Scale reduction for realistic explosion
                        part[6] = [part[6][i] + random.uniform(-1, 1) for i in range(3)]  # Update rotation

                        if abs(part[0]) <= 10 and abs(part[1]) <= 10 and abs(part[2]) <= 10:
                            if random.random() < 0.05:
                                new_parts.extend(split_part(part))
                            else:
                                new_parts.append(part)
                parts = new_parts

            if current_time - break_time >= 0 and not show_stone:
                show_stone = True
                start_stone_rotation = True

            if show_stone:
                draw_oval_stone(0.0, 0.0, stone_z, 0.25, stone_angle)
                if start_stone_rotation:
                    stone_z += 0.01
                    stone_angle += 1.0

        pygame.display.flip()
        pygame.time.wait(10)

        # Update the rotation angle
        angle += 1.0

if __name__ == "__main__":
    main()
