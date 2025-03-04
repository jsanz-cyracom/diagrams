import os
from diagrams import Diagram, Cluster
from diagrams.custom import Custom

ICON_PATH = "../assets/icons/"

with Diagram("svc-ccs-agents Component Diagram", filename="diagrams/generate_svc_ccs_agents_provisioning_component_diagram", show=False):
    with Cluster("svc-ccs-agents Microservice"):
        workday_api = Custom("WorkdayApi", ICON_PATH + "api.png")
        ccmp_api = Custom("CcmpApi", ICON_PATH + "api.png")

    workday = Custom("Workday", ICON_PATH + "workday.png")
    cisco_ccmp = Custom("Cisco CCMP", ICON_PATH + "cisco_ucce.png")

    # Define interactions explicitly
    workday >> workday_api >> ccmp_api >> cisco_ccmp