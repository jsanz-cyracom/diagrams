import argparse
from diagrams import Diagram, Cluster
from diagrams.custom import Custom

# Setting up the argument parser to accept an output format argument
parser = argparse.ArgumentParser(description="Generate a diagram for CCS Calls Service Architecture with a specified output format.")
parser.add_argument('--format', type=str, default='png', help='Output format of the diagram (e.g., png, jpg, svg)')
args = parser.parse_args()

# Creating the diagram with the specified output format
with Diagram("CCS Calls Service Architecture",
             show=False,
             direction="LR",
             outformat=args.format,
             filename="diagrams/generate_calls_service_component"):
    
    with Cluster(label=""):
        # Defining components
        api = Custom("API", "../assets/icons/api.png")
        auth = Custom("Auth", "../assets/icons/authentication.png")
        config = Custom("Config", "../assets/icons/config.png")
        context = Custom("Context", "../assets/icons/context.png")
        database = Custom("Database", "../assets/icons/database.png")
        models = Custom("Models", "../assets/icons/models.png")
        turn = Custom("TURN Info", "../assets/icons/turn.png")

        # Interconnections
        api >> auth >> turn
        api >> config
        api >> context
        api >> database >> models
