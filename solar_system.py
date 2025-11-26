from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math

# ================================
#  USER ROLL NUMBER
# ================================
roll = 20

rev_mul = (roll % 10 + 1) * 0.3     # noticeable revolution speed
rot_mul = (roll % 7 + 1) * 0.2      # visible self-spin
cam_distance = 20 + (roll % 5) * 5

angle = 0

# ================================
# Camera Orbit
# ================================
cam_yaw = 45
cam_pitch = 20

mouse_left = False
mouse_right = False
last_x = last_y = 0


def init():
    glEnable(GL_DEPTH_TEST)

    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)

    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1, 1, 1, 1])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1, 1, 1, 1])
    glLightfv(GL_LIGHT0, GL_POSITION, [0, 0, 0, 1])

    glClearColor(0, 0, 0, 1)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, 900/700, 0.1, 500)


# ================================
# Saturn Rings
# ================================
def draw_ring(inner, outer):
    glDisable(GL_LIGHTING)
    glColor4f(1, 1, 0.8, 0.4)

    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glBegin(GL_TRIANGLE_STRIP)
    for i in range(361):
        a = math.radians(i)
        glVertex3f(math.cos(a) * inner, math.sin(a) * inner, 0)
        glVertex3f(math.cos(a) * outer, math.sin(a) * outer, 0)
    glEnd()
    glPopMatrix()

    glEnable(GL_LIGHTING)


# ================================
# Orbit Circles
# ================================
def draw_orbit(r):
    glDisable(GL_LIGHTING)
    glColor3f(0.3, 0.3, 0.3)
    glPushMatrix()
    glRotatef(90, 1, 0, 0)
    glutWireTorus(0.02, r, 80, 80)
    glPopMatrix()
    glEnable(GL_LIGHTING)


# ================================
# Planet
# ================================
def draw_planet(rev, rot, orbit, size, color, rings=False):
    global angle

    glPushMatrix()

    glRotatef(angle * rev * rev_mul, 0, 1, 0)
    glTranslatef(orbit, 0, 0)
    glRotatef(angle * rot * rot_mul, 0, 1, 0)

    glColor3f(*color)
    glutSolidSphere(size, 50, 50)

    if rings:
        draw_ring(size + 0.2, size + 0.7)

    glPopMatrix()


# ================================
# Display
# ================================
def display():
    global angle, cam_distance

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # Orbit camera
    cx = cam_distance * math.cos(math.radians(cam_pitch)) * math.sin(math.radians(cam_yaw))
    cy = cam_distance * math.sin(math.radians(cam_pitch))
    cz = cam_distance * math.cos(math.radians(cam_pitch)) * math.cos(math.radians(cam_yaw))
    gluLookAt(cx, cy, cz, 0, 0, 0, 0, 1, 0)

    # Glowing Sun
    glPushMatrix()
    glMaterialfv(GL_FRONT, GL_EMISSION, [1, 1, 0, 1])
    glColor3f(1, 1, 0)
    glutSolidSphere(1.8, 80, 80)

    glMaterialfv(GL_FRONT, GL_EMISSION, [0, 0, 0, 1])
    glPopMatrix()

    # Orbits
    for r in [2, 3, 4, 5, 7, 9, 11, 13]:
        draw_orbit(r)

    # Planets (rev_speed, rot_speed, orbit, radius, color)
    draw_planet(1.0, 20,  2, 0.35, (0.8, 0.8, 0.8))
    draw_planet(0.8, 40,  3, 0.45, (1.0, 0.5, 0.1))
    draw_planet(0.6, 60,  4, 0.55, (0.2, 0.4, 1.0))
    draw_planet(0.5, 80,  5, 0.50, (1.0, 0.3, 0.2))
    draw_planet(0.3,100,  7, 0.95, (1.0, 0.7, 0.3))
    draw_planet(0.25,120, 9, 0.85, (1.0, 0.9, 0.5), True)
    draw_planet(0.2,140, 11, 0.75, (0.5, 1.0, 1.0))
    draw_planet(0.18,160,13, 0.75, (0.3, 0.5, 1.0))

    angle += 0.2
    glutSwapBuffers()


# ================================
# Mouse Controls
# ================================
def mouse(button, state, x, y):
    global mouse_left, mouse_right, last_x, last_y

    if button == GLUT_LEFT_BUTTON:
        mouse_left = (state == GLUT_DOWN)
    if button == GLUT_RIGHT_BUTTON:
        mouse_right = (state == GLUT_DOWN)

    last_x = x
    last_y = y


def motion(x, y):
    global cam_yaw, cam_pitch, cam_distance, last_x, last_y

    dx = x - last_x
    dy = y - last_y

    if mouse_left:
        cam_yaw += dx * 0.3
        cam_pitch -= dy * 0.3
        cam_pitch = max(-80, min(80, cam_pitch))

    if mouse_right:
        cam_distance += dy * 0.2
        cam_distance = max(10, min(80, cam_distance))

    last_x = x
    last_y = y

    glutPostRedisplay()


# ================================
# Main
# ================================
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(900, 700)
    glutCreateWindow(b"SOLAR SYSTEM - Roll-based Parameters")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutMainLoop()


main()
