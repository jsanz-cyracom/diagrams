# src/generate_zoom_integration_app_interpreter_request_sequence.py

import os

# Define the diagram in Mermaid syntax with adjusted font sizes and styles
diagram_definition = """
%%{init: {'theme': 'default', 'themeVariables': {
    'fontSize': '16px',
    'fontFamily': 'Arial',
    'sequenceNumberColor': '#000000',
    'actorFontSize': '16px',
    'actorFontFamily': 'Arial',
    'messageFontSize': '14px',
    'messageFontFamily': 'Arial'
}}}%%
sequenceDiagram
    participant User
    participant ZoomClient
    participant "Zoom Integration App" as ZoomIntegrationApp
    participant WSO2
    participant "CyraCom Direct API" as CyraComDirectAPI
    participant Microservices
    participant Interpreter
    participant ZoomMeeting

    User->>ZoomClient: Selects Zoom Integration App
    ZoomClient->>ZoomIntegrationApp: Accesses App
    ZoomIntegrationApp->>WSO2: Authentication Request
    WSO2-->>ZoomIntegrationApp: Authentication Response
    ZoomIntegrationApp-->>User: Displays Interface
    User->>ZoomIntegrationApp: Submits Interpreter Request
    ZoomIntegrationApp->>CyraComDirectAPI: API Call
    CyraComDirectAPI->>Microservices: Routes Request
    Microservices->>Interpreter: Assigns Interpreter
    Interpreter->>ZoomMeeting: Joins Meeting
"""

# Create the diagrams directory if it doesn't exist
os.makedirs('diagrams', exist_ok=True)

# Save the diagram definition to a temporary .mmd file
diagram_file = 'diagrams/zoom_integration_app_interpreter_request_sequence.mmd'
with open(diagram_file, 'w') as f:
    f.write(diagram_definition)

# Generate the diagram using Mermaid CLI with increased resolution and both SVG and PNG outputs
svg_output_file = 'diagrams/zoom_integration_app_interpreter_request_sequence.svg'
png_output_file = 'diagrams/zoom_integration_app_interpreter_request_sequence.png'

# Command to generate SVG
svg_command = f'mmdc -i {diagram_file} -o {svg_output_file} -t default'

# Command to generate high-resolution PNG (scale factor increased)
png_command = f'mmdc -i {diagram_file} -o {png_output_file} -t default --scale 2'

# Run the commands
os.system(svg_command)
os.system(png_command)

# Clean up the temporary .mmd file
os.remove(diagram_file)
