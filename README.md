# 📈 Trading Skills for Agentic AI

A curated collection of **50 trading skills** designed for AI agents. Built for [Embient.ai](https://embient.ai), but compatible with any agent that supports skills—including **Claude Code**, **Antigravity**, **Cursor**, and more.

These skills enable AI-powered trading assistants to understand market concepts, analyze charts, manage risk, and generate actionable trading insights.

[![Apache 2.0 License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-50-green.svg)](#skill-categories)
[![Embient](https://img.shields.io/badge/platform-Embient.ai-purple.svg)](https://embient.ai)
[![GitHub Stars](https://img.shields.io/github/stars/ske-labs/trading-skills?style=social)](https://github.com/ske-company/trading-skills)

---

## 🎯 What Are Trading Skills?

Trading skills are structured knowledge modules that teach AI agents how to:

- **Analyze** charts using technical and fundamental analysis
- **Identify** patterns, setups, and trading opportunities
- **Calculate** position sizes and manage risk
- **Generate** trading signals with proper entry/exit strategies

Each skill is a standalone markdown file with clear instructions, formulas, and workflows that AI agents can follow.

---

## 📁 Skill Categories

| Category                                                | Skills | Description                                                  |
| ------------------------------------------------------- | ------ | ------------------------------------------------------------ |
| [**ICT/Smart Money**](skills/ict-smart-money)           | 8      | Institutional trading concepts—order blocks, FVGs, liquidity |
| [**Technical Strategies**](skills/technical-strategies) | 10     | Indicator-based strategies—MACD, RSI, Fibonacci, VWAP        |
| [**Chart Patterns**](skills/chart-patterns)             | 8      | Classical patterns—head & shoulders, triangles, flags        |
| [**Risk Management**](skills/risk-management)           | 8      | Position sizing, stop losses, drawdown management            |
| [**Day Trading**](skills/day-trading)                   | 6      | Intraday strategies—scalping, breakouts, momentum            |
| [**Fundamental Analysis**](skills/fundamental-analysis) | 5      | Earnings, sentiment, economic calendar trading               |
| [**Crypto Trading**](skills/crypto-trading)             | 5      | Crypto-specific—on-chain analysis, funding rates, DCA        |

---

## ⚡ Quick Start

### Using with Embient.ai

1. Visit [embient.ai](https://embient.ai)
2. Browse the Skills Marketplace
3. Fork skills to your profile
4. Your AI trading assistant will use them automatically

### Using with Other AI Agents

These skills work with any AI coding agent that supports the skills format:

| Agent            | Setup                              |
| ---------------- | ---------------------------------- |
| **Claude Code**  | Add to `.claude/skills/` directory |
| **Antigravity**  | Add to `.agent/skills/` directory  |
| **Cursor**       | Add to `.cursor/skills/` directory |
| **Other agents** | Point to the `skills/` folder      |

```bash
git clone https://github.com/ske-company/trading-skills.git
# Copy skills to your agent's skills directory
cp -r trading-skills/skills/* .agent/skills/
```

Each skill follows a consistent structure in `SKILL.md`:

```yaml
---
name: skill-name
description: When to use this skill
---
# Skill Title
[Detailed instructions, formulas, workflows]
```

---

## 📚 Featured Skills

### ICT/Smart Money Concepts

- **Order Blocks** — Institutional buy/sell zones for high-probability entries
- **Fair Value Gaps** — Imbalances in price for retracement targets
- **Liquidity Zones** — Where stop losses cluster for smart money sweeps
- **Market Structure Shift** — Trend reversal confirmation signals

### Risk Management

- **Position Sizing** — Fixed %, ATR-based, and Kelly criterion methods
- **Stop Loss Strategies** — Technical, volatility, and time-based stops
- **Drawdown Management** — Recovery protocols and loss limits

### Technical Strategies

- **Fibonacci Trading** — Retracements and extensions for entries/targets
- **Multi-Timeframe Analysis** — HTF bias with LTF precision entries
- **VWAP Trading** — Volume-weighted levels for intraday trading

---

## 📝 Skill Format

> **Inspired by [Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)** — structured knowledge modules that extend AI agent capabilities.

Each skill follows this structure:

```markdown
---
name: skill-identifier
description: Brief description for skill selection
---

# Skill Title

## Identification / Setup

How to identify the pattern or setup

## Entry Strategy

Step-by-step entry workflow

## Risk Management

Stop loss and position sizing rules

## Best Practices

Do's and don'ts
```

---

## 🤝 Contributing

We welcome contributions! To add a new skill:

1. **Fork** this repository
2. **Create** a new folder under the appropriate category
3. **Add** a `SKILL.md` file following the format above
4. **Submit** a pull request

### Skill Guidelines

- Keep skills focused on a single concept
- Include practical workflows, not just theory
- Add tables for quick reference
- Provide specific parameters (percentages, pip values, etc.)

---

## 🔗 Related Links

- **Embient Platform**: [embient.ai](https://embient.ai)
- **More Skills**: Browse the full marketplace at [embient.ai/marketplace](https://embient.ai/marketplace)
- **Documentation**: [docs.embient.ai](https://docs.embient.ai)

---

## 📄 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

These skills are for educational purposes only. Trading involves substantial risk of loss. Past performance is not indicative of future results. Always do your own research and consider consulting a financial advisor before trading.

---

<p align="center">
  <a href="https://embient.ai">
    <strong>🚀 Discover more skills at Embient.ai</strong>
  </a>
</p>
