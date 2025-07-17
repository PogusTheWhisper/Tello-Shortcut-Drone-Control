# Requirements Document

## Introduction

This document outlines the requirements for a comprehensive drone control system designed for Tello drones. The system provides an interactive command-line interface that allows users to control drone movements, perform aerial maneuvers, monitor drone status, and execute predefined flight patterns. The system is built using the rcsa_dev_kit_edu_python_lib library and supports both basic drone operations and advanced features like QR code scanning and combo flight patterns.

## Requirements

### Requirement 1

**User Story:** As a drone operator, I want to control basic drone movements through simple commands, so that I can navigate the drone in all directions with precise distance control.

#### Acceptance Criteria

1. WHEN the user enters "w-[distance]" THEN the system SHALL move the drone forward by the specified distance in centimeters
2. WHEN the user enters "a-[distance]" THEN the system SHALL move the drone left by the specified distance in centimeters
3. WHEN the user enters "s-[distance]" THEN the system SHALL move the drone backward by the specified distance in centimeters
4. WHEN the user enters "d-[distance]" THEN the system SHALL move the drone right by the specified distance in centimeters
5. WHEN the user enters "up-[distance]" THEN the system SHALL move the drone upward by the specified distance in centimeters
6. WHEN the user enters "down-[distance]" THEN the system SHALL move the drone downward by the specified distance in centimeters

### Requirement 2

**User Story:** As a drone operator, I want to perform aerial flips in different directions, so that I can execute impressive maneuvers and demonstrations.

#### Acceptance Criteria

1. WHEN the user enters "f-w" THEN the system SHALL execute a forward flip
2. WHEN the user enters "f-a" THEN the system SHALL execute a left flip
3. WHEN the user enters "f-s" THEN the system SHALL execute a backward flip
4. WHEN the user enters "f-d" THEN the system SHALL execute a right flip

### Requirement 3

**User Story:** As a drone operator, I want to rotate the drone clockwise and counterclockwise, so that I can change the drone's orientation without changing its position.

#### Acceptance Criteria

1. WHEN the user enters "ror-[angle]" THEN the system SHALL rotate the drone clockwise by the specified angle in degrees
2. WHEN the user enters "rol-[angle]" THEN the system SHALL rotate the drone counterclockwise by the specified angle in degrees

### Requirement 4

**User Story:** As a drone operator, I want to control basic drone operations like takeoff and landing, so that I can safely start and end flight sessions.

#### Acceptance Criteria

1. WHEN the user enters "t" THEN the system SHALL initiate drone takeoff
2. WHEN the user enters "l" THEN the system SHALL initiate drone landing
3. WHEN the user enters "q" THEN the system SHALL safely stop the drone and exit the program

### Requirement 5

**User Story:** As a drone operator, I want to monitor drone status information, so that I can make informed decisions about flight operations.

#### Acceptance Criteria

1. WHEN the user enters "b" THEN the system SHALL display the current battery percentage
2. WHEN the user enters "speed" THEN the system SHALL display the current drone speed
3. WHEN the user enters "h" THEN the system SHALL display the current drone height

### Requirement 6

**User Story:** As a drone operator, I want to scan QR codes and execute automated flight patterns based on QR content, so that I can perform automated tasks and demonstrations.

#### Acceptance Criteria

1. WHEN the user enters "scan" THEN the system SHALL activate the drone camera and start QR code detection
2. WHEN a QR code is detected THEN the system SHALL decode the QR content
3. IF the QR code contains a valid number THEN the system SHALL execute that many 360-degree rotations followed by a backward flip
4. WHEN QR scanning is complete THEN the system SHALL deactivate the camera stream

### Requirement 7

**User Story:** As a drone operator, I want to execute predefined combo flight patterns, so that I can perform complex maneuvers with simple commands.

#### Acceptance Criteria

1. WHEN the user enters "combo1" or "cb1" THEN the system SHALL execute a staircase flight pattern in a square shape moving upward
2. WHEN the user enters "combo2" or "cb2" THEN the system SHALL execute a reverse staircase flight pattern in a square shape moving downward
3. WHEN executing combo1 THEN the system SHALL perform forward movement, forward flip, clockwise rotation, and upward movement for each side of the square
4. WHEN executing combo2 THEN the system SHALL perform backward movement, backward flip, counterclockwise rotation, and downward movement for each side of the square

### Requirement 8

**User Story:** As a drone operator, I want to see a clear menu and command reference, so that I can understand available commands and their usage.

#### Acceptance Criteria

1. WHEN the program starts THEN the system SHALL display a comprehensive menu showing all available commands
2. WHEN the program starts THEN the system SHALL display command syntax examples
3. WHEN the program starts THEN the system SHALL display credit information and contact details

### Requirement 9

**User Story:** As a drone operator, I want the system to handle errors gracefully, so that I can safely interrupt operations and recover from unexpected situations.

#### Acceptance Criteria

1. WHEN the user presses Ctrl+C THEN the system SHALL safely stop the drone and terminate the program
2. WHEN an invalid command is entered THEN the system SHALL display an error message and continue accepting commands
3. WHEN the system encounters an error THEN the system SHALL not crash and SHALL continue operation

### Requirement 10

**User Story:** As a drone operator, I want to configure the drone connection, so that I can connect to my specific drone using its serial number.

#### Acceptance Criteria

1. WHEN the program starts THEN the system SHALL use the configured drone serial number for connection
2. WHEN the drone connection is established THEN the system SHALL maintain the connection throughout the session
3. WHEN the program exits THEN the system SHALL properly close the drone connection