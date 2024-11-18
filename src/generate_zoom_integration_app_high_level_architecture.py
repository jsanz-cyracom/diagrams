# src/generate_zoom_integration_app_high_level_architecture.py

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
    with Diagram("Zoom Integration App - High-Level Architecture",
                 show=False,
                 direction="LR",
                 outformat=out_format,
                 filename=f"diagrams/zoom_integration_app_high_level_architecture",
                 graph_attr=graph_attr):

        # Icon paths
        user_icon = "../assets/icons/user.png"
        zoom_client_icon = "../assets/icons/zoom_client.png"
        zoom_integration_app_icon = "../assets/icons/zoom_integration_app.png"
        wso2_icon = "../assets/icons/wso2.png"
        citrix_lb_icon = "../assets/icons/citrix_load_balancer.png"
        kubernetes_icon = "../assets/icons/kubernetes.png"
        api_gateway_icon = "../assets/icons/api_gateway.png"
        microservices_icon = "../assets/icons/microservices.png"
        interpreter_icon = "../assets/icons/interpreter.png"
        cyracom_direct_api_icon = "../assets/icons/cyracom_direct_api.png"

        # Define nodes
        user = Custom("User", user_icon)
        zoom_client = Custom("Zoom Client", zoom_client_icon)
        zoom_integration_app = Custom("Zoom Integration App\n(Next.js)", zoom_integration_app_icon)
        wso2 = Custom("WSO2 Identity Server", wso2_icon)
        citrix_lb = Custom("Citrix Load Balancer", citrix_lb_icon)
        interpreter = Custom("Interpreter", interpreter_icon)

        # Diagram structure with clusters
        user >> Edge(label="Uses", **edge_attr) >> zoom_client >> Edge(label="Selects App", **edge_attr) >> zoom_integration_app
        zoom_integration_app >> Edge(label="Auth Request", **edge_attr) >> wso2

        # CyraCom Direct API Cluster
        with Cluster("CyraCom Direct API"):
            # API Gateway
            api_gateway = Custom("API Gateway\n(Azure APIM)", api_gateway_icon)
            # Kubernetes Cluster
            with Cluster("Kubernetes Cluster"):
                microservices = Custom("Microservices\n(Golang Services)", microservices_icon)

            zoom_integration_app >> Edge(label="API Calls", **edge_attr) >> api_gateway >> Edge(label="Routes Request", **edge_attr) >> microservices
            microservices >> Edge(label="Assigns", **edge_attr) >> interpreter

        # Interpreter interaction
        interpreter >> Edge(label="Joins Meeting", **edge_attr) >> zoom_client
