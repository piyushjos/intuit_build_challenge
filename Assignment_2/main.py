from pathlib import Path

from analysis import (
    load_sales_data,
    calc_total_revenue,
    revenue_by_region,
    revenue_by_product_line,
    monthly_revenue,
    top_n_product_lines_by_revenue,
)


def main() -> None:
    "Load the sample sales data and print a quick, human-friendly summary."
    # Build an absolute path to the bundled CSV so the script works from anywhere.
    base_dir = Path(__file__).resolve().parent
    csv_path = base_dir / "data" / "sales_data_sample.csv"

    sales = load_sales_data(str(csv_path))

    total = calc_total_revenue(sales)
    by_region = revenue_by_region(sales)
    by_product_line = revenue_by_product_line(sales)
    by_month = monthly_revenue(sales)
    top_products = top_n_product_lines_by_revenue(sales, n=3)

    print("=== Sales Analysis Results (Assignment 2) ===")
    print(f"Total revenue: {total:.2f}")
    print()

    print("Revenue by region (COUNTRY):")
    for country, value in by_region.items():
        print(f"  {country}: {value:.2f}")
    print()

    print("Revenue by product line (PRODUCTLINE):")
    for pl, value in by_product_line.items():
        print(f"  {pl}: {value:.2f}")
    print()

    print("Monthly revenue (YYYY-MM):")
    for month, value in by_month.items():
        print(f"  {month}: {value:.2f}")
    print()

    print("Top 3 product lines by revenue:")
    for pl, value in top_products:
        print(f"  {pl}: {value:.2f}")


if __name__ == "__main__":
    main()
