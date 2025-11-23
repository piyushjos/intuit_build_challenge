import csv
from itertools import groupby
from operator import itemgetter
from typing import List, Dict, Tuple


def load_sales_data(csv_path: str) -> List[dict]:
    """Read the raw sales CSV into a list of plain dicts we can analyze."""

    with open(csv_path, newline="", encoding="latin1") as f:
        reader = csv.DictReader(f)
        records = [
            {
                "order_number": int(row["ORDERNUMBER"]),
                "date": row["ORDERDATE"],          
                "country": row["COUNTRY"],
                "product_line": row["PRODUCTLINE"],
                "sales": float(row["SALES"]),
                "year": int(row["YEAR_ID"]),
                "month": int(row["MONTH_ID"]),
            }
            for row in reader
        ]
    return records


def calc_total_revenue(sales: List[dict]) -> float:
    """Add up the SALES column so we know the overall revenue."""
    return sum(map(lambda r: r["sales"], sales))


def revenue_by_region(sales: List[dict]) -> Dict[str, float]:
    """Keep a running total for each country to see which regions sell most."""
    key_fn = itemgetter("country")
    # groupby needs a sorted iterable to keep like items together
    sorted_sales = sorted(sales, key=key_fn)
    groups = groupby(sorted_sales, key=key_fn)

    return {
        country: sum(r["sales"] for r in rows)
        for country, rows in groups
    }


def revenue_by_product_line(sales: List[dict]) -> Dict[str, float]:
    """Aggregate revenue by product line so we can spot the top categories."""
    key_fn = itemgetter("product_line")
    sorted_sales = sorted(sales, key=key_fn)
    groups = groupby(sorted_sales, key=key_fn)

    return {
        product_line: sum(r["sales"] for r in rows)
        for product_line, rows in groups
    }


def monthly_revenue(sales: List[dict]) -> Dict[str, float]:
    """Roll up revenue per calendar month (YYYY-MM) to spot seasonality."""
    get_month = lambda r: f"{r['year']}-{r['month']:02d}"
    sorted_sales = sorted(sales, key=get_month)
    groups = groupby(sorted_sales, key=get_month)

    return {
        year_month: sum(r["sales"] for r in rows)
        for year_month, rows in groups
    }


def top_n_product_lines_by_revenue(
    sales: List[dict], n: int = 3
) -> List[Tuple[str, float]]:
    """Return the best-selling product lines, sorted by revenue."""
    revenue_map = revenue_by_product_line(sales)
    return sorted(
        revenue_map.items(),
        key=lambda item: item[1],
        reverse=True,
    )[:n]
