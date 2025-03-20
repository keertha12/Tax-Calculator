import streamlit as st

# Function to calculate tax
def calculate_tax(age, income, regime):
    tax = 0
    if regime == "Old Regime (FY 2024-25)":
        slabs = [(300000, 0), (700000, 0.05), (1000000, 0.1), (1200000, 0.15), (1500000, 0.2), (float('inf'), 0.3)]
    else:  # New Regime (FY 2025-26)
        slabs = [(400000, 0), (800000, 0.05), (1200000, 0.1), (1600000, 0.15), (2000000, 0.2), (2400000, 0.25), (float('inf'), 0.3)]

    previous_slab = 0
    for slab, rate in slabs:
        if income > slab:
            tax += (slab - previous_slab) * rate
            previous_slab = slab
        else:
            tax += (income - previous_slab) * rate
            break

    # Apply rebate under Section 87A (if income <= ₹7,00,000 in Old Regime or ₹5,00,000 in New Regime)
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

    name = st.text_input("Enter your Name:")
    age = st.number_input("Enter your Age:", min_value=18, max_value=100)
    occupation = st.selectbox("Select your Occupation Type:", ["", "Salaried", "Self-Employed", "Business Owner"], index=0)
    annual_income = st.number_input("Enter your Annual Package (in INR):", min_value=100000)
    regime = st.radio("Choose Tax Regime:", ["Old Regime (FY 2024-25)", "New Regime (FY 2025-26)"])

    if st.button("Calculate Tax"):
        if not age or not annual_income or regime is None:
            st.error("Please fill in all the fields before proceeding.")
        else:
            tax = calculate_tax(age, annual_income, regime)
            st.success(f"Hey {name}, based on your details, your total tax liability is ₹{tax}")

            if regime == "Old Regime (FY 2024-25)":
                st.markdown("### Old Regime Tax Slabs:")
                st.table([
                    ["Up to ₹3 lakh", "0%"],
                    ["₹3 lakh - ₹7 lakh", "5%"],
                    ["₹7 lakh - ₹10 lakh", "10%"],
                    ["₹10 lakh - ₹12 lakh", "15%"],
                    ["₹12 lakh - ₹15 lakh", "20%"],
                    ["More than ₹15 lakh", "30%"]
                ])
            else:
                st.markdown("### New Regime Tax Slabs:")
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
