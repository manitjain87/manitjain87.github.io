# GPU-as-a-Service: The New Capital Allocation

*May 2026 · 7 min read · Strategic Finance*

---

"Inference got a hundred times cheaper this year. The compute bill went up anyway."

Demian, an inference engineer at Nebius, posted that observation to X last month. If you understand why both sentences are true at the same time, you understand the most important thing happening in AI capital allocation right now.

---

## The Jevons Paradox, Computed

The cost to run an AI model through an API — inference — dropped by roughly 100x over the past year. DeepSeek V4 Flash now costs $0.14 per million input tokens. A year ago, the equivalent was $15.

The rational CFO response is: great, the technology is getting cheaper. We can do more for less.

The actual response of the market is: total compute spending is rising, not falling. Meta alone plans $60–65 billion in CapEx this year. Zuckerberg said he'd "rather risk building too much than too little." Amazon committed up to $25 billion more to Anthropic — on top of the $8 billion already invested — with a $100 billion-plus AWS commitment over the next 10 years. Microsoft, Google, and a dozen AI labs are spending at similar scale.

Cheaper inference does not reduce the compute bill. It increases the number of things worth computing. That is Jevons Paradox applied to AI — and it is the defining capital allocation question for every company building on top of these models.

---

## What GPU-as-a-Service Actually Means

The hyperscalers — AWS, Azure, Google Cloud — built their clouds for general workloads: web apps, databases, corporate IT. AI training and inference require something different: InfiniBand networking, liquid cooling, storage that moves data at a terabyte per second, and topology-aware job scheduling that optimises for model training speed rather than general throughput.

Most traditional cloud providers cannot deliver this. The ones that can are building infrastructure that looks less like software and more like a power plant.

Arkady Volozh, the founder and CEO of Nebius, describes the economics directly: "We build it through the whole stack. Land, power, racks, cloud platform, services. It's a full-stack build, which gives you economic efficiency — but more importantly, it gives you engineering efficiency. It is optimized to the last bolt."

This is not software infrastructure. It is physical infrastructure. The CapEx required to build it — $16–20 billion per year, in Nebius's case — is comparable to what a utility spends on generation capacity. The difference is that demand for GPU compute is growing at 100%+ annually, not the 2–3% of electricity demand.

Nebius got a $2 billion investment from NVIDIA and a preferred-provider designation with early access to the next-generation Rubin platform. Meta signed a $27 billion, five-year contract — the largest infrastructure commitment a company of this scale has ever made to an external provider. Microsoft signed a multi-billion-dollar deal separately. Meta and Microsoft choosing to buy capacity rather than build it internally — at this scale — is the signal that GPU-as-a-Service is a category, not a single-company experiment.

---

## "Whatever Is Built Is Consumed"

The phrase Volozh uses to describe market conditions is worth sitting with: "Whatever is built is consumed."

He is describing demand that cannot be satisfied by existing supply. Nebius is sold out. CoreWeave is sold out. Every major provider of GPU infrastructure is sold out, and the constraint is not chip supply — it is the physical speed at which data centers can be built, powered, and cooled. NVIDIA's co-investment in optical manufacturing facilities with Corning — three new factories, 3,000-plus jobs — tells the same story from the hardware side. The GPU company is co-investing in glass factories because the bottleneck has moved from chip design to physical manufacturing.

Here is what this means in practice. JPMorgan published a note last week titled "AI Token Costs: Eating Internet Profits Alive," flagging Shopify, Spotify, Meta, and Pinterest as companies where AI inference costs are compressing margins. These are not AI startups burning venture capital on experiments. These are scaled internet businesses whose core products — recommendations, search, content personalisation — now consume tokens at a rate that was not in the budget 12 months ago.

Enterprises across sectors are discovering the same thing: the per-unit cost of tokens is falling, but the volume of tokens their business consumes is growing faster than the price decline. Budgets built on year-ago assumptions are exhausted in months. The procurement model — negotiate an annual contract, allocate by quarter — was designed for software that costs roughly the same every month. GPU compute does not cost roughly the same every month.

Goldman Sachs published the optimistic version of the same observation the same week: as token costs continue to fall, agentic AI converts from a capex-heavy cost burden into a margin-expansion business. More complex agents become economically viable. Both notes are right. The question is timing — and which companies survive the gap between the JPMorgan present and the Goldman future.

---

## From Bare Metal to Token Factory

The shift in how GPU infrastructure is priced maps directly to the shift from seats to consumption that Salesforce and ElevenLabs have already made. Nebius began by selling bare-metal GPU access — rent this server, pay by the hour. It is now building a "Token Factory" that sells tokens rather than GPU hours, and an agentic services layer on top of the cloud platform.

The economics invert at each step up the stack. Bare metal is low margin, high volume — the wholesale layer. Token Factory is higher margin, consumption-priced. The agentic services layer — inference endpoints, model fine-tuning, embedding generation — is higher still. Volozh frames the bare-metal contracts as financing, not the end product: "We use these big bare metal contracts not as our main line of business, but as one of the ways to finance building our own cloud for the rest of the market."

The $27 billion Meta contract is not the business. It is the balance sheet that enables the business. The actual business is selling GPU compute on the spot market to thousands of AI startups and enterprises that cannot commit to five-year contracts — at higher rates than Meta pays.

---

## The Honest Take

This post is not a recommendation to buy Nebius stock. It is a recommendation to understand the capital allocation question that Nebius represents.

For most of the last decade, the CFO's technology budget was dominated by SaaS subscriptions — seats, licenses, per-user fees. That model is being replaced by consumption pricing — pay for what you use — across the software industry.

The next shift is from consumption to capacity. When the critical input to your business is not a software license but access to physical infrastructure that is structurally undersupplied, the capital allocation question changes:

1. **What is our GPU compute requirement for the next three years — not as a cost forecast, but as a capacity requirement?** If demand for AI inference is growing faster than infrastructure can be built, your access to compute is a competitive variable, not a procurement item.

2. **Are we buying at the right layer of the stack?** Bare-metal contracts lock in supply but commit capital. Spot market access preserves flexibility but exposes you to price volatility. The right answer depends on how central AI is to your revenue model.

3. **Who owns the infrastructure we depend on, and what happens if they can't deliver?** Concentration risk exists at every layer — chip design (NVIDIA), cloud infrastructure (hyperscalers + neoclouds), and model providers. If any layer tightens, your AI spend becomes a supply chain problem.

The Jevons Paradox observation that Demian posted — inference got cheaper, the compute bill went up — will hold for years. The companies that understand this as a physical capacity question rather than a software cost question will build the infrastructure to access the market. The ones that don't will find their AI budget is fully allocated — to the companies that did.

---

*Sources: Nebius Group, FY2025 Annual Report and Q4 2025 Earnings. Arkady Volozh, interview, Accel "Spotlight On" podcast, 2025-10-15. NVIDIA, Nebius Investment Announcement, March 2026. Meta, Q1 2026 Earnings Call and 2026 CapEx Guidance. Amazon, Anthropic Investment Announcement, April 2026. DeepSeek, V4 API Pricing, April 2026. JPMorgan, "AI Token Costs: Eating Internet Profits Alive," May 2026. Goldman Sachs, AI Infrastructure Report, May 2026. Corning/NVIDIA, Optical Manufacturing Partnership Announcement, May 2026.*
