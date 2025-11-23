import flet as ft
from Enterprise import Enterprise

def View_Enterprises_Page(page: ft.Page, Enterprises: list[Enterprise]) -> ft.ListView:
    Enterprises.sort(key=lambda x: x.profit, reverse = True)
    ft.DataColumnSortEvent
    return ft.Container(
        ft.DataTable(
            columns=[
                ft.DataColumn(ft.Text("Posição"), numeric=True),
                ft.DataColumn(ft.Text("Empresa"), numeric=False),
                ft.DataColumn(ft.Text("Custo Total"), numeric=True),
                ft.DataColumn(ft.Text("Faturamento Total"), numeric=True),
                ft.DataColumn(ft.Text("Lucro Total"), numeric=True)
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(f"{pos + 1}º 🥇" if pos == 0 else (f"{pos + 1}º 🥈" if pos == 1 else (f"{pos + 1}º 🥉" if pos == 2 else f"{pos + 1}º")))),
                        ft.DataCell(ft.Text(f"{ent.Name}")),
                        ft.DataCell(ft.Text(f"R$ {ent.total_costs:,.2f}")),
                        ft.DataCell(ft.Text(f"R$ {ent.total_revenue:,.2f}")),
                        ft.DataCell(ft.Text(f"R$ {ent.profit:,.2f}"))
                    ]
                ) for pos, ent in enumerate(Enterprises)
            ]
        ),
        expand=True
    )