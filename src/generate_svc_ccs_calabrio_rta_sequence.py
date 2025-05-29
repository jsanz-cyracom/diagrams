import os

# Define the sequence diagram in Mermaid syntax with custom font settings
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
    participant main
    participant Service
    participant HttpServer
    participant Api
    participant PluginCcsApi
    participant PluginRedis

    main->>Service: start()
    Service->>Api: register Api
    Service->>HttpServer: register HttpServer
    Service->>PluginCcsApi: register plugin
    Service->>PluginRedis: register plugin

    HttpServer->>Api: GET /service/health
    alt PluginCcsApi used
        Api->>PluginCcsApi: health check
        PluginCcsApi-->>Api: result
    else PluginRedis used
        Api->>PluginRedis: health check
        PluginRedis-->>Api: result
    end
    Api-->>HttpServer: 200 OK
"""

# Ensure the diagrams directory exists
os.makedirs("diagrams", exist_ok=True)

# Save the Mermaid definition to a temporary file
diagram_file = "diagrams/svc_ccs_calabrio_rta_sequence.mmd"
with open(diagram_file, "w") as f:
    f.write(diagram_definition)

# Generate SVG and PNG outputs using Mermaid CLI
svg_output_file = "diagrams/svc_ccs_calabrio_rta_sequence.svg"
png_output_file = "diagrams/svc_ccs_calabrio_rta_sequence.png"

svg_command = f"mmdc -i {diagram_file} -o {svg_output_file} -t default"
png_command = f"mmdc -i {diagram_file} -o {png_output_file} -t default --scale 4"

os.system(svg_command)
os.system(png_command)

# Remove the temporary Mermaid file
os.remove(diagram_file)
