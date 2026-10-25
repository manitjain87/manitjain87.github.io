---
title: "What Survives the Counterparty"
subtitle: "The infrastructure gets used even if the company that underwrote it does not survive. NVIDIA has committed a headline $12.93 billion to own where open models are distributed."
date: 2026-10-12
tags: ["#capital-allocation", "#2027-inflection", "#consumption-economics"]
series: "Ninety-Six Cents"
part: Three of four — What survives the counterparty
---

# What Survives the Counterparty

On 2 September NVIDIA signed a definitive agreement to acquire Hugging Face, the repository most open models are distributed through, and in the same filing wrote, in a risk factor of its own: *"Many of the world’s most popular and successful open-source models originated in China…"*

That is a headline **$12.93 billion** to own the place open models are distributed from, committed by the company with the most to lose from being wrong about them. As of 15 October it has not closed.

It is also the best single piece of evidence for the argument in this part, which is neither the bullish case nor the bearish one: the $164.9 billion of capital in [Part One](ninety-six-cents.html) will probably be used, and the equity in [Part Two](ninety-six-cents-part-two.html) probably will not be worth what it lists at. Those are not contradictory, because the thing that uses the compute does not have to be the thing that underwrote it.

*Third of four. **[Part One](ninety-six-cents.html)** · **[Part Two](ninety-six-cents-part-two.html)** · **[Part Four](ninety-six-cents-part-four.html)**. Each part stands on its own.*

*A note on sourcing. This part sits at a more varied bar than [Part One](ninety-six-cents.html) and is marked where it appears. NVIDIA’s 8-K announcing the acquisition, both risk-factor quotations and every commitment and guarantee figure are filed documents — the last from its 10-Q, including the form of the guaranty itself — as are Palantir’s quarterly figures and the absence of a sovereign-AI revenue line. A handful of figures come from the CFO commentary of the same date, which is expressly furnished rather than filed; I mark them where they appear. Nemotron’s parameter counts, licences and download figures are NVIDIA’s own and unaudited. Reflection AI’s compute commitments and the total it has raised are press-reported rather than primary contracts, and its open-weight release is promised rather than shipped. Gavin Baker’s argument is a named practitioner on a podcast, not a filing. The open-weight usage data is published production data under an open licence, and every publisher of it has an interest in the number — I say so where it is used. The post-window items are sourced to Sensor Tower, GeekWire and a Musk disclosure.*

---

**PART THREE — What survives the counterparty**

---

## The floor under the trade

**The mechanism has a name and a proponent.** Everything in [Part Two](ninety-six-cents-part-two.html) is a *model-layer* margin event. The $164.9 billion of capex in [Part One](ninety-six-cents.html) was spent two layers below it. Gavin Baker has made the case directly: margin compression at the frontier labs is net *positive* for power, semiconductors, hyperscalers, neoclouds and software, because cheaper models raise intelligence per dollar and therefore volume. Share moving away from 90%-margin frontier inference toward models a buyer can afford to run constantly is not a leak in the thesis — it is the thesis. Bloom's CEO makes the same Jevons argument from the power side. On that reading, Anthropic losing gateway share is not a problem for the capex; it is the mechanism that fills it.

The weakness is timing, not direction. Jevons needs the volume to arrive before the 2027 commitments mature, and nothing in these ten filings dates that. Baker's remarks are a named practitioner on a podcast, not a filing — a different bar from [Part One](ninety-six-cents.html).

[Part Two](ninety-six-cents-part-two.html) showed open-weight models taking the **volume** on Vercel's gateway without taking the **money** — in August, a majority of tokens on about 14 cents of every dollar. Read one way that is a failure to monetise. Read the other way it is the floor: if the frontier labs re-price, the workloads do not vanish, they move down the cost curve onto exactly the capacity that was built for them.

### Who is paying to make open weights work

The clearest evidence is not a usage chart. It is what NVIDIA did with its balance sheet.

On 2 September NVIDIA signed a **definitive agreement to acquire Hugging Face** — the repository through which most open models are distributed. The 8-K is specific in a way the coverage is not: **about $11.9 billion payable to Hugging Face stockholders, plus an equity retention programme of up to roughly $1 billion.** The $12.93 billion figure everyone quotes is the two added together, not the purchase price. Close is expected in the first half of 2027, subject to regulatory approval; no second request, EC decision or CMA action had appeared as of 11 October, which is not the same as clearance.

Why NVIDIA did it is in the filing's own risk language: *"Demand for open-source foundation models and applications based on them promotes the use of our products worldwide and sustains the Hugging Face platform."* That is the thesis of this section, told to the SEC by the company with the most to lose from being wrong about it.

The same filing also corrects the comfortable version of the story: *"Many of the world's most popular and successful open-source models originated in China and are then downloaded, revised, fine-tuned, and tested by developers in the United States and worldwide."* Open weights are not a Western phenomenon with Chinese participation. On OpenRouter's most recent week the three largest models by tokens processed are DeepSeek, Z.ai and Xiaomi, all MIT-licensed.

NVIDIA is also funding the models themselves, and that too is filed. Its Q2 FY2027 CFO commentary says its cloud-service agreements and data-centre leases fund *"the development of our open models, such as NVIDIA Nemotron, NVIDIA Cosmos, and GR00T."* Nemotron 3 Ultra — 550 billion parameters, 55 billion active — was the **only US model in OpenRouter's weekly top ten**, at 6.63 trillion tokens. One caveat, and it matters: that is the **free** variant, so it is subsidised traffic rather than paid demand. And the weights are open but the licences are not open-source — three different non-OSI licences across the family. Write open-weight, and mean it.

Then there is what an open-weight lab actually consumes. Reflection AI announced **Beam** on 5 October: 501 billion parameters, 23 billion active, pretrained on 23.8 trillion tokens. Its reinforcement-learning run used **10,500 NVIDIA GB300 GPUs for four weeks**; pretraining used **6,144 GB300 NVL72 GPUs** in under four. That is newest-generation Blackwell capacity, at frontier scale, for a model whose weights are going out under Apache 2.0. The weights are **not out yet** — Reflection says "later this month," and as of today nothing is downloadable — so this is an announced release, not a shipped one.

Reflection is also the thesis's own failure case in miniature. It has committed up to **$6.3 billion** to SpaceX's Colossus 2 and more than **$1 billion** to Nebius, against roughly **$4.6 billion** raised in total. Commitments exceed capital. The pattern that makes Anthropic fragile in [Part Two](ninety-six-cents-part-two.html) is not unique to Anthropic.

Sovereign demand is real but it is not what it is usually described as. Palantir grew revenue **93%** to **$1.94 billion** in the June quarter, and Karp's framing is explicit: *"Demand for AI sovereignty has now been unleashed… Their competitive advantage should never become the training data for future models."* Read the segments, though. The growth is **US commercial, up 149%** — enterprises wanting control of their own data, not governments buying national compute. Palantir discloses **no sovereign-AI revenue line at all**, and it sells software: it absorbs no GPU capacity. It is evidence of sovereign *demand*, never of capacity absorption. And sovereignty cuts both ways — **France terminated its decade-old Palantir relationship at the DGSI on 16 June**, replacing it with a French vendor alongside €655 million of national AI spending, six months after announcing a three-year renewal.

### Demand is still arriving, and it is not subtle

Start with the only demand figure in this post that comes from an 8-K exhibit rather than a newsletter. Alphabet said in July that its model APIs are *"processing approximately 22 billion tokens per minute. That's up from 16 billion just a quarter ago."* That is **+37.5% in a quarter**, and an annualised run-rate around **11.6 quadrillion tokens**.

Two things not to do with it. The basis is **model APIs only**, so it cannot be spliced with the wider "tokens across our surfaces" figures Google quotes elsewhere. And token growth overstates compute growth, because reasoning models emit far more tokens per unit of work than they used to. It is still the best-sourced growth number available, and it is accelerating.

**And the thing all this compute is actually for arrived.** Meta launched **Muse**, its personal agent, on 8 September. It was the **No. 1 free app in the US App Store** within a week — ahead of ChatGPT — and passed **5 million downloads by 30 September** (Sensor Tower), a milestone that took ChatGPT 56 days, Grok 103 and Claude 492.

Two caveats before reading that as pure demand. Sensor Tower notes Meta ramped house advertising for Muse from 16 September, at up to **50% of its own daily house-ad impressions** — so the curve is partly bought. And **Amazon has blocked Muse** from shopping on Amazon.com, saying Meta never disclosed the access, the agent does not identify itself, and it appears to capture and store customer credentials (GeekWire). Amazon has also sued Perplexity over Comet and moved against Google's and OpenAI's shopping agents.

That last one is the thread worth pulling. Meta is withholding compute it is offered a premium for, in order to build consumer agents — and the largest commerce platform in the world has just denied those agents entry. The capacity is contracted. The access is not.

**xAI is adding capacity at a rate that makes the hyperscalers' constraint language look conservative.** Per Musk's own disclosure, as reported, Colossus 2 runs **110,000 GB200 and 440,000 GB300** today, with three further batches of 220,000 GB300 scheduled — taking that site to 1.21 million and **1.44 million chips across both sites by the end of 2026**. (The widely-quoted "660,000 in three months" describes the scheduled batches, not what is installed.) That is a buyer nobody in this post reports to, consuming at hyperscaler scale, and it is incremental to every backlog figure in the table above.

**Read it the other way, though, because it cuts against me.** If a single site can absorb GPUs by the hundred thousand inside a quarter, the shortage looks more like a delivery queue than a physical ceiling — and nobody pays a scarcity premium for something arriving at that rate. The whole argument above assumes scarcity persists past 2027. This is the best available evidence that it might not.

### What would break this

Three things, and the first two come from my own sources.

**Open weights won the tokens and lost the money.** Vercel's own September index puts open-weight models at **56% of August gateway tokens on 14% of spend** — and in July, 29% of tokens on under 4%. A rival gateway, Requesty, independently reports **54.6% of tokens, 34.3% of requests and 14.9% of spend** in the week of 21 September. Two unconnected gateways, the same answer: roughly **seven times the token share of the dollar share.** Quoting the volume without the spend, from the same report, is cherry-picking. If open weights are the floor, they are currently a floor priced at about a seventh.

**And open weights run small, which is the harder problem for this argument.** On Hugging Face's own analysis, models under a billion parameters take **83% of all-time downloads**, everything above 100 billion takes **1%**, and only **3%** of 2026 download volume goes to models above 70 billion. The fastest-growing repository tags are the ones that decide where a model can physically run — **GGUF up 464%, Apple's MLX up 148%**, against transformers up 16%. That is local and consumer silicon, not the newest data-centre capacity. Reflection's 10,500 GB300s are real; they are also the exception, not the distribution.

**And the counterparty risk does not disappear, it moves to NVIDIA.** This is in NVIDIA's own commentary, and it is the most candid sentence any vendor published this season: *"AI clouds and model makers are seeing extraordinary demand for AI infrastructure, yet many are growing faster than their balance sheets and long-term credit profiles can support. In response, we have entered into arrangements that help select customers secure the land, power and data center capacity needed to support their growth."*

What those arrangements amount to, filed in the 10-Q across three separate tables. **$366 billion** of future commitments, of which supply and capacity alone went from **$119 billion to $279 billion** in a single quarter, primarily memory. A further **$56 billion** of additional commitments: **$36 billion** of AI cloud agreements and **$20 billion** of third-party data-centre leases NVIDIA expects to reassign. And **$108.5 billion** of guarantees, which the filing is careful to call *maximum gross* exposure, of which a **$105 billion** cap sits behind "approximately 4.25 gigawatts of IT load" at SB Energy’s campus in Pike County, Ohio — a site that, in exchange, "will exclusively host NVIDIA AI infrastructure, subject to limited exceptions."

Add those three tables together and you get the $530 billion now circulating as NVIDIA’s off-balance-sheet exposure. NVIDIA reports no such total, and the phrase "off-balance sheet" appears nowhere in the filing. The number is also doing more work than it can carry: $279 billion of it is supply commitments, mostly memory, and $33 billion is NVIDIA’s own spending plans rather than anyone else’s obligations ($8 billion of capital expenditure plus $25 billion of committed equity investments). The genuinely contingent part is the $108.5 billion of guarantees.

The **$36 billion of AI cloud agreements** is the line that shows the mechanism, because it is a revenue floor rather than a purchase. NVIDIA commits to buy cloud capacity from its partners; those partners "can unilaterally stop providing to us and sell to third-party customers at more advantageous rates"; NVIDIA’s commitment decreases "as capacity is used by third-party customers"; and NVIDIA takes a revenue share above the floor "if certain criteria are met." It is underwriting the downside of clusters it has already sold, while keeping an option on the upside. Two things the filing does not do are worth saying plainly: it names none of the AI clouds, and it says nothing about anyone’s cost of capital. What it gives is the motive, in the sentence quoted at the top of this section — customers growing faster than their credit profiles can support. That this lowers someone’s borrowing cost is the obvious inference, and it is an inference, not a disclosure. A quieter version of the same thing runs through the balance sheet: days sales outstanding stretched from **45 to 60** in the quarter, on extended payment terms the company attributes to "certain investment-grade customers." Even the strongest buyers are being carried for longer.

And the $105 billion is not live money. Each guarantee "becomes effective upon commencement of the applicable lease," rising "as each of the nine phases of data center construction is completed, the first of which is expected in fiscal year 2029," each is "limited to defined portions of lease and power payments and not the full cost of the site," and each "is expected to decrease over the course of each phase’s 20-year lease term." NVIDIA holds an option on roughly **3.8 additional gigawatts** beyond that. Against the exposure it also put its expected return on the record, in the CFO commentary rather than the filing: each generation deployed at the site "could represent approximately 1.5 million NVIDIA GPUs, or approximately $150 billion to $200 billion in NVIDIA revenue," across a 20-year site life it expects to support "multiple infrastructure upgrade cycles."

The trigger is where it turns circular. NVIDIA's exposure is set off only by **OpenAI's insolvency or failure to pay** — and *"OpenAI has agreed to reimburse and indemnify NVIDIA for any and all amounts actually paid."* The protection against OpenAI failing is a promise from OpenAI. It is worth precisely what OpenAI is worth on the day it is called.

The form of that guaranty is filed as an exhibit to the same 10-Q, and it states plainly what the support is for. NVIDIA is "automatically released from all further obligations" when the tenant or its parent achieves a credit rating, or posts a bank guaranty, letter of credit or surety bond from a rated issuer, or is replaced by a tenant that achieves a rating of its own. The rating thresholds themselves are redacted. So this is not permanent support. It is a bridge across the gap between what OpenAI’s credit can carry today and what this site needs it to carry, written to expire the moment that gap closes. The same exhibit shows the shape of the downside: what NVIDIA guarantees is a "Guaranteed Minimum Value" built from "data center, power, and transmission related costs," construction cost rather than market value. On a tenant default NVIDIA chooses among five remedies the exhibit names as the Assumption, Relet, Sale, Rejection and Deferral options, and the substance of all five is redacted. Electing assumption or deferral does not end the obligation: the exhibit is explicit that "no Covered Loss Amount shall be payable, but Guarantor shall be required to pay the applicable amounts set forth" elsewhere in the agreement. One of the five is becoming the tenant itself.

So the honest version of this part is narrower than "the compute gets used." If a frontier lab misses its commitments the capacity does not sit idle — the workloads move down the cost curve onto it. But the *loss* does not vanish. It sits with whoever wrote the guarantee, backed by an indemnity from the party whose failure triggers it and by exits that only work if somebody else turns out to be creditworthy.

---

## The 2027 cliff

Here is the thing I would actually diarise.

Read the four hyperscalers together and the pattern is clean: hard commitment through 2027, then a visible drop in willingness to commit.

Amazon commits furthest — not enough capacity in 2026, *"also be true in 2027,"* 2028 demand *"striking,"* and in Q&A the *"lion's share"* of 2027 capacity *"largely reserved"* with *"quite a bit"* already reserved for 2028. Alphabet commits directionally: capex *"to increase significantly in 2027,"* with no number. Microsoft guides one quarter — FQ1 FY2027 capex *"over $50 billion"* — plus a qualitative full-year direction.

Meta explicitly declines. Li: *"we aren't providing a specific outlook for 2027 CapEx at this time. Infrastructure planning remains highly dynamic."* Meta went further and described a deliberately *optional* 2028 — plans geared to *"maximizing 2026 and 2027 capacity,"* with 2028 preserved as flexibility by laying down data centre and network foundations *"to accommodate future server decisions."* Land and power now; chips decided later. Li's framing: near-term capacity is more valuable than long-term capacity.

Nebius, meanwhile, plans to deploy more than 1GW per year **starting in 2027**.

Micron dates the supply response, and it lands after the cliff. On the call, management put the cleanroom additions funded by its fiscal 2027 construction increase as coming online **late 2028 and beyond**, and industry DRAM bit supply growth at **low-20s% in calendar 2027 and 2028**, down from mid-20s in 2026. Supply growth decelerating while the new capacity arrives only after 2028 is the arithmetic underneath *"no line of sight."* Both are call figures, not filed ones.

So the disagreement in this sector is not about demand. It is about **duration** — and the companies closest to the data are split on it. Amazon is reserving 2028 capacity while Meta is explicitly buying the option not to.

I believe that is where the mispricing sits. Everyone agrees demand exceeds supply; nobody is differentiated by that view. The differentiated question is 2028, and the best-informed participants do not agree.

---

## The Honest Take

**For the operator rather than the investor:** your AI cost line is downstream of a memory price shock and two vendors currently outspending their own cash generation. If you are negotiating a multi-year cloud or AI platform commitment in the next two quarters, the thing to ask for is not a discount — it is a price-change mechanism, and visibility into which basis your vendor's capex is even quoted on. I'd want that language in writing before 2027 budgets lock.

**And the honest bear case is in Jassy's own words, not a sceptic's.** He described the AI adoption curve as *"very barbelled"* — AI labs and a handful of runaway applications at one end, enterprises getting real cost-avoidance value at the other, and in the middle all the existing enterprise production workloads, *"some of which are using inference in a pervasive way, but most of which aren't."* He expects that middle to become the largest segment, while explicitly declining to promise it arrives on the same trajectory: *"I don't know if the trajectory of that middle part of the barbell will be the same wildly steep trajectory that we've seen with the current barbell AI labs piece."*

That thin middle is the segment that has to arrive for this capital to earn its return. The CEO with the most capacity sold would not promise it.

Two disclosures from this season are worth more than any growth rate, and both are in [Part One](ninety-six-cents.html). Amazon's break-even arithmetic, because it can be checked. And Amy Hood's refusal to quantify ROI — because the absence of a number, from the CFO most likely to have one, is itself information.

---

## Sources

NVIDIA's acquisition of Hugging Face, the two price components, the expected close and both quoted risk-factor sentences are from NVIDIA's 8-K of 3 September 2026 (Item 8.01, accession 0001045810-26-000078); the $12.93 billion headline is from NVIDIA's own blog the same day. I checked for regulatory action myself on 11 October and found none — that is an absence, not a clearance, and no merger agreement was filed as an exhibit. The commitment and guarantee figures — the $279 billion of supply commitments, up from $119 billion; the $366 billion total; the $56 billion of additional commitments including $36 billion of AI cloud agreements and $20 billion of reassignable leases; the $108.5 billion of maximum gross guarantee exposure and its $105 billion cap; the nine construction phases and the fiscal 2029 first phase; and the quoted terms of the AI cloud agreements — are all from NVIDIA's 10-Q for the quarter ended 26 July 2026, accession 0001045810-26-000075, filed 26 August. Those three tables are disclosed separately and NVIDIA states no combined total: the $530 billion figure in circulation is their sum, not a number NVIDIA reports, and the filing never uses the phrase "off-balance sheet." The residual value guaranty terms are Exhibit 10.1 to that same 10-Q. It is a form, and the tenant's name, the loss formula, the discount rate and the credit-rating thresholds are all redacted; I identify it as the SB Energy guaranty because its $105 billion cap, its 4.25GW and its Piketon, Ohio premises match the arrangement described in the body of the filing. The remaining items are from the Q2 FY2027 CFO commentary of the same date, which Item 2.02 expressly furnishes and states "shall not be deemed filed": the passage about customers "growing faster than their balance sheets and long-term credit profiles can support" that opens that section, the open-model funding line, the move from 45 to 60 days' sales outstanding and its attribution to "certain investment-grade customers," the $150 billion to $200 billion of NVIDIA revenue and 1.5 million GPUs per infrastructure generation, and the expectation that the site supports "multiple infrastructure upgrade cycles" across a 20-year life. Nemotron parameter counts, licences and download figures are from NVIDIA's own repositories, read on 11 October; the OpenRouter ranking is OpenRouter's published data for the week to 10 October, and the model in question is the free variant.

Reflection AI: the Beam announcement, parameter counts, token count and GPU figures are Reflection's own blog of 5 October 2026. I confirmed on 11 October that no weights are published under its Hugging Face accounts, so the Apache 2.0 release is promised rather than shipped. Its compute commitments and total raised are reported figures — Bloomberg, the *Financial Times* and TechCrunch — not primary contracts, and NVIDIA's reported interest in a deeper deal was one day old when I wrote this.

Palantir: the quarterly figures and Karp's quotation are from the Q2 2026 results exhibit of 3 August 2026 and the 10-Q filed the following day. The absence of a sovereign-AI revenue line is a fact about the filing. The French termination is reported (Mobile World Live, 16 June 2026). The UK Ministry of Defence contract value is from Hansard, 10 February 2026, and the separately announced £1.5 billion is Palantir investing into the UK, not revenue.

Open-weight share: Vercel's AI Gateway Production Index for September 2026 for the 56%-of-tokens and 14%-of-spend figures; Requesty's own disclosure for the week of 21 September; Hugging Face's *State of Open Models: Summer 2026*, 14 August, for the download-by-size distribution and the repository-tag growth. Every one of those publishers sells or depends on cheap-model routing, and Hugging Face published while NVIDIA's approach was already under way — so each has an interest in the number. Gateway data also samples developers who are actively price-shopping; it sees no enterprise direct-API traffic, private deployments or first-party consumer surfaces. Tokens, requests, spend and downloads are four different units and I have tried to name the basis every time.

Vercel: the AI Gateway Production Index for September 2026 for the 56%-of-tokens and 14%-of-spend figures, and the open leaderboard export at `vercel.com/api/ai/leaderboard-export`, CC BY 4.0. That index reports data collected through **August** 2026, which is the month those two figures describe. Vercel also notes that its open-weight classification "is broader than the definition used in earlier reports" and that prior months may be revised as methodology changes, so part of the 7%-to-56% climb reflects a widening definition rather than migration alone. Spend is estimated at list prices, and every figure is a share — the published export contains no absolute volumes.

The NVIDIA guarantee, its $105 billion cap, the insolvency trigger and OpenAI’s indemnity are from NVIDIA’s 8-K of 17 August 2026.

The 2027-cliff section rests on the same issuer transcripts, releases and 8-K exhibits as [Part One](ninety-six-cents.html) — Alphabet 22 July 2026, Microsoft 29 July (FQ4 FY2026), Meta 29 July, Amazon 30 July, Nebius 12 August and Micron 30 September (FQ4 FY2026, quarter ended 3 September). Alphabet’s and Meta’s transcripts are issuer-published; the Microsoft and Amazon Q&A quotes and all Micron call figures — cleanroom timing, industry bit growth — come from third-party transcription, because neither company publishes a full Q&A transcript. Those were verified word-for-word. Jassy’s barbell remarks and Amy Hood’s exchange with Gabriela Borges are from the same 30 and 29 July calls.

Post-window items: xAI capacity per Musk’s disclosure as reported; Muse download figures and the house-advertising share from Sensor Tower; Amazon’s blocking of Muse and its stated reasons from GeekWire.

*This post builds on [The Token P&L](the-token-pl.html), which covered the unit economics one layer down — token pricing, inference cost and Jevons at the model layer. This one is about the capital cycle above it.*
