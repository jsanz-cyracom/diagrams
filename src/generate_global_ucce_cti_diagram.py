from diagrams import Diagram, Cluster
from diagrams.custom import Custom

# Define output file format
output_formats = ["svg", "png"]

# Define icon paths
icons_path = "../assets/icons/"
cisco_ucce_icon = f"{icons_path}cisco_ucce.png"
svc_ccs_agents_icon = f"{icons_path}golang.png"
rabbitmq_icon = f"{icons_path}rabbitmq.png"
datacenter_icon = f"{icons_path}database.png"

# Generate diagrams in both SVG and PNG formats
for out_format in output_formats:
    with Diagram(
        "Global UCCE CTI Server - Duplication Challenge",
        show=False,
        direction="TB",  # Top to Bottom for clear flow
        outformat=out_format,
        filename=f"diagrams/generate_global_ucce_cti",
    ):

        # UCCE CTI Server
        with Cluster("Cisco"):
            ucce_cti_server = Custom("Global UCCE CTI Server", cisco_ucce_icon)

        # Data Centers
        with Cluster("Data Centers"):
            with Cluster("DFW"):
                svc_ccs_agents_dfw = Custom("svc-ccs-agents", svc_ccs_agents_icon)
                rabbitmq_dfw = Custom("RabbitMQ", rabbitmq_icon)

            with Cluster("DEN"):
                svc_ccs_agents_den = Custom("svc-ccs-agents", svc_ccs_agents_icon)
                rabbitmq_den = Custom("RabbitMQ", rabbitmq_icon)

        # Define Interactions
        ucce_cti_server >> svc_ccs_agents_dfw  # Global UCCE CTI sends events to both svc-ccs-agents instances
        ucce_cti_server >> svc_ccs_agents_den  # Both DFW and DEN receive the same events (duplication risk)

        svc_ccs_agents_dfw >> rabbitmq_dfw  # DFW svc-ccs-agents publishes to RabbitMQ
        svc_ccs_agents_den >> rabbitmq_den  # DEN svc-ccs-agents publishes to RabbitMQ

