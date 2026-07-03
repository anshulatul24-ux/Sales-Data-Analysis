# ==========================================================
# Sales Data Analysis Dashboard
# Thiranex Data Science Internship
# Submitted by: Anshul Patil
# ==========================================================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Plot Style
plt.style.use("ggplot")
sns.set_theme(style="whitegrid")

print("=" * 60)
print("      SALES DATA ANALYSIS DASHBOARD")
print("=" * 60)

# Load Dataset
print("\nLoading Dataset...")

df = pd.read_csv("./dataset/Superstore.csv")

print("\nColumns in Dataset:")

print("Dataset Loaded Successfully!")

# First 5 Rows
print("\nFirst 5 Rows:")
print(df.head())

# Dataset Information
print("\nDataset Information:")
df.info()

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe(include="all"))

# ==========================================================
# Missing Values & Duplicate Records
# ==========================================================

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Remove Duplicates
df = df.drop_duplicates()

print("\nDataset Shape After Removing Duplicates:")
print(df.shape)

# Save Cleaned Dataset
df.to_csv("./dataset/Cleaned_Superstore.csv", index=False)

print("\nCleaned Dataset Saved Successfully!")

# ==========================================================
# SALES VISUALIZATIONS
# ==========================================================

print("\nGenerating Visualizations...")

# Sales by Category
plt.figure(figsize=(8,5))
sns.barplot(
    data=df,
    x="Category",
    y="Sales",
    estimator=sum,
    errorbar=None
)
plt.title("Total Sales by Category")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("./images/Sales_by_Category.png")
plt.show()

# Sales by Region
plt.figure(figsize=(8,5))
sns.barplot(
    data=df,
    x="Region",
    y="Sales",
    estimator=sum,
    errorbar=None
)
plt.title("Total Sales by Region")
plt.tight_layout()
plt.savefig("./images/Sales_by_Region.png")
plt.show()

# Sales Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["Sales"], bins=30, kde=True)
plt.title("Sales Distribution")
plt.tight_layout()
plt.savefig("./images/Sales_Distribution.png")
plt.show()

# Sales by Sub-Category
plt.figure(figsize=(12,6))
sns.barplot(
    data=df,
    x="Sub-Category",
    y="Sales",
    estimator=sum,
    errorbar=None
)
plt.xticks(rotation=60)
plt.title("Sales by Sub-Category")
plt.tight_layout()
plt.savefig("./images/Sales_by_SubCategory.png")
plt.show()

# Sales by Segment
plt.figure(figsize=(8,5))
sns.barplot(
    data=df,
    x="Segment",
    y="Sales",
    estimator=sum,
    errorbar=None
)
plt.title("Sales by Segment")
plt.tight_layout()
plt.savefig("./images/Sales_by_Segment.png")
plt.show()

# Number of Orders by Region
plt.figure(figsize=(8,5))
sns.countplot(data=df, x="Region")
plt.title("Orders by Region")
plt.tight_layout()
plt.savefig("./images/Orders_by_Region.png")
plt.show()

print("\nVisualizations Created Successfully!")