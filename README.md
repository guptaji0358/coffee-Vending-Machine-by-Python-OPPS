# coffee-Vending-Machine-by-Python-OPPS
DAY - Project - Python X opp X Coffee Vendong Machine

# Coffee Vending Machine Simulator

A Python-based Coffee Vending Machine simulator that allows users to order drinks, handle payments, and manage machine resources. This project is designed to simulate a real-world coffee vending machine in a console environment.

## Features

- Display coffee menu using **PrettyTable**
- Track machine resources: water, milk, coffee
- Accept coins and process payments
- Generate reports for resources and profit
- Refill machine resources:
  - **Half refill** (+100ml/g per resource)
  - **Full refill** (+1000ml/g per resource)
  - Deduct refill cost from machine profit or allow user to pay manually
  - Bonus +500g coffee if user pays refill manually
- User-friendly input system with commands:
  - `menu` → Show available drinks
  - `report` → Show current resources and profit
  - `refill` → Refill machine resources
  - `off` → Turn off the machine

## Installation

1. Make sure Python 3.x is installed.
2. Install dependencies:

```bash
pip install prettytable
