import argparse
from diagrams import Diagram, Cluster
from diagrams.custom import Custom

# Setting up the argument parser to accept an output format argument
parser = argparse.ArgumentParser(description="Generate a diagram for CFE Lite inbound SIP video architecture with a specified output format.")
parser.add_argument('--format', type=str, default='png', help='Output format of the diagram (e.g., png, jpg, svg)')
args = parser.parse_args()

# Creating the diagram with the specified output format
with Diagram(
    "CFE Lite Inbound SIP Video Architecture",
    show=False,
    direction="LR",
    outformat=args.format,
    filename="diagrams/cfe_lite_inbound_video_component",
):
    vonage = Custom("Vonage SIP\nInterconnect", "../assets/icons/vonage.png")
    cfe_lite = Custom("CFE Lite\nMicroservice", "../assets/icons/microservices.png")
    with Cluster("XMS Cluster (MRB)"):
        mrb = Custom("MRB", "../assets/icons/broker.png")
        xms_nodes = [
            Custom("XMS 1", "../assets/icons/xms.png"),
            Custom("XMS 2", "../assets/icons/xms.png"),
        ]
        mrb >> xms_nodes
    twilio = Custom("Twilio APIs", "../assets/icons/api.png")
    interpreter = Custom("Interpreter", "../assets/icons/interpreter.png")

    vonage >> cfe_lite >> mrb
    for xms in xms_nodes:
        xms >> interpreter
    cfe_lite >> twilio >> interpreter
