# Space Stone

This project is a 3D OpenGL simulation using Pygame and PyOpenGL, where the user interacts with a rotating textured cube. After a set time or action, the cube breaks apart, revealing a glowing "oval stone."

# Features
- **Textured 3D Cube**: A rotating cube with a custom texture.
- **Cube Destruction**: The cube breaks into smaller pieces after several rotations.
- **Glow Effect**: The stone glows using a blend of alpha transparency and color.
- **Stone Reveal**: After the cube breaks, a glowing oval stone appears and rotates.
- **OpenGL Graphics**: Utilizes OpenGL for 3D rendering with texture mapping and depth testing.

# Installation

1. **Install Dependencies**:
   Make sure you have the necessary Python libraries installed:
   ```bash
   pip install pygame PyOpenGL
   ```

2. **Clone the Repository**:
   Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/space-stone.git
   ```

3. **Run the Program**:
   Navigate to the project directory and run the Python script:
   ```bash
   python space_stone.py
   ```

# How to Use

1. **Start the Program**: Run the script to start the simulation.
2. **Observe**: Watch the cube rotate. After two full rotations, the cube will shrink, break apart, and reveal a glowing oval stone.
3. **End**: The program automatically ends after 15 seconds.

# File Structure

- **space_stone.py**: Main Python script for the 3D simulation.
- **background.jpg**: Background image used in the simulation.
- **tesseract.png**: Texture applied to the cube.

# Requirements
- Python 3.x
- Pygame
- PyOpenGL
