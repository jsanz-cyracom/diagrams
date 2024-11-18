# Install seqdiag if not already installed:
# pip install seqdiag

from seqdiag import parser, builder, drawer

diagram_definition = """
seqdiag {
    User -> Zoom Client [label = "Selects Zoom Integration App"];
    Zoom Client -> Zoom Integration App [label = "Accesses App"];
    Zoom Integration App -> WSO2 [label = "Authentication Request"];
    WSO2 -> Zoom Integration App [label = "Authentication Response"];
    Zoom Integration App -> User [label = "Displays Interface"];
    User -> Zoom Integration App [label = "Submits Interpreter Request"];
    Zoom Integration App -> API Gateway [label = "API Call"];
    API Gateway -> Microservices [label = "Routes Request"];
    Microservices -> Interpreter [label = "Assigns Interpreter"];
    Interpreter -> Zoom Meeting [label = "Joins Meeting"];
}
"""

# Parse the diagram definition using seqdiag's parser
tree = parser.parse_string(diagram_definition)

# Build and draw the diagram
diagram = builder.ScreenNodeBuilder.build(tree)
draw = drawer.DiagramDraw('PNG', diagram, filename="diagrams/zoom_integration_app_interpreter_request_sequence.png")
draw.draw()
draw.save()
