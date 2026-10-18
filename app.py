import math
import string
import streamlit as st

# ============================================================
# PAGE CONFIGURATION
# ============================================================
st.set_page_config(
    page_title="Bank Compare | Compare Loan EMI & Interest Rates",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# BLUE WEBSITE STYLING
# ============================================================
st.markdown("""
<style>
/* Main application background */
.stApp {
    background: linear-gradient(135deg, #FFFFFF 0%, #EAF4FF 60%, #BBDEFB 100%);
    color: #183153;
}

/* Main content spacing */
.block-container {
    padding-top: 4rem;      /* Space from the top */
    padding-bottom: 2rem;
    max-width: 1450px;
}


h1 {
    color: #87CEEB !important;
}

/* Warning message text color */
div[data-testid="stAlert"] p {
    color: #000000 !important;
}

/* Optional: make warning text bold */
div[data-testid="stAlert"] p {
    color: #000000 !important;
    font-weight: 600 !important;
}

/* Black borders for input fields */
.stNumberInput input,
.stTextInput input,
.stSelectbox div[data-baseweb="select"],
.stDateInput input,
.stTextArea textarea {
    border: 1.5px solid #000000 !important;
    border-radius: 9px !important;
    background-color: #F0F7FF !important;
    color: #183153 !important;
}

/* Black border on focus */
.stNumberInput input:focus,
.stTextInput input:focus,
.stSelectbox div[data-baseweb="select"]:focus-within,
.stDateInput input:focus,
.stTextArea textarea:focus {
    border: 2px solid #000000 !important;
    box-shadow: 0 0 0 1px #000000 !important;
}


/* Main headings */
h1, h2, h3 {
    color: #0B2545 !important;
    font-weight: 700 !important;
}

h1{
    color: #2196F3 !important;
    font-weight: 700 !important;
}

/* Captions and secondary text */
.stCaption, [data-testid="stCaptionContainer"] {
    color: #0077b6 !important;
}

/* Containers and cards */
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-color: #C5DDF5 !important;
    border-radius: 16px !important;
}




/* Input fields */
.stNumberInput input,
.stTextInput input,
.stSelectbox div[data-baseweb="select"] {
    background-color: #F0F7FF !important;
    color: #183153 !important;
    border-color: #B6D4F0 !important;
    border-radius: 9px !important;
}

/* Input labels */
.stNumberInput label,
.stTextInput label {
    color: #183153 !important;
    font-weight: 600 !important;
}

/* Primary buttons */
.stButton > button[kind="primary"] {
    background: linear-gradient(90deg, #1565C0, #2196F3) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 0.7rem 1.2rem !important;
    font-weight: 700 !important;
    transition: all 0.2s ease;
}

/* Button hover */
.stButton > button[kind="primary"]:hover {
    background: linear-gradient(90deg, #0D47A1, #1976D2) !important;
    box-shadow: 0 5px 14px rgba(25, 118, 210, 0.25);
    transform: translateY(-1px);
}

/* Secondary buttons */
.stButton > button {
    border-radius: 10px;
    border-color: #90CAF9;
}

/* Success messages */
div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Expanders */
div[data-testid="stExpander"] {
    background-color: #F5FAFF;
    border: 1px solid #C5DDF5;
    border-radius: 12px;
}

/* Tables */
div[data-testid="stDataFrame"] {
    border: 1px solid #C5DDF5;
    border-radius: 10px;
    overflow: hidden;
}

/* Dividers */
hr {
    border-color: #C5DDF5 !important;
}

/* Footer and header emphasis */
div[data-testid="stVerticalBlockBorderWrapper"] {
    box-shadow: 0 4px 18px rgba(21, 101, 192, 0.05);
}

/* Responsive layout */
@media (max-width: 768px) {
    .block-container {
        padding-left: 1rem;
        padding-right: 1rem;
    }
}



/* ==========================================
   BLACK BORDER AROUND THE COMPLETE CONTENT
   ========================================== */

/* Outer border around the entire application content */
div[data-testid="stAppViewBlockContainer"] {
    border: 2px solid #000000 !important;
    border-radius: 14px !important;
    padding: 2rem !important;
    box-sizing: border-box !important;
}

/* Header, body, and footer containers */
.st-key-site_header,
.st-key-site_body,
.st-key-site_footer,
div[data-testid="stVerticalBlockBorderWrapper"] {
    border: 2px solid #000000 !important;
    border-radius: 12px !important;
    box-sizing: border-box !important;
}

# /* Nested cards and bordered sections */
# div[data-testid="stVerticalBlockBorderWrapper"] > div {
#     border-color: #000000 !important;
# }

/* Expanders */
div[data-testid="stExpander"] {
    border: 2px solid #000000 !important;
    border-radius: 10px !important;
}

/* Tables */
div[data-testid="stDataFrame"],
div[data-testid="stTable"] {
    border: 2px solid #000000 !important;
    border-radius: 8px !important;
}

/* Input fields */
.stNumberInput input,
.stTextInput input,
.stDateInput input,
.stTimeInput input,
.stTextArea textarea,
div[data-baseweb="select"] > div {
    border: 1.5px solid #000000 !important;
}

/* All horizontal dividers */
hr {
    border: none !important;
    height: 2px !important;
    background-color: #000000 !important;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# THEME COLORS (fixed by .streamlit/config.toml)
# ============================================================

# ============================================================
# PROFESSIONAL BLUE THEME
# ============================================================
BACKGROUND = "#054F9E"     # Light blue background
CARD = "#FFFFFF"           # White cards
INPUT_BG = "#F0F7FF"       # Pale blue input fields
TEXT = "#183153"           # Dark navy text
HEADING = "#0B2545"        # Deep navy headings
MUTED = "#54718F"          # Muted blue-gray
BORDER = "#C5DDF5"         # Soft blue borders
PRIMARY = "#1976D2"        # Primary blue
SUCCESS_BG = "#E1F5FE"     # Light blue success background

# ============================================================
# HEADER
# ============================================================
with st.container(key="site_header", border=True):
    st.divider()
    st.caption("SMART LOAN COMPARISON")
    st.title("🏦 Bank Compare")
    st.divider()
    st.subheader("Compare Bank Loan Interest Rates, EMI and Total Repayment")
    st.write(
        "Compare loan offers from multiple banks using the reducing-balance "
        "EMI method. Estimate your monthly instalments, total interest payable "
        "and overall repayment to identify potentially lower-cost loan options."
    )
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**📊 Compare 2–10 banks**")
    with col2:
        st.markdown("**🧮 Calculate loan EMI**")
    with col3:
        st.markdown("**💰 Compare total interest**")

# st.divider()

with st.container(key="site_body", border=True):
    # ========================================================
    # HOW IT WORKS
    # ========================================================
    with st.container(border=True):
        st.subheader("How to Compare Bank Loan Offers")
        left, right = st.columns([3, 2], gap="large")
        with left:
            st.markdown(
                """
                Follow these steps to compare loan offers:

                1. Enter your loan amount and repayment tenure.
                2. Select the number of banks you want to compare.
                3. Enter each bank's annual interest rates and rate periods.
                4. Make sure the slab durations add up to the total tenure.
                5. Click **Compare Banks** to view estimated interest and repayment.
                """
            )
        with right:
            st.markdown("**Reducing-Balance EMI Formula**")
            st.latex(r"EMI = \frac{P r(1+r)^n}{(1+r)^n-1}")
            st.caption(
                "P = outstanding principal, r = monthly interest rate, "
                "n = remaining repayment months. For a zero-interest loan, "
                "EMI equals principal divided by remaining months."
            )

    # ========================================================
    # LOAN DETAILS
    # ========================================================
    st.divider()
    st.write("")
    st.header("1. Loan Details")
    principal_col, tenure_col = st.columns(2, gap="large")
    with principal_col:
        principal = st.number_input(
            "Principal / Loan Amount (₹)", min_value=1, max_value=1_000_000,
            value=100_000, step=5_000,
            help="Enter the amount you plan to borrow.",
        )
    with tenure_col:
        tenure = st.number_input(
            "Loan Tenure (Years)", min_value=1, max_value=50,
            value=3, step=1,
            help="Enter the total loan repayment period in years.",
        )
    principal = float(principal)
    tenure = int(tenure)
    st.caption(
        f"Loan amount: ₹{principal:,.0f} · Total tenure: {tenure} years "
        f"({tenure * 12} months)"
    )

    # ========================================================
    # BANK SELECTION
    # ========================================================
    st.write("")
    st.header("2. Select Banks")
    bank_count = int(
        st.number_input(
            "Number of banks to compare", min_value=2, max_value=10,
            value=2, step=1,
        )
    )
    bank_names = [f"Bank {letter}" for letter in string.ascii_uppercase[:bank_count]]
    st.caption(
        "You can compare between 2 and 10 banks. Use the bank labels as "
        "placeholders for your chosen lenders."
    )

    # ========================================================
    # BANK INTEREST-RATE INPUTS
    # ========================================================
    def bank_input(bank, loan_tenure):
        with st.container(border=True):
            st.subheader(f"🏦 {bank}")
            count = int(
                st.number_input(
                    "Number of interest-rate slabs", min_value=1,
                    max_value=min(30, loan_tenure),
                    value=min(2, loan_tenure), step=1,
                    key=f"{bank}_count",
                )
            )
            st.caption(
                "Enter the annual interest rate and duration for each "
                "consecutive period of the loan."
            )
            base_years = loan_tenure // count
            extra_years = loan_tenure % count
            slabs = []
            for i in range(count):
                default_years = base_years + (1 if i < extra_years else 0)
                st.markdown(f"**Slab {i + 1}**")
                rate_col, years_col = st.columns(2)
                with rate_col:
                    rate = st.number_input(
                        "Annual Rate (%)", min_value=0.0, max_value=100.0,
                        value=min(100.0, 8.0 + i), step=0.25,
                        key=f"{bank}_rate_{i}",
                    )
                with years_col:
                    years = st.number_input(
                        "Duration (Years)", min_value=1, max_value=loan_tenure,
                        value=default_years, step=1,
                        key=f"{bank}_years_{i}",
                    )
                slabs.append({"rate": float(rate), "years": int(years)})
                if i < count - 1:
                    st.divider()
            total_years = sum(slab["years"] for slab in slabs)
            if total_years != loan_tenure:
                st.warning(
                    f"Slab durations total {total_years} years. They must "
                    f"total exactly {loan_tenure} years."
                )
            return slabs, total_years

    st.write("")
    st.header("3. Enter Bank Interest Rates")
    bank_slabs = {}
    bank_periods = {}
    for start in range(0, bank_count, 2):
        columns = st.columns(2, gap="large")
        for offset in range(2):
            index = start + offset
            if index >= bank_count:
                break
            name = bank_names[index]
            with columns[offset]:
                slabs, total_years = bank_input(name, tenure)
                bank_slabs[name] = slabs
                bank_periods[name] = total_years

    # ========================================================
    # EMI CALCULATION
    # ========================================================
    def calculate_emi(balance, annual_rate, remaining_months):
        if remaining_months <= 0 or balance <= 0:
            return 0.0
        monthly_rate = annual_rate / 1200.0
        if monthly_rate == 0:
            return balance / remaining_months
        factor = (1 + monthly_rate) ** remaining_months
        return balance * monthly_rate * factor / (factor - 1)

    def calculate_bank(loan_principal, slabs, total_tenure_years):
        balance = float(loan_principal)
        total_repayment = 0.0
        total_interest = 0.0
        elapsed_months = 0
        total_months = int(total_tenure_years * 12)
        details = []

        for index, slab in enumerate(slabs, start=1):
            annual_rate = slab["rate"]
            slab_months = slab["years"] * 12
            remaining_months = total_months - elapsed_months
            if slab_months > remaining_months:
                raise ValueError("Slab durations exceed remaining tenure.")
            if balance <= 0 or remaining_months <= 0:
                break

            monthly_rate = annual_rate / 1200.0
            emi = calculate_emi(balance, annual_rate, remaining_months)
            slab_interest = 0.0
            slab_repayment = 0.0
            for _ in range(slab_months):
                if elapsed_months >= total_months or balance <= 0:
                    break
                interest = balance * monthly_rate
                payment = min(emi, balance + interest)
                balance = max(0.0, balance + interest - payment)
                if abs(balance) < 1e-8:
                    balance = 0.0
                slab_interest += interest
                slab_repayment += payment
                total_interest += interest
                total_repayment += payment
                elapsed_months += 1

            details.append(
                {
                    "Slab": index,
                    "Annual Rate": f"{annual_rate:.2f}%",
                    "Duration": f"{slab_months} months",
                    "Monthly EMI": f"₹{emi:,.2f}",
                    "Interest Paid": f"₹{slab_interest:,.2f}",
                    "Repayment": f"₹{slab_repayment:,.2f}",
                }
            )
        return total_interest, total_repayment, details

    # ========================================================
    # COMPARE BANKS
    # ========================================================
    st.write("")
    st.divider()
    st.subheader("4. Compare Your Loan Offers")
    st.markdown(
        "Review the bank details above, then calculate estimated monthly "
        "instalments, interest costs and total repayment."
    )
    compare = st.button("🧮 Compare Banks", type="primary", use_container_width=True)

    # ========================================================
    # RESULTS
    # ========================================================
    if compare:
        invalid_banks = [name for name in bank_names if bank_periods[name] != tenure]
        if invalid_banks:
            st.error(
                "Every bank's slab durations must add up to the total loan "
                f"tenure of {tenure} years."
            )
            st.write("Correct these banks: " + ", ".join(invalid_banks))
        else:
            results = {}
            for name in bank_names:
                interest, repayment, details = calculate_bank(
                    principal, bank_slabs[name], tenure
                )
                results[name] = {
                    "interest": interest,
                    "repayment": repayment,
                    "details": details,
                }

            st.write("")
            st.header("Loan Comparison Results")
            for start in range(0, bank_count, 2):
                columns = st.columns(2, gap="large")
                for offset in range(2):
                    index = start + offset
                    if index >= bank_count:
                        break
                    name = bank_names[index]
                    result = results[name]
                    with columns[offset]:
                        with st.container(border=True):
                            st.subheader(f"🏦 {name}")
                            st.caption("TOTAL INTEREST PAYABLE")
                            st.markdown(f"### ₹{result['interest']:,.2f}")
                            st.divider()
                            st.caption("TOTAL REPAYMENT")
                            st.markdown(f"### ₹{result['repayment']:,.2f}")
                            st.caption(
                                "Estimated average monthly payment: "
                                f"₹{result['repayment'] / (tenure * 12):,.2f}"
                            )
                            with st.expander(f"View {name} interest-rate slab details"):
                                st.dataframe(
                                    result["details"], use_container_width=True,
                                    hide_index=True,
                                )

            # FINAL RECOMMENDATION
            st.divider()
            st.header("🏆 Lowest-Interest Recommendation")
            lowest_interest = min(results[name]["interest"] for name in bank_names)
            winners = [
                name for name in bank_names
                if math.isclose(
                    results[name]["interest"], lowest_interest,
                    rel_tol=1e-9, abs_tol=0.01,
                )
            ]
            if len(winners) == bank_count:
                st.info("All banks have approximately the same estimated total interest.")
            elif len(winners) > 1:
                st.success(
                    "Lowest-interest options: " + ", ".join(winners)
                    + f" — ₹{lowest_interest:,.2f} estimated interest."
                )
            else:
                winner = winners[0]
                highest_interest = max(results[name]["interest"] for name in bank_names)
                st.success(
                    f"{winner} has the lowest estimated interest: ₹{lowest_interest:,.2f}."
                )
                st.info(
                    "Potential interest difference between the highest- and "
                    "lowest-interest offers: "
                    f"₹{highest_interest - lowest_interest:,.2f}."
                )

            # QUICK COMPARISON TABLE
            st.subheader("Quick Bank Loan Comparison")
            summary = [
                {
                    "Bank": name,
                    "Total Interest (₹)": round(results[name]["interest"], 2),
                    "Total Repayment (₹)": round(results[name]["repayment"], 2),
                }
                for name in bank_names
            ]
            summary.sort(key=lambda row: row["Total Interest (₹)"])
            st.dataframe(summary, use_container_width=True, hide_index=True)
            st.caption(
                "Banks are ranked by estimated total interest, not by approval "
                "probability or the full cost of borrowing."
            )

    # ========================================================
    # SEO-FRIENDLY INFORMATION SECTION
    # ========================================================
    st.write("")
    st.divider()
    with st.container(border=True):
        st.header("Understanding Loan EMI and Interest Rates")
        st.markdown(
            """
            Choosing a loan involves more than comparing the advertised interest rate. The repayment period, changing interest rates, processing fees and other lender charges can affect the overall cost of borrowing.

            **Bank Compare** is a loan comparison calculator that estimates total interest and repayment using the reducing-balance EMI method. You can compare multiple hypothetical bank offers and model different annual interest rates over consecutive loan periods.

            ### What is reducing-balance EMI?

            In the reducing-balance method, interest is calculated on the outstanding loan principal. As principal is repaid, the amount on which interest is charged generally decreases.

            ### How should you compare bank loans?

            Compare the estimated total interest, total repayment, fees, rate-reset conditions and other terms offered by each lender. A lower estimated interest cost does not necessarily mean a loan is the best option for every borrower.
            """
        )

# ============================================================
# FOOTER
# ============================================================
st.divider()
with st.container(key="site_footer", border=True):
    st.subheader("🏦 Bank Compare")
    st.write(
        "Compare bank loan interest rates, estimated EMI and total repayment "
        "in one place."
    )
    st.caption(
        "Disclaimer: Results are estimates for comparison purposes only. "
        "Actual EMI and repayment amounts may vary due to lender-specific "
        "calculation methods, fees, taxes, rounding, rate changes and repayment "
        "terms. This tool does not provide loan approval or financial advice. "
        "Verify the final loan terms directly with your lender."
    )
    st.divider()
    st.caption("© 2026 Bank Compare · Loan EMI and interest comparison tool")
