import pandas as pd
import numpy as np
import random
import uuid

def generate_hr_dataset(num_records: int = 3500) -> pd.DataFrame:
    """
    Generates a synthetic HR dataset modeled on enterprise demographic 
    and systemic attributes to facilitate attrition analytics.
    """
    # Initialize random seeds for reproducible data distribution
    np.random.seed(42)
    random.seed(42)

    departments = ['Sales', 'Research & Development', 'Human Resources', 'Engineering', 'Customer Support']
    
    # Tiered job roles ensuring hierarchical representation
    job_roles = {
        'Sales': ['Sales Executive', 'Sales Representative', 'Regional Manager'],
        'Research & Development': ['Laboratory Technician', 'Research Scientist', 'Manufacturing Director', 'Research Director'],
        'Human Resources': ['HR Generalist', 'HR Business Partner', 'HR Director'],
        'Engineering': ['Software Engineer', 'Senior Software Engineer', 'Engineering Manager'],
        'Customer Support': ['Support Specialist', 'Customer Success Manager', 'Support Director']
    }
    
    dataset = []
    
    for _ in range(num_records):
        # Generate persistent, unique enterprise identifiers
        emp_id = f"EMP-{uuid.uuid4().hex[:8].upper()}"
        
        # Age distribution modeled on typical workforce demographics (mean 38, SD 10)
        age = int(np.random.normal(loc=38, scale=10))
        age = max(18, min(age, 65))
        
        department = random.choice(departments)
        job_role = random.choice(job_roles[department])
        
        # Geospatial commute distribution
        distance_from_home = int(np.random.exponential(scale=10))
        distance_from_home = max(1, min(distance_from_home, 60))
        
        # Compensation modeling aligned with role seniority
        base_income = 4000
        multiplier = 1.0
        if 'Manager' in job_role or 'Director' in job_role:
            multiplier = 2.4
        elif 'Senior' in job_role or 'Partner' in job_role:
            multiplier = 1.5
            
        monthly_income = int(np.random.normal(loc=base_income * multiplier, scale=1200))
        monthly_income = max(2000, monthly_income)
        
        # Organizational tenure bounded by age limits
        max_tenure_possible = age - 18
        years_at_company = int(np.random.exponential(scale=5))
        years_at_company = min(years_at_company, max_tenure_possible)
        
        # Multivariable risk logic for dependent variable (Attrition)
        base_attrition_risk = 0.12 # Enterprise baseline turnover probability
        
        # Aggregate correlational risk factors
        if distance_from_home > 25:
            base_attrition_risk += 0.08
        if monthly_income < 3500:
            base_attrition_risk += 0.12
        if years_at_company <= 2:
            base_attrition_risk += 0.09
            
        attrition_flag = 'Yes' if random.random() < base_attrition_risk else 'No'
        
        dataset.append({
            'Employee ID': emp_id,
            'Age': age,
            'Department': department,
            'Job Role': job_role,
            'Distance From Home': distance_from_home,
            'Monthly Income': monthly_income,
            'Years At Company': years_at_company,
            'Attrition': attrition_flag
        })
        
    return pd.DataFrame(dataset)

if __name__ == "__main__":
    output_filename = "hr_attrition_dataset.csv"
    print("Initiating synthetic human resources data compilation...")
    df_enterprise_hr = generate_hr_dataset(num_records=3500)
    df_enterprise_hr.to_csv(output_filename, index=False)
    print(f"Data generation complete. Exported {len(df_enterprise_hr)} master records to {output_filename}.")
