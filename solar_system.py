from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle = 0

def init():
    glEnable(GL_TEXTURE_2D)
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 800/600, 0.1, 200)


def draw_planet(rev_speed, self_speed, orbit_radius, size, color):
    """Draw a single planet with revolution + rotation"""
    global angle

    glPushMatrix()

    # Revolution around Sun
    glRotatef(angle * rev_speed, 0, 1, 0)
    glTranslatef(orbit_radius, 0, 0)

    # Self rotation
    glRotatef(angle * self_speed, 0, 1, 0)

    glColor3f(*color)
    glutSolidSphere(size, 40, 40)

    glPopMatrix()


def draw_orbit(radius):
    """Draw orbit ring flat on XY plane"""
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glColor3f(0.4, 0.4, 0.4)
    glutWireTorus(0.01, radius, 80, 80)
    glPopMatrix()


def display():
    global angle

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Camera
    gluLookAt(0, 15, 30, 0, 0, 0, 0, 1, 0)

    # Sun
    glColor3f(1, 1, 0)
    glutSolidSphere(2, 50, 50)

    # ---- ORBITS (for all planets) ----
    draw_orbit(2)
    draw_orbit(3)
    draw_orbit(4)
    draw_orbit(5)
    draw_orbit(7)
    draw_orbit(9)
    draw_orbit(11)
    draw_orbit(13)

    # ---- PLANETS ----
    draw_planet(1.0,  20,  2, 0.3, (0.8, 0.8, 0.8))  # Mercury  
    draw_planet(0.8,  40,  3, 0.4, (1.0, 0.5, 0.1))  # Venus    
    draw_planet(0.6,  60,  4, 0.5, (0.2, 0.4, 1.0))  # Earth    
    draw_planet(0.5,  80,  5, 0.45,(1.0, 0.3, 0.2))  # Mars     
    draw_planet(0.3, 100,  7, 0.9, (1.0, 0.7, 0.3))  # Jupiter  
    draw_planet(0.25,120,  9, 0.8, (1.0, 0.9, 0.5))  # Saturn   
    draw_planet(0.2, 140, 11, 0.7, (0.5, 1.0, 1.0))  # Uranus   
    draw_planet(0.18,160, 13, 0.7, (0.3, 0.5, 1.0))  # Neptune  

    # Increase master angle
    angle += 0.2

    glutSwapBuffers()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(900, 700)
    glutCreateWindow(b"SOLAR SYSTEM - OpenGL + Python")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()


main()
