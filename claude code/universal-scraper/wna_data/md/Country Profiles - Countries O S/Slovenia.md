---
source: https://world-nuclear.org/information-library/country-profiles/countries-o-s/slovenia
downloaded: 2026-03-24 23:54:42
---

[HOME](https://world-nuclear.org/) / [Information Library](https://world-nuclear.org/information-library) / [country profiles](https://world-nuclear.org/information-library/country-profiles) / [countries-o-s](https://world-nuclear.org/information-library/country-profiles/countries-o-s) / Slovenia

country profiles

# Nuclear Power in Slovenia

Updated Tuesday, 16 September 2025

* **Slovenia has shared a nuclear power reactor with Croatia since 1981.**
* **The country is currently considering adding a second unit at the Krško nuclear power plant.**

1![](https://world-nuclear.org/images/icon-operable-reactor.png)

Operable  
Reactors

696 MWe

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
"Slovenia"
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

### Slovenia electricity generation by source (TWh)

!function(){"use strict";window.addEventListener("message",function(a){if(void 0!==a.data["datawrapper-height"]){var e=document.querySelectorAll("iframe");for(var t in a.data["datawrapper-height"])for(var r,i=0;r=e[i];i++)if(r.contentWindow===a.source){var d=a.data["datawrapper-height"][t]+"px";r.style.height=d}}})}();

Source: [EMBER Electricity Data Explorer](https://ember-energy.org/data/electricity-data-explorer/)

**Total generation (in 2023):**15.9 TWh

**Generation mix:** nuclear 5.6 TWh (35%); hydro 5.3 TWh (34%); coal 3.1 TWh (20%); solar 1.0 TWh (6%); natural gas 0.5 TWh (3%); biofuels & waste 0.3 TWh (2%).

**Import/export balance:**1.5 TWh net export (9.1 TWh imports; 10.6 TWh exports).

**Total consumption:** 12.4 TWh

**Per capita consumption:** c. 5800 kWh in 2023

*Source: International Energy Agency and The World Bank. Data for year 2023*

Per capita electricity consumption in Slovenia has slightly increased from 5300 kWh in 2000 to about 5800 kWh in 2023.

## Nuclear power industry

### Reactors operating in Slovenia

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
"Slovenia"
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

Slovenia has a 696 MWe Westinghouse nuclear reactor in operation, Krško 1, which is jointly owned by Croatia. This pressurized water reactor was the first Western nuclear power plant in Eastern Europe. Construction started in 1975 and the unit was connected to the grid in 1981, entering commercial operation in 1983. In 2001 its steam generators were replaced and the plant was uprated by 6%, followed by an additional 3% subsequently. Its operational lifetime was designed to be 40 years, but a 20-year extension was confirmed in mid-2015, subject to inspections in 2023 and 2033. In January 2023 after completion of an environmental impact assessment, the Ministry of the Environment approved a 20-year extension of Krško's operating lifetime. In December 2024 NEK said it would study the feasibility of extending the unit's operating lifetime beyond 60 years.

Krško is owned and operated by [Nuklearna Elektrarna Krško](http://www.nek.si/en/ "Nuklearna Elektrarna Krško") (NEK), jointly owned by Croatia's Hrvatska elektroprivreda ([HEP Group](https://www.hep.hr/en "HEP Group website")) and Slovenia's [GEN Energija](http://www.gen-energija.si "GEN Energija"). NEK produces and supplies electricity exclusively for the two partners, who each own 50% of its total output. Krško operates in base-load mode and achieves high capacity factors.

### Plans for further capacity

An application towards a second reactor of 1100 to 1600 MWe at the Krško nuclear plant was submitted to the country's ministry of economy by GEN Energija in January 2010. Parliament was expected to decide on this in 2011, and the project – referred to as [JEK 2](https://www.gen-energija.si/eng/investments-and-development/jek-2 "JEK 2 project") – remains an objective, though the required legislation was sidelined. In May 2020 the government of Slovenia stated that it would decide whether or not to proceed with a second unit at Krško by 2027. After the government’s climate strategy put nuclear power at its centre, the Infrastructure Ministry in July 2021 issued an energy permit for JEK 2, a first step in effective planning. Croatia would be co-owner, and Serbia is also a prospective partner.

In January 2024 the country’s prime minister said that a cross-party summit had agreed on the need for both renewables and nuclear energy as part of “the path to a carbon-free future.” The parties agreed on holding a referendum on the proposed JEK 2 project in 2024. However, in October 2024 the referendum was cancelled following challenges to the wording and allegations that it was not being properly conducted.

Technical feasibility studies completed in August 2025 confirmed the suitability of both Westinghouse’s AP1000 and EDF’s EPR and EPR1200 for the JEK2 project. (KHNP had been involved in earlier discussions but decided not to proceed.) In June 2025 Slovenia began a three-month public consultation as part of the planning process.

Earlier in November 2024 GEN Energija said that it is also studying the option of deploying small modular reactors.

### Reactors proposed in Slovenia

| Site | Technology | MWe  gross | Planned commercial  operation |
| --- | --- | --- | --- |
| JEK 2 | ? | 1 x 1200 |  |

## Fuel cycle

Operational low- and intermediate-level waste is stored at Krško, as is used fuel.

In February 2017 Holtec was confirmed as contractor for establishing a dry cask storage facility for used fuel at Krško. The facility is expected to begin operation in 2022.

The 1996 strategy for long-term management of used fuel recommends direct disposal of it, but leaves open the possibility of a later decision to reprocess it. In mid-2015 the intergovernmental commission responsible for the plant agreed to construct a dry storage facility for used fuel. The commission has requested a plan for the disposal of used fuel and decommissioning the plant, and in 2015 said that until this programme is developed and approved by both the Slovenian and Croatian governments, payments made by the two countries into a decommissioning fund would remain at the current level. Each country is responsible for half of the waste.

A permanent repository for low- and intermediate-level waste is planned at Vrbina, near the Krško plant. Site selection was undertaken over five years, and compensation of €5 million per year will be paid to the local community. The repository will consist of two silos holding 9400 m3 of material, enough for Slovenia's share of Krško arisings plus other Slovenian radioactive waste. In mid-2014, Slovenia allocated €157 million for the project. Croatia may participate, or will build its own repository.

In April 2023 a used fuel dry storage facility was commissioned at Krško. The first fuel loading campaign is expected to be completed by 2023 and includes 16 HI-STORM FW casks holding a total of 592 used fuel elements.

## Research and development

Slovenia has a 250 kW Triga research reactor operating since 1966 at the [Josef Stefan Institute](https://www.ijs.si/ijsw/JSI "Josef Stefan Institute"), which is a major research establishment and also operates a nuclear training centre.

## Regulation, safety and non-proliferation

Krško is supervised and licensed by the [Slovenian Nuclear Safety Administration](https://www.gov.si/en/state-authorities/bodies-within-ministries/slovenian-nuclear-safety-administration/) (SNSA), as well as by international expert missions organized by the IAEA, EU, WANO, among others.

The Slovenian [Ministry of Infrastructure](http://www.mzi.gov.si/en/ "Ministry of Infrastructure") is responsible for environmental approvals.

The [Agency for Radwaste Management](http://www.arao.si/?lang=en "Agency for Radwaste Management") (ARAO) is responsible for managing all radioactive waste.

### Non-proliferation

Slovenia has been a party to the Nuclear Non-Proliferation Treaty since 1992, and in 2000 the Additional Protocol on its safeguards agreement with the International Atomic Energy Agency entered into force. It has been party to the Paris Convention on civil liability for nuclear damage since 2001 and the supplementary Brussels Convention since 2003.

---

## Notes & references

### General sources

International Atomic Energy Agency, [Country Nuclear Power Profiles: Slovenia](https://cnpp.iaea.org/countryprofiles/Slovenia/Slovenia.htm "IAEA, Country Nuclear Power Profiles: Slovenia")

Contents

---

[Electricity sector](#electricity-sector)
[Nuclear power industry](#nuclear-power-industry)
[Fuel cycle](#fuel-cycle)
[Research and development](#research-and-development)
[Regulation, safety and non-proliferation](#regulation-safety-and-non-proliferation)
[Notes & references](#notes-amp-references)
