import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        buy_rate = float(entry_buy.get())
        sell_rate = float(entry_sell.get())
        capital = float(entry_capital.get())
        trades_per_day = int(entry_trades.get())

        spread = round(sell_rate - buy_rate, 4)
        usdt_bought = round(capital / buy_rate, 4)
        profit_per_trade = round(usdt_bought * spread, 2)
        daily_profit = round(profit_per_trade * trades_per_day, 2)
        monthly_profit = round(daily_profit * 30, 2)
        roi_percent = round((profit_per_trade / capital) * 100, 4)

        label_spread_val.config(text=f"₨{spread}")
        label_usdt_val.config(text=f"{usdt_bought}")
        label_profit_val.config(text=f"₨{profit_per_trade}")
        label_daily_val.config(text=f"₨{daily_profit}")
        label_monthly_val.config(text=f"₨{monthly_profit}")
        label_roi_val.config(text=f"{roi_percent}%")

    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

def clear_fields():
    entry_buy.delete(0, tk.END)
    entry_sell.delete(0, tk.END)
    entry_capital.delete(0, tk.END)
    entry_trades.delete(0, tk.END)
    label_spread_val.config(text="₨0.00")
    label_usdt_val.config(text="0.00")
    label_profit_val.config(text="₨0.00")
    label_daily_val.config(text="₨0.00")
    label_monthly_val.config(text="₨0.00")
    label_roi_val.config(text="0.00%")

root = tk.Tk()
root.title("P2P Arbitrage Spread & Profit Calculator")
root.geometry("400x400")
root.resizable(False, False)

tk.Label(root, text="Buy Rate (PKR):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Sell Rate (PKR):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Capital (PKR):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
tk.Label(root, text="Trades per Day:").grid(row=3, column=0, padx=10, pady=5, sticky="e")

entry_buy = tk.Entry(root)
entry_sell = tk.Entry(root)
entry_capital = tk.Entry(root)
entry_trades = tk.Entry(root)

entry_buy.grid(row=0, column=1, padx=10, pady=5)
entry_sell.grid(row=1, column=1, padx=10, pady=5)
entry_capital.grid(row=2, column=1, padx=10, pady=5)
entry_trades.grid(row=3, column=1, padx=10, pady=5)

# Output
tk.Label(root, text="Spread per USDT:").grid(row=5, column=0, padx=10, pady=5, sticky="e")
label_spread_val = tk.Label(root, text="₨0.00")
label_spread_val.grid(row=5, column=1, sticky="w")

tk.Label(root, text="USDT Bought:").grid(row=6, column=0, padx=10, pady=5, sticky="e")
label_usdt_val = tk.Label(root, text="0.00")
label_usdt_val.grid(row=6, column=1, sticky="w")

tk.Label(root, text="Profit per Trade:").grid(row=7, column=0, padx=10, pady=5, sticky="e")
label_profit_val = tk.Label(root, text="₨0.00")
label_profit_val.grid(row=7, column=1, sticky="w")

tk.Label(root, text="Daily Profit:").grid(row=8, column=0, padx=10, pady=5, sticky="e")
label_daily_val = tk.Label(root, text="₨0.00")
label_daily_val.grid(row=8, column=1, sticky="w")

tk.Label(root, text="Monthly Profit:").grid(row=9, column=0, padx=10, pady=5, sticky="e")
label_monthly_val = tk.Label(root, text="₨0.00")
label_monthly_val.grid(row=9, column=1, sticky="w")

tk.Label(root, text="ROI (%):").grid(row=10, column=0, padx=10, pady=5, sticky="e")
label_roi_val = tk.Label(root, text="0.00%")
label_roi_val.grid(row=10, column=1, sticky="w")

tk.Button(root, text="Calculate", command=calculate).grid(row=11, column=0, pady=20)
tk.Button(root, text="Clear", command=clear_fields).grid(row=11, column=1, pady=20)

root.mainloop()