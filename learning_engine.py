import json

def load_json_data(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def find_roles_by_input(input_string, data):
    matched_roles = []
    input_keywords = input_string.lower().split()  # Splitting the input string into keywords
    
    for role in data['job_roles']:
        name_keywords = role['name'].lower().split()
        skills_keywords = ' '.join(role['skills']).lower()
        
        # Check if any input keyword is in the job role's name or skills
        if any(keyword in name_keywords for keyword in input_keywords) or any(keyword in skills_keywords for keyword in input_keywords):
            matched_roles.append(role)
    
    return matched_roles

def aggregate_skills(matched_roles):
    all_skills = set()  # Using a set to avoid duplicate skills
    
    for role in matched_roles:
        for skill in role['skills']:
            all_skills.add(skill)
    
    return ' '.join(all_skills)  # Returning a single string containing all skills

# Assuming the user input is provided to this function
def process_user_input(input_string):
    input_string = ' '.join(input_string) if isinstance(input_string, list) else input_string
    data = load_json_data("C:/Users/Owner/Desktop/dop_project/data/jd/dummy_JD_skills.json")
    matched_roles = find_roles_by_input(input_string, data)
    skills_string = aggregate_skills(matched_roles)
    
    # Here, instead of printing, you can use the skills_string wherever needed in your application
    return skills_string  # For demonstration purposes only
