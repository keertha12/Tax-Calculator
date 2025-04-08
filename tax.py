import streamlit as st

# Function to calculate tax based on income classification
def calculate_tax(age, income, regime, income_breakdown):
    total_tax = 0

    # Old Regime Tax Calculation
    if regime == "Old Regime (FY 2024-25)":
        if income_breakdown['Salary'] > 0:
            # Apply tax on Salary income
            salary_tax = 0
            if income_breakdown['Salary'] <= 300000:
                salary_tax = 0
            elif income_breakdown['Salary'] <= 700000:
                salary_tax = income_breakdown['Salary'] * 0.05
            elif income_breakdown['Salary'] <= 1000000:
                salary_tax = income_breakdown['Salary'] * 0.1
            elif income_breakdown['Salary'] <= 1200000:
                salary_tax = income_breakdown['Salary'] * 0.15
            elif income_breakdown['Salary'] <= 1500000:
                salary_tax = income_breakdown['Salary'] * 0.2
            else:
                salary_tax = income_breakdown['Salary'] * 0.3

            total_tax += salary_tax

        if income_breakdown['Business Income'] > 0:
            # Apply tax on Business Income (assuming Business Tax rate is 30%)
            total_tax += income_breakdown['Business Income'] * 0.3

        if income_breakdown['Capital Gains'] > 0:
            # Apply tax on Capital Gains (assuming 15% tax for short-term and 10% for long-term)
            if income_breakdown['Capital Gains'] < 500000:
                total_tax += income_breakdown['Capital Gains'] * 0.15
            else:
                total_tax += income_breakdown['Capital Gains'] * 0.1

    # New Regime Tax Calculation
    elif regime == "New Regime (FY 2025-26)":
        if income_breakdown['Salary'] > 0:
            # Apply tax on Salary income
            salary_tax = 0
            if income_breakdown['Salary'] <= 400000:
                salary_tax = 0
            elif income_breakdown['Salary'] <= 800000:
                salary_tax = income_breakdown['Salary'] * 0.05
            elif income_breakdown['Salary'] <= 1200000:
                salary_tax = income_breakdown['Salary'] * 0.1
            elif income_breakdown['Salary'] <= 1600000:
                salary_tax = income_breakdown['Salary'] * 0.15
            elif income_breakdown['Salary'] <= 2000000:
                salary_tax = income_breakdown['Salary'] * 0.2
            elif income_breakdown['Salary'] <= 2400000:
                salary_tax = income_breakdown['Salary'] * 0.25
            else:
                salary_tax = income_breakdown['Salary'] * 0.3

            total_tax += salary_tax

        if income_breakdown['Business Income'] > 0:
            # Apply tax on Business Income (assuming Business Tax rate is 30%)
            total_tax += income_breakdown['Business Income'] * 0.3

        if income_breakdown['Capital Gains'] > 0:
            # Apply tax on Capital Gains (assuming 15% tax for short-term and 10% for long-term)
            if income_breakdown['Capital Gains'] < 500000:
                total_tax += income_breakdown['Capital Gains'] * 0.15
            else:
                total_tax += income_breakdown['Capital Gains'] * 0.1

    # Apply rebate under Section 87A
    if regime == "Old Regime (FY 2024-25)" and income <= 700000:
        total_tax = 0
    elif regime == "New Regime (FY 2025-26)" and income <= 500000:
        total_tax = 0

    # Add cess (4%)
    total_tax += total_tax * 0.04

    return round(total_tax, 2)

# Main function to create the Streamlit app
def main():
    st.title("Indian Income Tax Calculator")

    name = st.text_input("Enter your Name:", value="")
    age = st.number_input("Enter your Age:", min_value=18, max_value=100, value=None)
    occupation = st.selectbox("Select your Occupation Type:", ["", "Salaried", "Self-Employed", "Business Owner"], index=None)
    
    # Income breakdown
    salary_income = st.number_input("Enter your Salary Income (in INR):", min_value=0, value=0)
    business_income = st.number_input("Enter your Business Income (in INR):", min_value=0, value=0)
    capital_gains = st.number_input("Enter your Capital Gains (in INR):", min_value=0, value=0)
    
    annual_income = salary_income + business_income + capital_gains  # Total income
    regime = st.radio("Choose Tax Regime:", ["Old Regime (FY 2024-25)", "New Regime (FY 2025-26)"], index=None)

    if st.button("Calculate Tax"):
        if not age or not annual_income or regime is None:
            st.error("Please fill in all the fields before proceeding.")
        else:
            income_breakdown = {
                'Salary': salary_income,
                'Business Income': business_income,
                'Capital Gains': capital_gains
            }
            tax = calculate_tax(age, annual_income, regime, income_breakdown)
            st.success(f"Hey {name}, based on your details, your total tax liability is ₹{tax}")

if __name__ == "__main__":
    main()
