# TUIO C# Demo

This project is a demonstration of using the TUIO tracking protocol in C# to detect and respond to TUIO markers for various interactive applications. It includes features to measure stretches between markers and handle specific interactions based on marker IDs.

## Features

- Track multiple TUIO markers simultaneously.
- Special handling for marker ID 2 to clear the screen and enable stretch measurement mode.
- Measure stretches between two specific markers (IDs 22 and 23).
- Display stretch status and count the number of good stretches.

## Prerequisites

Before you can run this demo, you need to have the following installed:
- .NET Framework (at least version 4.6.1)
- A TUIO Server broadcasting TUIO messages (e.g., reacTIVision or any compatible TUIO source)

## Setup

1. Clone this repository to your local machine:
 git clone https://github.com/Mostafa-Hesham1/HCI-Project.git


2. Open the solution file in Visual Studio (or your preferred .NET-compatible IDE).
3. Build the solution to resolve dependencies and compile the project.

## Running the Demo

To run the demo:
1. Ensure your TUIO server is running and properly configured to send messages to the IP and port that the TUIO client in this demo is listening to.
2. Run the `TuioDemo` application from Visual Studio or execute the built executable directly from the build output directory.
3. Interact with the TUIO markers. Bring marker ID 2 into the detection area to activate the stretch measurement mode, and use markers 22 and 23 to perform stretch actions.

## Customization

You can customize the following aspects:
- Change the TUIO server IP and port by modifying the `serverIP` and `port` variables in `TuioDemo.cs`.
- Adjust the threshold for what is considered a "good stretch" by editing the `updateTuioObject` method.


