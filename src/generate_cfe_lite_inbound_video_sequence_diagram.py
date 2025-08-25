import os

# Define the diagram in Mermaid syntax with adjusted font sizes and styles
sequence_diagram = """
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
    participant Vonage
    participant CFE_Lite as CFE Lite
    participant MRB
    participant XMS
    participant Twilio
    participant Interpreter

    Vonage->>CFE_Lite: SIP INVITE
    CFE_Lite->>MRB: Allocate media server
    MRB->>XMS: Select XMS node
    CFE_Lite-->>Vonage: 200 OK
    CFE_Lite->>Twilio: Request interpreter
    Twilio-->>CFE_Lite: Interpreter selected
    CFE_Lite->>XMS: Dial interpreter
    XMS->>Interpreter: Connect call
    Interpreter-->>XMS: Answer
    XMS-->>CFE_Lite: Media session established
    CFE_Lite-->>Twilio: Status callbacks
"""

os.makedirs('diagrams', exist_ok=True)

diagram_file = 'diagrams/cfe_lite_inbound_video_sequence_diagram.mmd'
with open(diagram_file, 'w') as f:
    f.write(sequence_diagram)

svg_output = 'diagrams/cfe_lite_inbound_video_sequence_diagram.svg'
png_output = 'diagrams/cfe_lite_inbound_video_sequence_diagram.png'

svg_command = f'mmdc -i {diagram_file} -o {svg_output} -t default'
png_command = f'mmdc -i {diagram_file} -o {png_output} -t default --scale 4'

os.system(svg_command)
os.system(png_command)

os.remove(diagram_file)
