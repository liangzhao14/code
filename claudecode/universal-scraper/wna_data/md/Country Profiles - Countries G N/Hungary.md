---
source: https://world-nuclear.org/information-library/country-profiles/countries-g-n/hungary
downloaded: 2026-03-24 23:53:44
---

[HOME](https://world-nuclear.org/) / [Information Library](https://world-nuclear.org/information-library) / [country profiles](https://world-nuclear.org/information-library/country-profiles) / [countries-g-n](https://world-nuclear.org/information-library/country-profiles/countries-g-n) / Hungary

country profiles

# Nuclear Power in Hungary

Updated Tuesday, 10 February 2026

* **Hungary has four nuclear reactors generating about half of its electricity.**
* **Its first commercial nuclear power reactor began operating in 1982.**
* **Construction of the first of two large Russian-designed units commenced in February 2026.**

4![](https://world-nuclear.org/images/icon-operable-reactor.png)

Operable  
Reactors

1,916 MWe

1![](https://world-nuclear.org/images/icon-construction-reactor.png)

Reactors Under  
Construction

1,100 MWe

0![](https://world-nuclear.org/images/icon-down-reactor.png)

Reactors  
Shutdown

0 MWe

#### Operable nuclear power capacity

var RDB\_WIDGET\_CONFIG\_widget\_t6xou = { "id": "widget\_t6xou", "type": "chart\_status", "query": { "query": { "filtered": { "filter": { "bool": { "must": [ { "terms": { "reactor.country.exact": [ "Hungary" ] } } ] } }, "query": { "match\_all": {} } } } }, "base": "//reactordb.world-nuclear.org", "include": "/embed.html", "settings": { "chart": "bar", "start": "1970", "end": "2099", "status": "operable", "primary": "operational\_reference\_unit\_power", "fallback": "reference\_unit\_power\_capacity\_net", "label": "Reference Unit Power MWe", "height": "300", "left": "80", "distance": "0" }}

## Electricity sector

**Total generation (in 2023):**35.5 TWh

**Generation mix:** nuclear 15.9 TWh (45%); natural gas 7.3 TWh (20%); solar 6.9 TWh (19%); coal 2.5 TWh (7%); biofuels & waste 1.9 TWh (5%); wind 0.6 TWh (2%).

**Import/export balance:**11.1 TWh net import (20.0 TWh imports; 8.9 TWh exports)

**Total consumption:**40.2 TWh

**Per capita consumption:** c. 4200 kWh in 2023

*Source: International Energy Agency and The World Bank. Data for year 2023.*

Imports are mainly from Slovakia, Ukraine and Austria, whilst most exports go to Croatia. Total installed capacity was about 9.9 GWe in 2020. The government plans to increase the nuclear proportion of electricity generation to about 60%.

## Nuclear power industry

**Operable power reactors in Hungary**

var RDB\_WIDGET\_CONFIG\_widget\_3e8jp = { "id": "widget\_3e8jp", "type": "table\_reactor", "query": { "query": { "filtered": { "filter": { "bool": { "must": [ { "terms": { "reactor.country.exact": [ "Hungary" ] } }, { "terms": { "reactor.status.exact": [ "Operable" ] } } ] } }, "query": { "match\_all": {} } } } }, "base": "//reactordb.world-nuclear.org", "include": "/embed.html", "settings": { "order": { "field": "reactor.alternate\_name", "dir": "asc", "sort\_type": "exact" }, "limit": "50", "countryPageTemplate": "/nuclear-reactor-database/summary/{country}", "reactorPageTemplate": "/nuclear-reactor-database/details/{reactor}", "reactor": [ { "field": "reactor.name", "display": "Reactor Name", "formatting": "reactor\_link" }, { "field": "reactor.model", "display": "Model" }, { "field": "reactor.process", "display": "Reactor Type" }, { "field": "reactor.reference\_unit\_power\_capacity\_net", "display": "Net Capacity (MWe)", "formatting": "number" }, { "field": "reactor.construction\_start", "display": "Construction Start", "formatting": "year\_month" }, { "field": "reactor.first\_grid\_connection", "display": "First Grid Connection", "formatting": "year\_month" } ] }}

![](https://world-nuclear.org/images/articles/6c5de815-9682-47bc-8d98-3f8385afd3cc.png)

Hungary's National Atomic Energy Committee (OAB) was set up in 1956 and the country's first research reactor went critical in 1959. An interstate treaty between Hungary and the Soviet Union to build a nuclear power plant was signed in 1966 and, in 1967, the Paks site 100 km south of Budapest was chosen. An 880 MWe nuclear plant was ordered in 1971, and construction of the first two units by Atomenergoexport started in 1974, with the second two in 1979. The four VVER-440 reactors (model V-213) started up between 1982 and 1987.

**Under construction nuclear reactors in Hungary**

var RDB\_WIDGET\_CONFIG\_widget\_lo9f4 = {
"id": "widget\_lo9f4",
"type": "table\_reactor",
"query": {
"query": {
"filtered": {
"filter": {
"bool": {
"must": [
{
"terms": {
"reactor.country.exact": [
"Hungary"
]
}
},
{
"terms": {
"reactor.status.exact": [
"Under Construction"
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
"order": {
"field": "reactor.name",
"dir": "asc",
"sort\_type": "exact"
},
"limit": "10",
"countryPageTemplate": "//www.world-nuclear.org/country/default.aspx/{country}",
"reactorPageTemplate": "//www.world-nuclear.org/reactor/default.aspx/{reactor}",
"reactor": [
{
"field": "reactor.name",
"display": "Reactor name",
"formatting": "reactor\_link"
},
{
"field": "reactor.model",
"display": "Model"
},
{
"field": "reactor.process",
"display": "Reactor type"
},
{
"field": "reactor.reference\_unit\_power\_capacity\_net",
"display": "Net capacity (MWe)"
},
{
"field": "reactor.construction\_start",
"display": "Construction start"
}
]
}
}

### Paks

The Paks plant is owned and operated by MVM Paks Nuclear Power Plant Ltd, which is a subsidiary company of state-owned MVM Hungarian Electricity Ltd (*Magyar Villamos Művek*, MVM).

#### Operating lifetime extension

The design lifetime of the reactors is 30 years, so the four units at Paks would have reached the end of their service lifetimes between 2012 and 2017. A feasibility study on extending the operational lifetimes of the units by 20 years, carried out in 2000 (and updated in 2005), found no technical or safety objection to a 50-year service lifetime. In November 2005, the Hungarian Parliament overwhelmingly supported a 20-year operating lifetime extension project for Paks. The Hungarian Atomic Energy Authority (HAEA or OAH) has now approved the operating lifetime extension of all four reactors – unit 1 in December 2012 (licensed to 2032), unit 2 in November 2014 (to 2034), unit 3 in December 2016 (to 2036), and unit 4 in December 2017 (to 2037).

In December 2022 parliament approved plans to further extend the lifespan of the four units at Paks, with 170 votes in favour of the legislation, eight votes against, and one abstention. Government approval enables the state to begin preparations to operate the Paks nuclear power plant for an additional 20 years.

In December 2023 MVM Paks Nuclear Power Plant Ltd notified the European Union of its intention to extend the operating lifetimes of the four units at Paks to 70 years.

#### Capacity increase

Though originally 440 MWe gross, the Paks units were progressively uprated in the 1990s and early 2000s to 470 MWe. An 8% uprate was then carried out between 2002 and 2009 to give 500-510 MWe gross. A contract signed in May 2007 with Atomstroyexport relates to this work[1](#Notes_references "See Reference 2"), in particular: new design fuel assemblies, modernisation of the in-core monitoring system, the reconstruction of the primary pressure control system, and the modification of the turbine and the turbine control system.

In July 2015, Ukraine's Turboatom was contracted to upgrade low-pressure turbines and replace high-pressure turbines at all four Paks units, the latter to yield an increase in power. GE has a contract over 2013-2021 to refurbish the eight generators, and in January 2017, completed the fifth.

## New nuclear power capacity

### Paks II

In the 1980s, the government planned to construct two VVER-1000 units as Paks 5&6 (each 950 MWe net). Preparations were almost completed when the project was cancelled in 1989 due to decreased power demand.

In 1996-97, Paks Nuclear Power Plant proposed building a further one or two units of 600-700 MWe capacity – either the Westinghouse AP600 design, the AECL Candu-6, or the Atomstroyexport/ Siemens VVER-640. This was later rejected by MVM because it did not fit government policy at that time.

Ten years later, with the need to build about 6000 MWe of new generating capacity by 2030, new nuclear plant was again considered, and two 1000 MWe units for the Paks site were proposed – referred to as Paks II. In March 2009, the Hungarian Parliament (330 for; 6 against; 10 abstentions) gave preliminary approval to this, though some foreign investment would be needed. Paks expected to issue an invitation to tender in 2012, with a decision in 2013, and the government set up a project company MVM Paks Nuclear Power Plant Ltd or MVM Paks II as a subsidiary of state-owned MVM in 2012. It was considering five PWR reactor types: Areva's EPR; the Areva-Mitsubishi Atmea1; Atomstroyexport's VVER-1000 or -1200; the Westinghouse AP1000[2](#Notes_references)and Korea's APR-1400. It was not keen on first-of-a-kind designs and hoped to avoid the need for cooling towers. The new units should be capable of load-following. A nuclear cooperation agreement with South Korea was signed in October 2013.

Rather than proceeding with open tender, in January 2014 the government signed an agreement with Rosatom to build two reactors at Paks. The government said that the EU had already approved a draft plan for building the units of up to 1200 MWe each, at a likely cost of around €12 billion. The units were originally scheduled to start operating in 2025/2026.

A €10 billion financing deal from Russia was agreed in February to cover 80% of the anticipated project cost, with Hungary to repay the loan over 21 years of operation, starting in 2026. The interest rate would be set below 4% for 11 years then 4.5% then 4.95%. In a 256-29 vote the parliament approved the finance deal. The loan agreement was adjusted in May 2019 such that Hungary would start repaying only once the two reactors are connected to the grid. Earlier in February 2017 the Russian President said that Russia was prepared to finance 100% of the plant if necessary. In May 2021 Hungary's finance ministry stated that it had agreed with the Russian government that the loan repayments would commence in 2031.

Earlier in December 2014 MVM Paks II signed three implementation agreements with NIAEP-ASE of Nizhny Novgorod. These formalize the design, procurement and construction parameters for the new units, conditions related to their operation and maintenance support, and details regarding fuel supply and the handling and storage of used nuclear fuel.

An environmental permit was issued in September 2016, and a site licence was issued in March 2017.

Fuel is to be supplied solely by Rosatom for the first 10 years of operation. This aspect of the deal was challenged by the EU’s Euratom Supply Agency (ESA), backed by the European Commission (EC), on the basis of there being no alternative supplier for the particular fuel design in the event of a supply disruption. The contract was later approved by the ESA with the duration of the exclusive contract with Rosatom being cut from 20 to 10 years, after which time alternative suppliers will be able to bid to supply fuel.

In November 2015, the EC announced it had started legal action against Hungary over the Rosatom contract for the Paks II project (Paks 5&6), expressing concerns about its compatibility with EU public procurement rules but clearing the matter in November 2016. The EC also opened a state aid investigation into the project financing for Paks II, but in March 2017 the EC approved it, as being in line with state aid rules. The new plant is to be “functionally and legally” independent of the existing plant.

In February 2018, Austria launched a lawsuit against the EC for its approval of Hungarian state subsidies for the two new reactors to be constructed at Paks. (In 2015, Austria, which has no nuclear power plants, unsuccessfully launched a similar action against the EC over its approval of the UK's Hinkley Point C project. In 2019 Austria objected to the start-up of Mochocve 3&4 in Slovakia.) In November 2022 the EU General Court dismissed the lawsuit brought forward by the Austrian government. However, in September 2025 the European Court of Justice backed an appeal by Austria on the grounds that the EC had not properly considered whether the award of a direct contract to Nizhny Novgorod Engineering complied with EU public procurement rules. The ECJ ruling annuls the original approval of the state aid, and the process has technically returned to the stage of the EC reviewing Hungary’s proposed state subsidies. Hungarian ministers and Rosatom said it would not delay or halt the project, and said first concrete was expected before the end of 2025.Later that month, Rosatom confirmed that the company would continue to implement the Paks II project in partnership with Hungarian counterparts.

A licence application for Paks 5&6 was submitted to the regulator in July 2020. In December 2020 Rosatom reported that it expected to receive the final permit to begin construction by Q4 2021. However, in September 2021, the HAEA announced that it needed more time to carry out analyses and assessments before deciding whether to issue a construction licence. The initial licence evaluation period was one year, and a three-month extension was later granted. The HAEA did not specify the length of extra time needed in its September 2021 announcement. In December 2021 Hungary's government said it expected construction to start in 2022.

In January 2022, project company MVM submitted an application to build the containment building of the first unit at Paks II. MVM said that the submission should be approved before the end of May. In August 2022 the HAEA issued the construction licence for the two VVER-1200 PWRs at Paks II, to be built by Rosatom.

In January 2023 energy minister Csaba Lantos announced a two-year delay to the construction of Paks II, pushing the completion date to 2032. The following month, Foreign Minister Peter Szijjarto accused Germany of blocking shipments of nuclear equipment for the construction of Paks II. German company Siemens Energy is responsible for shipping the control equipment to the Paks site, but the German government failed to provide the permit for the export licence.

In September 2023 Rosatom director general Alexei Likhachev announced that first concrete would be poured in early 2025. Construction licences were issues by the HAEA in November 2025, and first concrete for Paks II-1 was poured in February 2026.

Earlier in April 2025 forging of parts of the reactor pressure vessel for unit 6 began at Rosatom's AEM-Spetsstal plant in St Petersburg. Production of the first turbine elements for unit five also began at Arabelle Solutions in Belfort, France.

In June 2025 the HAEA granted permission to resume construction activity in the entire working pit area for the planned first unit, following a temporary halt after a perimeter wall collapsed in January. Also in June 2025, the Foreign Affairs and Trade Minister said that US sanctions restrictions related to the Paks II project had been lifted and that a US Treasury general licence authorizing certain civil nuclear energy transactions would support progress on Paks II.

### Small modular reactors

In August 2025 Hunatom signed a letter of intent with Poland's Synthos Green Energy to establish a framework for joint work on development of up to ten GE Vernova Hitachi [BWRX-300](https://world-nuclear.org/information-library/nuclear-power-reactors/small-modular-reactors/small-modular-reactor-smr-design-database?detail=BWRX-300) small modular reactors. Poland's Synthos Green Energy is project developer for BWRX-300 reactors in the region.

**Planned power reactors in Hungary**

| Reactor | Type | MWe gross | Start construction | First power |
| --- | --- | --- | --- | --- |
| Paks II-2 | VVER-1200/V-527 | 1200 | 2026 | 2032 |

*The V-527 is based on the V-491 at Leningrad II.*

Beyond Paks 5&6, consideration of future options for Hungary involves the so-called Visegrád Four group countries – Poland, Slovakia, the Czech Republic and Hungary – which are cooperating closely on nuclear power issues, including in research into future reactor designs and infrastructure development.

## Fuel cycle

Hungary has some uranium resources around the Mecsek deposit in the south of the country, but no present production. The Mecsek underground mine near Pécs operated from 1958 to 1997. Initially ore was shipped to Estonia for milling, but from 1963 it was milled on site and the concentrate was exported to the Soviet Union. A total of about 21,000 tU was produced at an average recovery of 50-60%. Since 1997, the mine has been decommissioned and remediated at considerable expense (about €110 million).

In August 2008, the Australian company Wildhorse Energy Ltd joined with state-owned Mecsekérc to assess the feasibility of restarting uranium mining at Mecsek Hills. This led to an agreement with Mecsekérc and Mecsek‐Öko signed in October 2009 which covered all of the uranium resources in the Mecsek region over some 72 sq km[a](#Notes_references "See Note b"). A further joint venture agreement with both government-owned groups was signed early in 2012, bringing Mecsek‐Öko's MML-E licence (the former uranium mine area) together with Wildhorse's Pecs licence to give combined JORC-compliant inferred resource of 30,000 tU at 0.061%U. The company expected to increase this substantially. The government commenced a social, technological, and environmental inquiry into the feasibility of restarting uranium production. However, having completely written off the project, in October 2014 the company cited “lack of progress and high operational costs” as its reason not to proceed and to divest the project.

Wildhorse was also developing an underground coal gasification project nearby at Mecsek Hills, in conjunction with uranium plans. In October 2014 it terminated the project.

### Fuel supply

Historically, Hungary's nuclear fuel supply has come from TVEL in Russia. In October 2024 a long-term supply contract was signed with Framatome to fuel the four reactors at the Paks plant.

Hungary’s MVM Group signed a contract with Westinghouse in November 2025 for the supply of VVER-440 fuel from 2028. The contract is part of measures to diversify supply for the Paks nuclear power Plant.

#### 2003 fuel damage incident

A programme to chemically clean partially used fuel was curtailed following an accident, which was rated Level 3 on the International Nuclear Event Scale (INES)[b](#Notes_references "See Note c"). In 2001, unit 2 at Paks was the first ever reactor to be reloaded with fuel that had been chemically cleaned[3](#Notes_references "See Reference 4"); however, in April 2003, at the same unit, 30 fuel assemblies were badly damaged inside a cleaning tank due to insufficient cooling[4](#Notes_references "See Reference 5"). The assemblies overheated in the cleaning tank which was submerged in the transfer pond so that most became deformed with burst cladding, releasing a lot of radioactivity into the water, with noble gases into the plant area. Five batches of fuel had been cleaned before the incident, to remove magnetite corrosion products from the steam generators, which impeded coolant flow in the core. Radioactive gases were emitted through the stack for several days, and the reactor was out of service until the end of 2006. In 2014 the damaged fuel was sent to Mayak in Russia for reprocessing.

### Waste management

Although preparations are being made for direct disposal of used fuel without reprocessing, there is no policy decision on reprocessing and it appears unlikely that used nuclear fuel will be reprocessed. In the past, some used fuel has been returned to Russia for reprocessing, but without repatriation of separated fissile materials.

Since 1998, a levy on nuclear power production is paid into the Central Nuclear Financial Fund to pay for storage and disposal of radioactive waste, including used fuel, and decommissioning. At the end of 2015 this fund totalled HUF 254 billion (€807 million).

The state-owned body responsible for all waste management, waste disposal and decommissioning is the Public Limited Company for Radioactive Waste Management (*Radioaktív Hulladékokat Kezelő Kft.*, RHK Kft), formerly the Public Agency for Radioactive Waste Management (PURAM)[c](#Notes_references "See Note d").

Under 1995 policy, used fuel is stored in pools at Paks for five years then transferred to an interim (50-year) dry storage facility there. This has 20 vaults with capacity for 9308 fuel assemblies. Plans included provision for a further eight vaults to be added by 2025.

For low- and intermediate-level waste, the Püspökszilágy Radioactive Waste Treatment and Disposal Facility (RWTDF) began operation in 1977[d](#Notes_references "See Note e"). The RWTDF also accepted waste from Paks until 1996 and the 5040 m3 capacity facility became full in 2005.

Following the decision to construct a new repository for low- and intermediate-level waste from Paks[e](#Notes_references "See Note f"), PURAM carried out geological investigations over a decade, and finally focused on a repository site in granite in the south of the country, about 30 km from Pécs. In mid-2005, the residents of Bátaapáti voted to approve construction of a repository for low- and intermediate-level waste there, and this was approved by Parliament. In December 2006, the government declared the Bátaapáti site an "investment of extraordinary significance", paving the way for accelerated licensing. The €150 million surface facilities of the National Radioactive Waste Repository were opened in October 2008, and construction of underground vaults 200-250 m deep for short-lived intermediate-level waste allowed operation from December 2012.[5](#Notes_references "See Reference 6") It will eventually accommodate 40,000 cubic metres of waste.

Paks waste that was sent to RWTDF at Püspökszilágy in the north of the country will eventually be moved to Bátaapáti National Radioactive Waste Repository for final disposal, so that waste disposed at RWTDF will only derive from institutional (*i.e.* non-power) sources.

For long-lived ILW and high-level waste, a claystone formation near Buda in the southwest Mecsek Mountains is being investigated, and a preliminary safety analysis has been made for a deep geological repository there[f](#Notes_references "See Note g"). It is expected to begin operation after 2065.

## Research & development

The Atomic Energy Research Institute (KFK AEKI) operates the Budapest research reactor of 10 MW, which started up in 1959 and was rebuilt in 1991. In 2009, it was converted to operate on low-enriched uranium. The Technical University of Budapest (BUTE) operates a training reactor of 100 kW. A zero-power critical assembly has been decommissioned.

## Regulation, safety and non-proliferation

Under the amended Atomic Energy Act 1996, the Hungarian Atomic Energy Authority (HAEA or OAH) is responsible for safety policy, safeguards arrangements, licensing, safety, wastes and regulation. The Nuclear Safety Directorate of the HAEA is responsible for the safety of nuclear installations. In December 2014, HAEA signed a new cooperation agreement with Russia’s Rostechnadzor, updating a 2001 one.

Handling of radioactive materials and wastes, together with radiation protection generally, is regulated by the Minster of Health. However, ensuring low levels of release and exposure are among HAEA's responsibilities.

The Hungarian Energy Office advises on tariffs for both grid network and the public service, and these are set by the Minister for Economy & Transport.

### Non-proliferation

Hungary is a party to the Nuclear Non-Proliferation Treaty (NPT) since 1969 as a non-nuclear weapons state. It is a member of the Nuclear Suppliers Group and since May 2004, of Euratom. The Additional Protocol in relation to its safeguards agreements with the International Atomic Energy Agency came into force in 2000.

---

## Notes & references

### Notes

a. WildHorse executed a cooperation agreement with Mecsekérc and Mecsek‐Öko in October 2009 to develop the Mecsek Hills Uranium Project Area, which includes WildHorse’s Pécs uranium licence and the MML‐E licence held by Mecsek‐Öko. The Hungarian state-owned mining agencies Mecsek‐Öko and Mecsekérc hold the mining concession for the areas covering the closed Mecsek uranium mine, which joins the western boundary of the WildHorse Pécs and Abaliget licences, acquired in 2006. The Mecsek Hills Project Area has an exploration target of 41-54,000 tonnes U3O8, with a grade range of 0.08‐0.12% U3O8.

Mecsek‐Öko is responsible for the environmental remediation, reclamation and monitoring works associated with the historic Mecsek uranium industry. Mecsekérc is involved in radioactive waste disposal and various environmental remediation projects, as well as geological, hydrogeological and mineral resource prospecting. [[Back](#Notea "Back")]

b. Chemical cleaning of partially used fuel assemblies is only known to have been carried out on used fuel at Paks. The fuel assemblies supplied by Russian manufacturer Mashinostroitelny Zavod (MSZ) had been in the reactor core for between 0.5 and 2.5 years. During this time, corrosion products had built up on the assemblies, restricting the flow of coolant. A method of cleaning these fuel assemblies was developed by Framatome ANP by adapting the chemical oxidation reduction decontamination (CORD) process, which uses permanganic acid (for oxidation) and oxalic acid (for reduction). [[Back](#Noteb "Back")]

c. In January 2008, the Public Agency for Radioactive Waste Management (PURAM) became the Public Limited Company for Radioactive Waste Management. The agency is often still referred to as PURAM. [[Back](#Notec "Back")]

d. An isotope burial site at Solymár, located about 20 km north of Budapest, operated from 1960 until 1975, by which time a total volume of 900 m3 radioactive waste had been accepted. Between 1977 and 1980, the waste was moved to the Püspökszilágy facility and the storage facility in Solymár was decommissioned. [[Back](#Noted "Back")]

e. Expansion of the Püspökszilágy Radioactive Waste Treatment and Disposal facility (RWTDF) to meet the requirements of the Paks power plant was ruled out for a number of reasons. Paks Nuclear Power Plant then attempted to find an alternative site but initially failed when, in 1990, the local citizens of Ófalu opposed the construction of a facility there. As an interim solution, the capacity of RWTDF was expanded and, between 1992 and 1996, waste from Paks was sent to RWTDF.

After extensive surveys covering the whole country, in 1996, the region of Üveghuta (not far from the Paks nuclear plant) was chosen for further investigation. Site studies over the next few years eventually resulted in a final report in 2003 that concluded that the Bátaapáti (Üveghuta) site is geologically appropriate for the disposal of low- and intermediate-level waste (LILW). Underground investigation work commenced at the beginning of 2005 and Parliament gave preliminary approval by an overwhelming majority later that year. A 2006 government decree declared construction of the Bátaapáti waste repository to be a priority investment project. [[Back](#Notee "Back")]

f. Investigations in the Boda Claystone in the west part of Mecsek began in 1993. However, in 1999, the government rejected a proposal to establish an underground research laboratory there. A new investigation program in the same area commenced in 2003. Subject to the results of the site qualification test program and regulatory approval, construction of an underground research laboratory is expected to commence by 2020. [[Back](#Notef "Back")]

### References

1. [More power for Paks](https://www.world-nuclear-news.org/Articles/More-power-for-Paks "More power for Paks, World Nuclear News (25 May 2007)"), World Nuclear News (25 May 2007) [[Back](#Ref1 "Back")]  
2. [MVM Zrt Board of Directors accepts the concept for preparation of capacity expansion](http://www.atomeromu.hu/hu/Sajtoszoba/Sajtokozlemenyek/Sajtokozlemenyeink/Lapok/SajtokozlemenyReszletek?hirId=29 "Paks Nuclear Power Plant press release in Hungarian (26 February 2010)"), Paks Nuclear Power Plant press release (26 February 2010) [[Back](#Ref2 "Back")]  
3. [Chemical cleaning of fuel assemblies](https://www.neimagazine.com/features/featurechemical-cleaning-of-fuel-assemblies/ "Chemical cleaning of fuel assemblies, Nuclear Engineering International (30 August 2001)"), Nuclear Engineering International (30 August 2001) [[Back](#Ref3 "Back")]  
4. [INES level 3 for Paks](https://www.neimagazine.com/news/newsines-level-3-for-paks "INES level 3 for Paks, Nuclear Engineering International (17 May 2003)"), Nuclear Engineering International (17 May 2003) [[Back](#Ref4 "Back")]  
5. [Hungary inaugurates permanent waste repository](https://www.world-nuclear-news.org/WR_Hungary_inaugurates_permanent_waste_repository_0910081.html "Hungary inaugurates permanent waste repository"), World Nuclear News (9 October 2008) [[Back](#Ref5 "Back")]

### General sources

Public Limited Company for Radioactive Waste Management (RHK, formerly PURAM) website ([www.rhk.hu](https://rhk.hu/ "RHK Kft. website"))  
Paks Nuclear Power Plant website ([www.atomeromu.hu](http://www.atomeromu.hu/hu/Lapok/default "Paks"))  
Hungarian Atomic Energy Authority (HAEA) [website](https://www.oah.hu/web/v3/HAEAportal.nsf/web?openagent "Hungarian Atomic Energy Authority")  
Country Nuclear Power Profiles: [Hungary](https://cnpp.iaea.org/pages/index.htm "IAEA Country Nuclear Power Profiles: Hungary"), International Atomic Energy Agency

Contents

---

[Electricity sector](#electricity-sector)
[Nuclear power industry](#nuclear-power-industry)
[New nuclear power capacity](#new-nuclear-power-capacity)
[Fuel cycle](#fuel-cycle)
[Research & development](#research-amp-development)
[Regulation, safety and non-proliferation](#regulation-safety-and-non-proliferation)
[Notes & references](#notes-amp-references)
