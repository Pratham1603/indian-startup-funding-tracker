import pandas as pd

def classify_stage(series):
    if pd.isna(series):
        return "Unknown"
    
    series = series.lower()
    
    if "pre" in series or "seed" in series:
        return "Early Stage"
    elif "series a" in series or "series b" in series or "series c" in series:
        return "Growth Stage"
    elif "series d" in series or "series e" in series or "series f" in series:
        return "Late Stage"
    elif "debt" in series:
        return "Debt"
    else:
        return "Other"