from diagrams import Diagram, Cluster, Edge
from diagrams.custom import Custom

# Common graph attributes
graph_attr = {
    "fontsize": "16",
    "fontname": "Arial",
    "dpi": "300",
    "bgcolor": "white",
    "nodesep": "1.5",  # Increased separation between nodes
    "ranksep": "1.5"   # Increased separation between ranks
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
    with Diagram("",
                 show=False,
                 direction="LR",  # Left-to-right layout
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

        # Create sub-cluster for Mobile User
        with Cluster("User Actions", graph_attr={"ranksep": "0.5"}):  # Slightly reduced for compactness
            invisible_top = Custom("", "../assets/icons/empty.png")  # Invisible top node for better control
            mobile_user = Custom("Mobile User", mobile_user_icon)

        # Main Workflow Nodes
        zoom_mobile_app = Custom("Zoom Mobile App", zoom_mobile_app_icon)
        zoom_integration_app = Custom("Zoom Integration App\n(Next.js)", zoom_integration_app_icon)
        wso2 = Custom("WSO2 Identity Server", wso2_icon)
        interpreter = Custom("Interpreter", interpreter_icon)

        # Workflow starting with Mobile User
        invisible_top >> Edge(label="Opens", **edge_attr) >> zoom_mobile_app
        mobile_user >> Edge(label="Submits Request", style="solid", color="black", constraint="false", **edge_attr) >> zoom_integration_app
        zoom_mobile_app >> Edge(label="", taillabel="Selects App", **edge_attr) >> zoom_integration_app
        zoom_integration_app >> Edge(label="Displays Interface", style="dashed", color="blue", fontcolor="blue", **edge_attr) >> mobile_user
        zoom_integration_app >> Edge(label="Auth Request", **edge_attr) >> wso2

        # CyraCom Direct API Cluster
        with Cluster("CyraCom Direct API", graph_attr={"nodesep": "1.2"}):  # Increased separation
            api_gateway = Custom("API Gateway\n(Azure APIM)", api_gateway_icon)
            with Cluster("Kubernetes Cluster", graph_attr={"ranksep": "1.0"}):  # Additional spacing in cluster
                microservices = Custom("Microservices\n(Golang Services)", microservices_icon)

            # Increased spacing for edges
            zoom_integration_app >> Edge(label="", xlabel="API Call", minlen="2", **edge_attr) >> api_gateway
            api_gateway >> Edge(label="", xlabel="Routes Request", minlen="2", **edge_attr) >> microservices
            microservices >> Edge(label="", xlabel="Assigns", minlen="2", **edge_attr) >> interpreter

        interpreter >> Edge(label="Joins Meeting", minlen="2", **edge_attr) >> zoom_mobile_app
