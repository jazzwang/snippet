---
presentation:
    theme: night.css
    width: 1920
    height: 1080
    slideNumber: true
    hideAddressBar: true
    history: true
---

<!-- slide -->

## Virtical Integration <br/> in Healthcare

By [Jazz Yao-Tsung Wang](https://slideshare.net/jazzwang)
2019-09-02

<!-- slide -->

### My first impression ...

* Reviewing my idea for DevCon 2018 after I joined for 6 months ...

Vertival Integration of <font color="red">**Data Pipeline**</font>
from <font color="hotpink">**Provider**</font> to <font color="orange">**Payer**</font> for providing <font color="greenyellow">**Value**</font> to <font color="aqua">**Consumer**</font>

![DevCon_2018_Ideation](https://i.imgur.com/fHEnDvz.png)
DevCon 2018 Ideation by Jazz Yao-Tsung Wang @ 2018-07-14 

<!-- slide -->

![DevCon_2018_Ideation](https://i.imgur.com/fHEnDvz.png)

* **Business Model**: B-to-B-to-C ( CHC - Payer - Patient )
* **Deliverable**: Web Services for each Payer that help Patient to identify their best package for each payer.
* **Value proposition for Payer**: Customer Relationship Management (inspired by Telecom fare diagnosis service in Taiwan).

<!-- slide -->

#### Vertical Integration in "Change Healthcare"?

![Vertical_Integration_CHC](https://i.imgur.com/TxL8jIq.png)

https://www.google.com/search?q="vertical%20integration"+site%3Achangehealthcare.com

<!-- slide -->

#### But ...

Learned from the perspective of <font color='red'>Cardiologist</font>

<iframe width="560" height="315" src="https://www.youtube.com/embed/S40xaVjmetM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<blockquote>
A presentation from the <font color="red">2015</font> The New Orleans Conference<br/> covering the topic of <font color="red">integration in healthcare</font> <br/>and how it affects those in the cardiac surgery specialty.
</blockquote>

<i>-- Source: "Vertical vs Horizontal Integration in Cardiac Surgery", Arie Blitz, MD, 2015</i>
https://www.youtube.com/watch?v=S40xaVjmetM

<!-- slide -->

# Definitions

<!-- slide -->

### What is 'Horizontal integration'?

<iframe width='80%' src='https://en.wikipedia.org/wiki/Horizontal_integration' height="600"></iframe>

https://en.wikipedia.org/wiki/Horizontal_integration

<!-- slide -->

#### Horizontal integration

* Increase production of goods or services **at the same part of the supply chain** via:
  * internal expansion
  * acquisition 
  * merger

@import "https://upload.wikimedia.org/wikipedia/commons/f/fc/Integration_in_English.svg"

<!-- slide -->

### What is 'Vertical Integration'?

##### https://en.wikipedia.org/wiki/Vertical_integration

<iframe width='80%' src='https://en.wikipedia.org/wiki/Vertical_integration' height="600"></iframe>

<!-- slide -->

### Vertical Integration

* Bring large portions of the supply chain not only **<u>under a common ownership</u>**, 
but also **<u>into one corporation</u>**
* Three types of Vertical Integration: (A) **backwards** (upstream), (B) **forwards** (downstream), 
(C) **balanced** (both upstream and downstream)

@import "https://upload.wikimedia.org/wikipedia/commons/f/fc/Integration_in_English.svg"

<!-- slide -->

## Goal of Vertical Integration in Healthcare:
### <font color="hotpink">Create superior Value in the healthcare marketplace</font>
#### - improving patient care quality
#### - bending the cost curve

* Remember the definition of `Healthcare Value` in "Value-based Healthcare" sharing?

$$
\text{Healthcare Value}\text{ } = \text{ } {\text{Quality of Care} \over \text{Cost of Care}}
$$

<!-- slide -->

### Vertical Integration in Healthcare Provider

```dot
digraph G {
	subgraph cluster_0 {
		style=filled;
		color=lightgrey;
    fontsize=32
		node [style=filled,color=white,fontsize=32];
		label = "Inpatient";
    "Hospital" -> "ED";
    "ED" -> "Hospitalist";
    "Hospitalist" -> "Specialist";
    "Specialist" -> "Nurses";
    "Nurses" -> "Inpatient";
	}

	subgraph cluster_1 {
		node [style=filled,fontsize=32];
		label = "Outpatient";
		color=blue;
    fontsize=32

    "Nurse Practitioner" -> "Primary Care";
    "Primary Care" -> "Cardiologist";
    "Cardiologist" -> "Interventionalist";
    "Interventionalist" -> "Cardiac Surgeon";
    "Cardiac Surgeon" -> "Outpatient";
	}
}
```
* Emergency department (ED)
<i>-- Source: "Vertical vs Horizontal Integration in Cardiac Surgery", Arie Blitz, MD, 2015</i>
https://www.youtube.com/watch?v=S40xaVjmetM

<!-- slide -->

### Vertical Integration: 80’s Fad or Health Care’s Future?
July 1, <font color="red">**1997**</font>

@import "https://i.imgur.com/cwYsuBk.png" {width=45%}

https://www.strategy-business.com/article/18205?gko=a00f6

<!-- slide -->

### Cases for Vertical Integration between Payors and Providers

* owning physicians gives a health plan greater influence over practice patterns and **reduces the use of medical resources**

* owning hospitals allows an insurer to **control medical facility capacity** and generate **lower unit costs**

* combining insurance, physician and hospital components under one entity yields **reductions in administrative costs**

<i>-- Source: "Vertical Integration: 80’s Fad or Health Care’s Future?", 1997-07-01</i>
https://www.strategy-business.com/article/18205?gko=a00f6

<!-- slide -->

### Vertical Integration throughtout <font color='yellow'>1980's</font> ...

* <font color='red'>**Kaiser**</font> expand its owned hospitals and contracted exclusively with the **<font color='red'>Permanente</font> Group**

* <font color='hotpink'>**Aetna**</font> built staff model clinics across the country

* <font color='orange'>**CIGNA**</font> also built staff model clinics and acquired the **Lovelace integrated health system**

* **FHP** owned health plans, physician clinics and hospitals

* **Prudential** invested in the "group model" [H.M.O.](https://en.wikipedia.org/wiki/Health_maintenance_organization) and owned/managed clinic assets

* **Humana** owned health plans and hospitals

* **Henry Ford Hospital System**, **Sentara** and **Geisinger** started up their own [H.M.O.](https://en.wikipedia.org/wiki/Health_maintenance_organization)'s

<i>-- Source: "Vertical Integration: 80’s Fad or Health Care’s Future?", 1997-07-01</i>
https://www.strategy-business.com/article/18205?gko=a00f6

<!-- slide -->

### Horizontal Consolidation in <font color='aqua'>1990's</font>

* <font color='red'>**Kaiser**</font> is **renting hospital capacity** rather than owning it, and has started to **contract with non-<font color='red'>Permanente</font> physicians** to supplement its core networks.

* <font color='hotpink'>**Aetna**</font> sold its physician practice management company to <font color='greenyellow'>**MedPartners**</font>.

* <font color='orange'>**CIGNA**</font> divested its southern California clinics to <font color='greenyellow'>**MedPartners**</font>.

* **FHP** sold its hospitals and created a separate subsidiary for its group practice, ostensibly as a first step toward spinning it off.

<i>-- Source: "Vertical Integration: 80’s Fad or Health Care’s Future?", 1997-07-01</i>
https://www.strategy-business.com/article/18205?gko=a00f6

<!-- slide -->

### Why refocus on vertical intergration again?

## <font color='yellow'>Affordable Care Act (ACA)</font>
### March 23, <font color='red'>**2010**</font>

![Affordable-Care-Act](https://i.imgur.com/PIrA7AP.png)
https://en.wikipedia.org/wiki/Patient_Protection_and_Affordable_Care_Act

<!-- slide -->

### <font color='yellow'>ACA</font> encourages integration

<table>
<tr>
<td>
<ul>
  <li>Payment Reform
  <ul>
    <li>Pay-for-performance (P4P)
    <li>Bundled payments
    <li>Episodes of Care
    <li>Coverage of uninsured
  </ul>
  <li>Health Care Delivery
  <ul>
    <li>Medical Homes being formed
    <li>Accountable Care Organizations (ACOs)
    <li>Reengineering of care
  </ul>
</ul>
</td>
<td>
<img src="https://i.imgur.com/Qp3EP9X.png">
</td>
</table>

<i>-- Source: "Vertical vs Horizontal Integration in Cardiac Surgery", Arie Blitz, MD, 2015</i>
https://www.youtube.com/watch?v=S40xaVjmetM

<!-- slide -->

### The Way Forward for Integrated Care
#### 31 March, <font color='red'>**2014**</font>

##### https://ldi.upenn.edu/way-forward-integrated-care

![way-forward-integrated-care](https://i.imgur.com/utXs08X.png)

<!-- slide -->

### Hospital-Physician Integration

<blockquote>
The percentage of physicians employed by hospitals has increased<br/> from <font color="red">11% in 2000</font> to nearly <font color="greenyellow">15% in 2008</font>.
</blockquote>

<blockquote>
It has led to <font color="red">financial losses</font> approaching <font color="aqua">$200,000 per year per physician</font>, double the losses incurred <br/> during the early period of integration in the 1990s.
</blockquote>

<i>-- "The Way Forward for Integrated Care", 2014-03-31</i>
https://ldi.upenn.edu/way-forward-integrated-care

<!-- slide -->

### "Virtual Integration" ?

<blockquote>
There is also a movement towards "virtual integration" which allows a physician to <font color='hotpink'>remain independent</font> but exploit some of the advantages of group practice, including <font color='aqua'>centralized administration, risk spreading</font>, and leverage with health plans. 
</blockquote>

<i>-- "The Way Forward for Integrated Care", 2014-03-31</i>
https://ldi.upenn.edu/way-forward-integrated-care

<!-- slide -->
### Vertical Integration in Healthcare Provider (PROs & CONs)

![VI_Benefits](https://i.imgur.com/45m9elj.jpg)

<i>-- Source: "Vertical vs Horizontal Integration in Cardiac Surgery", Arie Blitz, MD, 2015</i>
https://www.youtube.com/watch?v=S40xaVjmetM

<!-- slide -->
### Horizontal Integration in Healthcare Provider (PROs & CONs)

![HI_Benefits](https://i.imgur.com/642cV1y.jpg)

<i>-- Source: "Vertical vs Horizontal Integration in Cardiac Surgery", Arie Blitz, MD, 2015</i>
https://www.youtube.com/watch?v=S40xaVjmetM

<!-- slide -->
### Economic Barriers to Integration

![Barries_to_Integration](https://i.imgur.com/EEDlGiP.jpg)

* Fee-for-service (FFS)
<i>-- Source: "Vertical vs Horizontal Integration in Cardiac Surgery", Arie Blitz, MD, 2015</i>
https://www.youtube.com/watch?v=S40xaVjmetM

<!-- slide -->

### Vertical Integration in Healthcare <br/>Doesn’t Boost Care Quality
#### February 14, <font color='red'>2019</font>

@import "https://i.imgur.com/aK9hmUb.png" {width=30%}

<blockquote>
A new study from Rice University’s Baker Institute for Public Policy shows <font color='hotpink'>vertical integration in healthcare has little to no impact on care quality</font>.
</blockquote>

<i>-- Source: "Vertical Integration in Healthcare Doesn’t Boost Care Quality", 2019-02-14</i>
https://revcycleintelligence.com/news/vertical-integration-in-healthcare-doesnt-boost-care-quality

<!-- slide -->

## How about the role of 
# "Platform"
## in Vertical Integration?

<!-- slide -->

# Discussion
## The position of Change Healthcare in Vert?

<!-- slide -->

### Let's take a look Roles<br/> in Digital Marketing (AdTech)

@import "https://image.slidesharecdn.com/2017-11-12datapipelinematters-171112161249/95/data-pipeline-matters-16-638.jpg" {width=70%}

<!-- slide -->

### Revisit the position of Change Healthcare

<font color='black'>
<table style="border: 0.5pt solid black; text-align: center; vertical-align:middle;">
<tr>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#D9EAD3">
Digital Marketing (AdTech)
</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FFFFFF">
⟷</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FCE5CD">
Healthcare IT
</td>
</tr>
<tr>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#D9EAD3">
Audience: website visitor</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FFFFFF">
⟷</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FCE5CD">
Patient</td>
</tr>
<tr>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#D9EAD3">
Demand side</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FFFFFF">
⟷</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FCE5CD">
<b>Payer</b>: Insurer</td>
</tr>
<tr>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#D9EAD3">
Advertising Network (Platform)</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FFFFFF">
⟷</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FCE5CD">
<b>Financial Data</b>: Cleaning House</br><b>Clinic Data</b>: CommonWell</td>
</tr>
<tr>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#D9EAD3">
Supply side: Publisher (Website)</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FFFFFF">
⟷</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FCE5CD">
<b>Provider</b>: Hospital, Clinic, Dental, Lab</td>
</tr>
</font>

<!-- slide -->

# Q & A