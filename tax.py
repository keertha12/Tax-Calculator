import streamlit as st

# Function to calculate tax
def calculate_tax(age, income, regime):
    tax = 0

    if regime == "Old Regime (FY 2024-25)":
        if income <= 300000:
            tax = 0
        elif income <= 700000:
            tax = income * 0.05
        elif income <= 1000000:
            tax = income * 0.1
        elif income <= 1200000:
            tax = income * 0.15
        elif income <= 1500000:
            tax = income * 0.2
        else:
            tax = income * 0.3

    else:  # New Regime (FY 2025-26)
        if income <= 400000:
            tax = 0
        elif income <= 800000:
            tax = income * 0.05
        elif income <= 1200000:
            tax = income * 0.1
        elif income <= 1600000:
            tax = income * 0.15
        elif income <= 2000000:
            tax = income * 0.2
        elif income <= 2400000:
            tax = income * 0.25
        else:
            tax = income * 0.3

    # Apply rebate under Section 87A
    if regime == "Old Regime (FY 2024-25)" and income <= 700000:
        tax = 0
    elif regime == "New Regime (FY 2025-26)" and income <= 500000:
        tax = 0

    # Add cess (4%)
    tax += tax * 0.04

    return round(tax, 2)

# Main function to create the Streamlit app
def main():
    st.title("Indian Income Tax Calculator")

    name = st.text_input("Enter your Name:", value="")
    age = st.number_input("Enter your Age:", min_value=18, max_value=100, value=None)
    occupation = st.selectbox("Select your Occupation Type:", ["", "Salaried", "Self-Employed", "Business Owner"], index=None)
    annual_income = st.number_input("Enter your Annual Package (in INR):", min_value=100000, value=None)
    regime = st.radio("Choose Tax Regime:", ["Old Regime (FY 2024-25)", "New Regime (FY 2025-26)"], index=None)

    if st.button("Calculate Tax"):
        if not age or not annual_income or regime is None:
            st.error("Please fill in all the fields before proceeding.")
        else:
            tax = calculate_tax(age, annual_income, regime)
            st.success(f"Hey {name}, based on your details, your total tax liability is ₹{tax}")

            if regime == "Old Regime (FY 2024-25)":
                st.markdown("## Old Regime Tax Slabs")
                st.table([
                    ["Up to ₹3 lakh", "0%"],
                    ["₹3 lakh - ₹7 lakh", "5%"],
                    ["₹7 lakh - ₹10 lakh", "10%"],
                    ["₹10 lakh - ₹12 lakh", "15%"],
                    ["₹12 lakh - ₹15 lakh", "20%"],
                    ["More than ₹15 lakh", "30%"]
                ])
            else:
                st.markdown("## New Regime Tax Slabs")
                st.table([
                    ["0 - ₹4,00,000", "0%"],
                    ["₹4,00,001 - ₹8,00,000", "5%"],
                    ["₹8,00,001 - ₹12,00,000", "10%"],
                    ["₹12,00,001 - ₹16,00,000", "15%"],
                    ["₹16,00,001 - ₹20,00,000", "20%"],
                    ["₹20,00,001 - ₹24,00,000", "25%"],
                    ["Above ₹24,00,000", "30%"]
                ])

if __name__ == "__main__":
    main()
