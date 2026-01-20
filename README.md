# 📈 Agent Trading Skills

A curated collection of **50 trading skills** designed for AI agents. Built for [Embient.ai](https://embient.ai), but compatible with any agent that supports skills—including **Claude Code**, **Antigravity**, **Cursor**, and more.

[![Apache 2.0 License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-50-green.svg)](#skill-categories)
[![Embient](https://img.shields.io/badge/platform-Embient.ai-purple.svg)](https://embient.ai)

---

## About This Repository

Trading skills are structured knowledge modules that teach AI agents how to:

- **Analyze** charts using technical and fundamental analysis
- **Identify** patterns, setups, and trading opportunities
- **Calculate** position sizes and manage risk
- **Generate** trading signals with proper entry/exit strategies

Each skill is a standalone markdown file with clear instructions, formulas, and workflows. Browse through these skills to get inspiration for your own or to integrate them into your trading AI.

---

## Skill Sets

| Directory                  | Description                           |
| -------------------------- | ------------------------------------- |
| [**./skills**](skills)     | 50 trading skills across 7 categories |
| [**./spec**](spec)         | The Trading Skills specification      |
| [**./template**](template) | Skill template for contributors       |

### Skill Categories

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

## Quick Start

### Using with Embient.ai

1. Visit [embient.ai](https://embient.ai)
2. Browse the Skills Marketplace
3. Fork skills to your profile
4. Your AI trading assistant will use them automatically

### Using with Other AI Agents

| Agent            | Setup                              |
| ---------------- | ---------------------------------- |
| **Claude Code**  | Add to `.claude/skills/` directory |
| **Antigravity**  | Add to `.agent/skills/` directory  |
| **Cursor**       | Add to `.cursor/skills/` directory |
| **Other agents** | Point to the `skills/` folder      |

```bash
git clone https://github.com/ske-labs/trading-skills.git
cp -r trading-skills/skills/* .agent/skills/
```

---

## Creating a Trading Skill

Skills are simple to create—just a folder with a `SKILL.md` file:

```yaml
---
name: my-skill-name
description: A clear description of what this skill does and when to use it.
---

# My Skill Name

[Add your instructions here]

## Identification
How to identify the setup

## Entry Strategy
Step-by-step workflow

## Risk Management
Stop loss and sizing rules
```

The frontmatter requires only two fields:

| Field         | Description                                                     |
| ------------- | --------------------------------------------------------------- |
| `name`        | Unique identifier (lowercase, hyphens for spaces)               |
| `description` | What the skill does **and when to use it** (trigger conditions) |

Use the [template](template/SKILL.md) as a starting point. See the [spec](spec/README.md) for detailed guidelines.

---

## Contributing

We welcome contributions! To add a new skill:

1. **Fork** this repository
2. **Create** a new folder under the appropriate category
3. **Copy** [template/SKILL.md](template/SKILL.md) and fill in your content
4. **Submit** a pull request

### Skill Guidelines

- Keep skills focused on a single concept
- Include practical workflows, not just theory
- Add tables for quick reference (levels, parameters)
- Provide specific values (percentages, pip values, ratios)

---

## Related Links

- **Embient Platform**: [embient.ai](https://embient.ai)
- **Skills Marketplace**: [embient.ai/marketplace](https://embient.ai/marketplace)
- **Documentation**: [docs.embient.ai](https://docs.embient.ai)

---

## Disclaimer

These skills are provided for demonstration and educational purposes only. Trading involves substantial risk of loss. Past performance is not indicative of future results. Always do your own research and consider consulting a financial advisor before trading.

---

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <a href="https://embient.ai">
    <strong>🚀 Discover more skills at Embient.ai</strong>
  </a>
</p>
