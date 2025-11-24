<br>

 \[[🇧🇷 Português](README.pt_BR.md)\] \[**[🇺🇸 English](README.md)**\]


<br><br>



# 📘 Business Game Simulation — 3º Projeto da Disciplina

Este repositório reúne o código e a interface do **Business Game Simulation**, atividade prática da disciplina.

O jogo será aplicado em múltiplos grupos, cada um montando sua própria empresa, inserindo custos, despesas, estratégias e valores de venda.

Após preencherem seus dados no sistema, cada grupo poderá visualizar automaticamente:

* **Lucro total** da empresa
* **Comparação** entre empresas
* **Identificação do grupo com melhor desempenho

🎯 **Objetivo:**
👉 Vence o grupo que apresentar o **maior lucro**.

---

## 💡 Exemplo de Empresas e Cálculos

| Posição | Empresa     | Folha de Pagamento | Aluguel/Escritório | Produção  | Galpão/Estoque | Marketing | Criação/Produção | Impostos | Hora Extra | Benefícios | Materiais | Manutenção | Terceiros | Valor Produto | Quantidade Vendida | Faturamento Total | Custos Totais | Lucro Total |
| ------- | ----------- | ------------------ | ------------------ | --------- | -------------- | --------- | ---------------- | -------- | ---------- | ---------- | --------- | ---------- | --------- | ------------- | ------------------ | ----------------- | ------------- | ----------- |
| 🥇 1º   | Alpha Tech  | 50.000,00          | 20.000,00          | 10.000,00 | 5.000,00       | 10.000,00 | 5.000,00         | 5.000,00 | 2.000,00   | 3.000,00   | 1.000,00  | 2.000,00   | 1.500,00  | 50,00         | 2.000              | 100.000,00        | 114.500,00    | 80.000,00   |
| 🥈 2º   | Vision Corp | 60.000,00          | 25.000,00          | 15.000,00 | 7.000,00       | 12.000,00 | 6.000,00         | 7.000,00 | 3.000,00   | 3.500,00   | 1.200,00  | 2.500,00   | 1.800,00  | 60,00         | 2.500              | 150.000,00        | 144.000,00    | 80.000,00   |
| 🥉 3º   | Nova Labs   | 40.000,00          | 15.000,00          | 8.000,00  | 3.000,00       | 8.000,00  | 4.000,00         | 4.000,00 | 1.500,00   | 2.000,00   | 800,00    | 1.500,00   | 1.000,00  | 40,00         | 1.000              | 40.000,00         | 88.800,00     | 40.000,00   |

> **Nota:** Em caso de empate de lucro, a ordem segue a posição original na lista.

---

## 🖥️ Código de Exibição da Tabela (Flet)

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
                ft.DataColumn(ft.Text("Custo Total"), numeric=True),
                ft.DataColumn(ft.Text("Faturamento Total"), numeric=True),
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

---

## 🧮 Cálculo do Lucro

Cada empresa tem seus custos e faturamento calculados automaticamente:

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



```

ofit = self.total_revenue - self.total_costs
```

## 📚 Objetivo do Módulo

Este projeto será utilizado para simular decisões de negócio, estratégias de custos, precificação e impacto financeiro das escolhas de cada grupo, ajudando os alunos a entender melhor a relação entre custos, receita e lucro.

