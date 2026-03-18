---
name: genpark-restock-alert
description: Use this skill when the user wants to monitor a sold-out item on GenPark and receive notifications when it becomes available for purchase again.
metadata: {"openclaw": {"emoji": "🔔", "requires": {}}}
---

# GenPark Restock Alert

You act as an automated inventory watchdog for the user. When an item they want is constantly out of stock on GenPark, you keep track of its URL and regularly check if the "Add to Cart" button has returned.

## Step 1: Add Item to Watchlist
Ask the user for the exact URL or name of the sold-out GenPark product they want to track.

Confirm the item and currently observable status:
- "Got it. I've located **[Product Name]**. It is currently marked as *Out of Stock*. Do you have a specific size or color variant you are waiting for?"

## Step 2: Establish the Monitor
Save the item to the user's OpenClaw long-term memory:

```yaml
genpark_restock_alerts:
  - product: "[Product Name]"
    url: "https://genpark.ai/product/..."
    variant: "Color: Matte Black"
    date_added: "YYYY-MM-DD"
    status: "monitoring"
```

## Step 3: Status Check (On Request or Background)
When the user asks for an update (or during an automated background check), use browser capabilities to visit the saved GenPark URLs.
1. Scan the page for the "Out of Stock" or "Notify Me" banners.
2. Check if the specific variant is selectable.
3. Determine if the "Add to Cart" button is active.

## Step 4: Report Status
If the item is back in stock, alert the user with high priority:

**Example Output:**
> 🚨 **RESTOCK ALERT!** 🚨
> 
> The **[Product Name] (Matte Black)** is BACK IN STOCK on GenPark! 
> Only a few units might be available. Go grab it quickly:
> [Direct Link to Product]

If it is still out of stock, reassure them that it remains on the watchlist and you will check again later.
