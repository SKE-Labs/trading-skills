# Trading Skills Specification

Trading skills are structured knowledge modules that teach AI agents how to analyze markets, identify trading setups, manage risk, and generate actionable insights.

## Skill Structure

Each skill lives in its own folder with a `SKILL.md` file:

```
skills/
└── category-name/
    └── skill-name/
        ├── SKILL.md           # Required
        ├── scripts/           # Optional: executable scripts
        ├── references/        # Optional: detailed docs
        └── assets/            # Optional: templates, images
```

## Required Fields

Every `SKILL.md` must include YAML frontmatter with:

| Field         | Description                                                        |
| ------------- | ------------------------------------------------------------------ |
| `name`        | Unique identifier (lowercase, hyphens for spaces)                  |
| `description` | Complete description of what the skill does and **when to use it** |

### Description Best Practices

The `description` field should clearly state:

1. **What** the skill does
2. **When** Claude should use it (trigger conditions)

**Good example:**

```yaml
description: Identify bullish and bearish order blocks where institutional orders were executed. Use when analyzing price action for high-probability entry zones, detecting smart money accumulation/distribution, or finding areas where price may react on retest.
```

**Weak example:**

```yaml
description: A skill for order blocks trading.
```

## Recommended Sections

Trading skills should include these sections:

| Section             | Purpose                                        |
| ------------------- | ---------------------------------------------- |
| **Identification**  | How to identify the pattern or setup           |
| **Entry Strategy**  | Step-by-step entry workflow                    |
| **Risk Management** | Stop loss, position sizing, and target rules   |
| **Workflow**        | Integration with tools (e.g., `draw_on_chart`) |
| **Best Practices**  | Do's and don'ts, common mistakes               |

## Formatting Guidelines

- Use **tables** for quick reference (levels, parameters, rules)
- Use **code blocks** for formulas
- Keep instructions **actionable**, not just theoretical
- Include **specific parameters** (percentages, pip values, ratios)

## Tool References

Skills may reference trading tools. Use consistent naming:

| Tool                      | Purpose                            |
| ------------------------- | ---------------------------------- |
| `draw_on_chart`           | Draw zones, levels, patterns       |
| `get_candles_around_date` | Retrieve historical candle data    |
| `calculate_position_size` | Calculate risk-based position size |
