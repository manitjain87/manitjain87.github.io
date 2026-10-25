---
title: "Ninety-Six Cents"
subtitle: "Everyone is arguing about the AI capex number. The cash flow statement already settled it."
date: 2026-10-12
tags: ["#capital-allocation", "#2027-inflection", "#consumption-economics"]
series: "Ninety-Six Cents"
part: One of four — Where the money went
---

# Ninety-Six Cents

On Microsoft's 29 July earnings call, Gabriela Borges of Goldman Sachs asked Amy Hood a direct question: when you track the ROI on the capex decisions you are making today, how does it compare with a year ago?

Hood's answer: *"I don't know that, quite frankly, my math has changed in terms of how I do it over the past year."* Then she moved to TAM confidence and margin levers — silicon, model diversification, infrastructure efficiency.

No number. No payback period. No framework.

Across Microsoft, Alphabet, Amazon and Meta, capital expenditure absorbed **96 cents of every dollar those four generated from operations** in the June quarter.

That is the post. The capex debate is being argued on the wrong line of the P&L.

*This is the first of four parts. **Part One** is where the money went: ten companies along one chain, what each actually spent, and which of them can afford to be early. **[Part Two](ninety-six-cents-part-two.html)** is whether whoever took that money keeps it. **[Part Three](ninety-six-cents-part-three.html)** is what survives if it does not. **[Part Four](ninety-six-cents-part-four.html)** is who holds the credit risk, and whether you can see it.*

*A note on sourcing. Part One rests on the companies' own transcripts, releases and 8-K exhibits: 71 claims, each put through three independent checks against the primary documents — 213 checks. Where a number is management's, I quote it; where it is my arithmetic on their disclosed line items, I say so. Micron and Samsung are issuer-disclosed and inside the window but were added after the 71-claim gate ran, so they did not pass through it; Micron's contractual figures come from the 10-K filed on 9 October and Samsung's from its own quarterly releases.*

---

**PART ONE — Where the money went**

---

## What ten companies said, and where they said it

Ten companies along one value chain reported between 22 July and 30 September: the two memory makers who are the actual bottleneck (Micron, Samsung), the seller of the compute (NVIDIA), the four buyers who own their own infrastructure (Microsoft, Alphabet, Amazon, Meta), two independent AI clouds that are the highest-rated in the industry and the most heavily financed (CoreWeave, Nebius), and the fuel-cell maker whose product exists to shorten time-to-power (Bloom Energy).

Read in that order it is a chain: memory, to GPUs, to the clouds that run them, to the electricity and the wait to be connected to it. Each tier's constraint becomes the next tier's cost — and this season you can watch that happen inside a single company's accounts.

On demand versus supply they were unanimous. Not one forecast supply catching up.

| Company | What they said | Where |
|---|---|---|
| **Microsoft** — Amy Hood, CFO | *"demand exceeds available supply in a sort of relatively extreme moment"* | **Q&A**, to Bernstein |
| **Alphabet** — Anat Ashkenazi, CFO | *"we're still in a supply-constrained environment… the demand still outpaces that investment"* | **Q&A**, to Morgan Stanley |
| **Amazon** — Andy Jassy, CEO | *"we will still not have enough capacity to meet all the demand we have in 2026, and I believe this dynamic will also be true in 2027, too"* | Prepared remarks |
| **Meta** — Susan Li, CFO | *"we are today, and expect to be in the sort of foreseeable future, supply constrained"* | **Q&A** |

Note the right-hand column. Three of those four are CFOs, and all three CFO statements came in Q&A — not in the scripted section where the lawyers have been. The one prepared-remarks statement is a CEO's.

When a CFO volunteers "extreme moment" live and unscripted, that is not marketing copy.

Two things said this season are harder to spin than adjectives. Mark Zuckerberg, in prepared remarks: Meta is *"getting a lot of offers for compute at a significant premium over what we paid for it"* — and in Q&A, *"there's just nowhere near enough compute for all the demand."* Meta is declining to sell, because *"it would be foolish to basically just sell all of the compute and take a short-term profit."*

Meanwhile Alphabet is renting from other people. Ashkenazi, in *prepared* remarks: given the supply constraint, Alphabet will *"expand the use of third-party capacity in Q3 as a bridging strategy,"* accepting *"modest margin pressure in the near-term."*

Alphabet designs its own silicon, owns its own data centres, and raised $49.6 billion of equity in June. It is still going outside for capacity and paying a margin price to do it.

The operating results underneath are genuinely strong. Alphabet's cloud revenue grew **82% to $24.8 billion**, with operating margin expanding from **20.7% to 35.6%** — more than tripling operating income. Microsoft said Azure passed **$100 billion** of annual revenue for the first time, up 41%. AWS grew **36.7%**, its fifth consecutive quarter of acceleration and fastest in 18 quarters.

---

## Ground Reality: not everyone raised capex

This is the most misreported fact of the season, and it matters if you are modelling your own vendors.

| Company | 2026 capex | What changed | Stated cause |
|---|---|---|---|
| **Amazon** | ~$220B cash capex | **Raised** from ~$200B | *"The higher cost of memory pushing this number up"* |
| **Alphabet** | $195–205B | **Raised** from $180–190B | *"acceleration in the delivery of capacity to meet growing demand"* |
| **Meta** | $130–145B incl. finance-lease principal | **Narrowed** from $125–145B — low end lifted, **top end unchanged** | not attributed to demand |
| **Microsoft** | ~$175B CY2026 | **Reporting change** | finance→operating lease reclassification |

Two raised. One narrowed. One restated for an accounting reason.

Microsoft's ~$175 billion needs care, because it is the number most likely to be misquoted. Hood: *"Outside of this useful life impact, our calendar year 2026 CapEx investment expectations remain unchanged. However, the shift from finance to operating leases adjusts our expectation to approximately $175 billion."* Operating leases sit outside capex; finance leases sit inside it. The figure moved because of where leases are booked — not because Microsoft changed its mind about how much compute to buy.

And the two genuine raises are not the same event. Alphabet's is **volume** — more capacity, delivered faster. Amazon's is **price** — the same plan costing more because memory got expensive. Same arrow, opposite economics. One is demand strength; the other is cost inflation eating the identical plan.

I won't add those four numbers together. They are stated on four different bases — cash capex, capex including finance-lease principal, and a calendar figure that now *excludes* operating leases. You will see a single trillion-dollar hyperscaler capex figure quoted this quarter. It is arithmetic without meaning.

---

## Ninety-six cents, line by line

Guidance is a plan. The cash flow statement is the outcome, and it is where this season actually resolves.

Every input below is a disclosed line item from the same three months ended 30 June. The totals and percentages are my arithmetic, shown so you can redo them.

| Company | Operating cash flow | Cash invested (capex) | Free cash flow | Capex % of OCF |
|---|---:|---:|---:|---:|
| Microsoft (FQ4 FY26) | $55,441M | $35,802M | **$19,639M** | 64.6% |
| Alphabet (Q2 26) | $39,069M | $44,924M | **$(5,855)M** | 115.0% |
| Amazon (Q2 26) | $45,387M | $53,076M | **$(7,689)M** | 116.9% |
| Meta (Q2 26) | $31,862M | $31,078M | **$784M** | 97.5% |
| **Combined** | **$171,759M** | **$164,880M** | **$6,879M** | **96.0%** |

$171.8 billion of operating cash went in. $6.9 billion of free cash flow came out.

Spending more than you generate is a statement about funding, and three of these four became net raisers of capital in the first half of 2026 while the fourth funded its build through leases instead. [Part Four](ninety-six-cents-part-four.html) works through what each of them issued.

Three of the four reconcile exactly to the company's own reported free cash flow. The exception is Amazon, and the reason is structural: Amazon publishes free cash flow **only on a trailing-twelve-month basis**, so its reported −$7,604M is a TTM figure and the −$7,689M above is my arithmetic on its quarterly line items. Anyone quoting "Amazon's free cash flow was minus $7.6 billion this quarter" has put a TTM number in a quarterly sentence. Recomputed on a stricter basis — gross purchases of property and equipment only, no finance-lease principal, no netting of proceeds — the combined figure is $6,709M, or 96.1%. The conclusion does not depend on which basis you pick.

The aggregate hides the part that matters. Microsoft is still converting about a third of operating cash into free cash flow. Meta is at breakeven — $784 million, from a company guiding to $130–145 billion of capex this year. **Alphabet and Amazon each spent more on capital expenditure than their operations produced in the quarter.**

Strip out Microsoft and the other three together produced free cash flow of **negative $12,760M**.

Now put the seller on the same page. NVIDIA reported fiscal Q2 2027 on 26 August: revenue $96.2 billion, up 106%; Data Center revenue $89.0 billion, up 117%; gross margin 75.0%.

| | Operating cash flow | Cash invested | Free cash flow | Capex % of OCF |
|---|---:|---:|---:|---:|
| **Micron (FQ4 FY26)** | $43,973M | $11,110M | **$32,863M** | **25.3%** |
| **NVIDIA (FQ2 FY27)** | $24,077M | $2,677M | **$21,341M** | **11.1%** |
| *Four hyperscalers combined* | *$171,759M* | *$164,880M* | *$6,879M* | *96.0%* |

The component supplier at the top of the chain spent 25 cents of each operating dollar on its own capital base. The seller of the compute spent 11. The buyers spent 96.

Two notes on that table. Micron's quarter is not the same quarter — its FQ4 ended 3 September and ran 14 weeks — so read it as position in the chain, not as a like-for-like period. And Micron's figure is gross expenditures for property, plant and equipment; on the net basis Micron itself reports, after $327M of government incentives, capex was $10,774M and free cash flow $33,199M, or 24.5% of operating cash flow. The ranking does not move.

Jensen Huang's framing of why that holds is the entire bull case in six words: *"It's doing useful work. Its tokens are productive and profitable. Now, compute is revenue."*

One caution on NVIDIA's own quarter, because it is not in the headline growth rates. Net income was $59,688M; operating cash flow was only $24,077M. The gap is working capital — accounts receivable moved **$22,346M** against the company and inventories a further **$5,784M** in a single quarter. Revenue is being recognised considerably faster than cash is collected, from customers who are themselves borrowing to pay.

**What this bridge is not.** It shows how cash was allocated. It is not a counterfactual, and it cannot be read as what these companies would earn without AI — operating cash flow already contains the depreciation add-back on prior capex, and without this spending there is no Azure, no AWS and no Google Cloud, so much of the $171.8 billion would not exist either. Nor is $164.9 billion purely data-centre spend: none of the four discloses a data-centre-only capex line.

---

## The constraint has a name, and it is not power

If you take one operational fact from this season, take this one. The binding *cost* constraint is memory.

Amazon raised its 2026 capex expectation for that reason and said so plainly. Jassy: *"We now believe we will spend approximately $220 billion in cash CapEx in 2026. The higher cost of memory pushing this number up from our prior estimate of about $200 billion."* In Q&A he was blunter: *"there are inflated prices right now on some of the components like memory and hard drives and SSDs."*

Microsoft attributed part of its $41 billion quarter to *"the impact from higher component pricing as noted in our guide."*

This was foreseeable. Sundar Pichai said on the Cheeky Pint podcast that memory is *"one of the most critical components now."* Three of this season's prints then moved because of it.

**Ground Reality for a CFO:** this is the part that reaches your P&L. You are not buying GPUs. You are buying cloud capacity and AI vendor licences from companies whose input costs just went up, two of whom are now spending more than they earn from operations. That cost has one place to go.

Power still binds, but the binding variable is not generation — it is **time**. A datacentre that cannot get a grid connection cannot serve a token, however many GPUs are inside it, and interconnection queues now run years. That is what Bloom sells against: behind-the-meter fuel cells energise a site without waiting in that queue. Revenue was $1.065 billion, up 166%, its first billion-dollar quarter, with full-year guidance raised to $3.9–4.2 billion. More telling than the number: a named customer, Nebius, **cancelled combustion-turbine orders and switched to on-site fuel cells** — and Nebius's own shareholder letter confirms the other side of it, a long-term Bloom partnership announced in May.

Read Bloom as a clock, not a utility: its order book measures how many operators decided that waiting for the grid costs more than generating on site.

Two independent issuers, both sides of the same transaction. That is what a binding lead time looks like when it changes someone's generation technology.

### The suppliers' side, and it is worse than the buyers let on

Micron reported fiscal Q4 on 30 September, after every other print in this post, and it settles the question of whether memory was a one-quarter squeeze. It is the top of the chain: its output is the cost line inside everyone else's capex.

It was not. FQ4 revenue was **$54.2 billion, up 379% year-over-year**, at an **86.8% gross margin** against 44.7% a year earlier. The composition matters more than the growth: DRAM revenue rose 27% sequentially on **bit shipments up only mid-single digits** — because **prices rose high-teens percent**. NAND bits rose ~10% while **prices rose ~30%**.

That is a price event, not a volume event. And it is the input cost sitting inside Amazon's $220 billion.

**Samsung is the better witness — bigger, and inside the window.** On 30 July it posted **revenue of KRW 171.5 trillion and operating profit of KRW 89.5 trillion** — both all-time highs — of which the Device Solutions semiconductor division was **KRW 127.5 trillion of revenue and KRW 89.2 trillion of operating profit.** Chips were essentially the entire company's profit. Memory ASPs rose **mid-40% sequentially for DRAM and high-60% for NAND**, against Micron's high-teens — the same event, further along.

**And here is the line that settles it.** In the same release, Samsung's own phone division — MX and Networks — posted an **operating loss of KRW 0.7 trillion**, which Samsung attributes to *"elevated component cost pressures across the industry."* The company extracting the most profit in history from the memory shortage is simultaneously losing money downstream because of it. "Each tier's constraint becomes the next tier's cost" is not a framework here. It is two lines of the same P&L.

On duration Samsung is more specific than Micron. Jaejune Kim, who runs the memory business, said the shortage will persist **through 2028** and that constraints will be **"even more severe in 2027 than 2026"** — because new fab lead times exceed **three years**, so no meaningful incremental supply can arrive before then. Samsung's own written outlook is the same: the market is *"projected to keep the market undersupplied"* and *"despite efforts to increase production, supply constraints are expected to continue."*

**One post-window number, because it changes the shape, not the direction.** On 8 October — after this window closed — Samsung pre-announced third-quarter operating profit of **KRW 107.4 trillion, about $80 billion**, on revenue of roughly **KRW 195 trillion**: up 782% year on year, the first Korean company ever to clear KRW 100 trillion in a quarter, at a ~55% operating margin. These are preliminary figures with no divisional breakdown; full results come on 29 October.

Now the sequence, not the record. Samsung's operating profit ran **KRW 20.1 trillion → 57.2 → 89.5 → 107.4** across four consecutive record quarters — sequential gains of roughly **+184%, +56%, +20%.** Four records in a row, each one smaller than the last. Micron's own guidance says the same thing in words: price increases are expected to *"moderate."* [Part Two](ninety-six-cents-part-two.html) shows the identical curve at the other end of the chain, in Anthropic's revenue. The level is still extraordinary. The second derivative turned some time ago.

Micron expects supply-demand to be *"much tighter in fiscal 2027 and 2028 than they were in 2026."* Sanjay Mehrotra: *"we do not have a line of sight to when supply and demand will get in balance."* On the call, management said more than **75% of fiscal 2027 output is already committed** — a call figure, not a filed one.

**The mechanism is the part worth stealing.** Micron's Strategic Customer Agreements are **take-or-pay** contracts with, in the company's own words, *"binding commitments for specific contractually enforceable volumes."* The 10-K it filed on 9 October puts the remaining performance obligations at **approximately $134 billion**. A year earlier they were *"not material."* Non-current customer contract liabilities went from **$142 million to $12,895 million** across that same year, and **$12.75 billion of customer deposits arrived as a financing inflow** in fiscal 2026.

Two details most coverage drops, both from the filing. The deposits are not revenue and not permanent capital — *"nearly all of the deposits are scheduled to be repaid between 2029 and 2031."* And the $134 billion is Micron's floor, not its forecast: it is *"based on expected purchases to satisfy committed volumes and minimum pricing,"* agreements without fixed pricing or price bands are excluded from it, and Micron states plainly it is *"not expected to be indicative of future revenue."* About a quarter of it is expected to land as revenue in the next twelve months.

Buyers are now pre-funding their own supply, two to five years out, in cash. That is the same structure as Nebius's prepayments one layer up — and it is the clearest signal in this entire chain that the people closest to the constraint do not expect it to clear.

**The counter-argument runs through the buyers' engineering, not the sellers' capacity.** Scarcity per wafer is not the same as scarcity per system. SemiAnalysis argued in September that accelerator HBM is moving from 12-high to 8-high as the standard, and that frontier labs would prefer **4-high for inference** — because bandwidth per stack is the same at any height, HBM is priced per gigabyte, and shorter stacks yield more stacks from the same scarce DRAM wafer. The cost comparison bites: **12-high costs about 26% more per system than 4-high for roughly 10% more throughput.** If the buyers standardise downward, effective supply rises without a single new fab, and the three-year lead time stops being the binding number. Micron's own bear case lists exactly this — "HBM content per accelerator falling" — among the things that break its thesis. That is third-party analysis, not an issuer disclosure — and the strongest case against the section you have just read.

**And it is not a Micron innovation.** Samsung said on the same call that it has signed **five-year rolling supply agreements with top-five datacentre customers**, is in final talks with five more, and is targeting **60–70% of its total DRAM and NAND capacity under long-term contract** with minimum price floors and substantial advance payments — of which it has already received about a quarter. Two of the three producers are re-contracting the same way in the same quarter. That is not one company locking in a good year. It is an industry converting a commodity cycle into a backlog — Samsung's stated aim. Whether it works is the open question. That it is happening is now disclosed by both.

Two honest caveats. The price bands are now issuer-disclosed, not inferred: the 10-K says the majority of the agreements carry *"pricing that is subject to minimum and maximum bands"* — a **ceiling** as well as a floor, so heavier contract coverage caps Micron's own upside. (The separate claim that the ceiling sits near Q2-2026 market prices is third-party, not Micron's.) Micron's answer to that is the boldest sentence in the filing: it expects those agreements, *"even at floor pricing levels, to yield gross margins meaningfully above our peak quarterly margins in any past cycle."* That is a striking thing to commit to in a 10-K, and it has not been tested through a price decline. The same filing lists the other side of the trade: the agreements *"could constrain our available supply and limit our flexibility to respond to changes in market conditions."* And fiscal 2026 was a 53-week year with the extra week landing in FQ4, so the sequential comparison flatters slightly.

Model layer solved. Chip layer expensive. Memory layer inflationary — and now contractually locked out to 2031. Power layer physical. Permitting layer political.

---

## Two companies showed their arithmetic. Neither was Microsoft.

Return to Hood's non-answer, because the asymmetry is the finding.

**Amazon published a break-even framework.** Jassy split the investment into two capital cycles. Data centres: capital spent starting *two years* before servers go in, then monetised for *"30+ years,"* expected to yield *"at least five to six generations of server economics."* Servers and networking: bought months before service, and *"on average, it takes a little less than three years to break even on that investment"* — against servers with *"a useful life of at least five to six years,"* with *"most of our AI capacity these days… contracted for at least five-year terms."*

Accept the assumptions or not, that is a falsifiable structure: a three-year payback against a five-to-six-year asset backed by five-year contracts. It can be checked later.

**Nebius published the other one.** Expected payback on deals closed in Q2: **1 year 10 months**, down from a historical two-to-three-year range.

Here is the part most write-ups will miss. Those two numbers are not comparable.

Roughly **70% of Nebius's Q2 deals carried customer prepayments covering 50–60% of the associated capex** — an all-time high for them. The payback compresses arithmetically, because the customer funds half the asset before it is built.

Amazon's is self-funded. So the faster number is partly a financing structure, not purely better economics — and it transfers risk to the customer rather than creating operating efficiency.

Alphabet answered an ROIC question qualitatively — Pichai: *"if anything, over the past year, we have gotten more bullish on the opportunities ahead."* Meta pointed at *"numerous ROI positive places that we would put compute toward if we had it"* without disclosing a hurdle.

So: of six companies buying or reselling compute at scale, **two published payback math — and they are the two with the least room to be wrong.** The best-capitalised did not. That is the reverse of what you would expect, and not an accident. A three-year payback is a promise you can be held to. If your balance sheet can absorb being wrong, you don't make the promise.

---

## What the depreciation fight is actually about

Extending the depreciable life of an asset reduces the annual charge and flatters margins, so any change deserves scrutiny. Here is what actually happened, because this is the easiest thing in the season to get wrong.

**Microsoft extended the life of *buildings*, not servers.** Hood: effective at the start of FY2027, Microsoft is extending the estimated useful life of *"our data centers and office buildings from 15[to] 25 years."* Shells and offices. Servers sit on a separate, much shorter schedule. Hood also pre-empted the margin reading: the change *"affects only the timing of future depreciation and is expected to have a minimal benefit to FY 2027 operating income."*

Alphabet and Meta changed nothing. Amazon disclosed 5–6 year server lives and left them alone — while noting a track record of extending equipment life.

So the claim that the hyperscalers stretched server lives this season to flatter margins is **false**. The only server-life change in this value chain was at a neocloud: Nebius uses a five-year life for server and network equipment, up from four prior to 2026, on a company whose depreciation and amortisation runs at **45% of revenue** — $259.7 million against $582.3 million of revenue.

Which raises the real question — is the longer life justified? The best available evidence comes from a competitor, not from Nebius. CoreWeave: *"we remain largely sold out of prior generations of NVIDIA GPUs in addition to the current SKUs… we recently signed an **A100 contract that extends into 2029**. As a reminder, this SKU was introduced in **2020**."* Intrator added the pricing side on the same call: *"Pricing and margins for our Blackwell and Vera Rubin SKUs are setting new highs while pricing for prior generation SKUs is at or above where it was years ago."*

A nine-year commercial life on hardware the bear case assumes is obsolete in three or four. Nebius independently reported **more than 30% higher pricing on older-generation GPUs** versus Q1.

One contract is not a fleet, and CoreWeave has every reason to volunteer its most flattering example. But it is specific, dated and checkable — and the depreciation argument has largely been conducted without evidence of that kind on either side.

---

## The best operators are the most exposed

CoreWeave and Nebius are where the same demand shows up without a balance sheet to absorb it. The numbers are not subtle.

| | CoreWeave Q2 2026 | Nebius Q2 2026 |
|---|---|---|
| Revenue | $2,575M (+112%) | $582.3M (+454%) |
| Adjusted EBITDA | $1,510M (59% margin) | $236.2M (41%); AI cloud 49.7% |
| Adjusted operating income | **$128M (5% margin)** | — |
| GAAP operating income | **$(49)M — a loss** | — |
| Interest expense | **$640M** (vs $267M a year ago) | — |
| Q3 interest guidance | **$860–940M** | — |
| Net loss | $(626)M | — |
| Backlog / commitments | $104B (+246%), excl. >$25B added early Q3 | >$40B customer commitments |
| Contracted power | 3.7GW → 4.2GW at the call | 5GW target for year-end 2026 |
| FY2026 capex / revenue guidance | $35–39B / $12.4–13.2B | $20–25B / $3.0–3.4B |

CoreWeave's interest expense of $640M was roughly **five times** its $128M of adjusted operating income in the same quarter — and Q3 interest is guided higher again. That is the neocloud trade in one line: the demand is real, the pricing is improving, and the financing cost is several times the operating profit.

Look at the last row too. Both are guiding to capex that dwarfs revenue — CoreWeave roughly three times its own, Nebius roughly seven. The hyperscalers spend a fraction of theirs. These are not the same business model in different sizes.

Two cautions. CoreWeave's "$9.4 billion capex" for the quarter is management-defined and was never reconciled on the call to cash purchases of property and equipment. The cash flow statement says **$6,422 million** — a gap of roughly $3 billion, with construction in progress rising to **$11.9 billion from $9.6 billion**. Use the cash number beside the hyperscaler table; the management figure is not on that basis. And the widely-repeated claim that Microsoft is the vast majority of CoreWeave's backlog **is not sourced from that call**: the word "Microsoft" does not appear in the transcript.

**First, correct the lazy framing — I had it wrong too.** These two are not middlemen reselling someone else's capacity. In SemiAnalysis's ClusterMAX 3.0 review (September 2026), which tests compute, networking, storage, orchestration, support, pricing and security across 80-plus providers, **CoreWeave and Nebius are the only two in the Platinum tier.** Google Cloud and Oracle are a tier below in Gold, **Azure** two below in Silver, **AWS** three below in Bronze. On the benchmark buyers negotiate against, the two most financially exposed companies here run the best infrastructure in the industry, and every hyperscaler cloud is behind them.

They are moving up the stack, too. CoreWeave's managed-inference ARR went from **$1 million to more than $100 million** booked in the months since launch, guided to **at least $250 million exiting 2026**, alongside Weights & Biases, serverless reinforcement learning and its own orchestration layer. Nebius prices capacity by auction. That is a product business, not a landlord's.

How far to push that, honestly: ClusterMAX rates the cloud, not inference. SemiAnalysis is still testing serverless endpoints and was *disappointed* by CoreWeave's model coverage — it wanted Kimi K3 and GLM 5.3, which CoreWeave does not serve, though it serves the prior K2.6, K2.7 Code, GLM 5.2 and MiniMax M3. Best cloud is established. Best inference is not yet adjudicated.

**Which makes the balance sheet the interesting part, not a footnote.** One more number belongs next to the contracted-power row: the denominator. CoreWeave's **active** power was about **1.5GW against 3.7GW contracted** — roughly 41% — and it added some 500MW of active capacity in the quarter with **300MW of that in June alone**, so the revenue lands in later quarters. Nebius discloses no active figure at all. Contracted power is a claim on the future; active power is what can be billed this quarter.

How they fund it is the tell. Nebius entered its first secured debt financing in July — **$775 million at SOFR + 2.50%**, backed by deployed GPU infrastructure and contracted cash flows from an investment-grade customer — alongside roughly **$2.8 billion raised through an at-the-market equity programme** (12.7 million shares at a $223.6 weighted average) through 30 June. It expects **over $9 billion of customer prepayments in 2026**. Deployed GPUs are now collateral, and customers are now a funding source. And one layer up, the seller has started doing something adjacent: in the quarter to 26 July, NVIDIA disclosed for the first time **$36 billion** of commitments to buy capacity from AI clouds it does not name — capacity those clouds stay free to sell to anyone who pays more. [Part Three](ninety-six-cents-part-three.html) has the terms.

**And then, two weeks after the print, it raised far more than either.** On 24 August Nebius closed **$5.75 billion** of convertible senior notes — **$3.45 billion at 0.50% due 2030 and $2.3 billion at 4.50% due 2034** — after the initial purchasers took their full options. In the same transaction it exchanged **$400 million of its 2029 notes and $400 million of its 2031 notes for about 15.8 million shares**. So the funding stack is not $775 million and an equity programme. It is that, plus $5.75 billion of converts, on a company whose depreciation already runs at 45% of revenue — and the coupon on the long tranche is **4.50%**, against 2.00% on the 2029 notes it was simultaneously retiring. The cost of being early is rising for the people who have to borrow to be early.

What these two also give you is price discovery. The hyperscalers describe scarcity in adjectives. These two price it. Nebius ran its first capacity auction and secured *"the highest price we have cleared for NVIDIA Blackwell chips to date."* Its Q2 landmark deals — four, averaging more than $1 billion of total contract value each — were struck at **$20–25 million of annual contract value per megawatt**, against a roughly $12 million 2026 base, and it now sees a $40–50 million per MW opportunity on short-duration deals. CoreWeave's Q2-signed contracts carry contribution margins **5–10 percentage points above** recent quarters.

And then the line that says the most about the balance:

> *"We could sell our entire 2027 capacity on these terms today. We are deliberately not doing so because we see higher value in retaining some capacity for immediate customer needs."*

That is Nebius, in its Q2 2026 Letter to Shareholders. Read the whole sentence, not the first half — the reason they give is immediate customer needs, not a signal about scarcity.

Read that next to Meta declining premium offers for its own compute. Two companies at opposite ends of the balance sheet, both withholding capacity from a market that wants it.

**Nebius reiterated the constraint after its print.** At a Goldman Sachs conference on 19 September, management repeated that demand exceeds supply, and the company is reporting improving revenue per gigawatt of power capacity. Revenue per GW is the metric to watch in this tier — it is the closest thing to a same-store-sales number for an AI cloud, and it separates genuine pricing power from simply plugging in more hardware.

---

## What Part One settles

**Watch cash, not capex.** Capex guidance is a plan, announced with a press release. The cash flow statement is the outcome. In the June quarter these four converted $171.8 billion of operating cash flow into $6.9 billion of free cash flow, two of them spent more than they generated, and the positive aggregate is essentially one company. Guidance figures will keep being announced. This is the line where the cost of the cycle stops being optional.

**Position in the chain now matters more than a view on AI.** Micron spent 25% of its operating cash flow on capex, NVIDIA 11%, the four buyers 96% — and CoreWeave's interest bill ran at five times its operating profit. Identical demand, four entirely different cash profiles, four different tolerances for being early. And the ranking is inverted: SemiAnalysis rates CoreWeave and Nebius the best AI clouds in the industry, ahead of every hyperscaler — and they are the two that have to borrow to stay there. Operating quality and balance-sheet quality are different variables; this cycle prices them as one. "Long AI infrastructure" is not one position. It is at least four, and they do not fail together.

Those two conclusions hold on filed numbers alone. What they do not settle is whether the revenue being used to justify the spending is actually collectible — which is a question about one counterparty, not four. That is [Part Two](ninety-six-cents-part-two.html).

---

## Sources

Core company figures are from the issuers' own earnings-call transcripts, press releases and 8-K exhibits for the quarters indicated. Reporting dates: Alphabet 22 July 2026 (calendar Q2); Bloom Energy 28 July (calendar Q2); Microsoft 29 July (**FQ4 FY2026**, the June quarter); Meta 29 July (calendar Q2); Samsung 30 July (calendar Q2); Amazon 30 July (calendar Q2); CoreWeave 11 August (calendar Q2); Nebius 12 August (calendar Q2); NVIDIA 26 August (**FQ2 FY2027**, quarter ended 26 July 2026); Micron 30 September (**FQ4 FY2026**, quarter ended 3 September 2026 — a 14-week quarter in a 53-week fiscal year).

Alphabet's and Meta's call transcripts are issuer-published (abc.xyz and Meta's IR site). CoreWeave's is its own corrected transcript; Nebius's figures are from its Q2 2026 Letter to Shareholders. Microsoft's and Amazon's headline financials are from their IR releases and SEC exhibits — but the *Q&A* quotes from those two calls come from third-party transcription, because neither company publishes a full Q&A transcript. Those quotes were verified word-for-word against those transcripts; the transcription is a vendor's, not the issuer's.

Micron: the FQ4 and full-year 2026 press release and 8-K Exhibit 99.1 of 30 September 2026, plus the FY2026 10-K filed 9 October (quarter ended 3 September — 14 weeks, in a 53-week fiscal year). Those two filings carry the cash-conversion figures, the $134 billion of remaining performance obligations, the contract liabilities, the take-or-pay and "minimum and maximum bands" language and the floor-pricing margin expectation. Call-sourced figures — fiscal 2027 output committed, cleanroom timing, industry bit growth, the price-increase commentary — rest on third-party transcription, the same caveat as Microsoft and Amazon above. The price ceiling sitting near Q2-2026 market prices is third-party analysis, not Micron's. HBM and DRAM shares are Counterpoint estimates on a revenue basis via Yonhap and Businesskorea; Micron does not disclose them.

Samsung: the Q2 2026 release of 30 July from Samsung's own newsroom — revenue KRW 171.5tn, operating profit KRW 89.5tn, DS division KRW 127.5tn/89.2tn, the MX operating loss and the H2 outlook language all come from it — plus the preliminary Q3 announcement of 8 October (operating profit KRW 107.4tn on about KRW 195tn), unaudited and with no divisional breakdown until 29 October. Jaejune Kim's remarks on duration and the five-year supply-agreement structure are from the Q2 call via third-party transcription; Samsung publishes no transcript. The 12-high versus 4-high HBM cost comparison is SemiAnalysis, 13 September 2026, not an issuer figure.

SemiAnalysis ClusterMAX 3.0, September 2026, for the GPU-cloud tiering (Platinum: CoreWeave, Nebius; Gold: Google Cloud, Oracle; Silver: Azure; Bronze: AWS) and for the observation that its serverless-inference testing is unfinished. That is a third-party benchmark, not an issuer disclosure, and it rates the cloud rather than inference specifically. CoreWeave's managed-inference ARR figures ($1M to more than $100M booked, at least $250M expected exiting 2026) are from its own Q2 2026 call.

Nebius commentary post-window is from a Goldman Sachs conference, 19 September 2026, not a filing.

Alphabet's token figure is from its Q2 2026 earnings release of 22 July 2026, an 8-K exhibit; the quarter-on-quarter and annualised figures are my arithmetic on it. I have deliberately left out Microsoft's Foundry figure, which is a count of customers rather than a volume.

Pichai on memory: Cheeky Pint, *The History and Future of AI at Google*.

Bloom Energy material is second-hand throughout — drawn from an internal research memo's extraction of the call rather than my own read of Bloom's transcript, and labelled as such. Bloom's claim of "visibility for 25 gigawatts of deployments" is deliberately excluded here: the implied scandium requirement (~620 tonnes per year) exceeds roughly 62 tonnes of total 2025 global consumption, and that constraint is unrebutted.

Every published claim was checked by three independent verifiers working from the original source documents rather than from this draft, with unanimity required — 71 claims, 213 checks. Figures I derived myself are labelled as arithmetic on disclosed line items. Three figures that circulated in press coverage of these calls — a +69% capex change, a −23% free-cash-flow change and a +100% capex change — were removed from a late draft because they do not appear in the companies' own transcripts.

*This post builds on [The Token P&L](the-token-pl.html), which covered the unit economics one layer down — token pricing, inference cost and Jevons at the model layer. This one is about the capital cycle above it.*
