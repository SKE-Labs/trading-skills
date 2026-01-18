---
name: position-sizing
description: Calculate risk-based position sizes using fixed %, Kelly criterion, or volatility. Use when determining trade size, managing account risk, or standardizing risk across trades.
license: Apache-2.0
metadata:
  author: ske-labs
  version: "1.0"
---

# Position Sizing

Position sizing determines how much capital to risk per trade for consistent risk management.

## Position Sizing Methods

### 1. Fixed Percentage Risk

Most common and recommended:

```
Position Size = (Account × Risk %) / (Entry - Stop)
```

Example:

- Account: $10,000
- Risk: 1% = $100
- Entry: $100, Stop: $95 (risk $5/share)
- Position: $100 / $5 = 20 shares

### 2. Fixed Dollar Amount

- Risk same dollar amount per trade
- Simple but doesn't scale with account
- Good for beginners

### 3. Volatility-Based (ATR)

Adjust size based on volatility:

```
Position Size = (Account × Risk %) / (ATR × Multiplier)
```

- More volatile = smaller position
- Less volatile = larger position

### 4. Kelly Criterion (Advanced)

Optimal growth formula:

```
Kelly % = W - (1-W)/R
```

- W = Win rate
- R = Risk/Reward ratio
- Use half-Kelly for safety

## Recommended Guidelines

| Account Phase | Risk per Trade |
| ------------- | -------------- |
| Learning      | 0.5%           |
| Developing    | 1%             |
| Experienced   | 1-2%           |
| Maximum ever  | 3%             |

## Tool Integration

Use `calculate_position_size` tool with:

- Entry price
- Stop loss price
- User profile (contains balance, risk settings)

The tool automatically calculates:

- Position quantity
- Capital allocation
- Recommended leverage

### Script

Alternatively, run the bundled script:

```bash
python scripts/calculate_position.py --balance 10000 --risk 1 --entry 100 --stop 95
```

## Risk Rules

| Rule              | Guideline                |
| ----------------- | ------------------------ |
| Single trade max  | 2% of account            |
| Correlated trades | Treat as single position |
| Daily loss limit  | 5% of account            |
| Weekly loss limit | 10% of account           |

## Position Sizing Workflow

1. **Determine entry and stop loss**
2. **Calculate risk per share/unit**
3. **Apply position sizing formula**
4. **Verify against max limits**
5. **Execute with calculated size**
