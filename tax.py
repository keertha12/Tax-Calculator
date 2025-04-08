import streamlit as st

# Function to calculate tax based on income classification
def calculate_tax(age, income, regime):
    total_tax = 0

    # New Regime (FY 2025-26) Tax Calculation
    if regime == "New Regime (FY 2025-26)":
        # First 4 lakhs: Nil tax
        if income <= 400000:
            total_tax = 0
        elif income <= 800000:
            total_tax = (income - 400000) * 0.05
        elif income <= 1200000:
            total_tax = (400000 * 0.05) + (income - 800000) * 0.1
        elif income <= 1600000:
            total_tax = (400000 * 0.05) + (400000 * 0.1) + (income - 1200000) * 0.15
        else:
            total_tax = (400000 * 0.05) + (400000 * 0.1) + (400000 * 0.15) + (income - 1600000) * 0.15

    # Apply rebate under Section 87A
    if regime == "New Regime (FY 2025-26)" and income <= 500000:
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
    
    # Income breakdown (only salary income now)
    salary_income = st.number_input("Enter your Salary Income (in INR):", min_value=0, value=0)
    
    annual_income = salary_income  # Total income now consists only of salary
    regime = st.radio("Choose Tax Regime:", ["Old Regime (FY 2024-25)", "New Regime (FY 2025-26)"], index=None)

    if st.button("Calculate Tax"):
        if not age or not annual_income or regime is None:
            st.error("Please fill in all the fields before proceeding.")
        else:
            tax = calculate_tax(age, annual_income, regime)
            st.success(f"Hey {name}, based on your details, your total tax liability is ₹{tax}")

            if regime == "New Regime (FY 2025-26)":
                st.markdown("## New Regime Tax Slabs")
                st.table([
                    ["Up to ₹4 lakh", "0%"],
                    ["₹4 lakh - ₹8 lakh", "5%"],
                    ["₹8 lakh - ₹12 lakh", "10%"],
                    ["₹12 lakh - ₹16 lakh", "15%"],
                    ["Above ₹16 lakh", "15%"]
                ])

                st.markdown("### Tax-Saving Tips")
                st.markdown("Tax-saving investments like **PPF**, **EPF**, **ELSS**, **NSC**, and **Health Insurance Premiums (80D)** can help reduce your taxable income. Ensure to explore deductions for investments in **NPS** (Section 80CCD) and **Home Loan Interest** (Section 24).")

if __name__ == "__main__":
    main()
