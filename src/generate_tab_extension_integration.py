import argparse
from diagrams import Diagram, Cluster
from diagrams.custom import Custom

parser = argparse.ArgumentParser(description="Generate a diagram with a specified output format.")
parser.add_argument('--format', type=str, default='png', help='Output format of the diagram (e.g., png, jpg, svg)')
args = parser.parse_args()

with Diagram(show=False,
             direction="TB",
             outformat=args.format,
             filename="diagrams/generate_tab_extension_integration") as diagram:
    
    with Cluster(label=""):
        interpreter = Custom("Interpreter", "../assets/icons/interpreter.png")
        teams_int = Custom("Microsoft Teams", "../assets/icons/teams.png")
        tab_extension_int = Custom("Tab Extension", "../assets/icons/teams_extension.png")
        authentication_int = Custom("Auth", "../assets/icons/authentication.png")
        waiting_int = Custom("Waiting", "../assets/icons/waiting.png")
        join_call_int = Custom("Join Call", "../assets/icons/join.png")
        interpretation_int = Custom("Conference", "../assets/icons/conference.png")
        
        interpreter >> teams_int >> tab_extension_int >> authentication_int >> waiting_int >> join_call_int >> interpretation_int

    with Cluster(label=""):
        patient = Custom("Patient", "../assets/icons/patient.png")
        teams_pat = Custom("Microsoft Teams", "../assets/icons/teams.png")
        tab_extension_pat = Custom("Tab Extension", "../assets/icons/teams_extension.png")
        authentication_pat = Custom("Auth", "../assets/icons/authentication.png")
        join_call_pat = Custom("Join Call", "../assets/icons/join.png")
        interpreter_join_pat = Custom("Interpreter Joins", "../assets/icons/interpreter.png")
        consultation_pat = Custom("Conference", "../assets/icons/conference.png")
        
        patient >> teams_pat >> tab_extension_pat >> authentication_pat >> join_call_pat >> interpreter_join_pat >> consultation_pat

    with Cluster(label=""):
        doctor = Custom("Doctor", "../assets/icons/doctor.png")
        teams_doc = Custom("Microsoft Teams", "../assets/icons/teams.png")
        tab_extension_doc = Custom("Tab Extension", "../assets/icons/teams_extension.png")
        authentication_doc = Custom("Auth", "../assets/icons/authentication.png")
        patient_join_doc = Custom("Patient Joins", "../assets/icons/patient.png")
        interpreter_request_doc = Custom("Interpreter Request", "../assets/icons/request.png")
        rtc_bridge_doc = Custom("RTC Bridge", "../assets/icons/golang.png")
        interpreter_join_doc = Custom("Interpreter Joins", "../assets/icons/interpreter.png")
        consultation_doc = Custom("Conference", "../assets/icons/conference.png")
        
        doctor >> teams_doc >> tab_extension_doc >> authentication_doc >> patient_join_doc >> interpreter_request_doc
        interpreter_request_doc >> rtc_bridge_doc >> interpreter_join_doc >> consultation_doc

diagram
