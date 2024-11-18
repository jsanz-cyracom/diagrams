# src/generate_zoom_integration_app_mobile_workflow_diagram.py

from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

# Common graph attributes
graph_attr = {
    "fontsize": "16",
    "fontname": "Arial",
    "dpi": "300",
    "bgcolor": "white"  # Changed from "transparent" to "white"
}

# Node and edge attributes
node_attr = {
    "fontsize": "16",
    "fontname": "Arial"
}
edge_attr = {
    "fontsize": "14",
    "fontname": "Arial"
}

# Generate both SVG and PNG outputs
for out_format in ["svg", "png"]:
    with Diagram("User Workflow on Mobile Devices",
                 show=False,
                 direction="LR",
                 outformat=out_format,
                 filename=f"diagrams/zoom_integration_app_mobile_workflow",
                 graph_attr=graph_attr):

        # Icon paths
        mobile_user_icon = "../assets/icons/mobile_user.png"
        zoom_mobile_app_icon = "../assets/icons/zoom_client.png"
        zoom_integration_app_icon = "../assets/icons/zoom_integration_app.png"
        wso2_icon = "../assets/icons/wso2.png"
        api_gateway_icon = "../assets/icons/api_gateway.png"
        microservices_icon = "../assets/icons/microservices.png"
        interpreter_icon = "../assets/icons/interpreter.png"
        cyracom_direct_api_icon = "../assets/icons/cyracom_direct_api.png"

        # Nodes
        mobile_user = Custom("Mobile User", mobile_user_icon)
        zoom_mobile_app = Custom("Zoom Mobile App", zoom_mobile_app_icon)
        zoom_integration_app = Custom("Zoom Integration App\n(Next.js)", zoom_integration_app_icon)
        wso2 = Custom("WSO2 Identity Server", wso2_icon)
        interpreter = Custom("Interpreter", interpreter_icon)

        # Diagram structure with clusters
        mobile_user >> Edge(label="Opens", **edge_attr) >> zoom_mobile_app >> Edge(label="Selects App", **edge_attr) >> zoom_integration_app
        zoom_integration_app >> Edge(label="Auth Request", **edge_attr) >> wso2
        mobile_user << Edge(label="Displays Interface", **edge_attr) << zoom_integration_app
        mobile_user >> Edge(label="Submits Request", **edge_attr) >> zoom_integration_app

        # CyraCom Direct API Cluster
        with Cluster("CyraCom Direct API"):
            api_gateway = Custom("API Gateway\n(Azure APIM)", api_gateway_icon)
            with Cluster("Kubernetes Cluster"):
                microservices = Custom("Microservices\n(Golang Services)", microservices_icon)

            zoom_integration_app >> Edge(label="API Call", **edge_attr) >> api_gateway >> Edge(label="Routes Request", **edge_attr) >> microservices
            microservices >> Edge(label="Assigns", **edge_attr) >> interpreter

        interpreter >> Edge(label="Joins Meeting", **edge_attr) >> zoom_mobile_app
