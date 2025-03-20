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
            previous_slab = income


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
                st.markdown("## How to Reduce Your Tax Liability")

                st.markdown("### ✅ Section 80C – Investments (Max ₹1.5L per year)")
                st.markdown("- **PPF** – Interest earned is tax-free; lock-in period of 15 years.")
                st.markdown("- **EPF** – Contribution to EPF is eligible for deduction; interest is tax-free up to certain limits.")
                st.markdown("- **ELSS** – Tax-saving mutual funds with a 3-year lock-in period; potential for high returns.")
                st.markdown("- **NSC** – Interest is taxable but reinvested, qualifying for 80C deduction.")
                st.markdown("- **Sukanya Samriddhi Yojana (SSY)** – For girl children; interest is tax-free; limit up to ₹1.5 lakh.")
                st.markdown("- **Life Insurance Premiums** – Premiums paid for life insurance policies are deductible under 80C.")

                st.markdown("### ✅ Section 80D – Health Insurance Premiums (Max ₹1L per year)")
                st.markdown("- Self, spouse, children – ₹25,000 per year")
                st.markdown("- Parents below 60 years – ₹25,000")
                st.markdown("- Parents above 60 years – ₹50,000")

                st.markdown("### ✅ Section 80E – Education Loan Interest")
                st.markdown("- Interest on education loans is 100% deductible for up to 8 years.")

                st.markdown("### ✅ Section 24(b) – Home Loan Interest (Max ₹2L per year)")
                st.markdown("- Up to ₹2 lakh deduction on home loan interest (self-occupied property).")

                st.markdown("### ✅ Section 10(14) – House Rent Allowance (HRA)")
                st.markdown("- Deduction based on actual HRA received, rent paid, and city of residence.")

                st.markdown("### ✅ Section 80CCD(1B) – National Pension Scheme (NPS) (Max ₹50K)")
                st.markdown("- Additional ₹50,000 deduction on top of Section 80C for NPS contributions.")

                st.markdown("### ✅ Section 80G – Donations to Charitable Organizations")
                st.markdown("- 50% to 100% of donations to certain government-notified charities are deductible.")

                st.markdown("### ✅ Section 80TTA/80TTB – Interest on Savings Account")
                st.markdown("- Up to ₹10,000 deduction for savings interest (below 60).")
                st.markdown("- Up to ₹50,000 deduction for senior citizens (on savings, FDs, RDs).")

                st.markdown("### ✅ Section 54 – Capital Gains Exemption")
                st.markdown("- Reinvest capital gains into property or bonds to avoid tax.")

                st.markdown("### ✅ Tax-Saving Tips for Business Owners")
                st.markdown("- Deduct business expenses like office rent, utilities, and salaries.")
                st.markdown("- Use Presumptive Taxation Scheme for small businesses.")
                st.markdown("- Depreciation on business assets can be claimed as a deduction.")

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
