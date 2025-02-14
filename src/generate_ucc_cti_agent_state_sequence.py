import os

# Define the sequence diagram in Mermaid syntax
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
    participant UCCE_CTIServer as UCCE CTI Server
    participant SvcCCSAgents as svc-ccs-agents
    participant RabbitMQ as RabbitMQ
    participant SvcCCSAir as svc-ccs-air
    participant CCS as CCS

    UCCE_CTIServer->>SvcCCSAgents: Sends agent state events via TCP
    SvcCCSAgents->>RabbitMQ: Publishes agent state events as AMQP messages
    SvcCCSAir->>RabbitMQ: Consumes AMQP messages
    SvcCCSAir->>CCS: Sends SOAP request to update agent state
"""

# Ensure the diagrams directory exists
os.makedirs("diagrams", exist_ok=True)

# Save the diagram definition to a Mermaid file
diagram_file = "diagrams/ucc_cti_agent_state_sequence.mmd"
with open(diagram_file, "w") as f:
    f.write(diagram_definition)

# Generate SVG and PNG outputs using Mermaid CLI
svg_output_file = "diagrams/ucc_cti_agent_state_sequence.svg"
png_output_file = "diagrams/ucc_cti_agent_state_sequence.png"

# Commands to generate the diagrams
svg_command = f"mmdc -i {diagram_file} -o {svg_output_file} -t default"
png_command = f"mmdc -i {diagram_file} -o {png_output_file} -t default --scale 4"

# Run the commands
os.system(svg_command)
os.system(png_command)

# Cleanup the temporary Mermaid file
os.remove(diagram_file)
