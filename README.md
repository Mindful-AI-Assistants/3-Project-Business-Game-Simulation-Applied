
<br>

 \[[🇧🇷 Português](README.pt_BR.md)\] \[**[🇺🇸 English](README.md)**\]
 

<br><br>


##   <p align="center"> 🦄 [***Applied Business Game Simulation Project***]() - in Humanistic AI & Data Science 



<br><br>

#### <p align="center"> [![Sponsor Mindful AI Assistants](https://img.shields.io/badge/Sponsor-Mindful%20AI%20%20Assistants-brightgreen?logo=GitHub)](https://github.com/sponsors/Mindful-AI-Assistants)



<br><br>

####  <p align="center"> Under the guidance of Professor Wagner Tufano -  [YouTube Channel](https://youtube.com/@wagnertufano611?si=bC8wqdmCcheEyqLL)



<br><br>


https://github.com/user-attachments/assets/e2771de0-ca57-4750-b708-74f0dceaade3

###### 🎶  ***[Vivaldi - The Four Seasons 'Winter']()  ⚡️ Art by Fabi***  



<br><br><br>


> [!TIP]
>
> * ***This repository is part of the main project Ethical Entrepreneurship amd Innovation in Humanistic AI & Data Science - PUC-SP.*** <br>
> * To explore all related materials, analyses, and notebooks, visit the repositories:  <br>
>
> * **Main Repo** - [1-Ethical_Entrepreneurship_Innovation_Humanistic-AI-DataScience-PucSP](https://github.com/Mindful-AI-Assistants/1-Ethical_Entrepreneurship_Innovation_Humanistic-AI-DataScience-PucSP)  <br>
>
> * **Project Startup Repo** - [2-Entrepreneurship-Project-Startup-Mindful-Emotional-AI-Scalable-Ethical-InferenceOps](https://github.com/Mindful-AI-Assistants/2-Entrepreneurship-Project-Startup-Mindful-Emotional-AI-Scalable-Ethical-InferenceOps)  <br>
> 
>   


<br><br>

#

<!--Confidentiality Statement-->

<br><br>


> [!IMPORTANT]
>
> ⚠️ Heads Up 
>
> * Projects and deliverables may be made [publicly available]() whenever possible.
>
> * The course prioritizes [**hands-on practice**]() with real data in consulting scenarios.
>
> *  All activities comply with the [**academic and ethical guidelines of PUC-SP**]().
>
> * [**Confidential information**]() from this repository remains private in [private repositories]().
>
> * [**Confidential information**]() from this repository remains private in [private repositories]().
>
>

<!--End-->



<br><br>

#  

<br><br>



#  Business Game Simulation — 3rd Project of the Course

<br>

This repository contains the code and interface for the **Business Game Simulation**, a practical activity of the course.

The game will be applied to multiple groups, each creating its own company, entering costs, expenses, strategies, and sales values.

After entering their data into the system, each group will automatically see:

<br>

* **Total company profit**
* **Comparison** between companies
* **Identification of the group with the best performance**
 
<br>

🎯 **Goal:**
👉 The group with the **highest profit** wins.


<br><br>


## 💡 Example of Companies and Calculations

<br>

| Position | Company     | Payroll   | Rent/Office | Production | Warehouse/Stock | Marketing | Creation/Production | Taxes    | Overtime | Benefits | Materials | Maintenance | Third Parties | Product Price | Units Sold | Total Revenue | Total Costs | Total Profit |
| -------- | ----------- | --------- | ----------- | ---------- | --------------- | --------- | ------------------- | -------- | -------- | -------- | --------- | ----------- | ------------- | ------------- | ---------- | ------------- | ----------- | ------------ |
| 🥇 1st   | Alpha Tech  | 50,000.00 | 20,000.00   | 10,000.00  | 5,000.00        | 10,000.00 | 5,000.00            | 5,000.00 | 2,000.00 | 3,000.00 | 1,000.00  | 2,000.00    | 1,500.00      | 50.00         | 2,000      | 100,000.00    | 114,500.00  | 80,000.00    |
| 🥈 2nd   | Vision Corp | 60,000.00 | 25,000.00   | 15,000.00  | 7,000.00        | 12,000.00 | 6,000.00            | 7,000.00 | 3,000.00 | 3,500.00 | 1,200.00  | 2,500.00    | 1,800.00      | 60.00         | 2,500      | 150,000.00    | 144,000.00  | 80,000.00    |
| 🥉 3rd   | Nova Labs   | 40,000.00 | 15,000.00   | 8,000.00   | 3,000.00        | 8,000.00  | 4,000.00            | 4,000.00 | 1,500.00 | 2,000.00 | 800.00    | 1,500.00    | 1,000.00      | 40.00         | 1,000      | 40,000.00     | 88,800.00   | 40,000.00    |


<br>

> **Note:** In case of a tie in profit, the order follows the original position in the list.


<br><br>


## 🖥️ Table Display Code (Flet)

<br>

```python
import flet as ft
from Enterprise import Enterprise

def View_Enterprises_Page(page: ft.Page, Enterprises: list[Enterprise]) -> ft.ListView:
    Enterprises.sort(key=lambda x: x.profit, reverse=True)
    return ft.Container(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Position"), numeric=True),
                ft.DataColumn(ft.Text("Company")),
                ft.DataColumn(ft.Text("Total Costs"), numeric=True),
                ft.DataColumn(ft.Text("Total Revenue"), numeric=True),
                ft.DataColumn(ft.Text("Total Profit"), numeric=True),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(f"{pos + 1}º 🥇" if pos == 0 else (f"{pos + 1}º 🥈" if pos == 1 else (f"{pos + 1}º 🥉" if pos == 2 else f"{pos + 1}º")))),
                        ft.DataCell(ft.Text(ent.Name)),
                        ft.DataCell(ft.Text(f"R$ {ent.total_costs:,.2f}")),
                        ft.DataCell(ft.Text(f"R$ {ent.total_revenue:,.2f}")),
                        ft.DataCell(ft.Text(f"R$ {ent.profit:,.2f}"))
                    ]
                ) for pos, ent in enumerate(Enterprises)
            ]
        ),
        expand=True
    )
```


<br><br>

## 🧮 Profit Calculation

Each company has its costs and revenue calculated automatically:

<br>

```python
self.total_costs = (
    self.cost_employees +
    self.Business_rental_cost +
    self.product_production_cost +
    self.warehouse_cost +
    self.marketing_cost +
    self.creation_production_cost +
    self.tax_cost +
    self.overtime_cost +
    self.bonus_cost +
    self.tools_cost +
    self.maintenance_cost +
    self.third_party_service_cost
)

self.total_revenue = self.value_of_each_product * self.sales_amount
self.profit = self.total_revenue - self.total_costs
```


<br><br>


##  Module Goal

This project will be used to simulate business decisions, cost strategies, pricing, and the financial impact of each group's choices, helping students better understand the relationship between costs, revenue, and profit.




<br><br>


## How to Run This Project

<br>


### uv

Run as a desktop app:

```
uv run flet run
```

Run as a web app:

```
uv run flet run --web
```

### Poetry

Install dependencies from `pyproject.toml`:

```
poetry install
```

Run as a desktop app:

```
poetry run flet run
```

Run as a web app:

```
poetry run flet run --web
```

For more details on running the app, refer to the [Getting Started Guide](https://flet.dev/docs/getting-started/).

## Build the app

### Android

```
flet build apk -v
```

For more details on building and signing `.apk` or `.aab`, refer to the [Android Packaging Guide](https://flet.dev/docs/publish/android/).

### iOS

```
flet build ipa -v
```

For more details on building and signing `.ipa`, refer to the [iOS Packaging Guide](https://flet.dev/docs/publish/ios/).

### macOS

```
flet build macos -v
```

For more details on building macOS package, refer to the [macOS Packaging Guide](https://flet.dev/docs/publish/macos/).

### Linux

```
flet build linux -v
```

For more details on building Linux package, refer to the [Linux Packaging Guide](https://flet.dev/docs/publish/linux/).

### Windows

```
flet build windows -v
```

For more details on building Windows package, refer to the [Windows Packaging Guide](https://flet.dev/docs/publish/windows/).



<br><br>




##  [Our Crew:]()

<br>

- 👨🏽‍🚀 [**Andson Ribeiro**](https://github.com/andsonandreribeiro09)

- 👩🏻‍🚀 [**Fabiana ⚡️ Campanari**](https://github.com/FabianaCampanari) 

- 👨🏽‍🚀  [**José Augusto de Souza Oliveira**](https://github.com/Jojose3)

- 🧑🏼‍🚀 [**Luan Fabiano**](https://github.com/LuanFabiano28)

- 👨🏽‍🚀 [**Pedro Barrenco**](https://github.com/Pgbarenco)
  
- 🧑🏼‍🚀 [**Pedro Vyctor**](https://github.com/Pgbarenco)




# 💌 [Let the data flow... Ping Me!]()


<br> 


#### <p align="center">  🛸๋ My Contacts [Hub](https://linktr.ee/fabianacampanari)


<br>

### <p align="center"> <img src="https://github.com/user-attachments/assets/517fc573-7607-4c5d-82a7-38383cc0537d" />


<br><br>

<p align="center">  ────────────── ⊹🔭๋ ──────────────

<!--
<p align="center">  ────────────── 🛸๋*ੈ✩* 🔭*ੈ₊ ──────────────
-->

<br>

<p align="center"> ➣➢➤ <a href="#top">Back to Top </a>
  


#

##### <p align="center"> Copyright 2026 Mindful-AI-Assistants. Code released under the  [MIT license.](https://github.com/Mindful-AI-Assistants/planet-smart-city-laguna-iot-pucsp/blob/7ac78ed36a9256cbdc0941dbd44fd13b545bc2dd/LICENSE)





