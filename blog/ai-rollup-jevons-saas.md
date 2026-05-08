# Nine Lines. Thirty-Five Points. One Trap.
### The AI math that every SaaS investor and operator needs to run right now.

---

"Inference got a hundred times cheaper this year. The compute bill went up anyway."

That's from the inference team at Nebius, who run open-source managed inference at scale. They called it the most important thing happening in AI right now.

They're right. And if you run or invest in a SaaS business, those two sentences also describe the single biggest risk hiding inside the most attractive trade of the current cycle.

Here's the trade. And here's the trap.

---

## The Nine Lines

A standard mid-market SaaS company at $100M revenue looks something like this:

**Cost of Revenue (COGS):**
| Line | Cost | % of Revenue |
|------|------|:---:|
| Hosting / Infrastructure | $10M | 10% |
| Customer Success / Support | $15M | 15% |
| Professional Services | $7M | 7% |
| Third-Party Data & Licenses | $3M | 3% |
| Capitalized Software Amortization | $2M | 2% |
| **Gross Profit** | **$63M** | **63%** |

**Operating Expenses:**
| Line | Cost | % of Revenue |
|------|------|:---:|
| Field Sales (AEs, Sales Engineers) | $16M | 16% |
| SDR / Outbound | $5M | 5% |
| Paid Marketing / Demand Gen | $10M | 10% |
| Partnerships / Channels | $4M | 4% |
| R&D / Engineering | $15M | 15% |
| G&A | $8M | 8% |
| **EBIT** | **$5M** | **5%** |

Five percent EBIT. That's the median. That's not a failing company — that's the industry.

AI restructures every line. Eight of those nine lines go down. One goes up if you're not paying attention.

---

## The Real Money: Lines 2 and 3

Customer Success is the biggest target in the P&L. It's also the most visible proof point that this isn't theoretical.

Klarna deployed an AI agent across their customer service operation. It now handles two-thirds of all support conversations — the equivalent of 700 full-time agents. Resolution time dropped from 11 minutes to 2.

That's not a pilot. That's a restructured cost line.

The same dynamic is playing out at Intercom, Zendesk, and Salesforce Agentforce — AI agents handling L1 and L2 support, automated onboarding flows, AI-generated QBR summaries, health scoring driven by product telemetry rather than CSM intuition.

**On a $15M Customer Success line, 60% automation frees $9M.** That's 9 points of gross margin. On its own, it would move a 63% GM business to 72%.

Professional Services is the quieter version of the same trade. Implementation teams charging $7M in COGS, often at near-breakeven margins — because getting customers live requires consultants who walk them through setup, data migration, and configuration. AI compresses that work.

A data migration that took a two-week sprint now takes two days. Standard implementations that required a dedicated PS manager now run through an AI-guided configuration flow. Some operators are going further: repositioning AI-accelerated onboarding as a *premium product tier* rather than a cost centre — converting a COGS line into a revenue line at 60%+ margins.

Combined, Lines 2 and 3 represent 12 points of potential gross margin improvement. That's the core of the roll-up thesis.

---

## The Second Tranche: Lines 7 and 8

The CS/PS opportunity is well-understood now. Less discussed: the Sales & Marketing stack.

**SDRs first.** The Sales Development Rep function is largely mechanical. Find ICP accounts. Identify the right contact. Write a relevant message. Follow up. Book a meeting. Hand off. Every one of those steps is now AI-executable — Clay for account identification and signal aggregation, AI personalization engines for outreach at scale, automated dialers for qualification calls.

Companies running these tools are reporting 40–60% SDR headcount reductions for the same pipeline volume. Or, choosing not to cut headcount and instead running the same team at 2–3× output. On a $5M SDR line, that's $2–3M back into the P&L. Three more points of EBIT.

**Content and demand generation next.** The marketing line has a sub-structure worth examining:

- Content production (blog posts, whitepapers, case studies, event decks): AI-generated at 10% of the previous production cost, with human editing maintaining quality
- Paid search and social: Google PMAX and Meta Advantage+ AI optimization consistently deliver 15–25% better CAC on the same budget
- Marketing analytics and attribution: AI-automated reporting replaces what was a 2–3 person analyst function

Events and field marketing — the relationship-building layer — are harder to automate. Don't cut those. The trap here is the same as it was for CS: operators who chase short-term EBIT by cutting brand presence pay for it 6–12 months later when pipeline dries up.

**The field sales team** — the AEs and Solutions Engineers — stays mostly intact. Enterprise deals close on trust and political navigation. What AI does is make those people more effective: RFP responses that took three days take four hours, pre-call research that took two hours takes fifteen minutes, forecast accuracy improves through AI-scored pipeline signals. Same headcount, more output, lower sales cycle drag. This is leverage, not replacement.

**Add Lines 7 and 8 to Lines 2 and 3, and you have a path from 5% EBIT to 35–40% EBIT at flat revenue.**

---

## The Trap: Line 1

This is where most operators get the math wrong.

The assumption is: AI infrastructure is more efficient → hosting costs go down. The Nebius team's insight is that the opposite happens. Not because efficiency didn't improve — it improved 100-fold. But because we built a generation of products that use the efficiency so aggressively that total consumption explodes.

**The token arithmetic:**
- A single-shot API call: ~2,000 tokens. Cost: fractions of a cent.
- A reasoning model working through a complex CS issue: ~200,000 tokens. It thinks out loud before answering.
- An agentic workflow that loops, calls tools, retries, and synthesizes: ~20 chained requests per task.
- A full onboarding session (the thing replacing your PS consultants): potentially millions of tokens.

You replaced a CSM handling 40 tickets a day with an AI agent that burns 200,000 tokens per ticket. Your CS headcount cost dropped $9M. Your compute bill went up.

By how much depends entirely on what you do about it.

---

## Naive vs. Expert

**The naive operator** routes everything through OpenAI or Anthropic APIs. No inference engineering. Pay per token, whatever the price.

On a $100M revenue business automating CS fully with API calls, the infrastructure line doesn't go from $10M to $8M. It goes from $10M to $14M.

That's still a net win — $9M CS savings minus $4M additional compute = $5M improvement. But you've captured 56% of the opportunity and left 44% on the table.

**The expert operator** treats the inference stack as a product capability, not a vendor relationship:
- Open-source models (Llama, Mistral) on reserved compute, not pay-per-token
- KV cache sharing across similar sessions — if 200 customers with the same product are asking similar onboarding questions, they share cached context
- Complexity routing — simple FAQ queries go to a cheap small model, complex troubleshooting routes to a frontier model
- Quantization — running models at INT8 precision cuts inference cost 3–4× with minimal quality loss

On the same $100M business, the expert operator's infrastructure line goes from $10M to $10.8M. CS savings of $9M. Net improvement: $8.2M.

**The delta between naive and expert execution: $3.2M per year on a $100M company.**

Across a PE portfolio of 10 acquired companies at $1B combined revenue: $32M per year in EBIT. At 15× EBIT, that gap in execution skill is worth $480M in equity value. On the same acquisitions, at the same purchase prices.

This is the capability that separates roll-up operators who are running a financial engineering strategy from those who are building a structural cost advantage.

---

## What the Math Looks Like When You Put It Together

| Line | Pre-AI | Post-AI (Expert) | Change |
|------|--------|-----------------|--------|
| Hosting / Inference | $10M / 10% | $10.8M / 10.8% | +0.8pp |
| Customer Success | $15M / 15% | $5M / 5% | −10pp |
| Professional Services | $7M / 7% | $3M / 3% | −4pp |
| Data / Licenses | $3M / 3% | $1.5M / 1.5% | −1.5pp |
| **Gross Profit** | **$63M / 63%** | **$79.7M / 79.7%** | **+16.7pp** |
| Field Sales | $16M / 16% | $13M / 13% | −3pp |
| SDRs | $5M / 5% | $2M / 2% | −3pp |
| Marketing | $10M / 10% | $6.5M / 6.5% | −3.5pp |
| Partnerships | $4M / 4% | $2.5M / 2.5% | −1.5pp |
| R&D | $15M / 15% | $9M / 9% | −6pp |
| G&A | $8M / 8% | $4.5M / 4.5% | −3.5pp |
| **EBIT** | **$5M / 5%** | **$42.2M / 42%** | **+37pp** |

Thirty-seven points of EBIT improvement at flat revenue. No product changes. No price increases. No market expansion. Just restructuring the cost of delivering the software you already sell.

The 5% company becomes the 40% company. That's the re-rating. At 6× revenue, you've gone from $300M to $600M in enterprise value — without growing revenue by a single dollar.

That's the trade. The trap is assuming Line 1 behaves like the other eight.

---

## The Honest Take

**If you're a PE operator running a SaaS roll-up:** The difference between a 30% EBIT portfolio and a 42% EBIT portfolio is almost entirely whether you built inference engineering capability before you started acquiring. Generic LLM API wrappers are not a strategy. Open-source model deployment, KV cache management, and complexity routing are the operational capabilities that determine whether the Jevons bill eats your CS savings or your CS savings flow through to the P&L.

The companies already doing this well: Nebius (NBIS) built the optimization stack as their core product. The SaaS operators who partner with or learn from that layer will outperform those who don't.

**If you're a SaaS CEO or founder:** The CS and PS lines are the first thing to address — the ROI case is clear and the evidence base (Klarna, Intercom Fin, Salesforce Agentforce) is validated. But before you sign the contracts, run the token arithmetic. Map your actual agent workloads — average session length, tool call depth, concurrent sessions — and model what the compute bill looks like at 70% automation. If it's routed entirely through a closed API, you'll have a new budget conversation with your CFO in Q3.

The repricing question is equally urgent. If you're charging per-seat while running per-token AI underneath, your margin is a function of customer usage — and you want customers using it more. Consumption pricing or outcome-based pricing aligns incentives. Seat pricing is a slow bleed.

**If you're an investor evaluating a SaaS roll-up:** Ask for the infrastructure line projection. If it's flat or down, the operator hasn't thought through the Jevons dynamic. If it's up but they can explain exactly why (model mix, KV cache volume, complexity routing assumptions), you're talking to someone who understands the real cost structure.

The trade is real. The numbers are large. The trap is specific and avoidable.

Same coal as 1865.

---

*Sources: Nebius inference team (Jevons Paradox analysis, 2026); Klarna AI customer service deployment data (2024); Charlie investment analysis framework (v20). Inference economics sourced from live production data; SaaS P&L benchmarks from mid-market composite analysis.*

*Tags: `#saas-economics` `#ai-rollup` `#gross-margin` `#inference-costs` `#jevons-paradox` `#pe-saas`*
