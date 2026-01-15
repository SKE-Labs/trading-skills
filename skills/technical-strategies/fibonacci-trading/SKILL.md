---
name: fibonacci-trading
description: Use Fibonacci retracement and extension for entries and targets. Use when finding pullback entries, setting profit targets, or identifying key reversal levels.
---

# Fibonacci Trading

Fibonacci ratios identify key retracement and extension levels for entries and targets.

## Key Fibonacci Levels

### Retracement Levels (Entries)

| Level | Use                      |
| ----- | ------------------------ |
| 23.6% | Shallow pullback         |
| 38.2% | Moderate pullback        |
| 50.0% | Half retracement         |
| 61.8% | Golden ratio (key level) |
| 78.6% | Deep pullback            |

### Extension Levels (Targets)

| Level        | Use                 |
| ------------ | ------------------- |
| -27% (127%)  | Conservative target |
| -62% (162%)  | Standard target     |
| -100% (200%) | Extended target     |
| -162% (262%) | Aggressive target   |

## Drawing Fibonacci

### For Bullish Setups

- Draw from **swing low** to **swing high**
- Retracements show potential buy zones
- Extensions show upside targets

### For Bearish Setups

- Draw from **swing high** to **swing low**
- Retracements show potential sell zones
- Extensions show downside targets

## Entry Strategy

1. **Identify clear swing** (impulsive move)
2. **Draw Fibonacci retracement**
3. **Wait for pullback** to key levels (38.2%, 50%, 61.8%)
4. **Enter with confirmation**:
   - Rejection candle
   - Structure break on LTF
   - Confluence with S/R
5. **Stop loss** beyond 78.6% or 100%
6. **Targets** at extension levels

## Confluence Zones

Best Fibonacci trades have confluence:

- Fib level + Order block
- Fib level + S/R zone
- Fib level + Moving average
- Fib level + Trendline

## Workflow

1. Use `get_candles_around_date` to get exact swing points
2. Calculate Fib levels manually or describe levels
3. Mark key levels using `draw_on_chart`
4. Wait for price to reach levels
5. Enter with confirmation

## Best Practices

| Do                     | Don't                   |
| ---------------------- | ----------------------- |
| Draw from clear swings | Use every tiny swing    |
| Wait for confluence    | Trade Fib alone         |
| Use 61.8% as primary   | Ignore the golden ratio |
| Combine time frames    | Only use one TF         |
