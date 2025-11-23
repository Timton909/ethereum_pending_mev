import requests, time

def mev_hunter():
    print("Ethereum Pending MEV Hunter — live bundle & sandwich detector")
    while True:
        r = requests.get("https://eigenphi.io/api/v1/transactions/pending")
        for tx in r.json().get("data", [])[:20]:
            profit = float(tx.get("profit", 0))
            if profit > 0.5:  # >0.5 ETH profit
                print(f"MEV BUNDLE LIVE (${profit*55000:,.0f} profit)\n"
                      f"Type: {tx['type'].upper()}\n"
                      f"Front tx: {tx['transactions'][0][:10]}...\n"
                      f"Victim tx: {tx['transactions'][1][:10]}...\n"
                      f"https://eigenphi.io/tx/{tx['txHash']}\n"
                      f"→ Sandwich / Arb / Liq happening RIGHT NOW\n"
                      f"{'💰'*30}")
        time.sleep(1.8)

if __name__ == "__main__":
    mev_hunter()
