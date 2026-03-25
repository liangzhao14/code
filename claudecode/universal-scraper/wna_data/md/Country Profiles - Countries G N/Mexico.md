---
source: https://world-nuclear.org/information-library/country-profiles/countries-g-n/mexico
downloaded: 2026-03-24 23:54:10
---

[HOME](https://world-nuclear.org/) / [Information Library](https://world-nuclear.org/information-library) / [country profiles](https://world-nuclear.org/information-library/country-profiles) / [countries-g-n](https://world-nuclear.org/information-library/country-profiles/countries-g-n) / Mexico

country profiles

# Nuclear Power in Mexico

Updated Wednesday, 23 July 2025

* **Mexico has two nuclear reactors generating over 3% of its electricity.**
* **Its first commercial nuclear power reactor began operating in 1989.**
* **There is some government support for expanding nuclear energy to reduce reliance on natural gas.**

2![](https://world-nuclear.org/images/icon-operable-reactor.png)

Operable  
Reactors

1,552 MWe

0![](https://world-nuclear.org/images/icon-construction-reactor.png)

Reactors Under  
Construction

0 MWe

0![](https://world-nuclear.org/images/icon-down-reactor.png)

Reactors  
Shutdown

0 MWe

#### Operable nuclear power capacity

var RDB\_WIDGET\_CONFIG\_widget\_t6xou = {
"id": "widget\_t6xou",
"type": "chart\_status",
"query": {
"query": {
"filtered": {
"filter": {
"bool": {
"must": [
{
"terms": {
"reactor.country.exact": [
"Mexico"
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
"base": "//reactordb.world-nuclear.org",
"include": "/embed.html",
"settings": {
"chart": "bar",
"start": "1970",
"end": "2099",
"status": "operable",
"primary": "operational\_reference\_unit\_power",
"fallback": "reference\_unit\_power\_capacity\_net",
"label": "Reference Unit Power MWe",
"height": "300",
"left": "80",
"distance": "0"
}
}

## Electricity sector

Per capita electricity consumption in Mexico has slightly increased from about 1750 kWh in 2000 to about 2600 kWh in 2023.

!function(){"use strict";window.addEventListener("message",function(a){if(void 0!==a.data["datawrapper-height"]){var e=document.querySelectorAll("iframe");for(var t in a.data["datawrapper-height"])for(var r,i=0;r=e[i];i++)if(r.contentWindow===a.source){var d=a.data["datawrapper-height"][t]+"px";r.style.height=d}}})}();

Mexico is rich in hydrocarbon resources. It is increasingly reliant on natural gas, particularly from the USA, and this is a central consideration in its energy policy. The Federal Electricity Commission (CFE) has invested in new gas-fired plant and converting coal plants to gas. In addition, it is investing in intermittent renewables and promoting the construction of major natural gas pipelines.

## Nuclear power industry

**Operable reactors in Mexico**

var RDB\_WIDGET\_CONFIG\_widget\_3e8jp = {
"id": "widget\_3e8jp",
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
"Mexico"
]
}
},
{
"terms": {
"reactor.status.exact": [
"Operable"
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
"base": "//reactordb.world-nuclear.org",
"include": "/embed.html",
"settings": {
"order": {
"field": "reactor.alternate\_name",
"dir": "asc",
"sort\_type": "exact"
},
"limit": "10",
"countryPageTemplate": "//www.world-nuclear.org/country/default.aspx/{country}",
"reactorPageTemplate": "//www.world-nuclear.org/reactor/default.aspx/{reactor}",
"reactor": [
{
"field": "reactor.name",
"display": "Reactor Name",
"formatting": "reactor\_link"
},
{
"field": "reactor.model",
"display": "Model"
},
{
"field": "reactor.process",
"display": "Reactor Type"
},
{
"field": "reactor.reference\_unit\_power\_capacity\_net",
"display": "Net Capacity (MWe)",
"formatting": "number"
},
{
"field": "reactor.construction\_start",
"display": "Construction Start",
"formatting": "year\_month"
},
{
"field": "reactor.first\_grid\_connection",
"display": "First Grid Connection",
"formatting": "year\_month"
}
]
}
}

![](https://world-nuclear.org/images/articles/143472b4-1142-4d35-a743-3f40ddacd45b.png)

### Nuclear industry development

Mexico's interest in nuclear energy was made official in 1956 with the establishment of the National Commission for Nuclear Energy (CNEN). That organization took general responsibility for all nuclear activities in the country except the use of radioisotopes and the generation of electric power. The [Federal Electricity Commission](https://www.cfe.mx/Pages/Index.aspx "Federal Electricity Commission") (CFE), one of the two state-owned electricity companies, was assigned the role of future nuclear generator.

Preliminary investigations to identify potential sites for nuclear power plants began in 1966, led by CNEN and CFE, and in 1969 CFE invited bids for proven power plant designs with a capacity of around 600 MWe. In 1972 a decision to build was made, and in 1976 construction began at Laguna Verde on two 654 MWe General Electric boiling-water reactors (BWRs).

Although Mexican industry did not supply major components for the Laguna Verde plant, Mexican companies undertook the civil engineering work and Mexican staff maintain the reactor and train to operate it at CFE's simulator.

The CNEN was later transformed into the National Institute on Nuclear Energy (INEN), which in turn was split in 1979 into the National Institute of Nuclear Research (ININ), Mexican Uranium (Uramex) and the National Commission on Nuclear Safety and Safeguards (CNSNS). Uramex's functions were taken over by the Ministry of Energy in 1985.

In February 2007 the CFE signed contracts with Spain's Iberdrola Engineering and also Alstom to fit new turbines and generators to the Laguna Verde plant at a cost of $605 million. The main modifications consisted of a turbine and condenser retrofit and the replacement of the electric generator, main steam reheater and the feedwater heater. With approval from the CNSNS, the reactors were uprated progressively by 138 MWe each from 2008 to January 2011. As a first step, 11.6 MWe uprates to both units were achieved in 2007 through better flow control. In February 2011 Iberdrola announced that both units were operating at 820 MWe gross. Their operating lifetime was also extended to 40 years. The project was completed early in 2013.

In May 2025 Nissan Mexicana signed a two-year contract with the CFE to obtain 90% of the electricity required for its three manufacturing plants from Laguna Verde.

#### Operating lifetime extension

In July 2020 Mexico's energy minister approved a 30-year extension to the operating licence of Laguna Verde 1, allowing it to operate until July 2050. Prior to its approval, plant operator Federal Electricity Commission (*Comisión Federal de Electricidad*, CFE) carried out a series of upgrades. An application for a similar extension was lodged for unit 2 and granted in August 2022, allowing the unit to operate until April 2055.

### New nuclear capacity

High-level government support exists for an expansion of nuclear energy, primarily to reduce dependence on natural gas, but also to cut carbon emissions – until 2011 the country's energy policy called for increasing carbon-free power generation from 27% to 35% of total by 2024. The CFE in May 2010 had four scenarios for new power generation capacity from 2019-28, ranging from a heavy reliance on coal-fired power plants to meet growing demand, to a low-carbon scenario that called for big investments in nuclear and wind power.

Under the CFE's most aggressive scenario, up to ten nuclear power plants were to be built so that nuclear energy supplied nearly a quarter of Mexico's power needs by 2028. An earlier proposal was for one new nuclear unit to come online by 2015 with seven more to follow it by 2025 to bring nuclear share of electricity up to 12% then. Cost studies showed nuclear being competitive with gas at about 4 ¢/kWh in all scenarios considered. However, with low gas prices in 2010 a decision on building new nuclear capacity was delayed until 2012.

CFE in November 2010 was talking about building six to eight 1400 MWe units, the first two at Laguna Verde. With the release of the 2012 energy policy, the government urged looking beyond low gas prices to consider building two more reactors at Laguna Verde or elsewhere in Veracruz state, as a first step in expanding nuclear capacity to 2026. This call was repeated in mid-2014. In mid-2015 the Development Programme of the National Electric System included plans to commission new capacity including three nuclear power plants, with a tentative schedule to enter commercial operation by 2026, 2027 and 2028. Then in December 2019 the proposal was for two more reactors at Laguna Verde and two more on the Pacific coast.

An [August 2022 Secretariat of Energy report](https://www.gob.mx/sener/articulos/reporte-anual-del-potencial-de-mitigacion-de-gei-en-el-sector-electrico) showed annual electricity production from nuclear energy doubling to 24 GWh by 2035.

In the longer term, Mexico may look to employ small reactors to provide power and desalinate seawater for agricultural use.

ININ has previously presented ideas for a plant consisting of three IRIS reactors sharing a stream of seawater for cooling and desalination. With seven reverse-osmosis desalination units served by the reactors, 140,000m3 of potable water could be produced each day, as well 840 MWe.

## Fuel cycle

Since incorporating Uramex, the Ministry of Energy has had responsibility for uranium prospecting, which it delegates to the Mineral Resources Board. Mexico has reasonably assured resources of about 2500 tonnes of uranium but this has not been mined to date.

A uranium milling plant operated on an experimental basis at Villa Aldana, in the Chihuahua region at the end of the 1960s but has now been decommissioned. Tailings were disposed of at Pena Blanca.

Under Mexican legislation, nuclear fuel is the property of the state and is under the control of the CNSNS.

### Radioactive waste management

The government of Mexico, through the Ministry of Energy is responsible for the storage and disposal of nuclear fuels and radioactive waste irrespective of their origin.

The Energy Ministry is beginning to take administrative and budgetary steps to create a national company to manage its radioactive waste. In 2018 Mexico became a contracting party to the IAEA Joint Convention on the Safety of Spent Fuel Management and on the Safety of Radioactive Waste Management.

Used nuclear fuel from the Laguna Verde reactors is stored underwater at the site. The storage pools have been re-racked to extend capacity, and in 2016 Holtec completed construction of the independent spent fuel storage installation (ISFSI). The ISFSI used Holtec HiStorm FW canisters on a pad large enough for 130 of them.

An engineered near-surface disposal site for low-level waste (LLW) operated at Piedrera between 1985 and 1987. In that time, 20,858m3 of waste was stored.

A collection, treatment and storage centre for LLW has operated at Maquixco since 1972.

## Research & development

The main nuclear research organization in Mexico is the National Nuclear Research Institute (NNRI). NNRI has operated a 1000kW Triga Mk III research reactor since November 1968.

The University Autonoma de Zacatecas has a subcritical Chicago Modelo 9000 assembly used for training, commissioned in 1969.

A nuclear cooperation agreement between Mexico and Canada was signed in 1995 for the exchange of information in R&D, health, safety, emergency planning and environmental protection. It also provides for the transfer of nuclear material, equipment and technology and the rendering of technical assistance.

## Regulation, safety and non-proliferation

The 1984 Act on Nuclear Activities states that the government, through the Ministry of Energy, is responsible for establishing the framework for the use and development of nuclear energy and technology, in accordance with the national energy policy.

The National Commission on Nuclear Safety and Safeguards (CNSNS) is a semi-autonomous body under the authority of the Ministry of Energy which takes the role of regulator. CNSNS is responsible for ensuring the proper application of regulations and safeguards for nuclear and radiation safety and for physical protection of nuclear and radiological installations to ensure public safety.

CNSNS is also responsible for revising, evaluating and approving the criteria for the siting, design construction operation and decommissioning of nuclear installations, proposing the relevant regulations. It has the power to amend of suspend the licenses of nuclear facilities, which are granted on CNSNS approval through the Ministry of Energy.

Mexico has ratified the IAEA Convention on Nuclear Safety.

### Non-proliferation

The Mexican Constitution states that nuclear energy may only be used for peaceful uses and this is reiterated in the 1984 Act on Nuclear Activities.

Mexico ratified the Nuclear Non-Proliferation Treaty in 1969 and the Additional Protocol in 2004. It is also party to the 1979 Convention on the Physical Protection of Nuclear Material, ratified in 1988. Furthermore, Mexico is the depository of the 1967 Treaty for the Prohibition of Nuclear Weapons in Latin America (the Tlatelolco Treaty) and has been party to the Treaty since 1967.

---

## Notes & references

IAEA, Country Nuclear Power Profiles.  
Nuclear Legislation in OECD Countries, Regulatory and Institutional Framework for Nuclear Activities, OECD/NEA, 2003.  
Nuclear Energy Agency, [Radioactive Waste Management Programmes in OECD/NEA Member Countries](https://www.oecd-nea.org/rwm/pubs/2005/5248-rwm-programmes-member-countries.pdf "Radioactive Waste Management Programmes in OECD/NEA Member Countries"), OECD (2005)  
Nuclear Engineering International, October 2004.

Contents

---

[Electricity sector](#electricity-sector)
[Nuclear power industry](#nuclear-power-industry)
[Fuel cycle](#fuel-cycle)
[Research & development](#research-amp-development)
[Regulation, safety and non-proliferation](#regulation-safety-and-non-proliferation)
[Notes & references](#notes-amp-references)
