import pandas as pd

# Load risk report
risk = pd.read_csv("../reports/var_cvar_report.csv")

# Sort by VaR (less negative = safer)
risk = risk.sort_values("VaR_95", ascending=False).reset_index(drop=True)


def recommend(risk_level):
    risk_level = risk_level.lower()

    if risk_level == "low":
        result = risk.head(3)

    elif risk_level == "moderate":
        start = len(risk) // 2 - 1
        result = risk.iloc[start:start + 3]

    elif risk_level == "high":
        result = risk.tail(3)

    else:
        print("Choose: Low / Moderate / High")
        return

    print(f"\nTop Recommendations for {risk_level.title()} Risk\n")
    print(result)


if __name__ == "__main__":
    level = input("Enter Risk Appetite (Low/Moderate/High): ")
    recommend(level)