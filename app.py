# AI Traffic Congestion Monitoring System
# IBM SkillsBuild / Edunet Hackathon Project

import json

def load_traffic_data():
    try:
        with open("traffic congestion.json", "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return "Traffic data file not found"

def analyze_congestion(data):
    congestion_report = []
    for area in data.get("areas", []):
        if area["vehicle_count"] > 100:
            congestion_report.append({
                "area": area["area_name"],
                "status": "High Congestion"
            })
        else:
            congestion_report.append({
                "area": area["area_name"],
                "status": "Normal Traffic"
            })
    return congestion_report

def main():
    print("AI Traffic Congestion Monitoring System")
    data = load_traffic_data()
    
    if isinstance(data, str):
        print(data)
    else:
        report = analyze_congestion(data)
        for r in report:
            print(f"Area: {r['area']} - Status: {r['status']}")

if _name_ == "_main_":
    main()