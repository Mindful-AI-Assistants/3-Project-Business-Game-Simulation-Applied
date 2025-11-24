import flet as ft
import numpy as np
from Enterprise import Enterprise

def View_Enterprises_Page(page: ft.Page, Enterprises: list[Enterprise]) -> ft.ListView:
    Enterprises.sort(key=lambda x: x.profit, reverse = True)
    Ranking_Enterprises = sorted(np.unique([enterprise.profit for enterprise in Enterprises]), reverse=True)
    
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
                        ft.DataCell(ft.Text(f"{Ranking_Enterprises.index(ent.profit) + 1}º 🥇" if Ranking_Enterprises.index(ent.profit) == 0 else (f"{Ranking_Enterprises.index(ent.profit) + 1}º 🥈" if Ranking_Enterprises.index(ent.profit) == 1 else (f"{Ranking_Enterprises.index(ent.profit) + 1}º 🥉" if Ranking_Enterprises.index(ent.profit) == 2 else f"{Ranking_Enterprises.index(ent.profit) + 1}º")))),
                        ft.DataCell(ft.Text(f"{ent.Name}")),
                        ft.DataCell(ft.Text(f"R$ {ent.total_costs:,.2f}")),
                        ft.DataCell(ft.Text(f"R$ {ent.total_revenue:,.2f}")),
                        ft.DataCell(ft.Text(f"R$ {ent.profit:,.2f}"))
                    ]
                ) for ent in Enterprises
            ]
        ),
        expand=True
    )