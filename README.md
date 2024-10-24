# Space Stone on Click

This project is a 3D OpenGL simulation using Pygame and PyOpenGL, where the user interacts with a rotating cube that breaks into pieces upon interaction, eventually revealing an "oval stone" with a glow effect. 
The project includes texture loading, rendering, and basic 3D transformations.

# Features
- **Textured Cube**: A rotating 3D cube with a custom texture.
- **Cube Destruction**: The cube breaks into smaller parts on interaction.
- **Oval Stone Reveal**: A glowing oval-shaped stone is revealed after the cube breaks.
- **3D Graphics**: Uses OpenGL for 3D rendering with texture mapping and depth testing.
- **Dynamic Glow Effect**: A glowing effect around the stone using blending in OpenGL.

## Installation

1. **Install Dependencies**:
   Ensure you have the following Python libraries installed:
   ```bash
   pip install pygame PyOpenGL
   ```

2. **Clone the Repository**:
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/space-stone-on-click.git
   ```

3. **Run the Program**:
   Navigate to the project directory and run the Python script:
   ```bash
   python space_stone_on_click.py
   ```

# How to Use

1. **Start the Program**: Run the script, and you'll see a rotating cube on the screen.
2. **Interact**: Press any key to decrease the cube’s size. After pressing the key again, the cube will break apart.
3. **Watch**: After a short delay, a glowing oval stone will appear and rotate while gradually moving forward.

# File Structure

- **space_stone_on_click.py**: Main script for the 3D simulation.
- **background.jpg**: The background image used in the simulation.
- **tesseract.png**: The texture applied to the cube.

# Requirements
- Python 3.x
- Pygame
- PyOpenGL
