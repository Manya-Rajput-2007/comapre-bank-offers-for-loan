# 🏦 Bank Compare — Loan EMI & Interest Rate Comparison

**Bank Compare** is an interactive loan comparison web application built with Python and Streamlit. It helps users compare hypothetical loan offers from multiple banks by calculating estimated monthly EMI, total interest payable, and total repayment.

Users can enter a loan amount, select the repayment tenure, compare 2–10 banks, and configure different annual interest rates across consecutive loan periods. The application then identifies the lowest-interest option based on the entered values.

## ✨ Features

- 🏦 **Multi-Bank Comparison:** Compare loan offers from 2 to 10 banks.
- 💳 **Loan Amount Input:** Specify the principal amount in Indian rupees (₹).
- 📅 **Flexible Loan Tenure:** Select a repayment period from 1 to 50 years.
- 📈 **Interest-Rate Slabs:** Configure multiple interest rates and their durations for each bank.
- 🧮 **EMI Calculation:** Calculate estimated monthly instalments using the reducing-balance method.
- 💰 **Total Interest Calculation:** Estimate the interest payable throughout the loan tenure.
- 📊 **Total Repayment Analysis:** Calculate the combined principal and interest repaid.
- 🏆 **Lowest-Interest Recommendation:** Identify the bank or banks offering the lowest estimated interest based on the supplied rates.
- 📋 **Detailed Results:** View interest-rate slab breakdowns and a ranked comparison table.
- ⚠️ **Input Validation:** Check that each bank's interest-rate slab durations add up to the total loan tenure.
- 🎨 **Modern Blue Interface:** Light blue background, sky-blue title styling, black input borders, blue buttons, and organized cards.
- 📱 **Responsive Layout:** Uses Streamlit's wide layout and column-based design.

## 🛠️ Tech Stack

- **Python** — Core application logic and calculations
- **Streamlit** — Interactive web interface
- **Math** — Floating-point comparisons for identifying equal interest costs
- **String** — Default bank labels and bank-count handling
- **HTML & CSS** — Custom blue theme and UI styling
- **uv** — Python dependency and environment management

## 📐 EMI Formula

The application uses the reducing-balance EMI formula:

\[
EMI = \frac{P \times r \times (1+r)^n}{(1+r)^n-1}
\]

Where:

- \(P\) = Outstanding loan principal
- \(r\) = Monthly interest rate, calculated as the annual rate divided by 12
- \(n\) = Remaining repayment period in months

For a zero-interest loan:

\[
EMI = \frac{P}{n}
\]

When a new interest-rate slab begins, the application recalculates the EMI using the outstanding principal and remaining repayment months.

## ⚙️ Installation and Setup

### Prerequisites

- Python installed on your system
- Git
- `uv` package manager

### 1. Clone the repository

```bash
git clone https://github.com/Manya-Rajput-2007/comapre-bank-offers-for-loan.git
cd comapre-bank-offers-for-loan
```

### 2. Install uv

If `uv` is not already installed, run:

```bash
pip install uv
```

### 3. Install dependencies

If the project dependencies are configured in `pyproject.toml` and `uv.lock`, run:

```bash
uv sync
```

### 4. Start the application

```bash
uv run streamlit run app.py
```

Open the local URL displayed in the terminal, usually:

```text
http://localhost:8501
```

## 🚀 How to Use

1. **Enter Loan Details:** Specify the principal amount and loan tenure.
2. **Select the Number of Banks:** Choose between 2 and 10 banks.
3. **Configure Interest Rates:** Enter the annual interest rate and duration for each consecutive interest-rate slab.
4. **Validate Durations:** Ensure that the sum of all slab durations for each bank equals the total loan tenure.
5. **Compare Offers:** Click the **Compare Banks** button.
6. **Review Results:** Examine each bank's total interest, total repayment, and estimated average monthly payment.
7. **View Slab Details:** Expand the interest-rate details to review the calculations for individual periods.
8. **Check the Recommendation:** Identify the lowest-interest option and the potential difference between the highest and lowest interest costs.
9. **Review the Comparison Table:** Compare and rank all banks by estimated total interest.

## 📁 Project Structure

```text
bankcompare/
│
├── app.py
├── pyproject.toml
├── uv.lock
├── README.md
│
└── src/
    └── bankcompare/
        └── __init__.py
```

| File | Description |
|---|---|
| `app.py` | Main Streamlit application, UI styling, EMI calculations, validation, and comparison results |
| `pyproject.toml` | Project metadata and dependency configuration |
| `uv.lock` | Locked dependency versions |
| `src/bankcompare/__init__.py` | Python package initialization |
| `README.md` | Project documentation |

## 🧠 Calculation Methodology

For each bank, the application:

1. Initializes the outstanding balance with the original loan principal.
2. Calculates the monthly EMI based on the current annual interest rate and remaining loan tenure.
3. Calculates monthly interest on the outstanding balance.
4. Updates the outstanding balance after each instalment.
5. Recalculates the EMI at the start of each subsequent interest-rate slab.
6. Accumulates interest and repayments across all slabs.
7. Compares the estimated total interest payable across the selected banks.
8. Displays the lowest-interest option and sorts the comparison table by total interest.

The application supports a zero-interest rate, for which EMI is calculated by dividing the outstanding principal by the remaining months.

## 🎨 User Interface

The application uses a custom blue theme designed for a clean and readable financial comparison experience.

- Light blue gradient background
- Sky-blue title accents
- Dark navy headings and text
- Black-bordered input fields
- Blue gradient primary button
- Rounded containers and comparison cards
- Organized sections for loan details, bank inputs, and results

## 🔮 Future Enhancements

Potential improvements include:

- Allow users to enter custom bank names directly.
- Add processing fees, insurance costs, and other borrowing charges.
- Display interactive charts comparing interest and repayment.
- Export results as PDF or CSV reports.
- Add verified, up-to-date bank interest-rate data.
- Support additional repayment scenarios and floating-rate loans.
- Add a downloadable amortization schedule showing monthly principal and interest.

## ⚠️ Disclaimer

Bank Compare is an educational loan comparison tool and does not provide financial advice or guarantee loan approval. The application calculates estimates using the interest rates and durations entered by the user; it does not fetch or verify live bank interest rates.

Actual loan costs may differ because of processing fees, taxes, lender-specific calculations, rounding, rate changes, and repayment conditions. Verify all loan terms directly with the lender before making a financial decision.

## 👩‍💻 Author

**Manya Rajput**

- GitHub: [Manya-Rajput-2007](https://github.com/Manya-Rajput-2007)

---

If you find this project useful, consider giving the repository a ⭐ star!