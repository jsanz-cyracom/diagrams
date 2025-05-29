import argparse
from diagrams import Diagram, Edge, Node

parser = argparse.ArgumentParser(description="Generate an error handling flow diagram for svc-ccs-calabrio-rta.")
parser.add_argument('--format', type=str, default='png', help='Output format of the diagram (e.g., png, svg)')
args = parser.parse_args()

graph_attr = {
    "fontsize": "16",
    "fontname": "Arial",
    "dpi": "300",
    "bgcolor": "white"
}

with Diagram(
    "svc-ccs-calabrio-rta Error Handling Flow",
    show=False,
    direction="TB",
    outformat=args.format,
    filename="diagrams/generate_svc_ccs_calabrio_rta_error_handling_flow",
    graph_attr=graph_attr
):
    start = Node("Start", style="filled", fillcolor="lightgray")
    query_im = Node("Query Info Manager", style="filled", fillcolor="lightblue")
    im_available = Node("Info Manager Available?", shape="diamond", style="filled", fillcolor="lightgray")
    circuit_breaker = Node("Circuit Breaker", style="filled", fillcolor="red")
    retry_im = Node("Retry After Delay", style="filled", fillcolor="lightgray")
    call_rta = Node("Call Calabrio RTA", style="filled", fillcolor="lightblue")
    rta_error = Node("Calabrio RTA Error?", shape="diamond", style="filled", fillcolor="lightgray")
    handle_rta_error = Node("Queue / Notify", style="filled", fillcolor="orange")
    network_issue = Node("Network Issue?", shape="diamond", style="filled", fillcolor="lightgray")
    handle_network = Node("Retry With Backoff", style="filled", fillcolor="yellow")
    success = Node("Success", style="filled", fillcolor="palegreen")

    start >> query_im >> im_available
    im_available >> Edge(label="Yes") >> call_rta
    im_available >> Edge(label="No") >> circuit_breaker >> retry_im >> query_im
    call_rta >> rta_error
    rta_error >> Edge(label="Yes") >> handle_rta_error
    rta_error >> Edge(label="No") >> network_issue
    network_issue >> Edge(label="Yes") >> handle_network >> call_rta
    network_issue >> Edge(label="No") >> success
