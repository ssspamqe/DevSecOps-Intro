import json

# Define the weights
SEVERITY = {"critical": 5, "elevated": 4, "high": 3, "medium": 2, "low": 1}
LIKELIHOOD = {"very-likely": 4, "likely": 3, "possible": 2, "unlikely": 1}
IMPACT = {"high": 3, "medium": 2, "low": 1}

def calculate_score(risk):
    s = SEVERITY.get(risk.get("severity", "low"), 1)
    l = LIKELIHOOD.get(risk.get("exploitation_likelihood", "unlikely"), 1)
    i = IMPACT.get(risk.get("exploitation_impact", "low"), 1)
    
    return (s * 100) + (l * 10) + i

try:
    with open("./../baseline/risks.json", "r") as f:
        risks = json.load(f)

    for r in risks:
        r["composite_score"] = calculate_score(r)
    sorted_risks = sorted(risks, key=lambda x: x["composite_score"], reverse=True)

    print("| Score | Severity | Category | Asset | Likelihood | Impact |")
    print("|---|---|---|---|---|---|")
    
    for r in sorted_risks[:5]:
        print(f"| {r['composite_score']} | {r['severity']} | {r['category']} | {r.get('most_relevant_technical_asset', 'N/A')} | {r['exploitation_likelihood']} | {r['exploitation_impact']} |")

except FileNotFoundError:
    print("Error:  not found")