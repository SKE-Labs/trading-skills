---
name: sentiment-analysis
description: Analyze news sentiment and social indicators for trading signals. Use when gauging market mood, confirming technical signals, or identifying contrarian opportunities.
---

# Sentiment Analysis

Sentiment analysis gauges market psychology to identify extremes and potential reversals.

## Sentiment Indicators

### News Sentiment

| Signal          | Bullish             | Bearish        |
| --------------- | ------------------- | -------------- |
| Headline tone   | Positive/optimistic | Negative/fear  |
| Coverage volume | Increasing          | Panic coverage |
| Analyst stance  | Upgrades            | Downgrades     |

### Social Sentiment

| Signal            | Extreme Bullish    | Extreme Bearish  |
| ----------------- | ------------------ | ---------------- |
| Social mentions   | Parabolic increase | Capitulation     |
| Retail enthusiasm | Everyone bullish   | Everyone bearish |
| Influencer calls  | "100x moon"        | "Going to zero"  |

### Market Sentiment Indicators

| Indicator          | Bullish                       | Bearish                         |
| ------------------ | ----------------------------- | ------------------------------- |
| Fear & Greed Index | Extreme Fear (contrarian buy) | Extreme Greed (contrarian sell) |
| Put/Call Ratio     | High puts (contrarian buy)    | High calls (contrarian sell)    |
| VIX                | Spike high (buy)              | Very low (caution)              |

## Contrarian Trading

Extreme sentiment often marks reversal points:

- **Extreme bullishness** → Market top risk
- **Extreme bearishness** → Market bottom opportunity

## Analysis Workflow

Use `get_financial_news` tool to:

1. **Assess current sentiment**

   - Read recent headlines
   - Note analyst commentary
   - Gauge overall tone

2. **Identify extremes**

   - "Best ever" / "worst ever" language
   - Capitulation signs
   - Euphoria indicators

3. **Combine with technicals**
   - Sentiment at resistance = Stronger sell
   - Extreme fear at support = Stronger buy

## Sentiment Cycle

| Phase        | Sentiment        | Price   | Action     |
| ------------ | ---------------- | ------- | ---------- |
| Disbelief    | Negative         | Rising  | Accumulate |
| Hope         | Improving        | Rising  | Hold       |
| Optimism     | Positive         | Rising  | Hold       |
| Euphoria     | Extreme positive | Peak    | Distribute |
| Anxiety      | Mixed            | Falling | Watch      |
| Denial       | Still positive   | Falling | Exit       |
| Panic        | Extreme negative | Falling | Watch      |
| Capitulation | Despair          | Bottom  | Accumulate |

## Limitations

| Limitation   | Reality                    |
| ------------ | -------------------------- |
| Timing       | Sentiment can stay extreme |
| Subjectivity | Hard to quantify           |
| Lagging      | News follows price         |

## Best Practice

Use sentiment as:

- Confirmation, not primary signal
- Contrarian indicator at extremes
- Context for technical setups
