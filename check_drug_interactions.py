import json
import sys
from enum import Enum

# Define an enum with both string and integer values to represent severity
class Severity(Enum):
    MINOR = ("minor", 1)
    MODERATE = ("moderate", 2)
    MAJOR = ("major", 3)

    def __init__(self, string_value, int_value):
        self.string_value = string_value
        self.int_value = int_value

    @classmethod
    def from_string(cls, string):
        for member in cls:
            if member.string_value == string.lower():
                return member
        raise ValueError(f"{string} is not a valid {cls.__name__}")

# Load interactions from JSON file
def load_interactions(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Build the drug interactions dictionary from JSON data
def build_interactions_dict(data):
    drug_interactions = {}
    for obj in data:
        drugs = obj["drugs"]
        severity = Severity.from_string(obj["severity"])
        description = obj["description"]
        key = tuple(sorted(drug.lower() for drug in drugs))
        if key in drug_interactions:
            existing_interaction = drug_interactions[key]
            if existing_interaction["severity"].int_value < severity.int_value:
                drug_interactions[key] = {
                    "severity": severity,
                    "description": description
                }
        else:
            drug_interactions[key] = {
                "severity": severity,
                "description": description
            }
    return drug_interactions

# Function to check interactions for a given list of drugs
def check_interactions(drugs, drug_interactions):
    max_severity = None
    interaction_info = None

    # Check all pairs of drugs
    n = len(drugs)
    for i in range(n):
        for j in range(i + 1, n):
            drug1, drug2 = drugs[i], drugs[j]
            key = tuple(sorted([drug1.lower(), drug2.lower()]))
            if key in drug_interactions:
                interaction = drug_interactions[key]
                if not max_severity or interaction["severity"].int_value > max_severity.int_value:
                    max_severity = interaction["severity"]
                    interaction_info = f"{interaction['severity'].string_value}: {interaction['description']}"
    
    return interaction_info if interaction_info else "No Interaction"

# Main function to process input and output the results
def main(interactions_file, input_file, output_file):
    interactions = load_interactions(interactions_file)
    drug_interactions = build_interactions_dict(interactions)

    # Read input lines
    with open(input_file, 'r') as file:
        input_lines = file.readlines()

    # Process each line
    results = []
    for line in input_lines:
        drugs = line.strip().split()
        result = check_interactions(drugs, drug_interactions)
        results.append(result)

    # Write results to output file
    with open(output_file, 'w') as file:
        for result in results:
            file.write(result + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("How To Use: python check_drug_interactions.py <interactions.json> <input.txt> <output.txt>")
        sys.exit(1)

    interactions_file = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    main(interactions_file, input_file, output_file)
