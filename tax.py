import streamlit as st

def calculate_tax(age, income, regime):
    """Calculate tax based on the selected tax regime."""
    tax = 0
    if regime == "Old Regime":
        deductions_80c = min(150000, income * 0.2)  # Can invest up to 1.5L under 80C
        taxable_income = max(0, income - deductions_80c)
        
        if age < 60:
            slabs = [(250000, 0.05), (500000, 0.1), (1000000, 0.2)]
        elif age < 80:
            slabs = [(300000, 0.05), (500000, 0.1), (1000000, 0.2)]
        else:
            slabs = [(500000, 0.05), (1000000, 0.2)]
        
        previous_slab = 0
        for slab, rate in slabs:
            if taxable_income > slab:
                tax += (slab - previous_slab) * rate
                previous_slab = slab
            else:
                tax += (taxable_income - previous_slab) * rate
                break
        if taxable_income > 1000000:
            tax += (taxable_income - 1000000) * 0.3
    
    else:  # New Regime
        slabs = [(250000, 0.05), (500000, 0.1), (750000, 0.15), (1000000, 0.2), (1250000, 0.25), (1500000, 0.3)]
        
        previous_slab = 0
        for slab, rate in slabs:
            if income > slab:
                tax += (slab - previous_slab) * rate
                previous_slab = slab
            else:
                tax += (income - previous_slab) * rate
                break
        if income > 1500000:
            tax += (income - 1500000) * 0.3
    
    if income <= 500000:
        tax = 0  # Rebate under Section 87A
    return round(tax, 2)


def main():
    st.title("Indian Income Tax Calculator")
    
    name = st.text_input("Enter your Name:")
    age = st.number_input("Enter your Age:", min_value=18, max_value=100, value=None, placeholder="Enter your age")
    occupation = st.selectbox("Select your Occupation Type:", ["", "Salaried", "Self-Employed", "Business Owner"], index=0)
    annual_income = st.number_input("Enter your Annual Package (in INR):", min_value=100000, value=None, placeholder="Enter your annual package")
    regime = st.radio("Choose Tax Regime:", ["Old Regime", "New Regime"], index=None)
    
    if st.button("Calculate Tax"):
        if not age or not annual_income or regime is None:
            st.error("Please fill in all the fields before proceeding.")
        else:
            tax = calculate_tax(age, annual_income, regime)
            st.success(f"Hey {name}, based on your details, your total tax liability is ₹{tax}")
            
            if regime == "Old Regime":
                investment_80c = min(150000, annual_income * 0.2)
                st.info(f"You can invest up to ₹{investment_80c} in tax-saving instruments like ELSS, PPF, NPS, etc. to reduce tax liability.")
                st.markdown("### Tax Saving Tips:")
                st.markdown("- **Section 80C:** Invest up to ₹1.5L in PPF, ELSS, EPF, NSC, etc.")
                st.markdown("- **Section 80D:** Health insurance premium up to ₹25,000 (₹50,000 for senior citizens)")
                st.markdown("- **Section 24(b):** Home loan interest deduction up to ₹2L per year")
                st.markdown("- **NPS (Section 80CCD):** Extra ₹50,000 deduction on NPS investment")
            else:
                st.warning("Under the New Regime, deductions are not available. Consider switching to the Old Regime if you want tax-saving benefits.")
    
if __name__ == "__main__":
    main()
