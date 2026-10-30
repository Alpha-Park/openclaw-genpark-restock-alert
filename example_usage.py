from client import RestockAlertEngine

if __name__ == "__main__":
    res = RestockAlertEngine.evaluate_inventory("SKU-AUDIO-50", 45, 12.0, supplier_lead_time_days=7, safety_stock=30)
    print("Restock Evaluation:", res)
