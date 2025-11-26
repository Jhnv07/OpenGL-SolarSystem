🌌 3D Solar System Simulation – OpenGL (Python)
By Jahnavi Yadav

A fully interactive 3D Solar System simulation built using Python, OpenGL, and GLUT.
This project visualizes the Sun and eight planets with revolution, rotation, lighting, Saturn rings, camera orbit control, and glow effects.

⭐ Project Overview

This Solar System simulation demonstrates:

Planetary revolution around the Sun

Individual planet self-rotation

Accurate orbit rings

Interactive 3D camera orbit and zoom

A glowing emissive sun

Realistic lighting and shading

Custom Saturn rings

Parameterization using my roll number: 20

The result is a smooth, visually appealing 3D model that can be observed from any angle.

🎯 Objectives

To understand and implement 3D transformation concepts: translation, rotation, perspective.

To visualize the Solar System using OpenGL primitives.

To apply lighting models (diffuse, specular, emissive).

To demonstrate interactive 3D navigation through input handling.

To integrate personal roll-number–based parameters into the simulation.

🧩 Features
🌞 Glowing Sun

Simulated using OpenGL emissive materials, making it emit light rather than reflect it.

🪐 Planetary Motion

Each planet:

Revolves around the Sun

Rotates on its axis

Has unique size + color for differentiation

💫 Orbit Rings

Generated using glutWireTorus to visualize each planet’s orbital path.

💍 Saturn Rings

Custom ring model created using a semi-transparent triangle strip.

🎥 Interactive Orbit Camera

Left Mouse Drag: Rotate camera around the Solar System

Right Mouse Drag: Zoom in/out

Free viewpoint similar to Blender/Maya camera orbit

✨ Shiny Planet Surfaces

Achieved through lighting and specular highlights.

🔢 How My Roll Number (20) Is Used

My roll number plays an important role in customizing my Solar System’s motion and camera behavior.

1️⃣ Revolution Speed Multiplier
rev_mul = (roll % 10 + 1) * 0.3


For roll = 20:

20 % 10 = 0 → (0 + 1) * 0.3 = 0.3


✔ Controls orbital speed of planets
✔ Higher roll = faster revolution

2️⃣ Self-Rotation Speed Multiplier
rot_mul = (roll % 7 + 1) * 0.2


For roll = 20:

20 % 7 = 6 → (6 + 1) * 0.2 = 1.4


✔ Determines how fast each planet spins
✔ Makes every student’s output unique

3️⃣ Initial Camera Distance
cam_distance = 20 + (roll % 5) * 5


For roll = 20:

20 % 5 = 0 → camera starts at distance = 20


✔ Customizes the default zoom level

📌 Why use the roll number?

Ensures every student's output is unique

Demonstrates application of mathematical expressions in graphics

Shows parameter-based animation control

Adds personalization to the simulation

🛠️ Tech Stack
Component	Used For
Python	Main programming language
OpenGL (PyOpenGL)	3D rendering
GLUT	Windowing, input handling
GLU	Camera and perspective utilities
📦 Installation & Running
1️⃣ Install Dependencies
pip install PyOpenGL PyOpenGL_accelerate

2️⃣ Run the Simulation
python solar_system.py

🎮 Controls
Action	Mouse
Orbit camera	Left-click + drag
Zoom	Right-click + drag
Auto animation	Runs continuously
📚 Learning Outcomes

Understanding 3D coordinate systems

Using OpenGL transformations

Implementing lighting models

Handling mouse-based camera control

Applying mathematical scaling using roll number

Creating custom geometry (Saturn Rings)

📜 Conclusion

This project effectively demonstrates 3D graphics concepts using Python and OpenGL.
Features like emissive lighting, orbit camera controls, roll-number–based parameters, and planetary motion create a visually realistic Solar System simulation.
