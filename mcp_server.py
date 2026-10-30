import sys
import json
from client import RestockAlertEngine

def handle_request(req):
    method = req.get("method")
    if method == "tools/list":
        return {
            "tools": [{
                "name": "evaluate_inventory",
                "description": "Calculate inventory burn rate, days remaining, and automated reorder points",
                "inputSchema": {
                    "type": "object",
                    "properties": {
                        "sku": {"type": "string"},
                        "current_stock": {"type": "integer"},
                        "daily_sales_velocity": {"type": "number"},
                        "supplier_lead_time_days": {"type": "integer"},
                        "safety_stock": {"type": "integer", "default": 20}
                    },
                    "required": ["sku", "current_stock", "daily_sales_velocity", "supplier_lead_time_days"]
                }
            }]
        }
    elif method == "tools/call":
        args = req.get("params", {}).get("arguments", {})
        out = RestockAlertEngine.evaluate_inventory(
            args.get("sku", ""),
            int(args.get("current_stock", 0)),
            float(args.get("daily_sales_velocity", 1.0)),
            int(args.get("supplier_lead_time_days", 7)),
            int(args.get("safety_stock", 20))
        )
        return {"content": [{"type": "text", "text": json.dumps(out, indent=2)}]}
    return {"error": "Unsupported method"}

if __name__ == "__main__":
    for line in sys.stdin:
        if not line.strip(): continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            print(json.dumps({"id": req.get("id"), "result": res}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"error": str(e)}))
            sys.stdout.flush()
