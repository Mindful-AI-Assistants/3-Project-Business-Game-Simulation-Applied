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
> * ***Este repositório faz parte do projeto principal Ethical Entrepreneurship and Innovation in Humanistic AI & Data Science - PUC-SP.*** <br>
>
> * Para explorar todos os materiais, análises e notebooks relacionados, visite os repositórios:  <br>
>
> * **Repositório Principal** - [1-Ethical_Entrepreneurship_Innovation_Humanistic-AI-DataScience-PucSP](https://github.com/Mindful-AI-Assistants/1-Ethical_Entrepreneurship_Innovation_Humanistic-AI-DataScience-PucSP)  <br>
>
> * **Repositório do Projeto Startup** - [2-Entrepreneurship-Project-Startup-Mindful-Emotional-AI-Scalable-Ethical-InferenceOps](https://github.com/Mindful-AI-Assistants/2-Entrepreneurship-Project-Startup-Mindful-Emotional-AI-Scalable-Ethical-InferenceOps)  <br>

<br><br>

#

<!--Confidentiality Statement-->

<br><br>

> [!NOTE]
>
> ⚠️ Atenção
>
> * Projetos e entregáveis podem ser disponibilizados [publicamente]() sempre que possível.
>
> * O curso prioriza [**prática hands-on**]() com dados reais em cenários de consultoria.
>
> * Todas as atividades seguem as [**diretrizes acadêmicas e éticas da PUC-SP**]().
>
> * [**Informações confidenciais**]() deste repositório permanecem privadas em [repositórios privados]().
>
> * [**Informações confidenciais**]() deste repositório permanecem privadas em [repositórios privados]().

<!--End-->

<br><br>

#

<br><br>

# [Business Game Simulation — 3º Projeto da Disciplina]()

<br>

Este repositório contém o código e a interface do **Business Game Simulation**, uma atividade prática da disciplina.

O jogo será aplicado a múltiplos grupos, cada um criando sua própria empresa, inserindo custos, despesas, estratégias e valores de vendas.

Após inserir seus dados no sistema, cada grupo verá automaticamente:

<br>

* [**Lucro Total**]() da empresa

* [**Comparação**]() entre empresas

* [**Identificação**]() do grupo com melhor desempenho

<br><br>

> [!TIP]
>
> 🎯 [**Objetivo:**]() <br>
>
> * O grupo com o [**maior lucro**]() vence.

<br><br>

## [Exemplo de Empresas e Cálculos]()

<br>

| [Posição]() | [Empresa]() | [Folha de Pagamento]() | [Aluguel/Escritório]() | [Produção]() | [Armazém/Estoque]() | [Marketing]() | [Criação/Produção]() | [Impostos]() | [Horas Extras]() | [Benefícios]() | [Materiais]() | [Manutenção]() | [Terceiros]() | [Preço do Produto]() | [Unidades Vendidas]() | [Receita Total]() | [Custos Totais]() | [Lucro Total]() |
| ----------- | ----------- | ---------------------- | ---------------------- | ------------ | ------------------- | ------------- | -------------------- | ------------ | ---------------- | -------------- | ------------- | -------------- | ------------- | -------------------- | --------------------- | ----------------- | ----------------- | --------------- |
| [🥇 1st]()  | Alpha Tech  | 50.000,00              | 20.000,00              | 10.000,00    | 5.000,00            | 10.000,00     | 5.000,00             | 5.000,00     | 2.000,00         | 3.000,00       | 1.000,00      | 2.000,00       | 1.500,00      | 50,00                | 2.000                 | 100.000,00        | 114.500,00        | 80.000,00       |
| [🥈 2nd]()  | Vision Corp | 60.000,00              | 25.000,00              | 15.000,00    | 7.000,00            | 12.000,00     | 6.000,00             | 7.000,00     | 3.000,00         | 3.500,00       | 1.200,00      | 2.500,00       | 1.800,00      | 60,00                | 2.500                 | 150.000,00        | 144.000,00        | 80.000,00       |
| [🥉 3rd]()  | Nova Labs   | 40.000,00              | 15.000,00              | 8.000,00     | 3.000,00            | 8.000,00      | 4.000,00             | 4.000,00     | 1.500,00         | 2.000,00       | 800,00        | 1.500,00       | 1.000,00      | 40,00                | 1.000                 | 40.000,00         | 88.800,00         | 40.000,00       |

<br><br>

> [!IMPORTANT]
>
> * [**Observação:**]() Em caso de empate no lucro, a ordem segue a posição original na lista.

<br><br>

## [Código de Exibição da Tabela]()

<br>

```python
import flet as ft
from Enterprise import Enterprise

def View_Enterprises_Page(page: ft.Page, Enterprises: list[Enterprise]) -> ft.ListView:
    Enterprises.sort(key=lambda x: x.profit, reverse=True)
    return ft.Container(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Posição"), numeric=True),
                ft.DataColumn(ft.Text("Empresa")),
                ft.DataColumn(ft.Text("Custos Totais"), numeric=True),
                ft.DataColumn(ft.Text("Receita Total"), numeric=True),
                ft.DataColumn(ft.Text("Lucro Total"), numeric=True),
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

## [Cálculo de Lucro]()

Cada empresa tem seus custos e receita calculados automaticamente:

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

> [!IMPORTANT]
>
> * ### Objetivo do Módulo
>
> * Este projeto será usado para simular decisões de negócios, estratégias de custos, precificação e o impacto financeiro das escolhas de cada grupo, ajudando estudantes a compreender melhor a relação entre custos, receita e lucro.

<br><br>

## [Como Executar Este Projeto]()

<br>

### [uv]()

<br>

[Executar como app desktop:]()

<br>

```
uv run flet run
```

<br>

[Executar como app web:]()

<br>

```
uv run flet run --web
```

<br>

### [Poetry]()

<br>

[Instalar dependências do]() `pyproject.toml`:

<br>

```
poetry install
```

<br>

[Executar como app desktop:]()

<br>

```
poetry run flet run
```

<br>

[Executar como app web:]()

<br>

```
poetry run flet run --web
```

<br><br>

> [!TIP]
>
> * Para mais detalhes sobre como executar o app, consulte o [Guia de Introdução](https://flet.dev/docs/getting-started/).

<br><br>

## [Build da Aplicação]()

<br>

### [Android]()

<br>

```
flet build apk -v
```

<br>

> Para mais detalhes sobre build e assinatura de `.apk` ou `.aab`, consulte o [Guia de Empacotamento Android](https://flet.dev/docs/publish/android/).

<br><br>

### [IOS]()

<br>

```
flet build ipa -v
```

<br>

> Para mais detalhes sobre build e assinatura de `.ipa`, consulte o [Guia de Empacotamento iOS](https://flet.dev/docs/publish/ios/).

<br><br>

### [MacOS]()

<br>

```
flet build macos -v
```

<br>

> Para mais detalhes sobre build para macOS, consulte o [Guia de Empacotamento macOS](https://flet.dev/docs/publish/macos/).

<br><br>

### [Linux]()

<br>

```
flet build linux -v
```

<br>

> Para mais detalhes sobre build para Linux, consulte o [Guia de Empacotamento Linux](https://flet.dev/docs/publish/linux/).

<br><br>

### [Windows]()

```
flet build windows -v
```

<br>

> Para mais detalhes sobre build para Windows, consulte o [Guia de Empacotamento Windows](https://flet.dev/docs/publish/windows/).


<br><br>


##  [Our Crew:]()

<br>

- 👨🏽‍🚀 [**Andson Ribeiro**](https://github.com/andsonandreribeiro09)

- 👩🏻‍🚀 [**Fabiana ⚡️ Campanari**](https://github.com/FabianaCampanari) 

- 👨🏽‍🚀  [**José Augusto de Souza Oliveira**](https://github.com/Jojose3)

- 🧑🏼‍🚀 [**Luan Fabiano**](https://github.com/LuanFabiano28)

- 👨🏽‍🚀 [**Pedro Barrenco**](https://github.com/Pgbarenco)
  
- 🧑🏼‍🚀 [**Pedro Vyctor**](https://github.com/Pgbarenco)



<br><br>


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





