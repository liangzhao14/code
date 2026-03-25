---
source: https://world-nuclear.org/information-library/country-profiles/countries-g-n/japan-nuclear-power
downloaded: 2026-03-24 23:53:57
---

[HOME](https://world-nuclear.org/) / [Information Library](https://world-nuclear.org/information-library) / [country profiles](https://world-nuclear.org/information-library/country-profiles) / [countries-g-n](https://world-nuclear.org/information-library/country-profiles/countries-g-n) / Japan: Nuclear Power

country profiles

# Nuclear Power in Japan

Updated Friday, 13 February 2026

* **Japan needs to import about 90% of its energy requirements.**
* **Its first commercial nuclear power reactor began operating in mid-1966, and nuclear energy has been a national strategic priority since 1973. This came under review following the 2011 Fukushima accident but has been confirmed.**
* **Up until 2011, Japan was generating some 30% of electricity from its reactors and this was expected to increase to at least 40% by 2017. The plan is now for at least 20% by 2030, from a depleted fleet.**
* **15 reactors have restarted and 10 reactors are currently in the process of restart approval.**

33![](https://world-nuclear.org/images/icon-operable-reactor.png)

Operable  
Reactors

31,679 MWe

2![](https://world-nuclear.org/images/icon-construction-reactor.png)

Reactors Under  
Construction

2,653 MWe

27![](https://world-nuclear.org/images/icon-down-reactor.png)

Reactors  
Shutdown

17,155 MWe

#### Operable nuclear power capacity

var RDB\_WIDGET\_CONFIG\_widget\_8keh8 = {
"id": "widget\_8keh8",
"type": "chart\_histogram",
"query": {
"query": {
"filtered": {
"filter": {
"bool": {
"must": [
{
"terms": {
"reactor.country.exact": [
"Japan"
]
}
}
]
}
},
"query": {
"match\_all": {}
}
}
}
},
"base": "https://reactordb.world-nuclear.org",
"include": "/embed.html",
"settings": {
"chart": "bar",
"start": "1970",
"end": "2025",
"value": "reference\_unit\_power",
"label": "Reference Unit Power (MWe)",
"height": "300",
"left": "80",
"distance": "0"
}
}

## Electricity sector

**Total generation (in 2023):** 1003 TWh

**Generation mix:** natural gas 331 TWh (33%); coal 284 TWh (28%); solar 96.5 TWh (10%); hydro 85.0 TWh (8%); nuclear 84.1 TWh (8%); biofuels & waste 62.6 TWh (6%); oil 30.2 TWh (3%); wind 10.5 TWh.

**Import/export balance:**Zero imports and exports.\*

**Total consumption:** 879 TWh

**Per capita consumption:** c. 7100 kWh in 2023

*\* The fossil fuels used to generate about 70% of Japan's electricity are imported.*

*Source: International Energy Agency and the World Bank. Data for year 2023.*

Despite being the only country to have suffered the devastating effects of nuclear weapons in wartime, with over 100,000 deaths, Japan embraced the peaceful use of nuclear technology to provide a substantial portion of its electricity. However, following the tsunami which killed 19,000 people and which triggered the [Fukushima nuclear accident](https://world-nuclear.org/information-library/safety-and-security/safety-of-plants/fukushima-daiichi-accident "Fukushima Daiichi Accident information page") (which killed no-one) in March 2011, public sentiment shifted markedly so that there were widespread public protests calling for nuclear power to be abandoned. The balance between this populist sentiment and the continuation of reliable and affordable electricity supplies is being worked out politically.

The government's stated aim is for nuclear power to provide around 20% of electricity by 2030. Earlier in 2011, nuclear energy had accounted for almost 30% of the country's total electricity production (29% in 2009), from 47.5 GWe of capacity (net) to March 2011, and 44.6 GWe (net) from then. There were plans to increase this to 41% by 2017, and 50% by 2030.

## Nuclear power industry

Japan has 33 nuclear power reactors classed as operable. However, in 2013 the Nuclear Regulation Authority (NRA) established new regulatory requirements, and just 15 reactors have since received clearance from the regulator to restart.

**Operable reactors in Japan**

var RDB\_WIDGET\_CONFIG\_widget\_l5z1b = { "id": "widget\_l5z1b", "type": "table\_reactor", "query": { "query": { "filtered": { "filter": { "bool": { "must": [ { "terms": { "reactor.status.exact": [ "Operable" ] } }, { "terms": { "reactor.country.exact": [ "Japan" ] } } ] } }, "query": { "match\_all": {} } } } }, "base": "https://reactordb.world-nuclear.org", "include": "/embed.html", "settings": { "order": { "field": "reactor.name", "dir": "asc", "sort\_type": "exact" }, "limit": "100", "countryPageTemplate": "/nuclear-reactor-database/summary/{country}", "reactorPageTemplate": "/nuclear-reactor-database/details/{reactor}", "reactor": [ { "field": "reactor.name", "display": "Name", "formatting": "reactor\_link" }, { "field": "reactor.model", "display": "Model" }, { "field": "reactor.process", "display": "Reactor Type" }, { "field": "reactor.reference\_unit\_power\_capacity\_net", "display": "Reference Unit Power (MWe)", "formatting": "number" }, { "field": "reactor.first\_grid\_connection", "display": "Grid Connection", "formatting": "year\_month" } ] }}

### Nuclear plant restarts and retirements

The first two reactors to restart after the March 2011 accident at Fukushima Daiichi did so in August and October 2015. Since then, a further 12 have restarted, and another 11 operable reactors are at various stages in the process of restart approval. Two under construction reactors (Ohma and Shimane 3) have also applied. In the light of the war between Ukraine and Russia, Japan’s prime minister announced that the country would accelerate the restart of nine units by winter 2022, and a further seven units by summer 2023, but this was not achieved.

**Status of nuclear power plants in Japan**

| **Reactor** | **Status** | **Type** | **Applied** | **Basic  design** | **Detailed  design** | **Safety  programme** | **Pre-service  inspection** | **Restart  date (commercial operation)** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Genkai 3 | OP | PWR | July 2013 | Jan 2017 | Aug 2017 | Sept 2017 | CO | May 2018 |
| After installation of the specialized safety facility (SSF), Genkai 3 started supplying power to the grid again in December 2022 and returned to commercial operation in January 2023. | | | | | | | |
| Genkai 4 | OP | PWR | July 2013 | Jan 2017 | Sept 2017 | Sept 2017 | CO | June 2018 |
| Periodic inspection from Sept 2022 to Feb 2023, the deadline for the installation of the SSF. Successful installation of SSF announced in Feb 2023. Power generation resumed in Feb 2023. | | | | | | | |
| Hamaoka 3 | OP | BWR | June 2015 | UR | NA | NA |  |  |
| Hamaoka 4 | OP | BWR | Feb 2014 | UR | UR | UR |  |  |
| Higashidori 1 Tohoku | OP | BWR | June 2014 | UR | UR | UR |  |  |
| Ikata 3 | OP | PWR | July 2013 | July 2015 | Mar 2016 | Apr 2016 | CO | Sept 2016 |
| Kashiwazaki-Kariwa 6 | OP | ABWR | Sept 2013 | Dec 2017 | Oct 2020 | Oct 2020 | UR | Jan 2026 |
| Kashiwazaki-Kariwa 7 | OP | ABWR | Sept 2013 | Dec 2017 | Oct 2020 | Oct 2020 | UR |  |
| End date of work on safety measures is undecided. | | | | | | | |
| Mihama 3 | OP | PWR | Mar 2015 | Oct 2016 | Oct 2016 | Nov 2016 | CO | June 2021 |
| The NRA approved a 20-year licence extension (beyond the 40-year initial licence period) in Nov 2016. Work on safety measures completed Sept 2020. Final approval for restart granted Apr 2021. Restarted June 2021. Shutdown Oct 2021 due to missing the deadline for the installation of the SSF, which was later completed on 28 July 2022.. Restart delayed due to water leak in auxiliary reactor building. Restarted in September 2022. | | | | | | | |
| Ohi 3 | OP | PWR | July 2013 | May 2017 | Aug 2017 | Sept 2017 | CO | Apr 2018 |
| Shut down in Aug 2022 due to the deadline of the installation of SSF on 24 August 2022. Power generation resumed in January 2023. | | | | | | | |
| Ohi 4 | OP | PWR | July 2013 | May 2017 | Aug 2017 | Sept 2017 | CO | June 2018 |
| Onagawa 2 | OP | BWR | Dec 2013 | Feb 2020 | Dec 2021 | Dec 2021 | CO | Oct 2024 |
| Sendai 1 | OP | PWR | July 2013 | Sept 2014 | Mar 2015 | May 2015 | CO | Aug 2015 |
| Sendai 2 | OP | PWR | July 2013 | Sept 2014 | May 2015 | May 2015 | CO | Nov 2015 |
| Shika 2 | OP | ABWR | Aug 2014 | UR | UR | UR |  | Expected January-March 2026 |
| Shimane 2 | OP | BWR | Dec 2013 | Sept 2021 | CO | CO | CO | December 2024 |
| Takahama 1 | OP | PWR | Mar 2015 | Apr 2016 | June 2016 | Feb 2021 | CO | August 2023 |
| Takahama 2 | OP | PWR | Mar 2015 | Apr 2016 | June 2016 | CO | CO | September 2023 |
| Takahama 3 | OP | PWR | July 2013 | Feb 2015 | Aug 2015 | Oct 2015 | CO | Feb 2016 |
| Takahama 4 | OP | PWR | July 2013 | Feb 2015 | Oct 2015 | Oct 2015 | CO | June 2017 |
| Tokai 2 | OP | BWR | May 2014 | Sept 2018 | Oct 2018 | UR | UR |  |
| The NRA approved a 20-year licence extension (beyond the 40-year initial licence period) in November 2018. Work on safety measures including the installation of specialized safety facility (SSF) was to be completed in September 2024. In October 2023 JAPC suspended construction works for the unit when multiple gaps near the seawall’s steel reinforcement pillars were discovered. JAPC had originally planned to restart Tokai 2 by 2025. It now expects to complete the required work by December 2026. | | | | | | | |
| Tomari 1 | OP | PWR | July 2013 | UR | UR | UR |  |  |
| Tomari 2 | OP | PWR | July 2013 | UR | UR | UR |  |  |
| Tomari 3 | OP | PWR | July 2013 | UR | UR | UR |  |  |
| Tsuruga 2 | OP | PWR | Nov 2015 | Dec 2024 | Mar 2025 | Apr 2025 |  |  |
|  | Japan's Nuclear Regulation Authority concluded in July 2024 that unit does not comply with regulatory safety standards due to active fault running under facility. | | | | | | | |
|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total applied restart |  |  | **25** |  | | |  | **15** |
|  |  |  |  |  | | |  |  |
| Ohma | UC | ABWR | Dec 2014 | UR | UR | NA |  |  |
| Shimane 3 | UC | ABWR | Aug 2018 | UR | NA | NA |  |  |

OP = operable; UC = under construction; UR = under review; NA = not applied; CO = complete  
Notes:  
- The NRA review process is split into three parts, but these are typically carried out in parallel. A description of each stage is provided on the [NRA website](https://www.nsr.go.jp/english/regulatory/20150826.html). Pre-service inspections may be carried out upon receipt of the detailed design from a utility that is reviewed in stage 2 but typically take place after all three stages of review have been completed.  
Sources: JAIF, NRA Japan.

In October 2012 the new Nuclear Regulation Authority (NRA), which had taken over from the Nuclear & Industrial Safety Agency (NISA) and the Nuclear Safety Commission (NSC), announced that henceforth nuclear power plant restart reviews would comprise both a safety assessment by the NRA and the briefing of affected local governments by the operators. The assessment would be based on safety guidelines in the [New Regulatory Requirements](http://www.nsr.go.jp/data/000067212.pdf "New Regulatory Requirements") formulated by the NRA in July 2013 after public consultation. In rulemaking, the NRA commissioners referred to the guidelines of the IAEA, Finland, France and the USA, as well as the former NISA July 2011 stress test rules and provisional 30-point measures, issued in April 2012, that were applied to the restarts of Ohi 3&4.

Apart from local government consent, the NRA procedures are:

* Construction plan application by operator.
* Permission for design change in reactor installation licence.
* Approval of plan for construction works.
* Approval of operational management system and safety programmes, and engineering work programme.
* Completion of integrated review.
* Inspection before start-up.
* Inspection after start-up.
* Final approval.

![](https://world-nuclear.org/images/articles/japan-reactor-restarts_b1aa958d.png)

Restarts have proceeded at a slower rate than previously anticipated for a number of reasons, including changing regulatory requirements. Most recently, in May 2019, the NRA ordered Kansai Electric Power to 'backfit' seven of its reactors based on a new analysis of the potential eruption of a dormant volcano, Mt. Daisen. All the affected reactors had previously cleared compatibility examinations based on new regulatory standards. A month earlier, the NRA announced it would not extend deadlines for utilities building facilities to meet new anti-terrorism guidelines. The ruling affects at least 10 reactors, and has resulted in operating reactors temporarily shutting down.

Onagawa 2 became the first BWR to restart in October 2024, followed by Shimane 2 in December. Unlike PWRs, BWRs require a filtered containment venting (FCV) system. Under the general terms of a nuclear operator's agreement with local government, prefectural approval is required for these because any use during an emergency would mean releasing radioactivity in the course of avoiding the kind of hydrogen build-up that caused the explosions at Fukushima, destroying the superstructure of three units there.

The reactor restarts are facing significant implementation costs ranging from $700 million to $1 billion per unit, regardless of reactor size or age. From FY 2011 to March 2017 the total cost was estimated at JPY 1900 billion ($17 billion) for eight companies, according to a JAIF survey.

In July 2016 the Institute of Energy Economics, Japan estimated that seven reactors could restart by the end of March 2017, 12 more in the following year to March 2018, with significant reduction in fossil fuel imports. In relation to local judicial rulings which might hinder restarts, the report noted: "As a rule, if one nuclear plant with a capacity of 1 GWe stops operation for one year in an area where annual demand is about 100 TWh, total fossil fuel costs increase by JPY 60 billion and the energy-related CO2 emissions increase by 4 million tonnes CO2 (7% locally). The average electricity unit cost will increase by JPY 400/MWh (1.8%)".

#### Decommissioning small old units

In mid-March 2015, the Ministry of Economy, Trade & Industry’s (METI's) Agency for Natural Resources and Energy (ANRE) revised the accounting provisions in the Electricity Business Act so that the electric power companies could calculate decommissioning costs in instalments of up to ten years, instead of one-time as previously. This enhanced cost recovery provision was to encourage the decommissioning of older and smaller units.

A few days later, Kansai announced that Mihama 1&2 PWRs (320 & 470 MWe net) would be retired, and Japan Atomic Power (Japco or JAPC) said it would decommission its Tsuruga 1 BWR (341 MWe), all in Fukui prefecture. Then Chugoku Electric Power announced the decommissioning of its Shimane 1 BWR (429 MWe net) in Shimane prefecture, and Kyushu Electric Power did the same for its Genkai 1 PWR (529 MWe net) in Saga prefecture. By October 2015 all would have been more than 40 years old, so that major expenditure on upgrades were hard to justify even though all of them already had operating lifetime extension approvals. Then in March 2016 Shikoku announced that Ikata 1 (538 MWe net) would be retired, due to the estimated JPY 170 billion cost of upgrades required on the 39-year-old unit for licence extension to 60 years. Announcement of Ikata 2's retirement followed in March 2018. In October 2018 Tohoku announced that Onagawa 1 BWR would be decommissioned rather than upgraded.

In May 2015 the NRA said that three faults running below Shika 1 (505 MWe BWR) may still be active. In July 2015 its expert panel said that activity could not be ruled out, and in April 2016 the NRA said that the fault could be active. Hokuriku is seeking review of the finding.

Tepco is considering the future of four Kashiwazaki-Kariwa reactors – units 1-4. These four units were shut down following a major earthquake in July 2007. Unit 1 restarted in 2010 but was shut down following the Fukushima-Daiichi accident. In June 2017 the mayor of Kashiwazaki requested that Tepco submit a decommissioning plan for at least one of units 1-5 as a pre-condition of approval for restart of units 6&7. In October 2025 Tepco said it was considering decommissioning units 1&2.

Earlier in July 2022, the NRA approved Tepco’s plans to complete the required anti-terrorism installation required to restart units 6&7. In December 2023 the NRA lifted the standing operational ban order on units 6&7 enabling Tepco to plan the restart of the units. The Niigata prefectural assembly approved a bill in December 2025 that cleared the way for TEPCO to restart one of the plant’s seven reactors. The Niigata prefectural assembly approved a bill in December 2025 that clears the way for TEPCO to restart one of the plant's seven reactors. TEPCO restarted unit 6 in January 2026.

## Energy policy

### Japan's energy situation and international dependence

Japan’s shortage of minerals and energy was a powerful influence on its politics and history in the 20th century. Today it depends on imports for over 90% of its primary energy needs. In January 2021 the country experienced critical power shortages due to heavy snowfalls and disruption to LNG supplies. The country's energy minister said supply was "touch-and-go... Solar wasn't generating. Wind wasn't generating," and that in his opinion "nuclear power will be indispensable."

As it recovered from World War II and rapidly expanded its industrial base it was dependent on fossil fuel imports, particularly oil from the Middle East (oil fuelled 66% of the electricity in 1974). This geographical and commodity vulnerability became critical due to the oil shock in 1973. At this time, Japan already had a growing nuclear industry, with five operating reactors. Re-evaluation of domestic energy policy resulted in diversification and in particular, a major nuclear construction program. A high priority was given to reducing the country's dependence on oil imports. A closed fuel cycle was adopted to gain maximum benefit from imported uranium.

Nuclear power had been expected to play an even bigger role in Japan's future. In the context of the government's 'Cool Earth 50' energy innovative technology plan in 2008, the Japan Atomic Energy Agency (JAEA) modelled a 54% reduction in CO2 emissions (from 2000 levels) by 2050 leading onto a 90% reduction by 2100. This would have led to nuclear energy contributing about 60% of primary energy in 2100 (compared with 10% in 2008), with 10% from renewables (up from 5%) and 30% fossil fuels (down from 85%). This would have meant that nuclear contributed 51% of the emissions reduction: 38% from power generation and 13% from hydrogen production and process heat.

In June 2010 METI resolved to increase energy self-sufficiency to 70% by 2030, for both energy security and CO2 emission reduction. It envisaged deepening strategic relationships with energy-producing countries. Nuclear power was to play a big part in implementing the plan, and new reactors would be required as well as achieving 90% capacity factor across all plants.

However, following the Fukushima accident, in October 2011 the government sought to greatly reduce the role of nuclear power. This appears to have been a significant factor in them losing office in 2012 elections (see later section). The new government in 2014 adopted the 4th Basic (or Strategic) Energy Plan, with 20-year perspective and declaring that nuclear energy is a key base-load power source and would continue to be utilized safely to achieve stable and affordable energy supply and to combat global warming.

In April 2015 the government announced that it wanted base-load sources to return to providing 60% of the power by 2030, with about one-third of this being nuclear. Analysis by the Research Institute of Innovative Technology for the Earth estimated that energy costs would then be reduced by JPY 2.4 trillion (USD 20.0 billion) per year compared with the present 40% base-load scenario (renewables being 30%). At the same time, it was reported that 43 coal-fired power projects were planned or under construction, totalling 21.2 GWe and expected to emit 127 million tonnes of CO2 per year. As well as the coal power revival with 20% increased consumption, Japan’s LNG imports increased from about $20 billion in 2010 to $70 billion in 2013.

The electricity market was deregulated in April 2016 at the distribution level, and the Revised Electricity Business Act 2015 required legal separation by April 2020 of generation from transmission and distribution. As the first step towards this, the Organization for Cross-Regional Coordination of Transmission Operators (OCCTO) was set up in April 2015 to function as a national transmission system operator (TSO). All power companies are required to join OCCTO. It will ensure greater interconnection among present utility networks, and increase the frequency converter capacity across the 50-60 Hz east-west divide to 3 GWe by 2021. OCCTO is expected to invest about JPY 300 billion.

### Development of nuclear program & policy 1950-2005

Japan started its nuclear research program in 1954, with ¥230 million being budgeted for nuclear energy. The Atomic Energy Basic Law, which strictly limits the use of nuclear technology to peaceful purposes, was passed in 1955. The law promoted three principles – democratic methods, independent management, and transparency – are the basis of nuclear research activities, as well as promoting international co-operation. Inauguration of the Atomic Energy Commission (JAEC) in 1956 promoted nuclear power development and utilisation. Several other nuclear energy-related organisations were also established in 1956 under this law: the Nuclear Safety Commission (NSC), the Science & Technology Agency; Japan Atomic Energy Research Institute (JAERI) and the Atomic Fuel Corporation (renamed PNC in 1967 – see below).

The first reactor to produce electricity in Japan was a prototype boiling water reactor: the Japan Power Demonstration Reactor (JPDR) which ran from 1963 to 1976 and provided a large amount of information for later commercial reactors. It also later provided the test bed for reactor decommissioning.

Japan imported its first commercial nuclear power reactor from the UK, Tokai 1 – a 160 MWe gas-cooled (Magnox) reactor built by GEC. It began operating in July 1966 and continued until March 1998.

After this unit was completed, only light water reactors (LWRs) utilising enriched uranium – either boiling water reactors (BWRs) or pressurised water reactors (PWRs) – have been constructed. In 1970, the first three such reactors were completed and began commercial operation. There followed a period in which Japanese utilities purchased designs from US vendors and built them with the co-operation of Japanese companies, who would then receive a licence to build similar plants in Japan. Companies such as Hitachi Co Ltd, Toshiba Co Ltd and Mitsubishi Heavy Industry Co Ltd developed the capacity to design and construct LWRs by themselves. By the end of the 1970s the Japanese industry had largely established its own domestic nuclear power production capacity and today it exports to other east Asian countries and is involved in the development of new reactor designs likely to be used in Europe.

Due to reliability problems with the earliest reactors they required long maintenance outages, with the average capacity factor averaging 46% over 1975-77 (by 2001, the average capacity factor had reached 79%). In 1975, the LWR Improvement & Standardisation Program was launched by the Ministry of International Trade and Industry (MITI) and the nuclear power industry. This aimed, by 1985, to standardise LWR designs in three phases. In phases 1 and 2, the existing BWR and PWR designs were to be modified to improve their operation and maintenance. The third phase of the program involved increasing the reactor size to 1300-1400 MWe and making significant changes to the designs. These were to be the Advanced BWR (ABWR) and the Advanced PWR (APWR).

A major research and fuel cycle establishment through to the late 1990s was the Power Reactor and Nuclear Fuel Development Corporation, better known as PNC. Its activities ranged very widely, from uranium exploration in Australia to disposal of high-level wastes. After two accidents and PNC's unsatisfactory response to them the government in 1998 reconstituted PNC as the leaner Japan Nuclear Cycle Development Institute (JNC), whose brief was to focus on fast breeder reactor development, reprocessing high-burnup fuel, mixed-oxide (MOX) fuel fabrication and high-level waste disposal.

A merger of JNC and JAERI in 2005 created the Japan Atomic Energy Agency (JAEA) under the Ministry of Education, Culture, Sports, Science & Technology (MEXT). JAEA is now a major integrated nuclear R&D organization.

A peculiarity of Japan's electricity grids is that on the main island, Honshu, the northeastern half including Tokyo is 50 Hz, served by Tepco (and Tohoku), the southwestern half including Nagoya, Kyoto and Osaka is 60 Hz, served by Chubu (with Kansai & Hokuriku), and there is only 1.2 GWe of frequency converters connecting them. (Japc has plants in both areas, which are separated by the Itoigawa River.) This frequency difference arises from original equipment coming from Germany and USA respectively. The interconnection was increased to 2.1 GWe by 2020, and is to be increased further to 3 GWe by 2027, funded by the utilities. Early in 2015 METI established OCCTO as a new body to balance electricity supply and demand in wide areas across Japan (see above).

### More recent energy policy 2002-2011: Focus on nuclear

Japan's energy policy was driven by considerations of energy security and the need to minimize dependence on imports. The main elements regarding nuclear power were to:

* Continue to have nuclear power as a major element of electricity production.
* Recycle uranium and plutonium from used fuel, initially in LWRs, and have reprocessing domestically.
* Steadily develop fast breeder reactors in order to improve uranium utilisation dramatically.
* Promote nuclear energy to the public, emphasising safety and non-proliferation.

In March 2002 the Japanese government announced that it would rely heavily on nuclear energy to achieve greenhouse gas emission reduction goals set by the Kyoto Protocol. A 10-year energy plan, submitted in July 2001 to METI, was endorsed by cabinet. It called for an increase in nuclear power generation by about 30 percent (13,000 MWe), with the expectation that utilities would have up to 12 new nuclear plants operating by 2011. In fact only five (5358 MWe net) came on line in that decade.

In June 2002, a new **Energy Policy Law** set out the basic principles of energy security and stable supply, giving greater authority to the government in establishing the energy infrastructure for economic growth. It also promoted greater efficiency in consumption, a further move away from dependence on fossil fuels, and market liberalisation.\*

\* In November 2002, the Japanese government announced that it would introduce a tax on coal for the first time, alongside those on oil, gas and LPG in METI's special energy account, to give a total net tax increase of some JPY 10 billion from October 2003. At the same time METI would reduce its power-source development tax, including that applying to nuclear generation, by 15.7% – amounting to JPY 50 billion per year. While the taxes in the special energy account were originally designed to improve Japan's energy supply mix, the change was part of the first phase of addressing Kyoto goals by reducing carbon emissions. The second phase, planned for 2005-07, was to involve a more comprehensive environmental tax system, including a carbon tax.

These developments, despite some scandal in 2002 connected with records of equipment inspections at nuclear power plants, paved the way for an increased role for nuclear energy.

In 2004 Japan's Atomic Industrial Forum (JAIF) released a report on the future prospects for nuclear power in the country. It brought together a number of considerations including 60% reduction in carbon dioxide emissions and 20% population reduction but with constant GDP. Projected nuclear generating capacity in 2050 was 90 GWe. This would mean doubling both nuclear generating capacity and nuclear share to about 60% of total power produced. In addition, some 20 GW (thermal) of nuclear heat would be utilised for hydrogen production. Hydrogen was to supply 10% of consumed energy in 2050 and 70% of this would come from nuclear plants.

In July 2005 the Atomic Energy Commission (JAEC) reaffirmed policy directions for nuclear power in Japan, while confirming that the immediate focus would be on LWRs. The main elements were that a "30-40% share or more" should be the target for nuclear power in total generation after 2030, including replacement of current plants with advanced light water reactors. Fast breeder reactors would be introduced commercially, but not until about 2050. Used fuel would be reprocessed domestically to recover fissile material for use in MOX fuel. Disposal of high-level wastes would be addressed after 2010.

In May 2006 the ruling Liberal Democratic Party urged the government to accelerate development of [fast breeder reactors](https://world-nuclear.org/information-library/current-and-future-generation/fast-neutron-reactors "Fast Breeder Reactor information page") (FBRs), calling this "a basic national technology".\* It proposed increased budget, better coordination in moving from R&D to verification and implementation, plus international cooperation. Japan was already playing a leading role in the Generation IV initiative, with focus on sodium-cooled FBRs, though the 280 MWe (gross) Monju prototype FBR remained shut down until May 2010, and then shut down again a few months later, with prospective restart repeatedly postponed.

\* In April 2007 the government selected Mitsubishi Heavy Industries (MHI) as the core company to develop a new generation of FBRs. This was backed by government ministries, the Japan Atomic Energy Agency (JAEA) and the Federation of Electric Power Companies of Japan. These were concerned to accelerate the development of a world-leading FBR by Japan. MHI has been actively engaged in FBR development since the 1960s as a significant part of its nuclear power business.

METI's 2010 electricity supply plan showed nuclear capacity growing by 12.94 GWe by 2019, and the share of supply growing from 2007's depressed 262 TWh (25.4%) to about 455 TWh (41%) in 2019. A regular AEC Policy Planning Council review ceased in 2011 and the Council was disbanded in 2012.

In March 2011 units 1-4 of the Fukushima Daiichi plant were seriously damaged in a major accident, hence written off for decommissioning, which removed 2719 MWe net from Tepco's – and the country's – system. In 2014 units 5&6 joined them in being decommissioned.

### Post-Fukushima energy policy changes

In July 2011 an Energy & Environment Council (Enecan or EEC) was set up by the Democratic Party of Japan (DPJ) cabinet office as part of the National Policy Unit to recommend on Japan's energy future to 2050.\* It was chaired by the Minister for National Policy to focus on future dependence on nuclear power. Its initial review was to recommend that nuclear power's contribution to electricity be targeted at 0%, 15%, or 20-25% for the medium term – a 36% option was dropped.

\* The Atomic Energy Commission (JAEC) and Central Environment Council apparently came under Enecan in 2011, and in 2012 were restored to previous status.

Meanwhile major Japanese companies such as Mitsui and Mitsubishi started investing heavily in LNG production capacity from Australia and elsewhere eg a 15% stake in Woodside's Browse LNG project for $2 billion. METI estimated that power generation costs would rise by over JPY 3 trillion ($37 billion) per year, an equivalent of about 0.7 percent of gross domestic product, if utilities replaced nuclear energy with thermal power generation. In February 2012 METI's minister said that electricity costs would need to increase up to 15% while the nuclear plants remained shut.\*

\* Meanwhile, costs of nuclear power relative to alternatives were published. The Institute of Energy Economics of Japan in 2011 put the cost of nuclear electricity generation at ¥8.5 per kWh taking into account compensation of up to ¥10 trillion ($130 billion) for loss or damage from a nuclear accident. Later in the year a draft report for Enecan estimated nuclear generation costs for 2010 to be ¥8.9 per kWh (11.4 US cents). This included capital costs (¥2.5), operation and maintenance costs (¥3.1), and fuel cycle costs (¥1.4). In addition, the estimate included ¥0.2 for additional post-Fukushima safety measures, ¥1.1 in policy expenses and ¥0.5 for dealing with future nuclear risks. The ¥0.5 for future nuclear risks is a minimum: the cost would increase by ¥0.1 for each additional ¥1 trillion ($13 billion) of damage. The ¥8.9 figure was calculated based on a model nuclear power plant using average figures from four plants operating over the period since the 2004 estimate, with an output of 1200 MWe and construction costs of ¥420 billion ($5.4 billion). Costs were calculated assuming a discount rate of 3%, a capacity factor of 70% and a 40-year operating life. The 2010 costs for fossil fuel generation, including costs for CO2 measures, ranged from ¥9.5 for coal through to ¥10.7 for LNG to ¥36.0 for oil. Projecting forward to 2030 the nuclear cost remains stable but fossil fuels costs increase significantly.

In July 2012 feed-in tariffs (FiTs) were introduced for solar and wind power. The solar FiT was ¥42/kWh (41 cents US) for ten years, which was reduced in April 2013 to ¥38 for small systems, and to be reduced again in April 2014 to ¥37/kWh residential and ¥32/kWh for systems over 10 kW. The wind FiT in 2012 was ¥23.1/kWh for units above 20 kW, and ¥57.75 for smaller units (of which none had been approved).

Enecan's "Innovative Energy and Environment Strategy" was released in September 2012, recommending a phase-out of nuclear power by 2040. Reprocessing of used fuel would continue. Enecan promised a "green energy policy framework" by the end of 2012, focused on burning imported gas (LNG) and coal, along with expanded use of intermittent renewables. This provoked a strong and wide reaction from industry, with a consensus that 20-25% nuclear was necessary to avoid very severe economic effects, not to mention high domestic electricity prices. Increased fossil fuel imports had been a major contributor to Japan's record trade deficit of JPY 2.5 trillion ($31.78 billion) in the first half of 2012. The Keidanren (Japan Business Federation) said the Enecan phase-out policy was irresponsible, as did the leadership of the Liberal Democratic Party (LDP).

Four days after indicating general approval of the Enecan plan, the DPJ cabinet backed away from it, relegating it as "a reference document" and the prime minister explained that flexibility was important in considering energy policy. The timeline was dropped. Reprocessing used nuclear fuel would continue and there would be no impediment to continuing construction of two nuclear plants – Shimane 3 and Ohma 1. A new Basic Energy Plan would be decided after further deliberation and consultation, especially with municipalities hosting nuclear plants.

However, at the end of 2012 the new Liberal Democratic Party (LDP) government promptly abolished Enecan, along with the National Policy Institute, so that METI’s Advisory Committee for National Resources and Energy became responsible for formulating energy plans, while MoE’s Central Environment Council focused on climate change matters. The new LDP prime minister ordered a ‘zero-based’ review of energy policies.

In December 2012, after a decisive victory in national elections for the Diet's lower house, with 294 out of 480 seats, the LDP took a more positive view of restarting idled nuclear power plants than its predecessor, which had seemed indifferent to electricity shortages and massive LNG and other fossil fuel import costs. (The DPJ won only 57 seats, down from 267)  The new government said it would take responsibility for allowing reactor restarts after the Nuclear Regulation Authority issued new safety standards and confirmed the safety of individual units. After abolishing Enecan it also said that abandoning reprocessing of used fuel was ruled out. Construction of Shimane 3 and Ohma 1 was to continue, and the construction of up to 12 further units could be approved.

In July 2013, elections for the Diet’s upper house gave the LDP 115 seats out of 242. Its coalition partner and another pro-nuclear party won 29 seats. This consolidated the LDP position and role in reviving the economy, including restoring power supplies. The DPJ with its policy of abandoning nuclear power by 2040 won only 59 seats. The LDP won a seat in every constituency with a nuclear power plant. In Fukushima prefecture the LDP candidate polled more than twice as many votes as the DPJ candidate. In Fukui prefecture, where Kansai Electric Power Co. has 11 units, Japan Atomic Power Co. has two units, and the government had the Monju prototype breeder reactor, an LDP candidate beat the DPJ contender, 237,000 votes to 56,000.

In February 2014 METI presented the proposed new **4th Basic (or Strategic) Energy Plan\*** with a 20-year perspective to government, which adopted it in April. It said that nuclear energy is a key base-load power source and would continue to be used safely to achieve stable and affordable energy supply and to combat global warming. Two other base-load options – hydro and geothermal – are limited, another is coal, and though cheap, its pollution works against emissions goals and represents a geopolitical risk. Natural gas/LNG was designated as intermediate between low-cost base-load and peaking oil, and capable of complementing the intermittency of renewables. Renewables were given the most space and will be "accelerated to full introduction" though without targets: solar is seen as useful to supply power during peak demand; large-scale deployment of wind could produce significant power, but this would come from northern areas and would require balancing with as-yet undeveloped storage systems. Nuclear power is presented as a quasi-domestic source that gives stable power at low operational cost and with low greenhouse gas profile. Nuclear power is an "important power source that supports the stability of the energy supply and demand structure," it said, though the degree of dependence on it should be reduced. Used fuel will receive more attention, and the nuclear fuel cycle will be promoted, including R&D on fast reactors.

\* updated every three years, under the Energy Policy law.

Later, in October 2014, at least seven of the ten major utilities limited the access of renewable energy to their grids due to potential overloads. The government addressed the problem by reducing the 2012 high fixed-price feed-in tariffs (FITs).

In January 2015 the Institute of Energy Economics, Japan (IEEJ) released a report looking at four electricity scenarios in 2030 and their implications, for about 1150 TWh (less than 10% up on 2013). They ranged from zero nuclear up to 30% nuclear contribution, with power costs for zero being 42% higher than the 30% nuclear scenario (21.0 vs 14.8 JPY/kWh), and GDP being JPY 10 trillion less. The other metric of obvious significance is energy self-sufficiency, only 7% in 2013, and ranging from 19% in zero-nuclear scenario to 28% in the 30% nuclear one (considering nuclear as quasi-indigenous, as it has been). LNG imports in the zero nuclear scenario are almost as high as in 2013, but reduce 20% from 2013 level in the 30% nuclear one. Reliance on renewables is 35% in zero-nuclear but only 20% in high-nuclear scenario, compared with 13.5% in 2013.

In June 2015 the government's **Plan for Electricity Generation to 2030** was approved. This had nuclear at 20-22% in 2030, renewables 22-24%, LNG 27% and coal 26%. It aims to reduce CO2 emissions by 21.9% by 2030 from the 2013 level, and to improve the energy self-sufficiency rate to 24.3%, from 6.3% in 2012.

In July 2015 the government approved the FY2014 Energy White paper (to March 2015). It showed that the percentage of power from fossil fuel had risen from 62% to 88% over four years, and the increased fuel cost due to nuclear shutdowns was JPY 2.3 trillion in FY2011, JPY 3.1 trillion in FY2012 and JPY 3.6 trillion in FY2013 (to March 2014). Household energy expenses had increased by an average of 13.7% over the four years.

In July 2017 the cabinet approved the draft Basic Concept on Nuclear Energy Use, developed over two years by JAEC, involving public consultation. It will provide a reference for future decisions about nuclear energy policy. It outlines eight priority activities in attaining the basic targets for using nuclear energy safely while promoting its benefits. JAEC’s previous policy advice was in July 2005 (see [above](#JAEC_July2005)), but it now plans to review and revise policy every five years.

The **5th Basic Energy Plan**,approved in July 2018, maintains the same electricity percentages as agreed in mid-2015. It presents nuclear power as “an important base-load power source contributing to the stability of the long-term energy supply-and-demand structure,” and states that necessary measures will be taken to achieve nuclear power’s share of 20-22% in the 2030 energy mix. Towards 2050 it proposes moving to a low-carbon scenario.

In October 2021 the cabinet approved the new **Plan for Electricity Generation to 2030** prepared by the Agency for Natural Resources and Energy (ANRE) and an advisory committee, following public consultation. The nuclear target for 2030 of 20-22% is unchanged from that in the 2015 plan, but renewables increase greatly to 36-38%, including geothermal and hydro. Hydrogen and ammonia are included at 1%. The plan would require the restart of another ten reactors.

Former Prime Minister Fumio Kishida in July 2022 announced that the country should consider building advanced reactors and extending operating licences beyond 60 years, as well as expediting the restart of nuclear reactors. However, in September 2022, the chairman of the NRA said that expediting restarts was unworkable due to the challenge of having to "prove something extremely difficult, which is that their facilities are able to bear the forces of nature."  
  
Prime Minister Sanae Takaichi, who took office in October 2025, has also adopted a pro-nuclear stance.

The 7th Strategic Energy Plan, approved by the cabinet in February 2025, maintains the nuclear target of around 20% for 2040, with renewables at 40-50%. Notably, this plan removed the phrase "reducing nuclear dependency as much as possible" that had appeared in previous plans since the Fukushima Daiichi accident. The plan also permits new reactor construction for the first time since 2011.

### Tsunami defences

Chubu Electric Power Co is undertaking increased tsunami and flooding protection for the Hamaoka nuclear power plant, which was closed in response to an extraordinary request from the Japanese prime minister. The plant is in a region of high seismic activity, where a large undersea earthquake can be expected within the next 30 years. Behind a row of sand dunes measuring between 10 and 15 metres high above sea level, the company has erected a new 1.6 km breakwater wall reaching 22 metres above sea level at a cost of JPY 400 billion. On the main plant site, measures will mitigate general serious flooding in case a tsunami overwhelms the breakwater. They include the waterproofing of diesel generator rooms and seawater pumps, as well as the installation of pumps in the building basements. Grid connections are to be doubled, with another set of diesel generators complete with long-term fuel supply installed on ground behind the main plant buildings about 25 metres above sea level. Spare parts for seawater pumps will be kept in a hardened building and heavy earthmoving capability will be maintained. Works for unit 4 were completed in 2016, and those for unit 3 a year later.

In April 2012 Kansai announced that it would spend more than JPY 200 billion ($2.5 billion) over four years on defences against earthquakes and tsunamis at its 11 reactors. Kansai submitted the plans to the government as a precondition for restarting its two Ohi reactors in western Japan.

Hokkaido Electric built a seawall 1.4 km long and up to 6.5 m high at its Tomari site, which is 10 m above sea level. It was completed in 2014, and one-third of its length is concrete, two-thirds a soil-cement mix, and has piles reaching bedrock. Hokkaido is building a new seawall 19 metres tall, expected to be completed around March 2027. The NRA approved Tomari 3 under post-Fukushima regulatory standards in July 2025 after a 12-year review, and Hokkaido governor approved restart in December 2025, with the company aiming to restart the reactor as soon as possible after seawall completion in 2027.

### Stress tests 2011-12

Nuclear risk and safety reassessments – 'stress tests' – along the lines of those in Europe were carried out in 2011. After some confusion the government decided that these would be in two stages.

In the primary stage, plant operators assessed whether main safety systems could be damaged or disabled by natural disasters beyond the plant design basis. This identified the sheer magnitude of events that could cause damage to nuclear fuel, as well as any weak points in reactor design. The 'tests' started from an extreme plant condition, such as operating at full power while used fuel ponds are full. From there, a range of accident progressions such as earthquakes, tsunamis and loss of off-site power were computer simulated using event trees, addressing the effectiveness of available protective measures as problems developed. Stage 1 tests had to be approved before reactors are restarted.

In the second stage even more severe events were considered, with a focus on identifying 'cliff-edge effects' – points in a potential accident sequence beyond which it would be impossible to avoid a serious accident. This stage included the effects of simultaneous natural disasters. A particular focus was the fundamental safety systems that were disabled by the tsunami of 11 March, leading to the Fukushima accident: back-up diesel generators and seawater pumps that provide the ultimate heat sink for a power plant.

The stage 1 stress test results for individual plants were considered first by NISA and then by the Nuclear Safety Commission before being forwarded to the prime minister's office for final approval. Local government must then approve restart.\*

\* Late in March 2012 NISA had received stage 1 assessments for 17 reactors – 12 PWRs and 5 BWRs. Three of these – Ohi 1&2 and Ikata 3 – had been approved by NISA and two confirmed by NSC. In September NISA finished reviewing those for six units: Hokkaido’s Tomari 1&2, Kansai’s Takahama 3&4 and Kyushu’s Sendai 1 & 2. Its findings and comments were forwarded to the new Nuclear Regulation Agency (NRA), which is now responsible for approving restarts. It appears that at least 12 stress test assessments then remained at the review stage, including Hokuriku’s Shika 1&2, Genkai 2, 3&4; Mihama 3; Tsuruga 2; Higashidori 1; Takahama 1; Kashiwazaki-Kariwa 1&7; Ohi 1 and Ikata 1.

In mid-April 2012, after a series of high-level meetings, the Japanese government approved the restart of Kansai Electric’s Ohi 3&4 reactors, and urged the Fukui governor and the Ohi mayor to endorse this decision. They restarted in July 2012 and ran through to September 2013, when they were shut down for routine maintenance.

### Economic impact of shutdowns

JAIF has said that increased fuel imports are costing about ¥3.8 to 4.0 trillion ($40 billion) per year (METI puts total fossil fuel imports at ¥9 trillion in FY2013).

Generation cost was up 56% from ¥8.6/kWh to 13.5/kWh in FY 2012. Losses across the utilities are about ¥1 trillion per year. The Ministry of Economy Trade and Industry (MITI) said in April 2013 that Japanese power companies had spent an additional ¥9.2 trillion ($93 billion) to then on imported fossil fuels since the Fukushima accident.

At the end of 2013 the Japan Business Federation (Keidanren) said that “By stopping nuclear power plants, national wealth of ¥3.6 trillion ($34.9 billion) per year is flowing overseas” due to increased fossil fuel imports. The ongoing slump of trade balance into the negative could lead to deterioration of government credit and must be addressed “with a sense of crisis.” “There can be no new capital investment in domestic industry which is power-intensive.” Keidanren urged the government to recognise that economic growth depends on stable and affordable power, and nuclear needs to be part of that rather than continuing undue reliance on LNG.

In June 2014 three major business lobbies – the Japan Business Federation (Keidanren), the Japan Chamber of Commerce and Industry, and the Japan Association of Corporate Executives (Keizai Doyukai) – submitted a written proposal to the Industry Minister seeking an early restart of the nuclear reactors. “The top priority in energy policy is a quick return to inexpensive and stable supplies of electricity”, they said.

In April 2015 the Institute of Energy Economics, Japan (IEEJ) said that an important economic role of nuclear power in the past was to reduce extreme dependence on imports, and this policy had saved Japan from sending ¥33 trillion ($276 billion) overseas. "We are effectively living on these savings and we may lose about two-thirds by 2020 if we stay on this course," due to the "drain of national wealth" caused by ¥3.6 trillion ($30 billion) being spent on imported fuel each year simply to compensate for idled reactors.

In March 2017 METI announced that the new levy on household electricity bills to support feed-in tariffs for renewables would be increased to JPY 9504 (US$ 83) per year for FY2017. The national total borne by consumers would be JPY 2140 billion ($18.77 billion).

In August 2017 the IEEJ in its *Economic and Energy Outlook for FY2018* said that it expected at least ten reactors to be online by March 2019, generating 65.6 TWh/yr and representing 7% of total electricity. These would contribute JPY 500 billion to GDP. In its high case scenario, 17 reactors were online then, providing 99 TWh/yr. As of June 2021, just 10 reactors had restarted.

### Climate change effects

Up to March 2011 the CO2 intensity of Japan’s power generation was 350 g/kWh. Over the next year, with progressive reactor shut-downs, it rose to 487 g/kWh in FY 2012. In FY 2013 the country’s overall emissions rose to 1395 million tonnes of CO2 equivalent, the highest since records began in 1990. Among Japan's climate change goals was for the electricity sector to reduce carbon intensity by 20% from 1990 levels, to 334 g/kWh CO2 on average, over the five years from 2008 to 2012.

On the eve of the UN climate change meeting in Warsaw in November 2013, Japan’s Minister of the Environment announced that his country was changing its CO2 emission reduction target from 25% lower than 1990 levels by 2020 to a 3.1% increase from then, or 3.8% reduction from 2005 levels. He cited the shutdown of Japan’s 50 nuclear power reactors, some possibly for an extended period, as a prime reason for this, forcing reliance on old fossil fuel plant.

Early in 2015 the government was considering a target of 20% reduction in greenhouse gas emissions from the 2005 level by 2030, which might be achieved with 45% of electricity generation being nuclear and renewables. The ruling LDP was reported to be in favour of 30% CO2 reduction.

In March 2017 the Ministry of Environment (MOE) said that increased construction of coal-fired plants as agreed with METI cut across CO2 emission targets (26% reduction from 2013 by 2030), and it urged utilities to employ CCS technology.

## Reactor development, 1970 onwards

In the 1970s a prototype Advanced Thermal Reactor (ATR) was built at Fugen. This had heavy water moderator and light water cooling in pressure tubes and was designed for both uranium and plutonium fuel, but particularly to demonstrate the use of plutonium. The 148 MWe unit, started up in 1978, was the first thermal reactor in the world to use a full mixed-oxide (MOX) core. It was operated by JNC until finally shut down in March 2003. Construction of a 600 MWe demonstration ATR was planned at Ohma, but in 1995 the decision was made not to proceed.

Since 1970, 30 BWRs (including four ABWRs) and 24 PWRs have been brought into operation. All the PWRs, comprising 2-, 3-, and 4-loop versions (600 to 1200 MWe classes) have been constructed by Mitsubishi.

### ABWR

The first ABWRs (of 1315 MWe) were Tokyo Electric Power Co's (Tepco's) Kashiwazaki-Kariwa units 6&7 which started up in 1996-97 and are now in commercial operation. These were built by a consortium of General Electric (USA), Toshiba and Hitachi. Four further ABWRs – Hamaoka 5, Shika 2, Shimane 3 and Ohma 1 – are in operation or under construction, and eight of the planned reactors in Japan are ABWR. These have modular construction. Hitachi-GE talks of its 1500 MWe class "global unified ABWR", and is developing a high-performance 1800 MWe class ABWR. Hitachi was also developing 600, 900 and 1700 MWe versions of the ABWR

### APWR

The 1500 MWe class [APWR design](http://www.iaea.org/NuclearPower/Downloadable/aris/2013/10.APWR%28Mitsubishi%29.pdf "APWR design") is a scale-up of the four-loop PWR and has been developed by four utilities with Mitsubishi Heavy Industries (MHI) and (earlier) Westinghouse. The APWR is in the process of being licensed in Japan with a view to the first 1538 MWe units being constructed at Tsuruga (units 3&4). Approval by Fukui prefecture was given in March 2004. It is simpler than present PWRs, combines active and passive cooling systems to greater effect, and has over 55 gigawatt days per tonne (GWd/t) burn-up. It will be the basis for the next generation of Japanese PWRs. The APWR+ is 1750 MWe and has full-core MOX capability.

MHI lodged an application for US design certification in January 2008. It was expected to be completed in February 2016, but Mitsubishi delayed the NRC schedule "for several years." The US-APWR was selected by TXU (now Luminant) for Comanche Peak, Texas, and by Dominion for its North Anna plant, though Mitsubishi withdrew from the Comanche Peak project, and both are now on hold. The 1700 MWe EU-APWR was accepted as meeting European Utility Requirements in 2014. (MHI also participated in developing the Westinghouse AP1000 reactor, but after Westinghouse was sold to Toshiba, MHI is developing PWR technology independently.)

### Atmea1

The Atmea1 has been developed by the Atmea joint venture established in 2007 by Areva NP and Mitsubishi Heavy Industries to produce an evolutionary 1100-1150 MWe net (3150 MWt) three-loop PWR using the same steam generators as EPR. This has 37% net thermal efficiency, 157 fuel assemblies 4.2 m long, 60-year life, and the capacity to use mixed-oxide fuel only. Fuel cycle is flexible 12 to 24 months with short refuelling outage and the reactor has load-following (100-25% range) and frequency control capability. It has three active and passive redundant safety systems and an additional backup cooling chain, similar to EPR. It has a core-catcher and is available for high-seismic sites. The first units are likely to be built at Sinop in Turkey, then possibly in Vietnam. Following an 18-month review, the French regulator ASN approved the general design in February 2012. Canadian design certification is under way.

### Next-generation LWR

In mid-2005 the Nuclear Energy Policy Planning Division of the Agency for Natural Resources and Energy instigated a two-year feasibility study on development of next-generation LWRs. The new designs, based on ABWR and APWR, were to lead to a 20% reduction in construction and generation costs and a 20% reduction in spent fuel quantity, with improved safety and three-year construction and longer life. They would have at least 5% enriched fuel and a design operating lifetime of 80 years with a 24-month operating cycle. In 2008 the Nuclear Power Engineering Center was established within the Institute of Applied Energy to pursue this goal, involving METI, FEPC and manufacturers. The project was expected to cost JPY 60 billion over eight years, to develop one BWR and one PWR design, each of 1700-1800 MWe. The government, with companies including Toshiba and Hitachi-GE, was to share the cost of these. The PWR was to have thermal efficiency of 40%. Basic designs were to be finished by 2015, with significant deployment internationally by 2030.

Next-generation PWR

In September 2022 MHI announced a conceptual design for an advanced 1200 MWe PWR called SRZ-1200. It is being developed in cooperation with Kansai Electric Power, Kyushu Electric Power, Hokkaido Electric Power, and Shikoku Electric Power. MHI said that the design will aim to “enhance operational flexibility” to work alongside “variable electric power sources”. The consortium aims to commercialize the design by the mid-2030s.

**Japanese reactors under construction**

| Reactor | Type | Gross capacity | Utility | Construction start | Operation\* |
| --- | --- | --- | --- | --- | --- |
| Shimane 3 | ABWR | 1373 MWe | Chugoku | December 2005, suspended 2011 | Applied to NRA for safety checks August 2018 |
| Ohma 1 | ABWR | 1383 MWe | EPDC/J-Power | May 2010, suspended 3/11 to 10/12 | Construction estimated to restart 2022 and finish 2028/2029 |
|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Total: 2 |  | 2756 MWe |  |  |  |

\* Latest announced commercial operation.

**Japanese reactors planned and proposed**

| Reactor | Type | MWe gross  (each) | Utility | Start \*  construction |
| --- | --- | --- | --- | --- |
| Higashidori 1 Tepco | ABWR | 1385 | Tepco | deferred |
| Total Planned: 1 |  | **1385 MWe** |  |  |
| Tsuruga 3 | APWR | 1538 | JAPC | deferred |
| Tsuruga 4 | APWR | 1538 | JAPC | deferred |
| Kaminoseki 1 | ABWR | 1373 | Chugoku | 6/2012  (deferred 3/11) |
| Sendai 3 | APWR | 1590 | Kyushu | 3/2014  (deferred 4/11) |
| Higashidori 2 Tepco | ABWR | 1385 | Tepco | deferred |
|
| Hamaoka 6 | ABWR | 1380 | Chubu | deferred |
| Higashidori 2 Tohoku | ABWR | 1385 | Tohoku | deferred |
| Kaminoseki 2 | ABWR | 1373 | Chugoku | 2018  (deferred 6/11) |
| Total Proposed: 8 |  | **11,562 MWe** |  |  |

\* According to METI FY2010 plan, unless updated by company. TBD = to be determined.  
Tsuruga 3&4 and Tepco's Higashidori 1 were undergoing final safety assessment by regulatory authorities.

## Licence extension and 30-year reviews

Power reactors are licensed for 40 years and then require approval for licence extension in 10-year increments. At 30 years, the regulator must review and approve the utility’s ageing management plan for each reactor. Following the Fukushima accident, the government tightened requirements for approving licence extension beyond 40 years, which became the default limit. Operators can apply for up to 20-year licence extensions from 40 years, to 60 years as in the USA. However, as of August 2022 Japan was considering the possibility of lifetime extensions of an additional 20 years to 80-year operating lifetimes.

In November 2022 the NRA announced an in-principle approval of METI’s proposal to extend the operational lifetimes of nuclear power plants at decade-long intervals, commencing after 30 years of operation. That month, METI also presented a so-called ‘exclusion plan’ to the Atomic Energy Subcommittee, outlining plans to maintain the 60-year cap on reactor lifespan, although this would not include those years when reactors were offline following the 2011 Fukushima disaster.

In December 2022 the NRAapproved a draft of a new rule that would allow the country's nuclear power reactors to operate beyond the 60-year limit by excluding the time they spent offline for inspections (the law came into force in June 2025). Later that month, the government adopted a new policy maximizing the use of existing reactors by restarting as many of them as possible and prolonging the operating lifetimes of ageing units, whilst also developing advanced reactors. In February 2023 the cabinet approved the new policy, whilst also giving the green light to build new reactors. In May 2023, Japan's parliament passed a law allowing offline periods to not be counted towards the 60-year operating lifetime limit, subject to approval by the economy minister. Inspections would be carried out by the Nuclear Regulation Authority every 10 years after 30 years of operation.

### Ten-year extensions

The Nuclear & Industrial Safety Agency (NISA) granted a 10-year licence extension for Fukushima Daiichi 1 in February 2011, after technical review and some modifications in 2010. However, this was destroyed in the 2011 accident.

In March 2010, local government approved a licence extension to 2016 for JAPC's Tsuruga 1, which started commercial operation in March 1970 in order to bridge the gap until units 3&4 at Tsuruga came online. (Construction of the two units was due to start later in 2010 and commissioning of the first was due in March 2016.)

Then Kansai applied for a 10-year licence extension from November 2010 for its Mihama 1 PWR. NISA approved Kansai's long-term maintenance and management plan for the unit and granted a licence extension accordingly in June 2010, which was then agreed by local government. Kansai in July 2011 applied for approval of its ageing management plan for Mihama 2, and NISA granted this in July 2012. In February 2014 the NRA approved Chugoku’s Shimane 1 BWR for a ten-year extension. In October 2014 Kyushu applied for a ten-year extension for Genkai 1, but in April 2015 all five of these were shut down.

Kyushu applied for a licence extension of Sendai 1 in December 2013, and this with its ten-year ageing management plan was approved by the NRA in August 2015. It applied for Sendai 2 in November 2014 and this was approved 12 months later.

In March 2012 NISA and METI approved Shikoku Electric's strategy for managing ageing and hence approved operation of its Ikata 2 PWR for 40 years, and in 2014 approved the same for Tepco’s Fukushima Daini 2 and Tohoku’s Onagawa 1 BWR. Despite the approval for continued operation of Fukushima Daini 2, Tepco in July 2019 decided to decommission all four units at the plant. In June 2014 Kansai sought approval for Takahama 4, which joined Takahama 3 and Kyushu’s Sendai 1 in being reviewed at 30 years and approved for age-related degradation issues. In January 2015 the NRA approved these issues being handled together with engineering work involved with Kansai meeting safety requirements for the restart of the two Takahama units. In November 2015 the NRA approved ten-year licence extensions for Takahama 3&4, as well as for Sendai 2. In October 2024 the NRA approved a ten-year licence extension for Takahama 1.

### 60-year licences

Kansai applied for a 20-year licence extension of Mihama 3 and if it had not been granted it was to be finally shut down in December 2016. In October 2016 the NRA approved a major works programme and in November granted the 20-year licence extension, to 2036. In June 2017 Kansai confirmed its plans for upgrading the reactor by 2020 to take it to 60 years. The required work was completed in September 2020.

Kansai applied for a ten-year cold shutdown of Takahama 2 to defer any decision on its future beyond its 40th anniversary in 2015, and in April 2015 the NRA approved a ten-year licence extension for it. In November 2014 the NRA approved a 10-year licence extension for Takahama 1. Then Kansai applied to extend the operating lifetimes of both Takahama units (1&2) to 60 years. The NRA confirmed that they meet new safety standards, with seismic rating upgraded to 700 Gal, and in June 2016 the NRA approved licence extension to 60 years, the first units to achieve this under the 2013 revised regulations. In September 2020 Kansai announced that upgrade work on Takahama 3 was completed, allowing the unit to operate for an additional 20 years to a total of 60 years. In May 2023 Kansai announced that it had applied for 20-year operating licence extensions for Takahama 3&4. In May 2024 the NRA approved the extensions, making them the seventh and eighth reactors permitted to operate beyond 40 years. Local approvals followed in July 2024.

In November 2017 Japco applied to the NRA to extend the licence for the Tokai 2 BWR by 20 years. The extension was granted in November 2018.

In November 2023 the NRA approved 20-year licence extensions for Sendai 1&2. In October 2024 the NRA approved Kansai Electric's plan to continue operating Takahama 1 for another 10 years, making it the first reactor in Japan to be allowed to operate beyond 50 years.

## Particular plants: under construction and planned

Chugoku's Shimane 3 was to enter commercial operation in December 2011, but this was delayed to March 2012 because control rod drives had to be returned to the manufacturer for modification and cleaning. The start-up date was then deferred until evaluation of the Fukushima accident could be undertaken. It was 94% complete when construction was suspended in March 2011. Chugoku finished building a 15 m high sea wall in January 2012, and then extended this to a total length of 1.5 km to also protect Shimane 1&2. With construction now almost complete, Chugoku in May 2018 sought permission from the local government to apply to the NRA for pre-operation safety assessment to enable it to start. Chugoku submitted its application to the NRA in August 2018 following local government approval. Seismic rating of the unit is 1000 Gal.

The Electric Power Development Corp (EPDC), also known as J-Power, is building its Ohma nuclear plant – 1383 MWe Advanced Boiling Water Reactor (ABWR) – in Aomori prefecture. Construction of unit 1 was due to start in August 2007 for commissioning in 2012, but was delayed by more stringent seismic criteria, then delayed again in 2008, and commenced in September 2009. Seismic criterion is now 650 Gal. Construction was suspended for 18 months after the Fukushima tsunami, with it 38% complete – JSW had completed manufacturing the major components. J-Power in mid-2012 affirmed its intention to complete and commission the unit, and announced resumption of work in October. In September 2015 the company said that it planned to complete construction by the end of 2021, and have it in commercial operation in 2022. It applied to the NRA for a safety review in December 2014, and in 2016 aspects of the safety review were being negotiated with the NRA. In September 2018, J-Power announced that the screening process of post-Fukushima safety standards had taken longer than anticipated.

Apart from the Fugen experimental Advanced Thermal Reactor (ATR), Ohma would be the first Japanese reactor built to run solely on mixed oxide (MOX) fuel incorporating recycled plutonium. It would be able to consume a quarter of all domestically-produced MOX fuel and hence make a major contribution to Japan's 'pluthermal' policy of recycling plutonium recovered from used fuel.

Tepco struggled for two years with the loss of its Kashiwazaki-Kariwa capacity – nearly half of its nuclear total – following the mid 2007 earthquake. While the actual reactors were undamaged, some upgrading to improve earthquake resistance and also major civil engineering works were required before they resumed operation. Overall, the FY2007 (ending March 2008) impact of the earthquake was estimated at JPY 603.5 billion ($5.62 billion), three quarters of that being increased fuel costs to replace the 8000 MWe of lost capacity. The Nuclear & Industrial Safety Agency (NISA) approved the utility's new seismic estimates in November 2008, and conducted final safety reviews of the units as they were upgraded and then restarted, the first in May 2009. Tepco undertook seismic upgrades of units 1 and 5, the two oldest, restarting them in 2010. In 2011 a one-kilometre southern seawall was constructed, but apparently some of this is on sediments and assumed Ss of 650 Gal. However the southern part of the site, with units 1-4, has proposed Ss of 2300 Gal. Units 5-7 are rated 1200 Gal since January 2016.

Review of earthquake design criteria meant that construction of Tepco's Higashidori 1&2 and Fukushima Daiichi 7&8 were delayed, requiring investment in coal-fired (1.6 GWe) and gas plant (4.5 GWe of LNG) to fill the gap. However, METI approved Tepco's Higashidori 1 in December 2010 and NISA approved it in January 2011, allowing Tepco to begin work on the site. Work stopped after the Fukushima accident, though JSW started manufacturing major components in 2011 after the accident. Tepco before this had forecast its overall nuclear capacity increasing from 24% of total in FY2007 to 27% of total in 2017, and nuclear output increasing from 23% to 48% of total supply in the same period. It then announced suspension of plans to build ABWR units 7&8 at Fukushima Daiichi. In 2012 it was reported that it could not afford to proceed with Higashidori, and in December 2017 Tepco said it was seeking a partner to build and operate the plant.

Tohoku's Higashidori 2 on the adjacent site as Tepco's was scheduled for construction start in 2016, though the company has yet to decide whether to proceed. The site is in Higashidori-mura, on the Pacific coast, near Mutsu on the eastern side of the Shimokita Peninsula in Aomori prefecture. The company is building a 2km seawall to protect the site.

Chubu's Hamaoka 1&2 reactors, closed in 2001 and 2004 respectively for safety-related upgrades, remained shutdown following the mid-2007 earthquake. In December 2008 the company decided to write them off (JPY 155 billion, $1.7 billion) and build a new one there. Modifying the two 1970s units to current seismic standards would cost about double the above amount and be uneconomic. The 540 and 840 MWe units (515 & 806 MWe net), which started operation in 1976 & 1978, were to be replaced by a single new one, Hamaoka 6**,** to start operating in 2020, though in April 2011 the company deferred construction start until 2016, and it has been delayed further since. Hamaoka is the company's only nuclear site, though it said that it recognizes that nuclear needs to be a priority for both "stable power supply" and environment. However, the shutdown of units 3-5 in May 2011 by government edict for modification has set back plans.

Japan Atomic Power Co first submitted plans for its Tsuruga units 3&4 to NISA in 2004, and after considerable delay due to siting problems, they were approved by the Fukui prefecture. JAPC then submitted a revised construction application based on new geological data to NISA in October 2009. The approval process, including safety checks by METI, was expected to take two years, but the process then passed to the new NRA. In December 2012 the NRA said that a fault zone directly beneath the existing Tsuruga unit 2 reactor (operating since 1987) was likely to be seismically active, and in May 2013 it endorsed an expert report saying that the reactor poses a risk in the event of a major earthquake. An international review group investigating the faults with a massive excavation concluded in 2014 that the faults were not active, but the NRA accepted another report in March 2015 saying that there was an active fault, making its restart unlikely. In July 2024 the Nuclear Regulation Authority concluded that the reactor could not meet safety standards due to the active fault. The matter may have implications for the planned units 3&4 and also for unit 1.

JAPC would need to spend JPY 140 billion ($1.75 billion) on civil engineering for site preparation, including land reclamation and a breakwater before construction start for units 3&4. Construction – estimated at JPY 770 billion ($7.4 billion) – was due to start in March 2012 with commercial operation in 2017-18. This would be the first Mitsubishi APWR plant, with each unit 1538 MWe.

Kyushu Electric Power Co. filed a draft environmental statement with METI in October 2009 for its Sendai 3 plant, also an APWR, but 1590 MWe. The Ministry of Environment told METI that the project was "absolutely essential, not just for ensuring energy security and a stable supply of electricity... but also to reduce greenhouse gas emissions." Local government has given approval. In 2010 METI began the process of designating it a key power source development project. Kyushu had expected to start construction in March 2014, for commercial operation in December 2019.

Chugoku Electric Power Co plans to build two Kaminoseki ABWR nuclear power units on Nagashima Island on the Seto Inland Sea coast in Kaminoseki Town, Yamaguchi prefecture. Some site works commenced but then halted after the Fukushima accident – 40% of the site is to be reclaimed land. The small island community of Iwaishima a few kilometres away has long opposed the plant. In October 2012 Chugoku confirmed its intention to proceed and awaited a safety assessment from the NRA. In August 2016 the Yamaguchi prefectural government renewed a licence for Chugoku to reclaim land for the plant. In June 2019 it was reported that Chugoku Electric Power Co had changed the proposed start date of new reactor construction at Kaminoseki from July 2019 to January 2023. Chugoku has recently completed geological surveys at the site that have determined there has been no recent seismic activity in the area.

Tohoku Electric Power Co planned to build the Namie-Odaka BWR nuclear power plant from 2017 at Namie town in Minami Souma city in the Fukushima prefecture on the east coast, but indefinitely deferred this project early in 2013.

### Further proposed plants

In September 2010 Tepco, Japan's biggest utility, had said it planned to invest JPY 2.5 trillion ($30.5 billion) on low-carbon projects domestically by 2020 to generate more than half of its power free of carbon. Most of this capacity was to be nuclear.

Early in 2011 Chubu Electric Co announced that it intended to build a new 3000-4000 MWe nuclear plant by 2030, with site and type to be decided.

Kansai began to consider expanding the Mihama plant in 2010 but shelved early work in March 2011. However, following the decommissioning of two old Mihama reactors in 2015, Kansai and local government discussed reviving earlier proposals to replace them at that site with units 4&5. In July 2025 Kansai announced it would start again, beginning with a site survey to assess the possibility of new build within current regulatory requirements. The survey would represent the first work on an entirely new reactor project in Japan since the Fukushima accident.

## Fast neutron reactors

The Joyo experimental fast breeder reactor (FBR) has been operating successfully since it reached first criticality in 1977, and has accumulated a lot of technical data. It is 140 MWt, and has been shut down since 2007 due to damage to some core components. The upper core structure had to be replaced, and this was completed in 2014. See also information paper on [Japan's Nuclear Fuel Cycle](https://world-nuclear.org/information-library/country-profiles/countries-g-n/japan-nuclear-fuel-cycle "Japan's Nuclear Fuel Cycle").

The 280 MWe Monju prototype FBR reactor started up in April 1994 and was connected to the grid in August 1995, but a sodium leakage in its secondary heat transfer system during performance tests in December 1995 meant that it was shut down after only 205 days actual operation, until May 2010.\* It then operated for 45 days but late in August 2010 it shut down again, due to refuelling equipment falling into the reactor vessel. This was retrieved in June 2011 and replaced with a new one, allowing potential restart. It had three coolant loops, used MOX fuel, and produced 714 MWt, 280 MWe gross and 246 MWe net.

\* A Supreme Court decision in May 2005 cleared the way for restarting it in 2008, but this was put back to May 2010. METI confirmed early in 2010 that Monju's seismic safety under new guidelines was adequate, and NSC approved its restart and operation for a three-year period, prior to "full operation" in 2014.

Monju's oversight and ownership passed to the JNC (now JAEA), and the Minister for Science & Technology was eager to see it restarted. In September 2014 the NRA approved JAEA’s management reorganisation for Monju, with its restart being contingent upon NRA approval of a new maintenance program. However, in November 2015 the NRA called for the ministry to find a new owner and operator for Monju, due to failure of safety checks. It said that the JAEA was “not competent to operate” Monju. The JAEA responded to NRA officials, asserting: "No entities other than the JAEA can manage Monju." MEXT was reported to be in favour of persevering with Monju, while METI was keen to scrap it, partly to get rid of the bad image. The Fukui governor reminded the panel that Monju was positioned in the national Strategic Energy Plan to become an international research base for studies on waste volume reduction, the mitigation of danger, and other improvements to technologies related to nuclear non-proliferation. The cabinet rejected a FY2016 budget request from MEXT for JPY 10 billion to prepare Monju for restart. In December 2016 the government confirmed plans to decommission it, despite the Fukui local government being adamantly opposed to this. The government cited the need to spend more than JPY 540 billion ($ 4.6 billion) to meet the NRA’s new regulatory standards as its reason for the decision.

The government’s draft decommissioning plan is expected to take 30 years and cost more than JPY 375 billion ($3.2 billion). This includes JPY 225 billion for maintenance, JPY135 billion for dismantling the plant and JPY15 billion for defuelling to mid-2022 and preparations for dismantling.

JAEA also undertakes FBR and related R&D at Oarai in Ibaraki prefecture, near Tokai-mura.

### Fast neutron reactor policy

Originally in 1960s the concept was to use fast breeder reactors (FBRs) burning MOX fuel, making Japan virtually independent regarding nuclear fuel. But FBRs proved uneconomic in an era of abundant low-cost uranium, so development slowed and the MOX program shifted to thermal LWR reactors.

From 1961 to 1994 there was a strong commitment to FBRs, with PNC as the main agency. In 1967 FBR development was put forward as the main goal of the Japanese nuclear program, along with the ATR. In 1994 the FBR commercial timeline was pushed out to 2030, and in 2005 commercial FBRs were envisaged by 2050. This evidently remains the plan: a demonstration breeder reactor of 500-750 MWe by 2025, and commercial 1500 MWe units by 2050.

In 1999 JNC initiated a program to review promising concepts, define a development plan by 2005 and establish a system of FBR technology by 2015. The parameters were: passive safety, economic competitiveness with LWR, efficient utilisation of resources (burning transuranics and depleted U), reduced wastes, proliferation resistance and versatility (include hydrogen production). Utilities were also involved, with CREIPI and JAEA.

Phase 2 of the JNC study focused on four basic reactor designs: sodium-cooled with MOX and metal fuels, helium-cooled with nitride and MOX fuels, lead-bismuth eutectic-cooled with nitride and metal fuels, and supercritical water-cooled with MOX fuel. All involve closed fuel cycle, and three reprocessing routes were considered: advanced aqueous, oxide electrowinning and metal pyroprocessing (electrometallurgical refining). This work is linked with the Generation IV initiative, where Japan has been playing a leading role with sodium-cooled FBRs.

In 2016 the government’s Conference on Fast Reactor Development met several times to formulate policy. It reiterated the need to promote the nuclear fuel cycle based on the government’s Strategic Energy Plan, as well as R&D on fast reactors to develop world-class technology. Further aims are to commercialise and establish fast reactors as the international standard, while achieving high levels of safety and economy at the same time.

In December 2018 the Ministry of Economy, Trade and Industry (METI) finalised an updated plan for developing domestic fast reactors and had it approved by relevant ministers. The plan calls for a new fast reactor to be in service by 2050, with its specifications to be decided about 2024. The future of collaboration on the French Astrid project will have a bearing on this.

Some work has been done by JAEA on reprocessing of used fuel from fast reactors, with higher plutonium levels. FEPC envisages aqueous reprocessing which recovers uranium, plutonium and neptunium together, and minor actinides being added to the MOX pellets for burning. JAEA is part of a project under the Generation IV International Forum investigating the use of actinide-laden fuel assemblies in fast reactors – The Global Actinide Cycle International Demonstration (GACID). See also information page on [Generation IV Nuclear Reactors](https://world-nuclear.org/information-library/nuclear-fuel-cycle/nuclear-power-reactors/generation-iv-nuclear-reactors "Generation IV Nuclear Reactors").

### Fast reactor designs

In April 2007 the government selected Mitsubishi Heavy Industries (MHI) as the core company to develop a new generation of FBRs, notably the **Japan Sodium-cooled Fast Reactor** (JSFR) concept, though with breeding ratio less than 1:1. This would be a large unit to burn actinides with uranium and plutonium in oxide fuel. It could be of any size from 500 to 1500 MWe. The demonstration JSFR model was due to be committed in 2015 and on line in 2025, and a 1500 MWe commercial unit was proposed by MHI for 2050. From July 2007 Mitsubishi FBR Systems (MFBR) has operated as a specialist company. It was responsible for a joint bid with Areva for work on the US Advanced Recycling Reactor project and is part of the Japanese involvement with the French Astrid project.

In May 2014 Japan committed to support the development of the French **Astrid** fast reactor project, and in August 2014 JAEA, Mitsubishi Heavy Industries and Mitsubishi FBR Systems concluded an agreement with the French Atomic Energy Commission (CEA) and Areva NP to progress cooperation on Astrid. Astrid was initially envisaged as a 600 MWe prototype of a commercial series of 1500 MWe sodium-cooled fast reactors which is planned to be deployed from about 2050 to utilise the abundant depleted uranium available by then and also burn the plutonium in used MOX fuel. Astrid arises from a 2006 French government commission to the CEA to develop a fast neutron reactor which is essentially a Generation IV version of the sodium-cooled type which already has 45 reactor-years' operational experience in France. A final decision on construction is envisaged in 2019 (see R&D section in the [Japan Fuel Cycle](https://world-nuclear.org/information-library/country-profiles/countries-g-n/japan-nuclear-fuel-cycle "Japan Fuel Cycle") paper).

In June 2018 the French government stated that Astrid will have its capacity scaled down from the initially planned 600 MWe to between 100 and 200 MWe to reduce construction costs and also because development of a commercial fast reactor was no longer a high priority. Toshiba said that the smaller Astrid would be a step back for Japan's fast reactor development process, possibly forcing the country to build its own larger demonstration reactor in Japan rather than rely on Astrid.

## Public opinion

A number of public opinion polls were taken in April and May 2011 following the Fukushima accident. Those in April showed around 50% supported the use of nuclear power at present or increased levels, but as the crisis dragged on the May polls showed a reduction in support to around 40% and a growth in opinion to over 40% of those wanting to decrease it. A steady 15% or so through May-June 2011 wanted it abolished. In March 2013, the proportion opting for increase or status quo had dropped to 22%, while 53% wanted to decrease it and 20% wanted to abolish it.

A poll taken in February 2015 by the Mizuho Information & Research Institute of Japan asked whether or not the respondent would use nuclear-generated electricity if the costs were the same or less than they were that month, and 67% said "yes”. Only 32% replied in the negative. This contrasts with a number of media polls with voluntary and hence non-representative participation, and the distortion is compounded by a 2012 news media survey finding that 47 of the 50 most popular press outlets in Japan said they were antinuclear.

In February 2023 a survey conducted by *Asahi Shimbun* found that 51% of the respondents in Japan were in favour of restarting nuclear plant operations with 42% opposed.

In December 2025 a Jiji Press opinion poll in Japan found that 44.7% of respondents support restarting nuclear power plants across the country while 26.1% oppose restarts and 29.2% reported no clear opinion.

---

## Notes & references

### General references

JAIF Atoms in Japan, various  
H. Tanaka, Japan's nuclear power program, World Nuclear Association Symposium 2006  
JAIF summary of 4th Strategic Energy Plan April 2014

## Related information

[Japan: Nuclear Fuel Cycle](https://world-nuclear.org/information-library/country-profiles/countries-g-n/japan-nuclear-fuel-cycle)
  
[Fukushima Daiichi Accident](https://world-nuclear.org/information-library/safety-and-security/safety-of-plants/fukushima-daiichi-accident)
  
[Nuclear Power Plants and Earthquakes](https://world-nuclear.org/information-library/safety-and-security/safety-of-plants/nuclear-power-plants-and-earthquakes)
  
[Fast Neutron Reactors](https://world-nuclear.org/information-library/current-and-future-generation/fast-neutron-reactors)
  
[Hiroshima, Nagasaki, and Subsequent Weapons Testing](https://world-nuclear.org/information-library/safety-and-security/non-proliferation/hiroshima-nagasaki-and-subsequent-weapons-testin)

Contents

---

[Electricity sector](#electricity-sector)
[Nuclear power industry](#nuclear-power-industry)
[Energy policy](#energy-policy)
[Reactor development, 1970 onwards](#reactor-development-1970-onwards)
[Licence extension and 30-year reviews](#licence-extension-and-30-year-reviews)
[Particular plants: under construction and planned](#particular-plants-under-construction-and-planned)
[Fast neutron reactors](#fast-neutron-reactors)
[Public opinion](#public-opinion)
[Notes & references](#notes-amp-references)
[Related Information](#related-information)
