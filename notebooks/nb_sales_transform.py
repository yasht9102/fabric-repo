# Notebook: nb_sales_transform
# Purpose: Transform sales data
# Layer: Silver → Gold

def transform_sales(df):
    """
    Applies business logic on sales data
    """
    df["amount_with_tax"] = df["amount"] * 1.18
    return df
