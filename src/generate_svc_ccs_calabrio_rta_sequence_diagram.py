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
    participant Scheduler
    participant PluginCcsApi
    participant StateProcessor
    participant PluginRedis
    participant PluginCalabrioRta
    participant CalabrioRTA

    %% Application startup
    Scheduler->>PluginCcsApi: Initialize component
    Scheduler->>PluginRedis: Initialize component
    Scheduler->>StateProcessor: Initialize component
    Scheduler->>PluginCalabrioRta: Initialize component
    Note over Scheduler,PluginCalabrioRta: Application Startup

    %% Agent state synchronization cycle
    Scheduler->>PluginCcsApi: Trigger sync job
    PluginCcsApi->>PluginCcsApi: Retrieve agent states
    PluginCcsApi-->>StateProcessor: Send agent states
    StateProcessor->>PluginRedis: Load previous states
    Note over StateProcessor: Buffer states for 10s
    StateProcessor->>StateProcessor: Filter & batch
    StateProcessor-->>PluginCalabrioRta: Batched states
    PluginCalabrioRta->>CalabrioRTA: Send batched states
    CalabrioRTA-->>PluginCalabrioRta: Acknowledge
    PluginCalabrioRta-->>StateProcessor: Delivery result
    StateProcessor->>PluginRedis: Update sync status
"""

# Ensure the diagrams directory exists
os.makedirs('diagrams', exist_ok=True)

# Save the diagram definition to a temporary .mmd file
diagram_file = 'diagrams/svc_ccs_calabrio_rta_sequence_diagram.mmd'
with open(diagram_file, 'w', encoding='utf-8') as f:
    f.write(diagram_definition)

# Generate SVG and PNG outputs using Mermaid CLI
svg_output_file = 'diagrams/svc_ccs_calabrio_rta_sequence_diagram.svg'
png_output_file = 'diagrams/svc_ccs_calabrio_rta_sequence_diagram.png'

svg_command = f'mmdc -i {diagram_file} -o {svg_output_file} -t default'
png_command = f'mmdc -i {diagram_file} -o {png_output_file} -t default --scale 4'

os.system(svg_command)
os.system(png_command)

os.remove(diagram_file)
