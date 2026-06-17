## Silver Business Intelligence Dashboard

 ## Project Overview

I built this project to practice the complete data analysis workflow, from creating a dataset in Python to building an interactive dashboard in Power BI.

The project is based on a fictional silver manufacturing and retail business called TRC Silvers. The goal was to understand business performance, customer behavior, product profitability, inventory management, supplier performance, and the impact of changing silver prices.

Instead of using an existing dataset, I generated the data myself using Python and then built a Power BI solution on top of it.

---
## What This Project Includes

* Python-generated business dataset
* Star schema data model
* 5-page Power BI dashboard
* 2 drill-through pages
* Bookmark navigation
* 25+ DAX measures
* Business insights and KPI tracking

---

## Dashboard Pages

### 1. Executive Command Center

Provides a high-level view of business performance through key metrics such as revenue, profit, profit margin, order count, and revenue growth.

Key visuals:

* Revenue Trend with Forecast
* Revenue vs Silver Rate
* Revenue Decomposition Tree

---

### 2. Customer Intelligence

Focused on understanding customer behavior and revenue contribution.

Key insights:

* Total Customers
* Repeat Customers
* Average Order Value
* Revenue by City
* Top Revenue-Contributing Customers

Includes a customer drill-through page for detailed analysis.

---

### 3. Product & Profitability

Helps identify which products contribute the most revenue and profit.

Key insights:

* Best Selling Product
* Highest Margin Product
* Revenue vs Profit Analysis
* Pareto Analysis

Includes a product drill-through page for detailed product performance analysis.

---

### 4. Inventory & Procurement

Tracks inventory levels and supplier performance.

Key insights:

* Inventory Value
* Products Requiring Reorder
* Supplier Lead Time
* Procurement Spend

Bookmark navigation allows switching between spend analysis and lead time analysis.

---

### 5. Market Intelligence

Analyzes the relationship between silver price movements and business performance.

Key insights:

* Current Silver Rate
* Highest and Lowest Silver Rates
* Silver Rate Trend Forecast
* Impact of Silver Prices on Sales Quantity and Profit

---

## Data Model

The dashboard follows a Star Schema design.

## Fact Tables

* Sales
* Purchases
* Inventory

## Dimension Tables

* Customers
* Products
* Suppliers
* Calendar
* Silver Rates

---

## DAX Concepts Used

Some of the DAX functions used in this project include:

* CALCULATE
* SAMEPERIODLASTYEAR
* RANKX
* FILTER
* ALL
* TOPN
* DIVIDE
* DISTINCTCOUNT
* SELECTEDVALUE

A full list of measures is available in the DAX_Measures folder.

---

## Dataset Creation

The dataset was generated using Python to simulate a real business environment.

The script creates:

* Customers
* Products
* Suppliers
* Sales Transactions
* Purchases
* Inventory Records
* Calendar Table
* Silver Rate History
---

## Repository Structure

* Dataset → CSV files used in Power BI
* Python_Code → Dataset generation script
* DAX_Measures → Calculated columns and measures
* Dashboard_Images → Dashboard screenshots

---

## Author

Susmitha T
