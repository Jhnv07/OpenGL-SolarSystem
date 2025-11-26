from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)
    glutWireSphere(1, 20, 20)   # simple sun
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"OpenGL Window")
    glEnable(GL_DEPTH_TEST)
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()

main()
