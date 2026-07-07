
# DAY 7 - DATA VISUALIZATION

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Improve chart style
sns.set_style("whitegrid")


# LOAD DATASET

df = pd.read_csv("RetailSales Day7.csv")

print(df.head())
print(df.info())
print(df.describe())

print("\nMissing Values")
print(df.isnull().sum())


# LINE CHART

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))

plt.plot(
    category_sales.index,
    category_sales.values,
    marker="o",
    color="blue",
    linewidth=3,
    label="Sales"
)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.legend()

plt.savefig("line_sales_category.png")

plt.show()

print("Insight: Technology/Furniture generates the highest sales.")


# BAR CHART

region_profit = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(8,5))

plt.bar(
    region_profit.index,
    region_profit.values,
    color="green"
)

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Profit")

plt.savefig("bar_profit_region.png")

plt.show()

print("Insight: Highest profit comes from the best-performing region.")


# HISTOGRAM

plt.figure(figsize=(8,5))

plt.hist(
    df["Sales"],
    bins=20,
    color="orange",
    edgecolor="black"
)

plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")

plt.savefig("hist_sales.png")

plt.show()

print("Insight: Most orders have lower sales values.")


# SCATTER PLOT

plt.figure(figsize=(8,5))

plt.scatter(
    df["Sales"],
    df["Profit"],
    color="red"
)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.savefig("scatter_sales_profit.png")

plt.show()

print("Insight: Higher sales generally produce higher profit.")


# PIE CHART

sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(7,7))

plt.pie(
    sales,
    labels=sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales Share by Category")

plt.savefig("pie_category.png")

plt.show()

print("Insight: Category contribution to total sales.")


# BOXPLOT

plt.figure(figsize=(8,5))

sns.boxplot(y=df["Sales"])

plt.title("Sales Boxplot")

plt.savefig("boxplot_sales.png")

plt.show()

print("Insight: Boxplot identifies outliers in Sales.")


# HEATMAP

corr = df[["Sales","Quantity","Discount","Profit"]].corr()

plt.figure(figsize=(8,6))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    linewidths=1
)

plt.title("Correlation Heatmap")

plt.savefig("heatmap.png")

plt.show()

print("Insight: Heatmap shows relationships among numeric columns.")


# SUBPLOTS

fig, axes = plt.subplots(1,2,figsize=(12,5))

# Sales by Category
category_sales.plot(
    kind="bar",
    ax=axes[0],
    color="skyblue"
)

axes[0].set_title("Sales by Category")
axes[0].set_xlabel("Category")
axes[0].set_ylabel("Sales")

# Profit by Region
region_profit.plot(
    kind="bar",
    ax=axes[1],
    color="lightgreen"
)

axes[1].set_title("Profit by Region")
axes[1].set_xlabel("Region")
axes[1].set_ylabel("Profit")

plt.tight_layout()

plt.savefig("subplots.png")

plt.show()

print("Insight: Subplots compare category sales and regional profit together.")


# COUNTPLOT

plt.figure(figsize=(8,5))

sns.countplot(
    x="Region",
    data=df
)

plt.title("Orders by Region")

plt.savefig("countplot_region.png")

plt.show()

print("Insight: Shows number of orders in each region.")


# BARPLOT

plt.figure(figsize=(8,5))

sns.barplot(
    x="Category",
    y="Sales",
    data=df
)

plt.title("Average Sales by Category")

plt.savefig("sns_barplot.png")

plt.show()

print("Insight: Shows average sales per category.")


# HISTPLOT

plt.figure(figsize=(8,5))

sns.histplot(
    df["Sales"],
    kde=True
)

plt.title("Sales Distribution")

plt.savefig("sns_histplot.png")

plt.show()

print("Insight: Distribution of sales with density curve.")

# Line Chart - Monthly Sales

df["OrderDate"] = pd.to_datetime(df["OrderDate"])

monthly_sales = (
    df.groupby(df["OrderDate"].dt.month)["Sales"]
    .sum()
)

plt.figure(figsize=(10,5))
plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    label="Sales"
)
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.savefig("monthly_sales_line_chart.png")
plt.close()

print("Insight: This line chart shows the monthly sales trend.\n")



print("\n==============================")
print("All charts generated successfully!")
print("==============================")
