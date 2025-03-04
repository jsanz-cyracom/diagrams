import os

# Define the correct diagram in Mermaid syntax with adjusted font sizes and styles
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
    participant svc-ccs-agents
    participant WorkdayApi
    participant Workday
    participant CcmpApi
    participant CiscoCCMP

    svc-ccs-agents->>WorkdayApi: Request Employee Data
    WorkdayApi->>Workday: Authenticate & Retrieve Data (SOAP)
    Workday-->>WorkdayApi: Employee Data Response
    WorkdayApi-->>svc-ccs-agents: Transformed Employee Data
    svc-ccs-agents->>CcmpApi: Provision Agent Request
    CcmpApi->>CiscoCCMP: Authenticate & Provision Agent (REST)
    CiscoCCMP-->>CcmpApi: Async Provisioning Accepted
    loop Polling for Provisioning Status
        CcmpApi->>CiscoCCMP: Check Provisioning Status
        CiscoCCMP-->>CcmpApi: Provisioning Status Response
    end
    CcmpApi-->>svc-ccs-agents: Final Provisioning Status
"""

# Create the diagrams directory if it doesn't exist
os.makedirs('diagrams', exist_ok=True)

# Save the diagram definition to a temporary .mmd file
diagram_file = 'diagrams/generate_svc_ccs_agents_provisioning_sequence_diagram.mmd'
with open(diagram_file, 'w') as f:
    f.write(diagram_definition)

# Generate the diagram using Mermaid CLI with increased resolution and both SVG and PNG outputs
svg_output_file = 'diagrams/generate_svc_ccs_agents_provisioning_sequence_diagram.svg'
png_output_file = 'diagrams/generate_svc_ccs_agents_provisioning_sequence_diagram.png'

# Command to generate SVG
svg_command = f'mmdc -i {diagram_file} -o {svg_output_file} -t default'

# Command to generate high-resolution PNG (scale factor increased)
png_command = f'mmdc -i {diagram_file} -o {png_output_file} -t default --scale 4'

# Run the commands
os.system(svg_command)
os.system(png_command)

# Clean up the temporary .mmd file
os.remove(diagram_file)