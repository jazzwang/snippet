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

# Virtical Integration <br/> in Healthcare

By [Jazz Yao-Tsung Wang](https://slideshare.net/jazzwang)
2019-09-02

<!-- slide -->

### My first impression ...

* Reviewing my idea for DevCon 2018 after I joined for 6 months ...

<hr/>

Vertival Integration of <font color="lightpink">**Data Pipeline**</font>
from <font color="hotpink">**Provider**</font> to <font color="orange">**Payer**</font> for providing <font color="greenyellow">**Value**</font> to <font color="aqua">**Consumer**</font>

![DevCon_2018_Ideation](https://i.imgur.com/fHEnDvz.png)
DevCon 2018 Ideation by Jazz Yao-Tsung Wang @ 2018-07-14 

<!-- slide -->

![DevCon_2018_Ideation](https://i.imgur.com/fHEnDvz.png)

* **Business Model**: <font color="lightpink">B-to-B-to-C ( CHC - Payer - Patient )</font>
* **Deliverable**: Web Services for each <font color="hotpink">Payer</font> that help <font color="orange">Patient</font> to identify their best package for each payer.
* **Value proposition for Payer**: <font color="greenyellow">Customer Relationship Management</font> <br/> (inspired by <font color="aqua">Telecom fare diagnosis service</font> in Taiwan).

<!-- slide -->

#### Vertical Integration in "Change Healthcare"?

@import "https://i.imgur.com/TxL8jIq.png" {width=40%}

<i><small>-- Source: https://www.google.com/search?q="vertical%20integration"+site%3Achangehealthcare.com</small></i>

<!-- slide -->

#### But ...

Learned from the perspective of <font color="lightpink">Cardiologist</font>

<iframe width="560" height="315" src="https://www.youtube.com/embed/S40xaVjmetM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<blockquote>
A presentation from the <font color="lightpink">2015</font> The New Orleans Conference<br/> covering the topic of <font color="lightpink">integration in healthcare</font> <br/>and how it affects those in the cardiac surgery specialty.
</blockquote>

<i><small>-- Source: "Vertical vs Horizontal Integration in Cardiac Surgery", Arie Blitz, MD, 2015
https://www.youtube.com/watch?v=S40xaVjmetM</small></i>

<!-- slide -->

# Definitions

<!-- slide -->

### What is "Horizontal integration"?

<iframe width="80%" src="https://en.wikipedia.org/wiki/Horizontal_integration" height="600"></iframe>

<i><small>-- Source: https://en.wikipedia.org/wiki/Horizontal_integration</small></i>

<!-- slide -->

#### Horizontal integration

* Increase production of goods or services **<font color="hotpink">at the same part of the supply chain</font>** via:
  * internal expansion
  * acquisition 
  * merger

@import "https://upload.wikimedia.org/wikipedia/commons/f/fc/Integration_in_English.svg" {width=40%}

<!-- slide -->

### What is "Vertical Integration"?

<iframe width="80%" src="https://en.wikipedia.org/wiki/Vertical_integration" height="600"></iframe>

<i><small>-- Source: https://en.wikipedia.org/wiki/Vertical_integration</small></i>

<!-- slide -->

### Vertical Integration

* Bring large portions of the supply chain not only **<font color="hotpink">under a common ownership</font>**, 
but also **<font color="greenyellow">into one corporation</font>**
* Three types of Vertical Integration: (A) **<font color="aqua">backwards</font>** (upstream), (B) **<font color="aqua">forwards</font>** (downstream), 
(C) **<font color="aqua">balanced</font>** (both upstream and downstream)

@import "https://upload.wikimedia.org/wikipedia/commons/f/fc/Integration_in_English.svg" {width=40%}

<!-- slide -->

## Goal of Vertical Integration in Healthcare

<hr/>

### Create superior <font color="hotpink">Value</font> in the healthcare marketplace
#### - improving patient care quality
#### - bending the cost curve

$$
\Huge
\text{Healthcare Value}\text{ } \uparrow \text{ } = \text{ } {\text{Quality of Care}\text{ }\uparrow \over \text{Cost of Care}\text{ }\downarrow}
$$

<i><small>Remember the definition of Healthcare Value in "Value-based Healthcare" sharing?</small></i>

<!-- slide -->

### Vertical Integration in Healthcare Provider

```dot
digraph G {
	subgraph cluster_0 {
		style=filled;
		color=lightgrey;
    fontsize=24
		node [style=filled,color=white,fontsize=24];
		label = "Inpatient";
    "Hospital" -> "ED";
    "ED" -> "Hospitalist";
    "Hospitalist" -> "Specialist";
    "Specialist" -> "Nurses";
    "Nurses" -> "Inpatient";
	}

	subgraph cluster_1 {
		node [style=filled,fontsize=24];
		label = "Outpatient";
		color=blue;
    fontsize=24

    "Nurse Practitioner" -> "Primary Care";
    "Primary Care" -> "Cardiologist";
    "Cardiologist" -> "Interventionalist";
    "Interventionalist" -> "Cardiac Surgeon";
    "Cardiac Surgeon" -> "Outpatient";
	}
}
```

* Emergency department (ED)
<i><small>
-- Source: "Vertical vs Horizontal Integration in Cardiac Surgery", Arie Blitz, MD, 2015
https://www.youtube.com/watch?v=S40xaVjmetM</small></i>

<!-- slide -->

### Vertical Integration: 80’s Fad or Health Care’s Future?
July 1, <font color="lightpink">**1997**</font>

@import "https://i.imgur.com/cwYsuBk.png" {width=40%}

<i><small>-- Source: "Vertical Integration: 80’s Fad or Health Care’s Future?", 1997-07-01
https://www.strategy-business.com/article/18205?gko=a00f6</small></i>

<!-- slide -->

### Cases for Vertical Integration between Payors and Providers

* owning physicians gives a health plan greater influence over practice patterns and <br/> **<font color="hotpink">reduces the use of medical resources</font>**

* owning hospitals allows an insurer to **<font color="orange">control medical facility capacity</font>** and generate <br/> **<font color="greenyellow">lower unit costs</font>**

* combining insurance, physician and hospital components under one entity yields <br/> **<font color="aqua">reductions in administrative costs</font>**

<i><small>-- Source: "Vertical Integration: 80’s Fad or Health Care’s Future?", 1997-07-01
https://www.strategy-business.com/article/18205?gko=a00f6</small></i>

<!-- slide -->

### Vertical Integration throughtout <font color="yellow">1980's</font> ...

* <font color="lightpink">**Kaiser**</font> expand its owned hospitals and contracted exclusively with the **<font color="lightpink">Permanente</font> Group**

* <font color="hotpink">**Aetna**</font> built staff model clinics across the country

* <font color="orange">**CIGNA**</font> also built staff model clinics and acquired the **Lovelace integrated health system**

* **FHP** owned health plans, physician clinics and hospitals

* **Prudential** invested in the "group model" [H.M.O.](https://en.wikipedia.org/wiki/Health_maintenance_organization) and owned/managed clinic assets

* **Humana** owned health plans and hospitals

* **Henry Ford Hospital System**, **Sentara** and **Geisinger** started up their own [H.M.O.](https://en.wikipedia.org/wiki/Health_maintenance_organization)'s

<i><small>-- Source: "Vertical Integration: 80’s Fad or Health Care’s Future?", 1997-07-01
https://www.strategy-business.com/article/18205?gko=a00f6</small></i>

<!-- slide -->

### Horizontal Consolidation in <font color="aqua">1990's</font>

* <font color="lightpink">**Kaiser**</font> is **renting hospital capacity** rather than owning it, and has started to **contract with non-<font color="lightpink">Permanente</font> physicians** to supplement its core networks.

* <font color="hotpink">**Aetna**</font> sold its physician practice management company to <font color="greenyellow">**MedPartners**</font>.

* <font color="orange">**CIGNA**</font> divested its southern California clinics to <font color="greenyellow">**MedPartners**</font>.

* **FHP** sold its hospitals and created a separate subsidiary for its group practice, ostensibly as a first step toward spinning it off.

<i><small>-- Source: "Vertical Integration: 80’s Fad or Health Care’s Future?", 1997-07-01
https://www.strategy-business.com/article/18205?gko=a00f6</small></i>

<!-- slide -->

### Why refocus on vertical intergration again?

## <font color="yellow">Affordable Care Act (ACA)</font>
### March 23, <font color="lightpink">**2010**</font>

![Affordable-Care-Act](https://i.imgur.com/PIrA7AP.png)
<i><small> -- Source: https://en.wikipedia.org/wiki/Patient_Protection_and_Affordable_Care_Act</small></i>

<!-- slide -->

### <font color="yellow">ACA</font> encourages integration

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

<i><small>-- Source: "Vertical vs Horizontal Integration in Cardiac Surgery", Arie Blitz, MD, 2015
https://www.youtube.com/watch?v=S40xaVjmetM</small></i>

<!-- slide -->

### The Way Forward for Integrated Care
#### 31 March, <font color="lightpink">**2014**</font>

![way-forward-integrated-care](https://i.imgur.com/utXs08X.png)

<i><small>-- Source: "The Way Forward for Integrated Care", 2014-03-31
https://ldi.upenn.edu/way-forward-integrated-care</small></i>

<!-- slide -->

### Hospital-Physician Integration

<blockquote>
The percentage of physicians employed by hospitals has increased<br/> from <font color="lightpink">11% in 2000</font> to nearly <font color="greenyellow">15% in 2008</font>.
</blockquote>

<blockquote>
It has led to <font color="lightpink">financial losses</font> approaching <font color="aqua">$200,000 per year per physician</font>, double the losses incurred <br/> during the early period of integration in the 1990s.
</blockquote>

<i><small>-- Source: "The Way Forward for Integrated Care", 2014-03-31
https://ldi.upenn.edu/way-forward-integrated-care</small></i>

<!-- slide -->

### Physician - Hospital - Health Plan Integration

<blockquote>
Another form of vertical integration is <br/> <font color="hotpink">between providers and health insurance plans</font>. 
</blockquote>
<blockquote>
There are several well-known examples of these systems, <br/>including <font color="lightpink">Kaiser Health Plan</font> and other major integrated systems <br/>(e.g., Mayo Clinic, Cleveland Clinic). 
</blockquote>
<blockquote>
The success of these integrated systems can be attributed to a number of features, in particular a notably <font color="greenyellow">physician-driven system</font>, <font color="aqua">unified clinical and administrative cultures</font>, a long history with sufficient time to develop this culture, and <font color="magenta">strong economic interdependence</font> among their three arms (the physicians, the hospital, and the health plan).
</blockquote>

<i><small>-- Source: "The Way Forward for Integrated Care", 2014-03-31
https://ldi.upenn.edu/way-forward-integrated-care</small></i>


<!-- slide -->

### "Virtual Integration" ?

<blockquote>
There is also a movement towards "virtual integration" which allows a physician to <font color="hotpink">remain independent</font> but exploit some of the advantages of group practice, including <font color="aqua">centralized administration, risk spreading</font>, and leverage with health plans. 
</blockquote>

<i><small>-- Source: "The Way Forward for Integrated Care", 2014-03-31
https://ldi.upenn.edu/way-forward-integrated-care</small></i>

<!-- slide -->
### Vertical Integration in Healthcare Provider (PROs & CONs)

@import "https://i.imgur.com/45m9elj.jpg" {width=60%}

<i><small>-- Source: "Vertical vs Horizontal Integration in Cardiac Surgery", Arie Blitz, MD, 2015
https://www.youtube.com/watch?v=S40xaVjmetM</small></i>

<!-- slide -->
### Horizontal Integration in Healthcare Provider (PROs & CONs)

@import "https://i.imgur.com/642cV1y.jpg" {width=60%}

<i><small>-- Source: "Vertical vs Horizontal Integration in Cardiac Surgery", Arie Blitz, MD, 2015
https://www.youtube.com/watch?v=S40xaVjmetM</small></i>

<!-- slide -->
### Economic Barriers to Integration

@import "https://i.imgur.com/EEDlGiP.jpg" {width=60%}

<i><small>-- Source: "Vertical vs Horizontal Integration in Cardiac Surgery", Arie Blitz, MD, 2015
https://www.youtube.com/watch?v=S40xaVjmetM</small></i>

* Fee-for-service (FFS)

<!-- slide -->

### Vertical Integration in Healthcare <br/>Doesn’t Boost Care Quality
#### February 14, <font color="lightpink">2019</font>

@import "https://i.imgur.com/aK9hmUb.png" {width=30%}

<blockquote>
A new study from Rice University’s Baker Institute for Public Policy shows <font color="hotpink">vertical integration in healthcare has little to no impact on care quality</font>.
</blockquote>

<i><small>-- Source: "Vertical Integration in Healthcare Doesn’t Boost Care Quality", 2019-02-14
https://revcycleintelligence.com/news/vertical-integration-in-healthcare-doesnt-boost-care-quality</small></i>

<!-- slide -->

## How about the role of 
# <font color="hotpink">"Platform"</font>
## in Vertical Integration?

<!-- slide -->

# <u>Discussion</u>
## The position of <br/> <font color="lightpink">Change Healthcare</font> <br/>in Vertical Integration?

<!-- slide -->

### Let's take a look at <br/><font color="greenyellow">Roles</font> in <font color="aqua">Digital Marketing (AdTech)</font>

@import "https://image.slidesharecdn.com/2017-11-12datapipelinematters-171112161249/95/data-pipeline-matters-16-638.jpg" {width=40%}

<i><small>-- Source: "Data Pipeline Matters -- take tracking pixel as an example", Jazz Yao-Tsung Wang, 2018
https://www.slideshare.net/jazzwang/data-pipeline-matters</small></i>


<!-- slide -->

### Revisit the position of Change Healthcare

<hr/>

Mapping roles in "Healthcare IT" and "Digital Marketing (AdTech)" ...

<font color="black">
<table style="border: 0.5pt solid black; text-align: center; vertical-align:middle;">
<tr>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#D9EAA3">
<b>Digital Marketing (AdTech)</b>
</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FFFFFF">
⟷</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FCE59D">
<b>Healthcare IT</b>
</td>
</tr><tr><td colspan="3"></td></tr><tr>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#D9EAD3">
<b>Audience</b>: Website Visitor</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FFFFFF">
⟷</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FCE5CD">
<b>Consumer</b>: Patient</td>
</tr>
</tr><tr><td colspan="3"></td></tr><tr>
<tr>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#D9EAD3">
<b>Demand</b> side: Budget Source</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FFFFFF">
⟷</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FCE5CD">
<b>Payer</b>: Insurer</td>
</tr>
</tr><tr><td colspan="3"></td></tr><tr>
<tr>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#D9EAD3">
<b>Platform</b>: Advertising Network</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FFFFFF">
⟷</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FCE5CD">
<b>Financial Data</b>: Cleaning House</br><b>Clinic Data</b>: CommonWell</td>
</tr>
</tr><tr><td colspan="3"></td></tr><tr>
<tr>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#D9EAD3">
<b>Supply</b> side: Publisher (Website)</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FFFFFF">
⟷</td>
<td style="border: 0.5pt solid black; text-align: center; vertical-align:middle;" bgcolor="#FCE5CD">
<b>Provider</b>: Hospital, Clinic, Dental, Lab</td>
</tr>
</table>
</font>

Can we reproduce the Disruptive innovation in AdTech like **Facebook**?

<!-- slide -->

# Q & A

<blockquote>
Today's sharing is majorly talking about <h3>different types of "Supply Chain"</h3> in healthcare!!
</blockquote>