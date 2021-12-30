---
layout: post
current: post
cover: assets/images/2021-11-30-mortality-existential-risk-ubi/cover.png
navigation: True
title: Mortality, existential risk, and universal basic income
date: 2021-11-30
tags: [effective altruism]
subclass: "post"
author: [max]
excerpt: "Revisiting my year-old book chapter on Giving Tuesday."
class: post-template
---

Below is a chapter I wrote for the book [*Death And Anti-Death, Volume 18: Fifty Years After Earth Day*](https://www.amazon.com/Death-Anti-Death-18-Fifty-University/dp/1934297348), published in December 2020.
In the chapter, I argue that poverty alleviation would reduce both mortality and existential risk, and that, among anti-poverty programs, universal basic income has a number of advantages over targeted and in-kind benefits.
I'm posting it on Giving Tuesday both to highlight the work of [GiveDirectly](https://givedirectly.org), which provides cash transfers to extremely poor people and conducts research on those payments that I cite extensively, and to invite readers to consider tax and benefit policy research as a cause area for effective giving--research like we and our sister nonprofit, [PolicyEngine](https://policyengine.org), conduct.

Beyond the information in this chapter, trends from the past year suggest greater potential for tax and benefit policy as a cause area.
[GiveWell has said](https://www.givewell.org/international/technical/programs/cash-transfers) that "Cash transfers have the strongest track record we've seen for a non-health intervention," yet governments continue to restrict uses of benefit dollars.
The US Bipartisan Infrastructure Package, for example, created a [\$14 billion broadband subsidy](https://www.fcc.gov/broadbandbenefit), and the Build Back Better Act would spend [\$500 billion on childcare subsidies](https://www.whitehouse.gov/briefing-room/statements-releases/2021/10/28/president-biden-announces-the-build-back-better-framework/) (twice as much as on the Child Tax Credit).
Both of these programs create _welfare cliffs_, in which higher earnings can leave people worse off due to lost benefits.
Developing countries enact policies that are similarly flawed, if not worse.

Last week, GiveWell [revealed](https://blog.givewell.org/2021/11/22/we-aim-to-cost-effectively-direct-around-1-billion-annually-by-2025/) that they're unlikely to find opportunities more than five to eight times more cost-effective than cash transfers.
In their [response](https://www.givedirectly.org/dont-wait/), GiveDirectly claimed that cash transfers are more effective than GiveWell estimates, suggesting that GiveWell will have difficulty finding opportunities even at the 5-8x-cash range.
And in their [previous blog post](https://www.givedirectly.org/1-million-households/), GiveDirectly said that, despite having sent cash transfers to a million households, they've reached under one percent of extremely poor households in Kenya, the country where they have the largest presence.

GiveDirectly continues to be exceptionally worthy, but governments too have a role to play.
The scale of reforming tax and benefit policy is enormous: OECD countries collect [a third of GDP in taxes](https://www.oecd.org/tax/tax-policy/revenue-statistics-highlights-brochure.pdf), and redistribute [a third of that as cash benefits](https://www.oecd.org/els/soc/OECD2020-Social-Expenditure-SOCX-Update.pdf)--and those shares are growing as economies get richer.
We believe we're targeting neglected angles on the broad cause area (technology and considering taxes and benefits together), and our early traction with policymakers in the UK suggests that these novel angles can make reform tractable as well.

With that, here is **Mortality, existential risk, and universal basic income**:

## Introduction

Toby Ord didn’t start his career thinking about the far future. When the Oxford philosopher created the organization _Giving What We Can_ (GWWC) in 2009, it focused on finding the most cost-effective charities for saving or improving lives today, like malaria bed nets, and encouraging members to pledge 10 percent of their income to those charities. This marked the beginning of the movement known as _effective altruism_ (EA), which [describes itself as](https://www.centreforeffectivealtruism.org/ceas-guiding-principles/) “about using evidence and reason to figure out how to benefit others as much as possible, and taking action on that basis.”

Thirty-seven years before Ord created the EA movement, Princeton philosopher Peter Singer formed the ideas that now underpin it. In his 1972 essay, [_Famine, Affluence, and Morality_](https://www.jstor.org/stable/2265052), Singer offered the following thought experiment:

> ...if I am walking past a shallow pond and see a child drowning in it, I ought to wade in and pull the child out. This will mean getting my clothes muddy, but this is insignificant, while the death of the child would presumably be a bad thing...It makes no moral difference whether the person I can help is a neighbor’s child ten yards from me or a Bengali whose name I shall never know, ten thousand miles away.

Singer taught, as EA now does, to look beyond one’s immediate circle to humanity as a whole when weighing how to do good. If saving a drowning child in front of you is worth some sacrifice, it must be worth the same sacrifice to save an out-of-view child from perishing, as well.

But what if the metaphorical drowning child, rather than being 10,000 miles away, is 10,000 years in the future? This is the question Ord explores in his 2020 book, [_The Precipice._](https://theprecipice.com/) The risks he considers are not children dying from preventable disease, but of children never being born at all—not hundreds or thousands of children, but billions or trillions of them throughout humanity’s vast potential future. Whether our species can end suffering, explore other worlds, and experience the unimaginable, all depends on whether we can survive to continue our story.

Ord argues that we may be living through the most important time in history, when our technological power is growing so rapidly that we could make humanity’s final mistake. Climate change, nuclear war, pandemics, or unaligned artificial intelligence could all spell the end of humanity if we’re not careful. The extremely high stakes of safeguarding humanity’s future potential makes it worth fighting for, even if the probability of catastrophe is low—and in estimating its odds at 1 in 6, Ord doesn’t believe it to be so low. He brought his optimism from addressing global poverty, identifying specific ways that individuals can help, not just by donating to effective organizations working to minimize existential risks, but also by directing their own careers to make the biggest difference.

While EA has grown over the past decade, so too has a much older idea: universal basic income, or UBI. UBI is an unconditional cash payment given to every member of society on a regular basis, typically monthly, sufficient to meet basic needs. No government has yet implemented it, though many have enacted programs that check some of the boxes.[^4] A number of cities have also pursued philanthropically-funded UBI pilots and experiments.[^5]

In this chapter, I will connect UBI to the theme of this book series, through the lens of effective altruism. In short, I will review how reducing poverty could save lives in the short and (very) long run, and how UBI policies could effectively achieve that egalitarianism.

## Poverty and mortality

The strong correlation between income, poverty, and mortality has long been known, across geographies and over time.[^6] In 2016, a 1 percent increase in per-capita income across countries was associated with an extra 0.06 years of life expectancy, a reduction in infant mortality of  0.16 percentage points (pp), and a reduction in child mortality of 0.23pp. The extreme poverty rate, defined as $1.90 per day of consumption in 2011 dollars, is also associated with these measures of mortality, even when controlling for per-capita income. A 1pp decrease in the extreme poverty rate is associated with an extra 0.30 years of life expectancy, a reduction in infant mortality of 0.75pp, and a reduction in child mortality of 1.03pp.[^7] 

Empirical economics research, which applies tools such as randomized controlled trials and identification of “natural experiments” to establish causal relationships, indicates that this is more than correlation: poverty conclusively shortens lives.

Evidence comes largely from cash transfer programs, studies of which compare recipients to similar people who, due to chance or circumstance, happened not to receive the transfers. Cash transfers fall into two categories: conditional cash transfers (CCTs), in which eligible households must take some action like schooling or vaccinating children to receive the transfers, and unconditional cash transfers (UCTs), which carry no requirements. UBI is essentially a regular, universal UCT set at an amount that covers basic needs.

The simplest form of evidence is randomized controlled trials (RCTs), in which individuals are randomly assigned to a treatment or control group, as in medical trials. An RCT in Rwanda, for example, found that a one-time $500 UCT to households that contain poor or underweight children, or pregnant or lactating women, reduced child mortality by 70 percent compared to a control group.[^8] However, the small sample size—two children died in the treatment group, compared to 13 children in the larger control group—justifies considering other evidence as well.

When cash transfers aren’t randomly assigned, they can often be evaluated when governments deploy them semi-randomly, as Mexico did when it staggered the rollout of its _Progresa_ CCT across geographies. Compared to households who would have received Progresa transfers if they’d been in early-rollout areas, treated rural households experienced 17 percent less infant mortality, though neonatal mortality did not significantly change.[^9] Brazil’s similar CCT, _Bolsa Familia,_ reduced child mortality by between 6 and 17 percent.[^10]

In 1911, the US government established its first welfare program, the Mother's Pension Program, which provided cash transfers representing 12 to 25 percent of family income, generally for about 3 years. Male children of mothers accepted for the US Mother's Pension Program lived one year longer than male children of mothers who were rejected after initial acceptance (Aizer et al., 2016). This study also reported other medium-term outcomes, which can help estimate the effects of other cash transfer results for which mortality data is not yet reliably available. The program "resulted in a significant 50 percent decrease in under-nutrition, a 13 percent increase in income, and an increase of 0.4 years of school among young adults." By comparing these results to other research on mortality and being underweight (Flegal et al., 2005), income (Deaton & Paxson, 2001), and education (Cutler & Lleras-Muney, 2006), the authors establish that education and income explain 75 to 95 percent of the longevity increase, while the underweight channel explains a small share.

Cash transfer experiments have established robust causal relationships between poverty and intermediate outcomes identified in the Mothers Pension Program study. A $1,000 UCT to extremely poor households in Kenya raised subsequent earnings by $270.[^11] UCTs in Malawi and Zambia raise school enrollment by between 4 and 19 percentage points.[^12] A UCT in Rwanda also raised height-for-age and weight-for-age, indicators of healthy child development.[^13] 

With time, researchers will be able to follow up with treatment and control groups from these experiments to determine long-run mortality effects. This will add precision to the existing finding that poverty shortens lives, via channels including income, education, and nutrition.

## Poverty and existential risk

Poverty is not itself an existential risk, nor is it directly related to any likely candidates. However, poverty  destabilizes society through short-termism, isolationism, and other problems, and that instability raises the risks of extinction.

Through a combination of evidence and expert opinion, Ord estimated the probabilities of each type of existential catastrophe, as shown in the table below.[^14] He acknowledges that these probabilities are somewhat speculative, saying, "Their purpose is to show the right order of magnitude, rather than a more precise probability." Nevertheless, it provides a guide for prioritizing the risks, identifying patterns across them, and especially, for determining the most effective ways to reduce them.

| Existential catastrophe via       | Chance within the next 100 years |
|-----------------------------------|----------------------------------|
| Asteroid or comet impact          | ~1 in 1,000,000                  |
| Supervolcanic eruption            | ~1 in 10,000                     |
| Stellar explosion                 | ~1 in 1,000,000,000              |
| **Total natural risk**            | **~1 in 10,000**                 |
| Nuclear war                       | ~1 in 1,000                      |
| Climate change                    | ~1 in 1,000                      |
| Other environmental damage        | ~1 in 1,000                      |
| ‘Naturally’ arising pandemics     | ~1 in 10,000                     |
| Engineered pandemics              | ~1 in 30                         |
| Unaligned artificial intelligence | ~1 in 10                         |
| Unforeseen anthropogenic risks    | ~1 in 30                         |
| Other anthropogenic risks         | ~1 in 50                         |
| **Total anthropogenic risk**      | **~1 in 6**                      |
| **Total existential risk**        | **~1 in 6**                      |

The first thing to note is that natural risks represent less than a thousandth of the total existential risk. This is in some ways encouraging, since there’s little to be done about them, except perhaps becoming a multiplanetary species more quickly.

The second is that risk probabilities vary by orders of magnitude. Nuclear war and climate change are major threats, but each is less than a hundredth as likely as unaligned artificial intelligence (which I’ll describe later). This isn’t to say nuclear war and climate change couldn’t kill millions, even billions of people; they’re just unlikely to kill everyone on Earth.[^15]

The third, and most relevant to this analysis, is that the risks share common threads. Avoiding nuclear war and engineered pandemics will require international safeguards of hazardous material. Avoiding unaligned artificial intelligence will require a more patient approach to developing this transformational technology. Avoiding disasters from climate change—and to a large degree, all these risks—will require both international cooperation and emphasis on sustainability.

As a growing share of the world’s population—now over half—lives under democracy,[^16] the extent to which individual citizens support cooperation and sustainability will affect country-level outcomes.

The available evidence suggests that lifting people out of poverty increases their future orientation and trust in the institutions, thereby increasing support for future-oriented, globally-cooperative public policy. Poverty reduction may also address specific risks, and I discuss its links to three of the top ones: climate change, pandemics, and unaligned AI.

### Patience

Investing in existential risk avoidance requires giving up short-term gains to secure long-term stability; indeed, those now espousing such investments often describe themselves as _longtermists._

Researchers characterize the patience of individuals and societies with a range of outcomes. In the economic sense, the _rate of time preference_ or _discount factor_ describe impatience, quantifying the amount of money one would have to receive tomorrow in exchange for giving up a dollar today. Psychologists measure delayed gratification with experiments like the famous _marshmallow test_.[^17] Other researchers elicit impulsivity through survey questions like, “I don’t spend enough time thinking over a situation before I act.”[^18] For simplicity, I refer to outcomes from various studies as _patience_, capturing different angles of this general concept.

Across countries, income correlates with patience.[^19] Cash transfers have helped measure patience, since the share of the new income spent vs. saved offers clear exogenous variation. Such designs show that households in rural Mexico and Guatemala are much less (economically) patient than households in the US[^20]

Economic panel data also shows that income and patience correlate within the US.[^21] This could be reverse causality, as more patient people could take the time to build careers that would generate higher lifetime income, but sociological and psychological research suggests that patience is largely cemented in childhood through cultural and socioeconomic circumstances. For example, residents of poorer neighborhoods have higher impulsivity,[^22] and income and maternal education at birth negatively correlate with impulsivity among 15-year-olds.[^23]

The question is: is it causal? Recent evidence on “hand to mouth” households—those who consume their entire income—offers conflicting accounts. The hand-to-mouth share generally exceeds the share that standard time preference models would predict. A 2020 paper on US households attributes this to heterogeneous preferences, rather than impatience.[^24] However, another 2020 paper from Bangladesh finds that large randomized asset transfers enable poor households to break out of consistent hand-to-mouth poverty;[^25] this would only occur if the wealth shock made them more patient, as some theories predict.[^26] As with many traits, patience results from more than economic conditions, but poverty reduction would likely have some positive effect on patience.

### Trust and global cooperation

Existential risks know no borders. Averting catastrophic climate change will require the US to rejoin the Paris Accords as a vital bare minimum, and other international partnerships will be necessary to hold countries accountable to shared goals. Similarly, international organizations can ensure countries adhere to bioengineering and nuclear engineering safety standards, and can deter great power wars that could make existential risks like pandemic and nuclear war more likely.

Few studies examine sentiment toward international cooperation directly, but income consistently predicts three potential proxies: views on immigration, views on trade, and social trust.

In Australia, income correlates negatively with isolationism and vote share for the anti-immigrant party, controlling for other demographics and attitudes.[^27] Correlational and experimental evidence from Switzerland finds a "v curve" where anti-immigrant sentiment is highest in low- and high-income groups; it also finds high anti-immigrant sentiment in low-wealth groups (with no v curve).[^28]

A UK survey experiment compared support for a child benefit program when respondents were either primed or not primed to consider that it benefits immigrants. While immigration priming reduced support among all groups, the effect was about three times larger for people without a high school degree than for university degree holders.[^29]

Similar patterns are observed from trade: high income Americans are about 10 percentage points more likely than low-income Americans to say that trade has a "mostly positive" effect on a variety of outcomes.[^30]

Education may be a channel through which income affects international views; for example, a dynamic model of education choice shows that it raises trust (as well as voter participation).[^31] The US survey also found a 10-point delta in trade sentiment by college completion.

More research is needed to understand these ties; for example, support for the United Nations is not significantly related to support for populist parties in Europe, though US Democrats are more than twice as likely to support the UN than Republicans.[^32] Overall, though, the available evidence is consistent with the hypothesis that reducing poverty would engender support for the international cooperation needed to fight existential risks.

### Climate change

Whether income increases carbon emissions is controversial and uncertain. From a purely correlational perspective, people in richer countries emit more carbon. In 2016 across countries, a 1 percent increase in per-capita income and a 1pp decrease in extreme poverty were associated with increases in per-capita carbon emissions of 1.3 and 1.0 percent, respectively.[^33]

The causal story at the individual level is more encouraging. CCTs in Indonesia reduced tree cover losses by 30 percent, as recipients relied less on deforestation in times of need, and consumed more market-purchased goods rather than deforestation-sourced goods.[^34] And a UCT in Pakistan shifted its ultra-poor recipients from traditional fuels like wood and dung to more modern fuels that are better for the environment.[^35]

Thanks to advances in clean energy technology, global per-capita emissions have fallen since 2012, and they’ve fallen faster in more advanced countries like the US and France, which is now about equal to the global average.[^36] It’s plausible then that poor countries would develop in less carbon-intensive ways than rich countries have, bypassing high-carbon technologies no longer needed, and even innovating more themselves.

Regardless, the ethics of slowing global poverty reduction in order to slow climate change are dubious, especially given the infeasibility of such an undertaking and its uncertain impact. What’s needed is public policy to accelerate the transition away from fossil fuels. Experts agree that one policy in particular is essential for averting catastrophic global warming: carbon pricing.

Unlike targeted policies like electric vehicle subsidies, carbon pricing reduces emissions throughout the economy. The state assesses fees on carbon emissions at the source—the oil well, coal mine, gas site, or border for imported goods—and the internalized cost of carbon emissions then flows through manufacturers, services, and consumers, each of whom chooses lower-carbon options, with encouragement from the price signal.

In its 2018 special report on global warming,[^37] the Intergovernmental Panel on Climate Change (IPCC) made carbon pricing a core benchmark for countries’ progress on climate goals. Simulations from MIT and Climate Interactive show that carbon pricing reduces temperature changes more than any other individual policy; it has a positive marginal effect even at low rates and with or without other policies; and without it, staying under 1.5℃ will be nearly impossible.[^38]

The environmental benefits of a carbon pricing policy would extend beyond the borders of the country that implements it. Domestic manufacturers could export the clean, innovative products promoted by the carbon pricing. And because carbon pricing bills typically come with a “border adjustment,” which equivalizes trading partners by adding a fee to carbon-intensive imports from countries without their own carbon prices, other countries would be incentivized to add their own carbon pricing to make exports competitive.

The question is: how should the revenue be used? The answer, according to over 3,500 US economists, is equal dividends. These “carbon dividends” would offset the higher costs of goods and services with carbon-based inputs.[^39] Signatories to the letter, the largest statement in the history of the economics profession, include 45 Nobel Prize winning economists, as well as former Treasury secretaries and chairs of the Federal Reserve and Council of Economic Advisors, from both political parties.

Several studies of carbon dividends find that it would be progressive on a net basis and benefit most people.[^40] This result follows from carbon consumption increasing with income.

65 percent of Americans support carbon dividends,[^41] following from another popular proposal for universal dividends: the Alaska Permanent Fund Dividend, a small UBI funded by the state’s oil wealth. 90 percent of Alaskans favor the dividend going to everyone, and 64 percent say they would rather raise state income taxes than end the program.[^42] A clean, habitable environment is a type of shared natural resource, and carbon dividends essentially require that people who consume more of it compensate the rest of society.

Poverty reduction may or may not reduce emissions to avert climate change directly, but poverty reduction policies like cash transfers can make carbon pricing more attractive, raising the odds of enacting effective climate policy.

### Pandemics

Ord published _The Precipice_ on March 3, 2020. By the end of that month, the Covid-19 pandemic had shut down much of the planet. Despite being unaware of the virus when writing the book, Ord warned of the risk of natural and engineered pandemics as the second most likely cause of existential catastrophe in the coming century. The combination of historical precedent (the Black Death is estimated to have killed between 30 and 60 percent of Europeans) and rapid investment in synthetic biology indicated that this area deserves caution. 

As I write this on September 28, 2020,  Covid-19 has just taken its millionth life worldwide.[^43] Excess mortality estimates suggest official statistics may significantly undercount the virus’s true impact,[^44] and forecasters expect its death toll to reach 3 million by March 2021.[^45] It has been one of the worst disasters in human history.

And yet, to wipe out humanity, a future pandemic would have to be orders of magnitude more deadly than Covid-19. It would have to kill over 2,000 times as many people, swinging its scythe at children and younger adults, who have been less vulnerable thus far. It would also have to reach isolated populations, not only to islands like those of Hawaii, whose death rate is projected to be 80 percent lower than that of the US,[^46] but also to uncontacted tribes and people in other remote locations.

The tools needed to contain such a calamitous pandemic will therefore differ from those deployed for Covid-19. Nevertheless, our current episode may help identify solutions to prepare for worse ones to come.

Coincidentally, the world’s first true UBI experiment sheds light on this topic. In 2017, the cash transfer NGO, GiveDirectly, began an experiment that promised monthly payments of about $22 to each adult in rural Kenyan villages. While many unconditional cash transfer experiments had been previously conducted, none were truly universal—GiveDirectly gave UBIs to all households in treated villages—and none lasted so long—the payments were guaranteed for up to 12 years.

GiveDirectly had planned to release its first results from the UBI study in 2020, and when the pandemic hit, they shifted gears into evaluating how UBI protected its beneficiaries. They found that the transfers “significantly improved well-being on common measures such as hunger, sickness and depression.”[^47]

Of greater relevance to existential risk is GiveDirectly’s finding that the transfers reduced hospital visits and decreased social interactions. In epidemiological parlance, UBI likely reduced “R<sub>0</sub>” (pronounced “R-naught”), which measures the contagion of a disease. If cash transfers can keep some of the world’s poorest people from taking unnecessary risks, that could mean the difference between humanity’s potential haven remaining populated or becoming exposed.

Other evidence points to poverty as a risk factor for contracting and dying from Covid-19. Compared to counties with under 5 percent poverty, counties in Illinois and New York with poverty rates above 20 percent had 72 percent higher death rates  from Covid-19.[^48] This could be due to job types, general health, and/or other reasons.

Poverty reduction may also improve public health behaviors through education. For example, 85 percent of American college graduates reported wearing masks “always” or “very often” when going outside in summer 2020, compared to 65 percent of non-college graduates.[^49] The relationship between education and trust may explain this effect, as evidence from Europe during Covid-19 shows that “high-trust regions decrease their mobility related to non-necessary activities significantly more than low-trust regions.”[^50]

### Unaligned artificial intelligence

Ord’s top existential risk is that of unaligned artificial intelligence, at about 1 in 10 odds of destroying humanity’s future. This has caused EA organizations to promote AI research organizations as primary donation sites and places to work to make the greatest impact. But what is unaligned AI, and how could it end humanity’s potential?

The canonical thought experiment on the topic dates back to 2003, from Nick Bostrom, a philosophy professor at Oxford and now director of its Future of Humanity Institute:

> The risks in developing superintelligence [advanced AI] include...a well-meaning team of programmers [making] a big mistake in designing its goal system. This could result...in a superintelligence whose top goal is the manufacturing of paperclips, with the consequence that it starts transforming first all of earth and then increasing portions of space into paperclip manufacturing facilities. 

A real paperclip manufacturer might add constraints to the AI’s optimization function, for example preventing it from killing any humans, or penalizing it for any mountains destroyed. This is similar to how social media recommendation systems work: they optimize for engagement, but also take down content that violates rules, and penalize content that comes close to rule-breaking or otherwise opposes the goals of the company. This can work as long as we humans stay ahead of the AI. But what if the paperclip maximizer AI finds the one way around our constraints and, for example, just pulls minerals from the ocean, killing all fish on Earth? AI technology is progressing quickly, so these possibilities might strike before we know it, before we’re prepared.

Stuart Russell, UC Berkeley computer science professor and director of the Center for Human Compatible AI, lays out a different approach in his 2019 book, _Human Compatible._[^51] Rather than adapting objectives to trim off the scenarios that violate human preferences one by one, he proposes the AI learn human preferences directly via these three principles (verbatim):

1. The machine's only objective is to maximize the realization of human preferences.
2. The machine is initially uncertain about what those preferences are.
3. The ultimate source of information about human preferences is human behavior.

A paperclip maximizer AI constructed under these principles will either know that emptying the seas violates human preferences (since humans have never attempted such a thing), or would have sufficient uncertainty about human preferences that it would hesitate to do so. It would also need a way to aggregate human preferences, to avoid empowering a selfish or sadistic human.

Whether an AI can be built under Russell’s framework is an engineering question, but taking it as given, poverty may inhibit its ability to maximize the realization of human preferences. Much of AI today is built for commercial ends: Amazon to sell products, Google and Facebook to sell ads, and so on. When certain groups of individuals lack the capacity to participate in the markets—the systems through which AIs are learning to predict human preferences—the AI will have greater uncertainty in estimating its preferences. Uncertainty about those heterogeneous preferences will translate into more uncertain aggregate preferences when considering actions that will affect others.

As long as the AI fully recognizes its uncertainty around poorer people’s preferences, their absence from the commercial systems that train them might not pose an existential threat. But uncertainty is difficult to get right, and without broad input, there’s a risk of recreating humanity disproportionately in the image of its market participants. Equalizing access to those markets by reducing poverty may be a safer bet.

## UBI among antipoverty programs

If poverty reduction reduces mortality and existential risk, how should societies reduce poverty? Why would they pursue UBI, specifically?

Existing antipoverty programs have unquestionably helped. The US safety net reduced the poverty rate by 46 percent in 2018, and reduced the poverty gap—which measures how far below the poverty line households are—by 66 percent.[^52] This chapter has cited a number of non-UBI programs that improved outcomes from mortality to income to sustainability.

Yet, those programs have drawbacks. One in four Americans living in poverty do not receive any antipoverty program support.[^53] Even the largest federal programs, which benefit from economies of scale, spend about 10 cents of each dollar on administration,[^54] and this administration costs recipients time and effort applying and complying with its rules. Purchase restrictions prevent recipients from meeting their particular needs, and means-testing penalizes their labor.

UBI addresses these drawbacks in three eponymous ways: it is Universal (not means-tested or restricted by conditions like work-seeking), Basic (sufficient to meet basic needs), and Income (cash, not in-kind). Given the subjectivity of defining “basic needs,” the move toward UBI arguably constitutes the parallel moves from non-cash benefits to cash, and from targeting to universality.[^55]

### Cash vs. in-kind benefits

The case for cash is growing in popularity and evidentiary basis, thanks in part to GiveDirectly, the NGO now conducting the UBI experiment. GiveDirectly was created in 2012 by graduate students frustrated that they couldn’t give direct cash to alleviate global poverty. It now operates in multiple countries in East Africa, as well as in the US for disasters like hurricanes and Covid-19, largely providing one-time payments, but now expanding into UBI.[^56]

GiveDirectly has also contributed to the UCT literature by running several RCTs. In 2018 and 2020, they released studies benchmarking existing USAID interventions to UCTs of the same value in Rwanda, randomly assigning eligible households to the existing benefit, cash, or a control group. One compared against a child nutrition program, and another compared against a workforce training program; in both cases and on virtually all relevant outcomes, including child mortality, the UCTs performed as well or better than the incumbent USAID program.[^57]

Some in-kind benefits produce subtler concerns. The inability of housing benefits to immediately meet new demand results in rationing systems like waitlists and lotteries. To get a public housing unit in the US, qualifying individuals typically wait for 9 months, and even Housing Choice Vouchers, which subsidize rents for people whose housing costs exceed 30 percent of income, have waiting lists of 1.5 years.[^58]

There’s evidence that this perceived scarcity of housing benefits primes people to view the world as zero-sum. In Austria, opening up public housing to immigrants increased support for populist anti-immigrant parties.[^59] Samuel Hammond of the Niskanen Center has argued that “Social welfare systems that rely heavily on ‘in-kind’ benefits (as opposed to direct cash transfers or vouchers) are comparatively supply-inelastic, which creates conflict during waves of immigration.”[^60]

Not all drawbacks of in-kind benefits are as quantifiable. The embarrassment of a mother trying to buy a block of cheese, only to be told at the register that her WIC card won’t allow it because the cheese was made outside the US.[^61] The annoyance of a minimum-wage worker preparing and transporting a sandwich to their job, because they can’t use SNAP to buy prepared food near their workplace.[^62] The risk of purchasing groceries in person amid a pandemic, because neither program can be used for grocery delivery.[^63] These hurdles follow from distrust of how the poor consume, now proven to be unwarranted.[^64]

### Universality vs. targeting

While in-kind benefits constrain recipients’ consumption, means-testing constrains their labor activity. Individual programs often phase out at about 30 cents on the dollar; for example, an extra dollar of earnings reduces SNAP (food stamp) benefits by 30 cents. This is equivalent to a 30 percent marginal tax on earnings, and when individuals participate in multiple programs that phase out together, those marginal tax rates add up. As a result, the Congressional Budget Office estimated that single parents in 2016 could face federal marginal tax rates in excess of 80 percent—far higher than the richest Americans.[^65] If those single parents have to pay for child care when working, they can easily end up worse off by increasing their working hours.

Especially acute cases arise from disability insurance, in which meaningfully entering the labor force can result in _lower_ take-home pay than remaining enrolled in benefit programs. These instances of marginal tax rates exceeding 100 percent are known as _welfare cliffs_, and while some reforms have softened them, they still exist in many cases.[^66]

Payment frequency, often either monthly or yearly, is an issue for means-tested programs, too. In the US, yearly-distributed targeted programs include refundable tax credits like the Earned Income Tax Credit or the Child Tax Credit.[^67] Monthly programs include SNAP and TANF (cash welfare).

Yearly programs have the advantage of running through the tax code, simplifying the process for the applicant and reducing overhead costs; EITC costs only 1 percent to administer.[^68] However, they fail to respond to changes in income: if someone gets a pay cut in January, they might not get a compensating tax credit until 15 months later.

Monthly programs are responsive, but at the cost of bureaucracy. Recipients must report every change to income or personal circumstance, often within days or weeks. A report on the UK’s efforts to make tax credits for low-income people pay out monthly found that the government underestimated the instability of recipients’ circumstances: half of single parents underwent “more than a dozen changes in circumstance a year.”[^69] Compliance burdens aside, the benefits offset some income volatility, but given the delay of several weeks, some felt that the responsiveness (itself a volatile income source) made it harder to plan their finances.

Universalizing programs eliminates issues with either yearly or monthly means-tested programs. Many developed countries have monthly child allowances, for example, without any need to evaluate income; these programs efficiently meet the needs of parents on a regular basis. Richer parents pay more in their annual taxes, with the single system already well-equipped for counting income.

Finally, part of universality is unconditionality. For example, unemployment benefits typically require recipients to seek employment and regularly report their activities to the government. These strings demonstrate distrust, and some evidence suggests they may evoke reciprocal distrust.

In 2017, Finland randomly assigned a subset of unemployment beneficiaries to receive a UBI; on all surveyed outcomes, the UBI group responded more favorably than those on unemployment benefits, including on measures of mental health and social trust.[^70] A UK survey experiment also found that social protection programs were less susceptible to anti-immigrant opposition when they were universal, compared to means-tested.[^71]

Perhaps of greatest relevance to this chapter: targeted programs leave more of the poor impoverished. A study of 42 anti-poverty social protection schemes across 25 low-and middle-income countries  found that universal or near-universal programs reached at least 80 percent of intended recipients, while means-tested programs often reached half or less.[^72]

Of course, universal programs cost more than targeted programs. Simply spreading out existing social assistance budgets across everyone increases poverty and inequality.[^73] Instead, universal safety nets require higher taxes.

Societies that pursue this strategy achieve lower disposable income inequality (inequality of income after taxes and transfers). The US, for example, ranks in the middle of OECD countries in market income inequality, but because it doesn’t redistribute much, its disposable income inequality is third from the bottom, more equal only than Chile and Mexico. Despite similar market income inequality to the US, Germany and Finland reduce inequality about twice as much as the US does.[^74]

How do these European social democracies reduce inequality so much? Counterintuitively, it’s not through progressive taxation, in which tax rates rise with income; the US actually taxes more progressively than any other OECD country. It’s through _high_ taxation that supports generous transfers. The US taxes 24 percent of its GDP, compared to the 34 percent OECD average; only Ireland, Chile, and Mexico tax less.[^75]

Low US taxes are largely explained by the absence of a _value added tax_ (VAT), the type of consumption tax levied in all other OECD countries.[^76] 2020 US presidential candidate Andrew Yang proposed remedying that: the Freedom Dividend plan at the heart of his campaign featured a UBI of $1,000 per month per adult citizen, primarily funded by a 10 percent VAT. In a distributional analysis of his plan, which also included other reforms like a carbon dividend, welfare reform, and treating capital gains as ordinary income, I found that this plan would be progressive, lowering US inequality by 15 percent.[^77] Others have also found VAT-funded UBIs to be progressive;[^78] although VAT incidence is slightly regressive, as consumption as a share of income falls with income, the considerable progressiveness of the UBI makes the overall policy progressive.

## Conclusion

UBI is unlikely to be the most effective tool for addressing any individual problem. To avert near-term deaths, dollars are best spent on health interventions in developing countries.[^79] To avert existential catastrophe, dollars may best be spent researching specific threats, such as AI safety or pandemics. To reduce inequality without raising tax revenue, dollars are best spent targeting the poor.

What UBI lacks in targeted depth, it makes up for in breadth. This explains its effectiveness as an anti-poverty tool, ensuring that people don’t slip through the cracks of a fragmented welfare system consisting of separate programs for each shard of the poor. Just as it ensures coverage of all the needy, it too ensures coverage of all their needs, from food to housing to all the heterogeneous preferences the market satisfies for most members of society. When those preferences are satisfied, people gain the ability to live longer, healthier lives, and to look beyond their particular place and time.

While effective altruists could do better than funding UBI programs in rich countries, governments have much to gain from considering the policy. Nominally cheaper means-tested systems hide their true cost: a surveillance apparatus that costs governments billions, steals the time, freedom, and privacy of its participants, and inevitably fails to reach those most in need. Their extreme marginal tax rates discourage poor people from working, in turn cementing perceptions of the poor as lazy.

If means-test-reliant governments choose to break this cycle, the path has already been laid: European social democracies have reduced inequality through generous, widely available transfers, funded by the types of high-rate, broad-based, relatively flat taxes that raise substantial revenue. Countries with such systems in place still have residents who fall through the cracks, or who face perverse incentives, or are subjected to onerous bureaucracy to meet basic needs. Their already-expansive taxation systems provide them the resources to more easily move to universal programs like UBI.

The evidence base linking poverty to mortality and existential risk factors is substantial and growing, but more research and quantification is needed. A rigorous review would also consider the costs of redistributional policy: How much does taxation increase mortality? Does it lower trust and patience by putting some into worse economic conditions? Will longtermism suffer from donors having less resources at their disposal? How do these effects vary with the UBI parameters and funding structure? Many effects in economics exhibit diminishing returns, suggesting that shifting resources to the poor will improve the relevant outcomes on a net basis, but this is uncertain and the stakes demand epistemic humility.

UBI advocate Conrad Shaw has said, “we may almost resemble a new species when our basest daily fears are unshouldered.”[^80] People are right to be fearful when their poverty puts their life at risk, or the life of their child. Providing economic security for all won’t only avoid deaths of individual humans, it might just help us avert the death of humanity.

[^1]: Centre for Effective Altruism (n.d.).

[^2]: Singer (1972).

[^3]: Ord (2020).

[^4]: For example, Alaska provides an annual dividend of between $1,000 and $3,000 per person, funded by its oil wealth. A number of countries have universal child allowances or flat old-age pensions.

[^5]: For example, the Economic Security Project and others are funding an [experiment in Stockton, California](https://static1.squarespace.com/static/6039d612b17d055cac14070f/t/603ef1194c474b329f33c329/1614737690661/SEED_Preliminary+Analysis-SEEDs+First+Year_Final+Report_Individual+Pages+-2.pdf), and OpenResearch (formerly Y-Combinator Research) is [running an experiment across two US states](https://openresearchlab.org/assets/publications/Basic-Income-Proposal.pdf).

[^6]: See [Preston (1975)](https://www.tandfonline.com/doi/abs/10.1080/00324728.1975.10410201) and [Gortmaker (1979)](https://doi.org/10.2307/2094510).

[^7]: [My calculations](https://colab.research.google.com/drive/1REzv4QbKUBnTiEnyRgF9DHNsrGXSxZKP#scrollTo=HTeLLhLYMCc8) based on World Bank data on 183 countries for income, or 76 countries for poverty, weighted by country population. Regressions including both log income and the extreme poverty rate show similar t-statistics between the two predictors across outcomes, both around 6 in absolute value and coefficients falling by roughly half compared to 1-predictor regressions; poverty and life expectancy is an exception at around -2.8, suggesting that extreme poverty has a stronger effect on infant and child mortality than on life expectancy. Infant and child mortality are defined as deaths of children under age 1 and 5, respectively.

[^8]: Despite the relatively few cases of child mortality, the result was statistically significant with a t-statistic of -2.05 [(McIntosh & Zeitlin, 2018)](https://www.poverty-action.org/sites/default/files/publications/Benchmarking.pdf).

[^9]: Progresa transfers increased income by about 22 percent [(Barham, 2011)](https://doi.org/10.1016/j.jdeveco.2010.01.003). Infant and neonatal mortality are defined as death in the first year and 28 days of life, respectively [(UNICEF, 2020)](https://data.unicef.org/topic/child-survival/neonatal-mortality/).

[^10]: Bolsa Familia “transfers ranged from $18 to $175 per month, depending on the income and composition of the family”; the effect size varied with the program’s coverage by municipality, the unit of analysis [(Rasella et al., 2013)](https://doi.org/10.1016/S0140-6736(13)60715-1).

[^11]: [Haushofer & Shapiro (2016)](https://doi.org/10.1093/qje/qjw025).

[^12]: Malawi [(Abdoulayi et al., 2016)](https://www.unicef.org/evaldatabase/index_94228.html) and Zambia ([Seidenfeld et al., 2016](https://www.air.org/system/files/downloads/report/MCTG_36Month_Final_Feb2016.pdf); [Seidenfeld & Handa, 2014](https://www.unicef.org/evaldatabase/files/Zambia_Child_Grant_Programe_-_36_month_impact_report.pdf)).

[^13]: [McIntosh & Zeitlin (2018)](http://arxiv.org/abs/2009.01749).

[^14]: Reproduced from Table 6.1 of _The Precipice_.

[^15]: Ord defines existential risk more broadly than killing all of humanity, as risks that destroy humanity’s potential. Climate change could, for example, threaten to kill so much of humanity, and leave the remainder in such uninhabitable environs, that our species spends the rest of its days living on subsistence without the capacity to advance; this would also qualify as an existential catastrophe.

[^16]: 55.8 percent of the world population lived in democratic states as of 2015 [(Roser, 2013)](https://ourworldindata.org/democracy).

[^17]: [Mischel & Ebbesen (1970)](https://content.apa.org/record/1971-02138-001).

[^18]: [Dickman (1990)](https://doi.org/10.1037/0022-3514.58.1.95).

[^19]: Based on a “representative data set on time preferences from 80,000 individuals in 76 countries,” this study also found correlations between income and discount factors	 at the individual level [(Dohmen et al., 2015)](https://econpapers.repec.org/paper/hkawpaper/2016-012.htm).

[^20]: Mexico [(Carvalho, 2008)](https://www.rand.org/pubs/working_papers/WR759.html) and Guatemala [(Aycinena et al., 2019)](https://doi.org/10.1080/15140326.2019.1596641).

[^21]: [Lawrance (1991)](https://doi.org/10.1086/261740).

[^22]: [Lynam et al. (2000)](https://pubmed.ncbi.nlm.nih.gov/11195980/).

[^23]: [Assari et al. (2018)](https://doi.org/10.3390/children5050058).

[^24]: [Aguiar et al. (2020)](https://doi.org/10.3386/w26643).

[^25]: [Balboni et al. (2020)](https://papers.ssrn.com/abstract=3594155).

[^26]: [Becker & Mulligan (1997)](https://doi.org/10.1162/003355397555334).

[^27]: [Mughan & Paxton (2006)](https://doi.org/10.1017/S0007123406000184).

[^28]: [Jetten et al. (2015)](https://doi.org/10.1371/journal.pone.0139156).

[^29]: [Muñoz & Pardos-Prado (2019)](https://doi.org/10.1017/psrm.2017.18).

[^30]: [Gallup (2019)](https://news.gallup.com/poll/315590/americans-face-mask-usage-varies-greatly-demographics.aspx).

[^31]: [Heckman et al. (2018)](https://doi.org/10.1086/697535).

[^32]: [Pew Research Center (2019)](https://www.pewresearch.org/fact-tank/2019/09/23/united-nations-gets-mostly-positive-marks-from-people-around-the-world/).

[^33]: Using World Bank data from 186 countries, weighted by population [(Ghenis, 2020)](https://colab.research.google.com/drive/1REzv4QbKUBnTiEnyRgF9DHNsrGXSxZKP#scrollTo=HTeLLhLYMCc8).

[^34]: [Ferraro & Simorangkir (2020)](https://doi.org/10.1126/sciadv.aaz1298).

[^35]: [Nawaz & Iqbal (2020)](https://doi.org/10.1016/j.enpol.2020.111535).

[^36]: As of 2018, global carbon emissions were 4.5 metric tons per capita, compared to 15.2 in the US and 4.6 in France [(World Bank, 2021)](https://data.worldbank.org/indicator/EN.ATM.CO2E.PC?locations=FR-US-1W). NB: I updated this number compared to the book chapter, which used data from 2014, the latest available at its publication.

[^37]: [IPCC (2018)](https://www.ipcc.ch/sr15/).

[^38]: [Climate Interactive (2019)](https://en-roads.climateinteractive.org/scenario.html).

[^39]: [Climate Leadership Council (n.d.)](https://www.econstatement.org).

[^40]: The US Treasury Department found that a carbon tax of $49 per metric ton could fund a rebate of $583 per person; this would raise the incomes of the bottom seven deciles, on average, at the cost of the upper three deciles [(Horowitz et al., 2017)](https://www.treasury.gov/resource-center/tax-policy/tax-analysis/Documents/WP-115.pdf). Another study found that a $50 per ton carbon dividend “benefits 56 percent of people, including 85 percent in the bottom half of the distribution” [(Fremstad & Paul, 2019)](https://econpapers.repec.org/article/eeeecolec/v_3a163_3ay_3a2019_3ai_3ac_3ap_3a88-97.htm).

[^41]: [Morning Consult (2020)](https://clcouncil.org/morning-consult-poll.pdf).

[^42]: Per a poll from the Economic Security Project [(Isenberg, 2017)](https://medium.com/economicsecproj/what-a-new-survey-from-alaska-can-teach-us-about-public-support-for-basic-income-ccd0c3c16b42).

[^43]: [New York Times (2020)](https://www.nytimes.com/interactive/2020/world/coronavirus-maps.html).

[^44]: As of August 12, 2020, US excess mortality was about 200,000, while official Covid-19 deaths were about 140,000 [(Lu, 2020)](https://www.nytimes.com/interactive/2020/08/12/us/covid-deaths-us.html).

[^45]: As of September 28, 2020, a group of “superforecasters,” selected based on prediction accuracy across other outcomes, had assigned a 57 percent probability to global Covid-19 deaths exceeding 2.7 million by March 2020 [(Good Judgment Project, 2020)](https://goodjudgment.io/superforecasts/#1388).

[^46]: Covid-19 is projected to kill 145 Hawaiians per million population, vs. 693 Americans per million [(Gu, 2020)](https://covid19-projections.com/). 

[^47]: [Banerjee et al. (2020)](https://www.poverty-action.org/publication/effects-universal-basic-income-during-pandemic).

[^48]: As of May 5, 2020, the COVID-19 death rate per 100,000 person-years was 143.2 in counties with 20% poverty or higher, and 83.3 in counties  with 5% poverty or lower, in Illinois and New York [(Chen & Krieger, 2020)](https://doi.org/10.1097/PHH.0000000000001263).

[^49]: Counterintuitively, the same survey found that Americans earning under $36,000 per year were slightly _more_ likely to wear masks than higher-income people [(Gallup, 2020)](https://news.gallup.com/poll/247970/slim-majority-trade-benefitting-workers.aspx).

[^50]: [Bargain & Aminjonov (2020)](https://papers.ssrn.com/abstract=3596671).

[^51]: [Russell (2019)](https://www.amazon.com/Human-Compatible-Artificial-Intelligence-Problem-ebook/dp/B07N5J5FTS).

[^52]: [Bruenig (2019)](https://www.peoplespolicyproject.org/2019/09/16/the-us-welfare-state-cut-poverty-by-two-thirds-in-2018/).

[^53]: [Minton & Giannarelli (2019)](https://www.urban.org/research/publication/five-things-you-may-not-know-about-us-social-safety-net).

[^54]: [Greenstein (2012)](https://www.cbpp.org/research/romneys-charge-that-most-federal-low-income-spending-goes-for-overhead-and-bureaucrats-is).

[^55]: [Ghenis (2017)](https://medium.com/basic-income/if-we-can-afford-our-current-welfare-system-we-can-afford-basic-income-9ae9b5f186af).

[^56]: [_GiveDirectly_ (2020)](https://www.givedirectly.org/).

[^57]: See papers on benchmarking UCTs to a child nutrition program [(McIntosh & Zeitlin, 2018)](https://www.poverty-action.org/sites/default/files/publications/Benchmarking.pdf) and to an workforce training program [(McIntosh & Zeitlin, 2020)](http://arxiv.org/abs/2009.01749).

[^58]: [National Low Income Housing Coalition (2016)](https://nlihc.org/resource/housing-spotlight-volume-6-issue-1).

[^59]: [Cavaille & Ferwerda (2017)](https://ideas.repec.org/p/cge/wacage/328.html).

[^60]: [Hammond (2018)](https://www.niskanencenter.org/denmark-ghettos-public-housing/).

[^61]: [USDA (2013)](https://www.fns.usda.gov/wic/wic-food-packages-regulatory-requirements-wic-eligible-foods#MILK).

[^62]: [USDA (2020)](https://www.fns.usda.gov/snap/eligible-food-items).

[^63]: Purchase limitations prevent the poor from accessing normal markets, which in turn will make commercially-motivated AIs more uncertain about their preferences.

[^64]: Cash transfers do not raise consumption of alcohol and tobacco [(Evans & Popova, 2014)](https://blogs.worldbank.org/impactevaluations/do-poor-waste-transfers-booze-and-cigarettes-no).

[^65]: [Mok (2018)](https://www.cbo.gov/sites/default/files/114th-congress-2015-2016/reports/50923-marginaltaxrates.pdf).

[^66]: [Stapleton et al. (2006)](https://doi.org/10.1111/j.1468-0009.2006.00465.x).

[^67]: Only the Additional Child Tax Credit component of the Child Tax Credit is refundable, meaning that it can reduce federal tax liability below zero.

[^68]: [Greenstein (2012)](https://www.cbpp.org/research/romneys-charge-that-most-federal-low-income-spending-goes-for-overhead-and-bureaucrats-is).

[^69]: [Millar & Whiteford (2020)](https://doi.org/10.1332/175982719X15723525915871).

[^70]: [Kangas et al. (2019)](https://julkaisut.valtioneuvosto.fi/handle/10024/161361).

[^71]: [Muñoz & Pardos-Prado (2019)](https://doi.org/10.1017/psrm.2017.18).

[^72]: [Kidd & Athias (2020)](https://www.developmentpathways.co.uk/publications/hit-and-miss-an-assessment-of-targeting-effectiveness-in-social-protection).

[^73]: [Hoynes & Rothstein (2019)](https://doi.org/10.3386/w25538).

[^74]: [Roser & Ortiz-Ospina (2016)](https://ourworldindata.org/income-inequality).

[^75]: [OECD (2019a)](https://www.oecd.org/tax/revenue-statistics-2522770x.htm).

[^76]: [OECD (2019b)](https://doi.org/10.1787/ctt-2018-7-en).

[^77]: I found that Yang’s plan would not be fully paid for [(Ghenis, 2019a)](https://medium.com/ubicenter/distributional-analysis-of-andrew-yangs-freedom-dividend-d8dab818bf1b), as did the Tax Foundation [(Pomerleau, 2019)](https://taxfoundation.org/andrew-yang-value-added-tax-universal-basic-income/). A budget-neutral version of Yang’s plan, providing a monthly payment of $471 rather than $1,000, would reduce inequality by 9 percent instead, as measured by the Gini index [(Ghenis, 2019b)](https://medium.com/ubicenter/a-revenue-neutral-version-of-andrew-yangs-freedom-dividend-d7d517dbeeea).

[^78]: [Gale (2020)](https://www.brookings.edu/wp-content/uploads/2020/01/Gale_LO_01.13.pdf).

[^79]: A death from malaria can be averted for under $4,000, and most of these averted deaths are of children under 5 [(GiveWell, 2020)](https://docs.google.com/spreadsheets/d/1BmFwVYeGMkpys6hG0tnfHyq__ZFZf-bmXYLSHODGpLY).

[^80]: [Shaw (2020)](https://medium.com/basic-income/how-to-build-a-movement-in-record-time-456c620dcf1c).
