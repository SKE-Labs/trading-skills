#!/usr/bin/env python3
"""
Position Size Calculator

Calculates the optimal position size based on account balance, risk percentage,
entry price, and stop loss price.

Usage:
    python calculate_position.py --balance 10000 --risk 1 --entry 100 --stop 95

Arguments:
    --balance   Account balance in dollars
    --risk      Risk percentage per trade (e.g., 1 for 1%)
    --entry     Entry price
    --stop      Stop loss price
    --atr       (Optional) ATR value for volatility-based sizing
    --atr-mult  (Optional) ATR multiplier (default: 2)
"""

import argparse
import sys


def calculate_fixed_risk(balance: float, risk_pct: float, entry: float, stop: float) -> dict:
    """Calculate position size using fixed percentage risk method."""
    risk_amount = balance * (risk_pct / 100)
    risk_per_unit = abs(entry - stop)
    
    if risk_per_unit == 0:
        return {"error": "Entry and stop loss cannot be the same price"}
    
    position_size = risk_amount / risk_per_unit
    position_value = position_size * entry
    
    return {
        "method": "Fixed Percentage Risk",
        "balance": balance,
        "risk_percent": risk_pct,
        "risk_amount": round(risk_amount, 2),
        "entry_price": entry,
        "stop_loss": stop,
        "risk_per_unit": round(risk_per_unit, 4),
        "position_size": round(position_size, 4),
        "position_value": round(position_value, 2),
        "direction": "LONG" if entry > stop else "SHORT"
    }


def calculate_atr_based(balance: float, risk_pct: float, atr: float, multiplier: float = 2) -> dict:
    """Calculate position size using ATR-based volatility method."""
    risk_amount = balance * (risk_pct / 100)
    risk_per_unit = atr * multiplier
    
    if risk_per_unit == 0:
        return {"error": "ATR cannot be zero"}
    
    position_size = risk_amount / risk_per_unit
    
    return {
        "method": "ATR-Based (Volatility)",
        "balance": balance,
        "risk_percent": risk_pct,
        "risk_amount": round(risk_amount, 2),
        "atr": atr,
        "atr_multiplier": multiplier,
        "stop_distance": round(risk_per_unit, 4),
        "position_size": round(position_size, 4)
    }


def calculate_kelly(win_rate: float, risk_reward: float) -> dict:
    """Calculate Kelly Criterion percentage."""
    if risk_reward == 0:
        return {"error": "Risk/Reward ratio cannot be zero"}
    
    kelly_pct = win_rate - ((1 - win_rate) / risk_reward)
    half_kelly = kelly_pct / 2
    
    return {
        "method": "Kelly Criterion",
        "win_rate": win_rate,
        "risk_reward": risk_reward,
        "kelly_percent": round(kelly_pct * 100, 2),
        "half_kelly_percent": round(half_kelly * 100, 2),
        "recommendation": "Use half-Kelly for safety"
    }


def main():
    parser = argparse.ArgumentParser(description="Calculate position size for trading")
    parser.add_argument("--balance", type=float, required=True, help="Account balance")
    parser.add_argument("--risk", type=float, required=True, help="Risk percentage (e.g., 1 for 1%)")
    parser.add_argument("--entry", type=float, help="Entry price")
    parser.add_argument("--stop", type=float, help="Stop loss price")
    parser.add_argument("--atr", type=float, help="ATR value for volatility-based sizing")
    parser.add_argument("--atr-mult", type=float, default=2, help="ATR multiplier (default: 2)")
    parser.add_argument("--win-rate", type=float, help="Win rate for Kelly (0-1)")
    parser.add_argument("--rr", type=float, help="Risk/Reward ratio for Kelly")
    
    args = parser.parse_args()
    
    results = []
    
    # Fixed risk calculation
    if args.entry and args.stop:
        result = calculate_fixed_risk(args.balance, args.risk, args.entry, args.stop)
        results.append(result)
    
    # ATR-based calculation
    if args.atr:
        result = calculate_atr_based(args.balance, args.risk, args.atr, args.atr_mult)
        results.append(result)
    
    # Kelly calculation
    if args.win_rate and args.rr:
        result = calculate_kelly(args.win_rate, args.rr)
        results.append(result)
    
    if not results:
        print("Error: Provide --entry and --stop, or --atr, or --win-rate and --rr")
        sys.exit(1)
    
    # Print results
    for result in results:
        print(f"\n{'='*50}")
        print(f"Method: {result.get('method', 'Unknown')}")
        print(f"{'='*50}")
        for key, value in result.items():
            if key != "method":
                print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
