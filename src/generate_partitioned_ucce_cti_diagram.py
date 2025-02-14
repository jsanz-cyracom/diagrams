from diagrams import Diagram, Cluster
from diagrams.custom import Custom

# Define output file format
output_formats = ["svg", "png"]

# Define icon paths
icons_path = "../assets/icons/"
cisco_ucce_icon = f"{icons_path}cisco_ucce.png"
svc_ccs_agents_icon = f"{icons_path}golang.png"
rabbitmq_icon = f"{icons_path}rabbitmq.png"

# Generate diagrams in both SVG and PNG formats
for out_format in output_formats:
    with Diagram(
        "Partitioned UCCE CTI Servers - No Duplication",
        show=False,
        direction="TB",  # Top to Bottom for clarity
        outformat=out_format,
        filename=f"diagrams/generate_partitioned_ucce_cti",
    ):

        # Data Centers with Separate UCCE CTI Servers
        with Cluster("Data Centers"):

            with Cluster("DFW"):
                ucce_cti_dfw = Custom("UCCE CTI Server", cisco_ucce_icon)
                svc_ccs_agents_dfw = Custom("svc-ccs-agents", svc_ccs_agents_icon)
                rabbitmq_dfw = Custom("RabbitMQ", rabbitmq_icon)

            with Cluster("DEN"):
                ucce_cti_den = Custom("UCCE CTI Server", cisco_ucce_icon)
                svc_ccs_agents_den = Custom("svc-ccs-agents", svc_ccs_agents_icon)
                rabbitmq_den = Custom("RabbitMQ", rabbitmq_icon)

        # Define Interactions (Each UCCE CTI Server sends events only to its local instance)
        ucce_cti_dfw >> svc_ccs_agents_dfw  # DFW UCCE CTI Server -> DFW svc-ccs-agents
        ucce_cti_den >> svc_ccs_agents_den  # DEN UCCE CTI Server -> DEN svc-ccs-agents

        svc_ccs_agents_dfw >> rabbitmq_dfw  # DFW svc-ccs-agents publishes to RabbitMQ
        svc_ccs_agents_den >> rabbitmq_den  # DEN svc-ccs-agents publishes to RabbitMQ
