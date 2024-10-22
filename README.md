# TUIO C# Demo

This project is a demonstration of using the TUIO tracking protocol in C# to detect and respond to TUIO markers for various interactive applications. It includes features to measure stretches between markers and handle specific interactions based on marker IDs.
# HCI Project - TUIO C# Demo

This TUIO C# Demo showcases interactive applications using the TUIO tracking protocol within a C# environment. It is particularly designed for physical therapy and training exercises, enabling dynamic interaction with TUIO markers.

## Key Features

- **Interactive Marker Tracking**: The application tracks multiple TUIO markers simultaneously, responding to their specific IDs with designated actions.
- **Patient Data Management**: Marker ID 0 is used to navigate a table of patient information. Rotation of this marker scrolls through the table, enhancing user interaction without traditional input devices.
- **Confirmation Actions**: Marker ID 1 serves as a confirmation or selection tool within the application, allowing users to confirm selections or choices made during navigation.
- **Stretch Measurement Mode**: Activated by Marker ID 2, this mode clears previous displays and sets up a real-time environment for evaluating stretches. It ensures the correct execution of physical stretches by providing visual feedback and rep counting.
- **Dynamic Stretch Evaluation**: Markers 22 and 23 are used for measuring the effectiveness of stretches by monitoring the distance between them. Proper distancing that indicates a "good stretch" is counted as a successful repetition, while insufficient distancing provides feedback to "keep stretching."

## Demo Videos

You can view the application in action here:
- [Demo Video Link](https://drive.google.com/drive/u/0/folders/1_c6VBfEOojF1gZi_87DSGCNoFxG23Ynp)
  - The first video shows how markers interact with our system.
  - The second video demonstrates a stretch training session, where the system counts reps during adequate stretches and prompts for adjustment when the stretch is insufficient.

## Prerequisites

To run this demo, ensure you have:
- .NET Framework (version 4.6.1 or later)
- A TUIO Server (such as reacTIVision) broadcasting TUIO messages to interact with the application.

## Setup

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/Mostafa-Hesham1/HCI-Project.git

2. Open the solution file in Visual Studio (or your preferred .NET-compatible IDE).
3. Build the solution to resolve dependencies and compile the project.

## Running the Demo

To run the demo:
1. Ensure your TUIO server is running and properly configured to send messages to the IP and port that the TUIO client in this demo is listening to.
2. Run the `TuioDemo` application from Visual Studio or execute the built executable directly from the build output directory.
3. Interact with the TUIO markers. Bring marker ID 2 into the detection area to activate the stretch measurement mode, and use markers 22 and 23 to perform stretch actions.



