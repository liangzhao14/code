---
source: https://world-nuclear.org/information-library/country-profiles/countries-a-f/argentina
downloaded: 2026-03-24 23:49:34
---

[HOME](https://world-nuclear.org/) / [Information Library](https://world-nuclear.org/information-library) / [country profiles](https://world-nuclear.org/information-library/country-profiles) / [countries-a-f](https://world-nuclear.org/information-library/country-profiles/countries-a-f) / Argentina

country profiles

# Nuclear Power in Argentina

Updated Tuesday, 20 January 2026

* **Argentina has three nuclear reactors generating about 5% of its electricity.**
* **Its first commercial nuclear power reactor began operating in 1974.**
* **A small locally-designed power reactor prototype, CAREM25, is under construction at the Atucha site, though work has been suspended.**
* **Further capacity at Atucha is now likely to be based on domestic small modular reactor technology.**

3![](https://world-nuclear.org/images/icon-operable-reactor.png)

Operable  
Reactors

1,641 MWe

1![](https://world-nuclear.org/images/icon-construction-reactor.png)

Reactors Under  
Construction

25 MWe

0![](https://world-nuclear.org/images/icon-down-reactor.png)

Reactors  
Shutdown

0 MWe

#### Operable nuclear power capacity

var RDB\_WIDGET\_CONFIG\_widget\_t6xou = { "id": "widget\_t6xou", "type": "chart\_status", "query": { "query": { "filtered": { "filter": { "bool": { "must": [ { "terms": { "reactor.country.exact": [ "Argentina" ] } } ] } }, "query": { "match\_all": {} } } } }, "base": "//reactordb.world-nuclear.org", "include": "/embed.html", "settings": { "chart": "bar", "start": "1970", "end": "2099", "status": "operable", "primary": "operational\_reference\_unit\_power", "fallback": "reference\_unit\_power\_capacity\_net", "label": "Reference Unit Power MWe", "height": "300", "left": "80", "distance": "0" }}

## Electricity sector

**Total generation (in 2024): 153 TWh**

**Generation mix:** natural gas 74.9 TWh (49%); hydropower 37.6 TWh (25%); wind 16.2 TWh (11%); nuclear 11.2 TWh (7%); 5.5 TWh oil (4%); solar 4.0 TWh (3%); biofuels & waste 2.6 TWh (2%); coal 1.4 TWh.

**Import/export balance:**9.2 TWh net import (10.1 TWh imports, 1.0 TWh exports)

**Total consumption:** c. 125 TWh

**Per capita consumption:** c. 2700 TWh in 2024

*Source: International Energy Agency and The World Bank. Data for year 2024.*

## Nuclear power plants

**Operable reactors in Argentina**

var RDB\_WIDGET\_CONFIG\_widget\_rpijw = {
"id": "widget\_rpijw",
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
"Argentina"
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
"base": "https://reactordb.world-nuclear.org",
"include": "/embed.html",
"settings": {
"order": {
"field": "reactor.name",
"dir": "asc",
"sort\_type": "exact"
},
"limit": "100",
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
"field": "reactor.design\_net\_capacity",
"display": "Net capacity (MWe)"
},
{
"field": "reactor.construction\_start",
"display": "Construction start"
},
{
"field": "reactor.first\_grid\_connection",
"display": "Grid connection"
}
]
}
}

**Under construction reactors in Argentina**

var RDB\_WIDGET\_CONFIG\_widget\_ep22j = {
"id": "widget\_ep22j",
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
"Argentina"
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
"limit": "100",
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
"display": "Process"
},
{
"field": "reactor.gross\_capacity",
"display": "Gross capacity (MWe)"
},
{
"field": "reactor.construction\_start",
"display": "Construction start"
}
]
}
}

![Nuclear Power Plants in Argentina map](https://world-nuclear.org/images/articles/66b9e186-a332-47ca-9554-829eecc79373.png)

## Nuclear industry development

The country's National Atomic Energy Commission (*Comisión Nacional de Energía Atómica*, [CNEA](https://www.argentina.gob.ar/cnea "CNEA")) was set up in 1950 and resulted in a spate of activity centred on nuclear R&D, including construction of several research reactors. Today, five research reactors are operated by CNEA and others. Two further research reactors are under construction.

In 1964, attention turned to nuclear power, and following a feasibility study for a 300-500 MWe unit for the Buenos Aires region, bids were invited. With the country's policy at the time firmly based on using heavy water reactors fuelled by natural uranium, Canadian and German offers were most attractive, and that from Kraftwerk Union (KWU)[a](#Notes "See Note a") – with 100% financing – was accepted. That 362 MWe (gross) Atucha plant was built near Lima, 100 km northwest of Buenos Aires.

### Atucha 1

Atucha 1 (officially named *Central Nuclear Juan Domingo Perón*) entered commercial operation in 1974. Originally fuelled with natural uranium, it now uses slightly enriched (0.9%) uranium fuel, which has doubled the burn-up from 6 to about 13 GWd/t or more and consequently reduced operating costs by 40%. Atucha 2 has followed suit. Each has a pressure vessel, unlike any other large heavy water reactor. The very high burn-up suggests that two-thirds of the energy is coming from plutonium, giving it the highest conversion rate of any non-breeder.

In April 2018 the operating licence was extended to the end of 2024.

In January 2023 a financial trust was opened by NA-SA with Nación Bursátil as well as Banco de la Provincia de Buenos Ares and Macro Securities. Investments made to the ‘Solidarity Financial Trust of Public Infrastructure NA-SA IV’ would go towards the licence extension for Atucha 1 as well as the construction of a dry storage facility for used fuel.

In April 2023 NA-SA announced that it had raised $93 million in the second tranche of funds supporting the 20-25-year lifetime extension of Atucha 1.

In October 2023 NA-SA submitted the environmental impact study for the operating lifetime extension project. Work commenced on the 30-month refurbishment at the end of September 2024.

### Atucha 2

In 1979, a third unit – Atucha 2 (officially named *Central Nuclear Néstor Kirchner*) – was ordered following a government decision to have four more units coming into operation 1987-97. It was a Siemens design, a larger version of unit 1, and construction started in 1981 by a joint venture of CNEA and Siemens-KWU. However, work proceeded slowly due to lack of funds and was suspended in 1994 with the plant 81% complete.

In 1994, NA-SA was set up to take over the nuclear power plants from CNEA and oversee the continued construction of Atucha 2.

The Siemens design of the Atucha PHWR units is unique to Argentina, and NA-SA was seeking expertise from Germany, Spain and Brazil to complete the unit. In 2003, plans for completing the 692 MWe Atucha 2 reactor (745 MWe gross) were presented to the government.

In August 2006, the government announced a $3.5 billion strategic plan for the country's nuclear power sector. This involved completing Atucha 2 and extending the operating lifetimes of Atucha 1 and Embalse.

Completing Atucha 2 was expected to cost $600 million, including $400 million for heavy water. Effective completion of Atucha 2 construction was in September 2011. The Neuquen heavy water plant completed production of 600 tonnes of heavy water in June 2012. This was loaded late in 2013, following the loading of the 451 fuel assemblies, each 9.76 metres long, which had commenced in December 2012. Local content is reported as about 90%. First criticality was achieved early in June 2014, and grid connection was later that month, with full power in February 2015. It entered commercial operation in May 2016.

### Embalse

In 1967, a second feasibility study was undertaken for a larger plant at Embalse in the Córdoba region, 500 km inland. In this case a Candu 6 reactor from Atomic Energy of Canada Ltd (AECL) was selected, partly due to the accompanying technology transfer agreement, and was constructed with the Italian company Italimpianti. The Embalse plant entered commercial operation in 1984, running on natural uranium fuel[c](#Notes "See Note b").

In 2010, an agreement was signed to refurbish the Embalse plant and increase its power by up to 7%. The refurbishment, undertaken in partnership with Candu Energy[d](#Notes "See Note c"), commenced in December 2015 and was completed in December 2018, with return to service in May 2019. The refurbishment extended the plant's operational lifetime by 30 years and increased power by 35 MWe. The whole project cost about $2.15 billion, and included replacing all pressure tubes and steam generators as well as process computer systems. Embalse was the third Candu 6 reactor to undergo a full refurbishment, after Wolsong 1 in South Korea and Point Lepreau in Canada.

## New nuclear capacity

**Reactors proposed in Argentina**

| Reactor name | Location / site | Type | Gross capacity (MWe) |
| --- | --- | --- | --- |
| Atucha 3-6 | Atucha, Lima, Buenos Aires province | ACR300 | 4 x 300 |

## Small-scale reactors

### CAREM reactor

Another aspect of the government's 2006 strategic plan was to build a 29 MWe prototype of the CAREM (*Central Argentina de Elementos Modulares*) reactor. Authorization for site use and construction at the Atucha site was received by CNEA from ARN in September 2013, and first concrete was in February 2014. Some 70% of components will be manufactured locally. The total cost was initially estimated at ARS 3.5 billion ($446 million). The ARS 298 million (then $64 million) contract for the 200-tonne reactor pressure vessel was signed with considerable fanfare in December 2013 with Industrias Metalurgicas Pescarmona SA (IMPSA), making it the first such large component to be made in the country. In September 2016 an ARS 1200 million ($80 million) contract was signed with a Tecna-Siemens joint venture for the balance of plant. At the time the target completion date was end of November 2021.

Developed by CNEA with [INVAP](http://www.invap.com.ar/en "INVAP")[e](#Notes "See Note e") and others since 1984, the [CAREM25](https://www.cnea.gob.ar/es/noticias/carem-se-licita-la-segunda-etapa/ "CAREM25") nuclear reactor is a modular 100 MWt simplified PWR with integral steam generators, designed to be used for electricity generation (29 MWe gross, 25 MWe net) or as a research reactor or for water desalination. CAREM has its entire primary coolant system within the reactor pressure vessel (11m high, 3.5 m diameter), self-pressurized and relying entirely on convection. Fuel is standard enriched PWR fuel, with burnable poison, and it is refuelled annually.

CAREM was considered for desalination in Saudi Arabia, and in March 2015 a joint venture company, Invania, was set up there with INVAP to develop technology for the Saudi nuclear power program.

In June 2016 Brazil’s INB contracted with Conaur, a CNEA subsidiary, to provide four tonnes of enriched uranium oxide for the CAREM25 reactor. It will be shipped in three batches with enrichment levels of 1.9%, 2.6% and 3.1% U-235.

The prototype (listed by the IAEA as a research reactor) was expected to be followed by a larger version, 100 MWe or possibly 200 MWe, in the northern Formosa province[1](#References "See Reference 1"). The site for this was reported as Colony Bouvier, 30 km south of Clorinda, and opposite the city of San Antonio on the Paraguay River, the national border. Paraguay expressed concern about the project. This larger version was intended for export. Though Rio Negro in the south rejected plans for a large power reactor in August 2017, it then said that a CAREM25 unit would be acceptable.

In November 2019 work was halted by contractor Techint Engineering & Construction due to late payments from the government, design changes and late delivery of technical documentation. A new construction agreement was signed in November 2021 with Henisa Sudamericana named as the main contractor. In October 2022 CNEA said that civil construction works were expected to be finished by 2024, with initial criticality expected by the end of 2027. However in September 2024 construction was once again stopped.

### ACR-300 reactors

In March 2025, Demian Reidel, chairman of the council of advisors of President Javier Milei, said that the country would install four ACR-300 small modular reactors, with a combined 1.2-GW capacity, at the Atucha nuclear plant site, with the aim to have the first unit in operation by 2030. The ACR-300 design has been developed by Invap, an Argentine technical project company. However, critics note the design is still at an early stage, with former CNEA president Adriana Serquis stating it "has no engineering detail of any kind."

## Large-scale reactors

Plans for large-scale reactors appear to have been superseded by plans for small reactors at Atucha.

### Unit IV (Atucha 3)

In February 2014 NA-SA and CNNC signed two agreements covering operations and technology. Under the first, NA-SA and CNNC would cooperate on issues related to reactor pressure tubes, including engineering, fabrication, operation and maintenance. It also covers the manufacture and storage of nuclear fuel, licensing, life extension and technological advances. This agreement is aimed at both operating and future nuclear power plant projects. The second 2014 agreement calls for the transfer of Chinese technology to Argentina. Under the accord, Argentina could act as a technology platform, supplying third countries with nuclear technology incorporating Chinese goods and services.

In July 2014 a high-level agreement was signed by the Argentine and Chinese presidents towards construction of Unit IV (Atucha 3) as a PHWR unit, though with NA-SA to be designer, architect-engineer, builder and operator of it. CNNC would assist by providing most of the equipment and technical services under long-term financing (it operates two similar units at Qinshan). Candu Energy would be a subcontractor to CNNC. In September NA-SA signed a commercial framework contract with CNNC to progress this, with CNNC’s Qinshan Phase III units (678 MWe net) as reference design for a Candu 6 unit.

The framework agreement also called for the creation of five commissions – including one on funding – to meet in Buenos Aires to develop around 12 specific contracts related to the new reactor. In February 2015 the 2014 agreement to build Unit IV (Atucha 3) was ratified by CNNC and the federal planning minister. The president then said that the cost was likely to be $5.8 billion. A decree to acquire the land was published in October 2015. NA-SA “in the role of owner, architect, and engineer will conduct the pre-project design, construction, commissioning and operation of the new 750 MWe plant.” The technical and commercial contracts involving SNC-Lavalin were signed in November 2015. Local content would be about 70%.

In November 2015 NA-SA signed a commercial contract with CNNC to build Unit IV (Atucha 3) and a framework agreement for a further reactor. The projects together are worth about $15 billion and China would contribute 85% of the required financing. In June 2016 a further agreement was signed with China National Energy Administration, firming up these arrangements and specifying early 2017 and 2019 for construction starts.

In May 2017 further contracts were signed between NA-SA and CNNC for construction of Unit IV (as Candu 6) and Unit V (as Hualong One) reactors.

However, in January 2019 reports suggested that the fourth unit, to be built at the Atucha site, would now be a 1150 MWe Hualong One unit (which had been planned as the fifth unit). China is to finance 85% of the reactor's construction. This was confirmed in 2021, and in February 2022 an EPC contract was signed by NA-SA and CNNC.

In September 2022 it was reported that progress was being hampered by Argentina's desire to fabricate the unit's fuel assemblies domestically. The planned large reactor at Atucha appears to have been superseded by the proposed construction of four 300 MWe SMRs (see above).

### Fifth reactor

Another July 2014 agreement signed by the Argentine and Chinese presidents covered Chinese cooperation in pressurized water reactor (PWR) construction in Argentina, and CNNC claimed that NA-SA had issued a pre-qualification certificate for the ACP1000 design.

Then in February 2015 a cooperation agreement was signed to "participate in the construction of a new nuclear plant featuring a light water reactor and enriched uranium in the Republic of Argentina, adopting ACP1000 technology." It was signed by the federal planning minister and the president of China's National Energy Administration and vice president of CNNC. The “ACP1000 technology” will become Hualong One, in the light of China’s policies, and China will supply the fuel. The agreement provides for NA-SA to be the architect-engineer of the project. It calls for the parties to strive for the maximum local content in the new unit in terms of materials and services. This will be achieved through the transfer of technology to Argentine companies, including the manufacturing of components and fuel fabrication. Between 50% and 70% of components and 100% of the civil works for the reactors will be sourced in Argentina, limiting foreign inputs to components and engineering services not available there. The agreement also guarantees the supply of enriched uranium and fuel assemblies throughout the life of the plant.

In line with the agreement a year earlier, the parties are also to consider "establishing a joint strategic partnership for the purpose of developing and building nuclear reactors in Latin America," so that Argentina becomes a Latin American technology platform, supplying countries with nuclear technology incorporating Chinese goods and services.

Under this PWR agreement, CNNC had three months in which to provide NA-SA with a proposal "covering technical, commercial aspects, pricing and financing." NA-SA then had three months in which to respond to CNNC's proposal. The proposal and its corresponding response then had to be approved by the Ministry of Federal Planning and China's National Energy Administration. The framework agreement for the project was signed by CNNC and NA-SA in November 2015. A commercial contract and financing agreement were envisaged by the end of 2016. The president suggested that the reactor cost was likely to be $7 billion. A further contract between CNNC and NA-SA was signed for construction of the Hualong One unit in May 2017 (see [above](#Atucha3)).

Possible sites mentioned but unconfirmed for further plants are in Monte Lindo, La Emilia, Riacho Tohué, Riacho Pilagá – all on the Paraguay River in Formosa province in the north. Colona Bouvier in Formosa has also been mentioned, but in connection with a full-sized (100-200 MWe) CAREM reactor. In 2017 Río Negro province came to the fore as a possible location, but was then withdrawn.

Reports in January 2019 suggested that plans for this 'Unit V' project might be cancelled but in August 2021 NA-SA was reported to be considering it as a Canadian project for a CANDU reactor with the site undecided.

### Other proposals: Russian overtures

Proposals from numerous countries in addition to China have been considered by Argentina for the construction of its fourth and fifth nuclear power units, most notably from Russia. The government also held earlier talks with reactor vendors from France, Japan, South Korea, and the USA.

In February 2010, the government signed an agreement with Rosatom to share technical information related to the construction of nuclear power plants and to look at possibly using Russian technology in the country. In April 2010, a nuclear cooperation agreement was signed with Russia, and in May 2011 Rosatom and the Argentine planning & investments minister said they were discussing the possibility of joint development and construction of a 640 MWe reactor of unspecified type.

In July 2014 a high-level and wide-ranging nuclear cooperation agreement was signed with Russia. This had special significance in light of Rosatom’s proposal to help build and fund Unit IV (Atucha 3). Russia’s President Putin said that the new agreement "will become a strong foundation for close cooperation" with Argentina in nuclear power.

In 2014 Rusatom Overseas had signed an agreement with Corporación América, an Argentinian holding company, for cooperation in future nuclear energy projects in Argentina. It includes the potential construction of new nuclear plants and cooperation in promoting floating nuclear plants in Argentina and other countries.

After China secured the contract to build Atucha 3 as a Candu 6 PHWR ([see above](#Atucha3 "see below"), but was later assumed likely to be Hualong One), in April 2015 the government signed an agreement with Russia establishing a framework for cooperation in construction of a 1200 MWe VVER unit, with Russian financing. Rusatom Overseas and NA-SA also signed a preliminary project development agreement on construction of the reactor. The government agreement calls for the two countries to work together to sell VVER reactors in South America and Africa. In addition CNEA and INVAP signed agreements with TVEL which provide for a broad cooperation and joint initiatives in the field of nuclear energy, including deliveries of low-enriched uranium fuel and its components for research and power reactors in Argentina, supplies of TVEL-manufactured zirconium components of the nuclear fuel cycle, and joint research and development projects.

In December 2018 a further cooperation agreement with Rosatom was signed for "the development of various project execution strategies to be applied to large and small capacity nuclear power plant construction projects in Argentina" and other countries.

## Uranium resources

Argentine uranium resources listed in the 2024 *Red Book*[2](#References "See Reference 2") total only about 10,500 tU. Uranium exploration and a little mining were carried out from the mid-1950s, but the last mine closed in 1997 for economic reasons. Cumulative national production until then from open pit and heap leaching at seven mines was 2582 tU from sandstone deposits.

There were plans to reopen the CNEA Sierra Pintada mine in Mendoza in the central west, which closed in 1997. However, objections from the provincial government mean this is now unlikely.

CNEA is also developing feasibility studies for the planned mining of the Cerro Solo deposit in Chubut province from 2018. Reasonably assured resources are 4600 tU in sandstone. Plans are complicated by a provincial ban on open pit mining.

In 2007, CNEA reached an agreement with the Salta provincial government in the north of the country to reopen the Don Otto uranium mine south of Salta, which operated intermittently from 1963 to 1981. Block leaching was envisaged, to produce 30 tU/yr, but no more has been heard of this.

A CNEA mining project at Quebrada de Alipan, La Rioja province, was also reported in 2014.

In 2017 Canada’s [U3O8 Corporation](http://www.u3o8corp.com "U3O8 Corporation website") leased 4600 ha around the old La Niquelina mine in the north of the province, near the Bolivian border, which produced a little uranium in the early 1950s. Cobalt and nickel could be co-products from the ‘five element’ vein mineralisation.

U3O8 Corporation also has leases over a surficial uranium deposit at [Laguna Salada](http://www.u3o8corp.com/projects/argentina/laguna-salada-project/ "U3O8 Corp webpage on the Laguna Salada project") in Chubut province and is using Marenica’s U-pgrade beneficiation process to test samples in Perth.

Australian-based [Cauldron Energy](http://www.cauldronenergy.com.au "Cauldron Energy website") Ltd holds leases over 16 km of outcropping uranium-copper mineralisation at Rio Colorado, Catamarca province. This was worked by CNEA in 1950s and 1960s, and Cauldron's exploration target is 6400 tU.

Canada-based [Blue Sky Uranium Corp](https://www.blueskyuranium.com/ "Blue Sky Uranium Corp") has reported 8750 tU at 0.03%U plus 5230 t vanadium oxide inferred resources (NI 43-101 compliant, February 2019) near surface in the Ivana deposit, part of its Amarillo Grande uranium-vanadium project in Rio Negro province. Its preliminary economic assessment suggests 520 tU/yr production with an all-in sustaining cost of $18.27/lb U3O8 ($47.50/kgU) net of vanadium credits.

## Fuel cycle

A 150 t/yr mill complex and refinery producing uranium dioxide operated by Dioxitek, a CNEA subsidiary, is at Córdoba. There are plans for Dioxitek to build another plant in the northern Formosa province next to the planned second CAREM reactor.

In January 2026 Dioxitek announced it had made 190 t of uranium dioxide (UO2) from a combination of U3O8, pre-existing UO2 scraps and ammonium diuranate (‘yellowcake’). The company noted that this was enough to supply Argentine consumption.

CNEA has a small conversion plant at Pilcaniyeu, near San Carlos de Bariloche, Rio Negro, with 60 t/yr capacity.

Enrichment services are currently imported from the USA. Over 1983-89, INVAP operated a small (20,000 SWU/yr) diffusion enrichment plant for CNEA at Pilcaniyeu, 60 km east of Bariloche in the far west of Rio Negro province. This was unreliable and produced very little low-enriched uranium. Argentina formally reactivated the plant in 2010, over two decades after production was halted. Although the Comisión Nacional de Energía Atómica (CNEA) re-opened it in December 2015, production was halted again in 2018. To date the Pilcaniyeu plant has not been used for either commercial or export needs.

All operating nuclear power capacity is PHWR, hence needing little or no enrichment for the fuel. World Nuclear Association's 2023 edition of *The Nuclear Fuel Report* tabulates no significant enrichment requirements until 2032, when about 250-300,000 SWU/yr would be required in the reference scenario.

Production of fuel cladding is undertaken by CNEA subsidiaries. Fuel assemblies are supplied by Combustibles Nucleares Argentinos (CONUAR) SA, also a CNEA subsidiary, located at the Ezeiza Centre near Buenos Aires. The fuel fabrication plant has a capacity of 160 tHM/yr for Atucha-type fuel and Candu fuel bundles.

Heavy water is produced by ENSI SE (*Empresa Neuquina de Servicios de Ingeniería*), which is jointly owned by CNEA and the Province of Neuquén where the 200 t/yr plant is located (at Arroyito). It is operated by Neuquen Engineering services, majority owned by the provincial government. This was rebuilt and scaled to produce enough for Atucha 2 and the three following reactors at a cost of about $1 billion, and so now has capacity for export.

There are no plans for reprocessing used fuel, though an experimental facility was run around in the early 1970s at Ezeiza.

### Radioactive waste management

The April 1997 National Law of Nuclear Activity assigns responsibility to CNEA for radioactive waste management, and creates a special fund for the purpose. Operating plants pay into this.

Low and intermediate-level wastes including used fuel from research reactors are handled at CNEA's Ezeiza facility. Used fuel is stored at each power plant. There is some dry storage at Embalse.

CNEA is also responsible for plant decommissioning, which must be funded progressively by each operating plant.

In August 2022 several Argentine firms constructed a $4.3 million dry storage facility to increase the space available for used fuel at the Atucha plant. Operations to transfer used fuel assemblies from the Atucha 1 used fuel pool began the same month. The facility includes 316 storage silos which together can house 2844 fuel bundles.

## Research & development

INVAP has built several research reactors for CNEA and international customers in Egypt (ETRR-2), Algeria (NUR), Peru (RP-0 & RP-10) and Australia (OPAL).

Its first was RA-6, a 0.5 MWt open-pool multi-purpose research reactor designed by CNEA and inaugurated in 1982. It is located in San Carlos de Bariloche, Rio Negro, on the premises of the Centro Atómico Bariloche (CAB) belonging to CNEA. It is principally for training, and uses 20%-enriched fuel.

RA-8 followed it and operated 1997-2001 in Pilcaniyeu, Río Negro, testing fuel enriched up to 3.4% and control rods for CAREM. It was an open-pool zero power critical assembly, no longer operating.

In May 2013 INVAP was awarded contracts to build the RA-10 research reactor in Argentina and the Brazil Multipurpose Reactor (RMB) there, with Australia’s OPAL reactor being the reference design for both. The two reactors will be used for the production of medical radioisotopes, as well as irradiation tests of advanced nuclear fuel and materials, and neutron beam research. Between them, they will provide the capacity to supply some 40% of global radioisotope demand. The research reactor project is part of the growing bilateral cooperation in nuclear energy between Argentina and Brazil.

In November 2014 the Nuclear Regulatory Authority granted a construction licence for RA-10, which will be used to increase the country's production of radioisotopes to enable the country to meet 10% of world demand. Currently radioisotopes are produced at the RA-3 research reactor at the Ezeiza Atomic Centre in Buenos Aires province. RA-3, a 10 MWt pool type, began operations in 1967. RA-10 is a 30 MWt open pool type reactor which will replace RA-3. Construction began in 2016. It is expected to enter operation in 2026.

There are three other research reactors in operation: RA-1 Enrico Fermi (40 kWt, tank) at Constituyentes Atomic Centre, RA-0 at Cordoba University and RA-4 at Rosario University (both very small). RA-2 critical assembly is decommissioned.

In February 2016 INVAP and Areva TA agreed to make a joint submission to develop a research reactor and a power reactor in South Africa. Areva TA is Areva's propulsion and research reactor unit (retained by Areva SA after 2017).

## Regulation, safety and non-proliferation

In 1994, the Nuclear Regulatory Authority (*Autoridad Regulatoria Nuclear*, ARN) was formed and took over all regulatory functions from the National Board on Nuclear Regulation (*Ente Nacional Regulador Nuclear*, ENREN) and CNEA. As well as radiation protection, it is responsible for safety, licensing and safeguards. It reports to the President.

The Nuclear Activity Law of 1997 establishes the respective roles of the CNEA and the Nuclear Regulatory Authority.  
  
The National Mining Code of 1994 stipulates that the government has the first option to purchase all uranium produced in Argentina, after guaranteeing domestic supply. It also regulates development activities against environmental standards.

### Non-proliferation

Argentina is a party to the nuclear Non-Proliferation Treaty (NPT) since 1995 as a non-nuclear weapons state, and has been a party to the Tlatelolco Treaty[f](#Notes "See Note f").

In 1991, the Brazilian-Argentine Agency for Accounting and Control of Nuclear Materials (ABACC) was set up. This led to the 1991 Quadripartite Agreement (INFCIRC 435) among Brazil, Argentina, ABACC and the International Atomic Energy Agency (IAEA) which entered force in 1994 with full-scope safeguards under IAEA auspices.

Argentina has not signed the Additional Protocol in relation to its safeguards agreements with the IAEA. The country is a member of the Nuclear Suppliers Group.

---

## Notes & references

### References

1. [CAREM small reactor set for Formosa province](https://www.world-nuclear-news.org/NN-First_CERAM_reactor_set_for_Formosa_province-0112094.html "CAREM small reactor set for Formosa province"), World Nuclear News (1 December 2009) [[Back](#1 "Back")]  
2. OECD Nuclear Energy Agency and International Atomic Energy Agency, [Uranium 2020: Resources, Production and Demand](https://www.oecd-nea.org/jcms/pl_52718/uranium-2020-resources-production-and-demand?details=true "Uranium 2020: Resources, Production and Demand") (2020) [[Back](#2)]

### Notes

a. In 1969, Siemens and AEG merged their nuclear activities, forming Kraftwerk Union (KWU). In 1977 AEG sold all its shares in KWU to Siemens. In 1987, Siemens-KWU was integrated into Siemens' Power Generation Group and, in 2001, Siemens merged its nuclear activities with Framatome to form Framatome ANP, which was later rebranded as Areva NP. In 2009, Siemens announced its intention to sell its 34% interest in the joint venture to Areva. [[Back](#a "Back")]

b. Nucleoelectrica Argentina SA comes under the Ministry of Economy. A 1996 law allowed for the privatization of NA-SA, but this has not occurred. [[Back](#b "Back")]

c. The Embalse nuclear power plant also produces the cobalt-60 isotope, which has several medical and industrial uses. [[Back](#c "Back")]

d. Candu Energy is a subsidiary of SNC-Lavalin Group, which took over AECL's reactor division in 2011. [[Back](#d "Back")]

e. The state-owned company INVAP (*Investigación Aplicada*) SE formed in 1976 undertakes applied research, engineering development and services to both domestic and foreign customers. It has been responsible for designing and building research reactors overseas, including Australia's 20 MW OPAL research reactor, and is a significant export earner. [[Back](#e "Back")]

f. The 1967 Treaty for the Prohibition of Nuclear Weapons in Latin America and the Caribbean, known as the Treaty of Tlatelolco, was signed by all Latin American countries other than Argentina and Cuba in 1967. [[Back](#f "Back")]

### General sources

Country Nuclear Power Profiles: Argentina, International Atomic Energy Agency

## Related information

[Desalination](https://world-nuclear.org/information-library/non-power-nuclear-applications/industry/nuclear-desalination)

Contents

---

[Electricity sector](#electricity-sector)
[Nuclear power plants](#nuclear-power-plants)
[Nuclear industry development](#nuclear-industry-development)
[New nuclear capacity](#new-nuclear-capacity)
[Small-scale reactors](#small-scale-reactors)
[Large-scale reactors](#large-scale-reactors)
[Uranium resources](#uranium-resources)
[Fuel cycle](#fuel-cycle)
[Research & development](#research-amp-development)
[Regulation, safety and non-proliferation](#regulation-safety-and-non-proliferation)
[Notes & references](#notes-amp-references)
[Related Information](#related-information)
