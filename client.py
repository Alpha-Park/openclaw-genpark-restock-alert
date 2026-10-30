"""Inventory Restock Alert & Safety Stock Engine.
100% Python Standard Library.
"""

class RestockAlertEngine:
    """Calculates days-of-inventory-remaining and generates purchase order triggers."""

    @staticmethod
    def evaluate_inventory(sku: str, current_stock: int, daily_sales_velocity: float, supplier_lead_time_days: int, safety_stock: int = 20) -> dict:
        burn_rate = max(0.1, daily_sales_velocity)
        days_remaining = current_stock / burn_rate
        reorder_point = (supplier_lead_time_days * burn_rate) + safety_stock

        needs_reorder = current_stock <= reorder_point
        urgency = "CRITICAL" if days_remaining <= supplier_lead_time_days else ("MODERATE" if needs_reorder else "ADEQUATE")

        return {
            "sku": sku,
            "current_stock": current_stock,
            "daily_velocity": round(daily_sales_velocity, 2),
            "days_inventory_remaining": round(days_remaining, 1),
            "reorder_point_threshold": round(reorder_point, 1),
            "needs_reorder": needs_reorder,
            "urgency": urgency,
            "recommended_order_quantity": max(0, int((reorder_point * 2) - current_stock)) if needs_reorder else 0
        }
