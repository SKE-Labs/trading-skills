#!/usr/bin/env python3
"""
Fibonacci Level Calculator

Calculates Fibonacci retracement and extension levels from swing points.

Usage:
    python calculate_fibonacci.py --high 150 --low 100
    python calculate_fibonacci.py --high 150 --low 100 --direction bullish

Arguments:
    --high       Swing high price
    --low        Swing low price
    --direction  Trade direction: bullish or bearish (auto-detected if omitted)
"""

import argparse


# Standard Fibonacci ratios
RETRACEMENT_LEVELS = [0.0, 0.236, 0.382, 0.5, 0.618, 0.786, 1.0]
EXTENSION_LEVELS = [0.0, -0.272, -0.618, -1.0, -1.618, -2.618]


def calculate_fibonacci(high: float, low: float, direction: str = "bullish") -> dict:
    """Calculate Fibonacci retracement and extension levels."""
    
    diff = high - low
    
    if direction == "bullish":
        # Bullish: retracements from high going down, extensions from high going up
        retracements = {
            f"{level*100:.1f}%": round(high - (diff * level), 4)
            for level in RETRACEMENT_LEVELS
        }
        extensions = {
            f"{abs(level)*100:.1f}%": round(high + (diff * abs(level)), 4)
            for level in EXTENSION_LEVELS if level != 0
        }
    else:
        # Bearish: retracements from low going up, extensions from low going down
        retracements = {
            f"{level*100:.1f}%": round(low + (diff * level), 4)
            for level in RETRACEMENT_LEVELS
        }
        extensions = {
            f"{abs(level)*100:.1f}%": round(low - (diff * abs(level)), 4)
            for level in EXTENSION_LEVELS if level != 0
        }
    
    return {
        "direction": direction.upper(),
        "swing_high": high,
        "swing_low": low,
        "range": round(diff, 4),
        "retracement_levels": retracements,
        "extension_levels": extensions,
        "key_levels": {
            "golden_ratio_38.2%": retracements["38.2%"],
            "half_retracement_50%": retracements["50.0%"],
            "golden_ratio_61.8%": retracements["61.8%"],
        }
    }


def main():
    parser = argparse.ArgumentParser(description="Calculate Fibonacci levels")
    parser.add_argument("--high", type=float, required=True, help="Swing high price")
    parser.add_argument("--low", type=float, required=True, help="Swing low price")
    parser.add_argument("--direction", type=str, default="bullish",
                        choices=["bullish", "bearish"],
                        help="Trade direction (default: bullish)")
    
    args = parser.parse_args()
    
    if args.high <= args.low:
        print("Error: High must be greater than low")
        return
    
    result = calculate_fibonacci(args.high, args.low, args.direction)
    
    print(f"\n{'='*50}")
    print(f"FIBONACCI LEVELS ({result['direction']})")
    print(f"{'='*50}")
    print(f"Swing High: {result['swing_high']}")
    print(f"Swing Low:  {result['swing_low']}")
    print(f"Range:      {result['range']}")
    
    print(f"\n--- Retracement Levels (Entries) ---")
    for level, price in result['retracement_levels'].items():
        marker = " ← KEY" if level in ["38.2%", "50.0%", "61.8%"] else ""
        print(f"  {level:>6}: {price}{marker}")
    
    print(f"\n--- Extension Levels (Targets) ---")
    for level, price in result['extension_levels'].items():
        print(f"  {level:>6}: {price}")


if __name__ == "__main__":
    main()
