import argparse
from diagrams import Diagram, Cluster
from diagrams.custom import Custom

parser = argparse.ArgumentParser(description="Generate a diagram with a specified output format.")
parser.add_argument('--format', type=str, default='png', help='Output format of the diagram (e.g., png, jpg, svg)')
args = parser.parse_args()

with Diagram(show=False,
             direction="TB",
             outformat=args.format,
             filename="diagrams/generate_in_meeting_extension_integration") as diagram:
    
    with Cluster(label=""):
        interpreter = Custom("Interpreter", "../assets/icons/interpreter.png")
        waiting_int = Custom("Waiting", "../assets/icons/waiting.png")
        teams_int = Custom("Microsoft Teams\r\nLink", "../assets/icons/teams.png")
        join_call_int = Custom("Join Call", "../assets/icons/join.png")
        interpretation_int = Custom("Conference", "../assets/icons/conference.png")
        
        interpreter >> waiting_int >> teams_int >> join_call_int >> interpretation_int

    with Cluster(label=""):
        patient = Custom("Patient", "../assets/icons/patient.png")
        teams_pat = Custom("Microsoft Teams", "../assets/icons/teams.png")
        join_call_pat = Custom("Join Call", "../assets/icons/join.png")
        interpreter_join_pat = Custom("Interpreter Joins", "../assets/icons/interpreter.png")
        consultation_pat = Custom("Conference", "../assets/icons/conference.png")
        
        patient >> teams_pat >> join_call_pat >> interpreter_join_pat >> consultation_pat

    with Cluster(label=""):
        doctor = Custom("Doctor", "../assets/icons/doctor.png")
        teams_doc = Custom("Microsoft Teams", "../assets/icons/teams.png")
        in_meeting_ext_doc = Custom("In-Meeting\r\nExtension", "../assets/icons/teams_extension.png")
        authentication_doc = Custom("Auth", "../assets/icons/authentication.png")
        patient_join_doc = Custom("Patient Joins", "../assets/icons/patient.png")
        interpreter_request_doc = Custom("Interpreter\r\nRequest", "../assets/icons/request.png")
        cyracom_api_doc = Custom("CyraCom API", "../assets/icons/golang.png")
        interpreter_join_doc = Custom("Interpreter Joins", "../assets/icons/interpreter.png")
        consultation_doc = Custom("Conference", "../assets/icons/conference.png")
        
        doctor >> teams_doc >> in_meeting_ext_doc >> authentication_doc >> patient_join_doc >> interpreter_request_doc
        interpreter_request_doc >> cyracom_api_doc >> interpreter_join_doc >> consultation_doc

diagram
