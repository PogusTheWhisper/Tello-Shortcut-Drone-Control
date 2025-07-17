# Drone Control System

A comprehensive Python-based control system for Tello drones with interactive command-line interface, featuring movement controls, aerial maneuvers, status monitoring, and automated flight patterns.

## Features

- **Basic Movement Controls**: Forward, backward, left, right, up, down with precise distance control
- **Aerial Maneuvers**: Flips in all four directions (forward, backward, left, right)
- **Rotation Controls**: Clockwise and counterclockwise rotation with angle precision
- **Status Monitoring**: Real-time battery, speed, and height information
- **QR Code Scanning**: Automated flight patterns based on QR code content
- **Predefined Combos**: Complex flight patterns with simple commands
- **Safety Features**: Graceful error handling and emergency stop functionality

## Requirements

- Python 3.x
- `rcsa_dev_kit_edu_python_lib` library
- Tello drone
- Drone serial number

## Installation

1. Install the required library:
```bash
pip install rcsa_dev_kit_edu_python_lib
```

2. Configure your drone serial number in the code:
```python
my_tellos = ['<your_drone_serial_number>']  # Replace with your actual drone serial number
```

## Usage

Run the program:
```bash
python 13rb_drone_control.py
```

### Basic Commands

#### Movement Commands
- `w-[distance]` - Move forward (e.g., `w-100` moves forward 100cm)
- `a-[distance]` - Move left (e.g., `a-50` moves left 50cm)
- `s-[distance]` - Move backward (e.g., `s-75` moves backward 75cm)
- `d-[distance]` - Move right (e.g., `d-60` moves right 60cm)
- `up-[distance]` - Move up (e.g., `up-30` moves up 30cm)
- `down-[distance]` - Move down (e.g., `down-20` moves down 20cm)

#### Flip Commands
- `f-w` - Flip forward
- `f-a` - Flip left
- `f-s` - Flip backward
- `f-d` - Flip right

#### Rotation Commands
- `ror-[angle]` - Rotate clockwise (e.g., `ror-90` rotates 90° clockwise)
- `rol-[angle]` - Rotate counterclockwise (e.g., `rol-180` rotates 180° counterclockwise)

#### Control Commands
- `t` - Takeoff
- `l` - Landing
- `q` - Exit program

#### Status Commands
- `b` - Check battery percentage
- `speed` - Check current speed
- `h` - Check current height

#### Special Features
- `scan` - Activate QR code scanning mode
- `combo1` or `cb1` - Execute upward staircase flight pattern
- `combo2` or `cb2` - Execute downward staircase flight pattern

## Command Examples

```bash
# Basic flight sequence
t           # Takeoff
w-100       # Move forward 100cm
ror-90      # Rotate 90° clockwise
d-50        # Move right 50cm
f-w         # Flip forward
l           # Land

# Status check
b           # Check battery
h           # Check height
speed       # Check speed

# Advanced maneuvers
combo1      # Execute combo pattern 1
scan        # Start QR scanning
```

## Combo Patterns

### Combo 1 (`combo1` or `cb1`)
Executes an upward staircase flight pattern in a square shape:
- Forward movement (50cm)
- Forward flip
- Clockwise rotation (90°)
- Upward movement (50cm)
- Repeats for 3 rounds, 4 sides each

### Combo 2 (`combo2` or `cb2`)
Executes a downward staircase flight pattern in a square shape:
- Backward movement (50cm)
- Backward flip
- Counterclockwise rotation (90°)
- Downward movement (50cm)
- Repeats for 3 rounds, 4 sides each

## QR Code Scanning

The `scan` command activates the drone's camera and looks for QR codes. When a QR code is detected:
1. The system decodes the QR content
2. If the QR contains a number, the drone performs that many 360° rotations
3. Executes a backward flip
4. Deactivates the camera

## Safety Features

- **Emergency Stop**: Press `Ctrl+C` to safely stop the drone and exit
- **Error Handling**: Invalid commands are ignored with error messages
- **Connection Management**: Automatic drone connection handling

## Troubleshooting

### Common Issues

1. **Drone not connecting**
   - Verify your drone serial number is correct
   - Ensure the drone is powered on and in range
   - Check Wi-Fi connection to the drone

2. **Commands not working**
   - Ensure proper command syntax (use hyphens for parameters)
   - Check that the drone has sufficient battery
   - Verify the drone is in a safe flying environment

3. **QR scanning not working**
   - Ensure good lighting conditions
   - Position QR code clearly in camera view
   - Check that QR code contains valid numeric data

## Credits

**Development Team:**
- Naphat Sornwichai
- Wasupol Chaowsanguan
- Hattakron Phannarak
- Surawit Pakeepol
- Thanayot Monthlchachat
- Nawin Charassangsomboon
- Metapat Nitimetviranon

**From:** RB134 M.5/2 & 5/3, Wat Rajabopit School

**Contact:** NaphatSorn.Contact@gmail.com

**Social Media:**
- Instagram: [@pogus_the_whisper](https://www.instagram.com/pogus_the_whisper/)
- LinkedIn: [Naphat Sornwichai](https://www.linkedin.com/in/naphat-sornwichai-25759426a/)

## License

Created: 25/10/23  
Last Modified: 28/10/23

---

**Note:** Always ensure you're flying in a safe, legal environment and following local drone regulations. Keep the drone within visual line of sight and maintain safe distances from people and property.