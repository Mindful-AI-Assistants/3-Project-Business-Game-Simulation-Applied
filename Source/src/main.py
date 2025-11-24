import flet as ft
from Enterprise import Enterprise
from ViewEnterprises import View_Enterprises_Page


def main(page: ft.Page):
    page.title = "Business Game"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.window.maximized = True


    Enterprises = []


    Home_page = True
    def Disabled_Button(e: ft.ControlEvent):
        nonlocal Add_Enterprise_Button, Name
    
        if all([Name.value.strip() != "", sales_amount.value != "0", value_of_each_product.value.strip() != "0.0"]):
            Add_Enterprise_Button.disabled = False
            Add_Enterprise_Button.bgcolor = "#B1B27A"
        
        else:
            Add_Enterprise_Button.disabled = True
            Add_Enterprise_Button.bgcolor = "#9E9E9E"
        
        Add_Enterprise_Button.update()
    
    
    def Add_Enterprise(e: ft.ControlEvent) -> None:
        nonlocal Enterprises, Remove_Enterprise_Button
        Enterprises.append(
            Enterprise(
                Name.value,
                cost_employees.value,
                Business_rental_cost.value,
                product_production_cost.value,
                warehouse_cost.value,
                marketing_cost.value,
                creation_production_cost.value,
                tax_cost.value,
                overtime_cost.value,
                bonus_cost.value,
                tools_cost.value,
                maintenance_cost.value,
                third_party_service_cost.value,
                value_of_each_product.value,
                sales_amount.value
            )
        )
        
        Name.value = ''
        cost_employees.value = '0.0'
        Business_rental_cost.value = '0.0'
        product_production_cost.value = '0.0'
        warehouse_cost.value = '0.0'
        marketing_cost.value = '0.0'
        creation_production_cost.value = '0.0'
        tax_cost.value = '0.0'
        overtime_cost.value = '0.0'
        bonus_cost.value = '0.0'
        tools_cost.value = '0.0'
        maintenance_cost.value = '0.0'
        third_party_service_cost.value = '0.0'
        value_of_each_product.value = '0.0'
        sales_amount.value = '0'

        Remove_Enterprise_Button.disabled = False
        
        Add_Enterprise_Button.disabled = True
        Add_Enterprise_Button.bgcolor = "#B1B27A"
        
        Calculate_Button.disabled = False
        Calculate_Button.bgcolor = "#74B835"
        
        page.update()


    def remove_all_enterprises(e: ft.ControlEvent) -> None:
        nonlocal Enterprises
        Enterprises.clear()
        
        Name.value = ''
        cost_employees.value = '0.0'
        Business_rental_cost.value = '0.0'
        product_production_cost.value = '0.0'
        warehouse_cost.value = '0.0'
        marketing_cost.value = '0.0'
        creation_production_cost.value = '0.0'
        tax_cost.value = '0.0'
        overtime_cost.value = '0.0'
        bonus_cost.value = '0.0'
        tools_cost.value = '0.0'
        maintenance_cost.value = '0.0'
        third_party_service_cost.value = '0.0'
        value_of_each_product.value = '0.0'
        sales_amount.value = '0'
        
        Remove_Enterprise_Button.disabled = True
        
        Add_Enterprise_Button.disabled = True
        Add_Enterprise_Button.bgcolor = "#9E9E9E"
        
        Calculate_Button.disabled = True
        Calculate_Button.bgcolor = "#9E9E9E"
        page.update()


    def Fix_value(e: ft.ControlEvent, variable: ft.TextField) -> None:
        nonlocal cost_employees

        variable.error = False
        variable.error_text = ""

        variable.value = variable.value.replace(',', '.')

        if variable.value.replace('.', '') and '.' in variable.value:
            if variable.value.strip()[0] == '.' and variable.value.count('.') == 1:
                variable.value = '0' + variable.value

            else:
                txt = variable.value.split('.')
                txt = ''.join(txt[:-1]) + '.' + txt[-1]
                variable.value = txt

        elif '.' not in variable.value and variable.value != "":
            variable.value += '.00'
        
        try:
            variable.value = str(float(variable.value))
        except ValueError:
            variable.value = '0.0'
            variable.error = True
            variable.error_text = "Formato correto: 1234.56, 1,234.56, 1.234,56, 1234.56, ou 1234"
        
        variable.update()
        Disabled_Button(e)


    def Sales_amount(e: ft.ControlEvent) -> None:
        nonlocal sales_amount
        
        e.control.error = False
        e.control.error_text = ""
        
        try:
            sales_amount.value = int(sales_amount.value.strip())
            sales_amount.value = str(sales_amount.value)
            
            Disabled_Button(e)
        
        except ValueError:
            sales_amount.value = '0'
            
            e.control.error = True
            e.control.error_text = "Digite um número inteiro válido"
        
        sales_amount.update()
    
    
    def TextField_on_focus(e: ft.ControlEvent) -> None:
        e.control.value = ''
        e.control.update()
        
    
    def Go_to_Results_Page(e: ft.ControlEvent) -> None:
        nonlocal Home_page
        Home_page = False
        update_layout(e)
        
    
    def Go_to_Home_Page(e: ft.ControlEvent) -> None:
        nonlocal Home_page
        Home_page = True
        update_layout(e)
    
    
    def update_layout(e: ft.ControlEvent = None) -> None:
        nonlocal Enterprises, Home_page

        page.clean()
        
        if Home_page:
            page.add(
                ft.Container(
                    body_page,
                    alignment=ft.alignment.top_center,
                    expand = True
                )
            )

        else:
            page.add(
                ft.Container(
                    content = ft.Column(
                        controls = [
                            head_body,
                            
                            ft.Container(content = View_Enterprises_Page(page, Enterprises), expand=True)
                        ],
                        scroll=ft.ScrollMode.AUTO,
                        spacing=40,
                        expand=True 
                    )
                )
            )

        page.update()

    body_page = ft.Column(
        controls = [
            head_body := ft.Container(
                content = ft.Row(
                    controls = [
                        ft.Image(src=r"PUCSP.png", width=200, height=130, fit=ft.ImageFit.CONTAIN),
                        
                        ft.Text("Business Game", size=45, weight=ft.FontWeight.BOLD, expand=True, text_align=ft.TextAlign.CENTER, color=ft.Colors.WHITE),
                    
                        ft.IconButton(ft.Icons.HOME, icon_size=40, tooltip="Página inicial", icon_color = ft.Colors.WHITE, on_click=Go_to_Home_Page)
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_AROUND,  # This distributes items horizontally
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,  # Add this to center items vertically
                    expand = True
                ),
                bgcolor = "#8DC2D3",
                height = 170,
                border_radius = 20,  # pode usar ft.border_radius.all(20)
                shadow = ft.BoxShadow(
                    spread_radius = 1,
                    blur_radius = 18,
                    color = ft.Colors.BLACK26,
                    offset = ft.Offset(0, 6)
                ),
                #alignment = ft.alignment.center_left
            ),

            ft.Container(
                content = ft.Column(
                    controls = [
                        Name := ft.TextField(
                            label="Nome da Empresa: *",
                            hint_text="Digite o nome da sua empresa",
                            color = ft.Colors.ON_SURFACE_VARIANT,
                            text_size=15,
                            width = 950,
                            border_radius = 10,
                            filled = True,
                            fill_color = ft.Colors.WHITE70,
                            content_padding = ft.padding.all(15),
                            input_filter = ft.InputFilter(
                                allow = True,
                                regex_string = r"^[a-zA-ZÀ-ÿ0-9\s]*$",
                                replacement_string = ""
                            ),
                            on_blur = Disabled_Button,
                            expand = True
                        ),
                        
                        
                        ft.Row(
                            controls=[
                                ft.Container(ft.Divider(thickness=1, color=ft.Colors.GREY_400), width=350),
                                ft.Text("Despesas da empresa", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_700),
                                ft.Container(ft.Divider(thickness=1, color=ft.Colors.GREY_400), width=350)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=15
                        ),
                        

                        ft.Row(
                            controls=[
                                cost_employees := ft.TextField(
                                    value = '0.0',
                                    label="Folha de pagamento mensal:",
                                    hint_text="Digite a quantidade total gasta com funcionários",
                                    prefix_text="R$ ",
                                    color = ft.Colors.ON_SURFACE_VARIANT,
                                    text_size=15,
                                    width = 300,
                                    border_radius=10,
                                    filled=True,
                                    fill_color=ft.Colors.WHITE70,
                                    content_padding=ft.padding.all(15),
                                    input_filter = ft.InputFilter(
                                        allow = True,
                                        regex_string = r"^[0-9,.]*$",
                                        replacement_string = ""
                                    ),
                                    on_blur = lambda e: Fix_value(e, e.control),
                                    on_focus = TextField_on_focus
                                ),
                                
                                Business_rental_cost := ft.TextField(
                                    value = '0.0',
                                    label="Custos totais do escritório administrativo:",
                                    hint_text="Aluguel, contas de luz, água, internet, etc...",
                                    prefix_text="R$ ",
                                    color = ft.Colors.ON_SURFACE_VARIANT,
                                    text_size=15,
                                    width = 300,
                                    border_radius=10,
                                    filled=True,
                                    fill_color=ft.Colors.WHITE70,
                                    content_padding=ft.padding.all(15),
                                    input_filter = ft.InputFilter(
                                        allow = True,
                                        regex_string = r"^[0-9,.]*$",
                                        replacement_string = ""
                                    ),
                                    on_blur = lambda e: Fix_value(e, e.control),
                                    on_focus = TextField_on_focus
                                )
                            ],
                            alignment = ft.MainAxisAlignment.CENTER,
                            spacing=20
                        ),


                        ft.Row(
                            controls=[
                                warehouse_cost := ft.TextField(
                                    value = '0.0',
                                    label="Custo total do galpão ou equivalente:",
                                    hint_text="Ex: galpão, AWS, terceirizados, etc...",
                                    prefix_text="R$ ",
                                    color = ft.Colors.ON_SURFACE_VARIANT,
                                    text_size=15,
                                    width = 300,
                                    border_radius=10,
                                    filled=True,
                                    fill_color=ft.Colors.WHITE70,
                                    content_padding=ft.padding.all(15),
                                    input_filter = ft.InputFilter(
                                        allow = True,
                                        regex_string = r"^[0-9,.]*$",
                                        replacement_string = ""
                                    ),
                                    on_blur = lambda e: Fix_value(e, e.control),
                                    on_focus = TextField_on_focus
                                ),

                                product_production_cost := ft.TextField(
                                    value = '0.0',
                                    label="Custos totais para armazenamento de um produto:",
                                    hint_text="Custo para armazenar um produto no estoque",
                                    prefix_text="R$ ",
                                    color = ft.Colors.ON_SURFACE_VARIANT,
                                    text_size=15,
                                    width = 300,
                                    border_radius=10,
                                    filled=True,
                                    fill_color=ft.Colors.WHITE70,
                                    content_padding=ft.padding.all(15),
                                    input_filter = ft.InputFilter(
                                        allow = True,
                                        regex_string = r"^[0-9,.]*$",
                                        replacement_string = ""
                                    ),
                                    on_blur = lambda e: Fix_value(e, e.control),
                                    on_focus = TextField_on_focus
                                )
                            ],
                            alignment = ft.MainAxisAlignment.CENTER,
                            spacing=20
                        ),
                        
                        ft.Row(
                            controls=[
                                marketing_cost := ft.TextField(
                                    value = '0.0',
                                    label="Custo com Marketing:",
                                    hint_text="Digite o valor gasto mensalmente com marketing",
                                    prefix_text="R$ ",
                                    color = ft.Colors.ON_SURFACE_VARIANT,
                                    text_size=15,
                                    width = 300,
                                    border_radius=10,
                                    filled=True,
                                    fill_color=ft.Colors.WHITE70,
                                    content_padding=ft.padding.all(15),
                                    input_filter = ft.InputFilter(
                                        allow = True,
                                        regex_string = r"^[0-9,.]*$",
                                        replacement_string = ""
                                    ),
                                    on_blur = lambda e: Fix_value(e, e.control),
                                    on_focus = TextField_on_focus
                                ),

                                creation_production_cost := ft.TextField(
                                    value = '0.0',
                                    label="Custos totais para produção/criação de um produto/serviço:",
                                    hint_text="Custo total para produzio um produto ou serviço",
                                    prefix_text="R$ ",
                                    color = ft.Colors.ON_SURFACE_VARIANT,
                                    text_size=15,
                                    width = 300,
                                    border_radius=10,
                                    filled=True,
                                    fill_color=ft.Colors.WHITE70,
                                    content_padding=ft.padding.all(15),
                                    input_filter = ft.InputFilter(
                                        allow = True,
                                        regex_string = r"^[0-9,.]*$",
                                        replacement_string = ""
                                    ),
                                    on_blur = lambda e: Fix_value(e, e.control),
                                    on_focus = TextField_on_focus
                                )
                            ],
                            alignment = ft.MainAxisAlignment.CENTER,
                            spacing=20
                        ),
                        
                        ft.Row(
                            controls=[
                                overtime_cost := ft.TextField(
                                    value = '0.0',
                                    label="Valor total de hora extra dos funcionários:",
                                    hint_text="Digite o valor total de hora extra dos funcionários",
                                    prefix_text="R$ ",
                                    color = ft.Colors.ON_SURFACE_VARIANT,
                                    text_size=15,
                                    width = 300,
                                    border_radius=10,
                                    filled=True,
                                    fill_color=ft.Colors.WHITE70,
                                    content_padding=ft.padding.all(15),
                                    input_filter = ft.InputFilter(
                                        allow = True,
                                        regex_string = r"^[0-9,.]*$",
                                        replacement_string = ""
                                    ),
                                    on_blur = lambda e: Fix_value(e, e.control),
                                    on_focus = TextField_on_focus
                                ),

                                tax_cost := ft.TextField(
                                    value = '0.0',
                                    label="Custos totais para Impostos e tributações:",
                                    hint_text="Ex: ISS, ICMS, Alvará, TFE, etc...",
                                    prefix_text="R$ ",
                                    color = ft.Colors.ON_SURFACE_VARIANT,
                                    text_size=15,
                                    width = 300,
                                    border_radius=10,
                                    filled=True,
                                    fill_color=ft.Colors.WHITE70,
                                    content_padding=ft.padding.all(15),
                                    input_filter = ft.InputFilter(
                                        allow = True,
                                        regex_string = r"^[0-9,.]*$",
                                        replacement_string = ""
                                    ),
                                    on_blur = lambda e: Fix_value(e, e.control),
                                    on_focus = TextField_on_focus
                                )
                            ],
                            alignment = ft.MainAxisAlignment.CENTER,
                            spacing=20
                        ),
                        
                        
                        ft.Row(
                            controls=[
                                tools_cost := ft.TextField(
                                    value = '0.0',
                                    label="Custo para materiais de funcionários:",
                                    hint_text="Ex: uniformes, EPIs, ferramentas, computadores, etc...",
                                    prefix_text="R$ ",
                                    color = ft.Colors.ON_SURFACE_VARIANT,
                                    text_size=15,
                                    width = 300,
                                    border_radius=10,
                                    filled=True,
                                    fill_color=ft.Colors.WHITE70,
                                    content_padding=ft.padding.all(15),
                                    input_filter = ft.InputFilter(
                                        allow = True,
                                        regex_string = r"^[0-9,.]*$",
                                        replacement_string = ""
                                    ),
                                    on_blur = lambda e: Fix_value(e, e.control),
                                    on_focus = TextField_on_focus
                                ),

                                bonus_cost := ft.TextField(
                                    value = '0.0',
                                    label="Gastos gerais com benefícios e eventos corporativos:",
                                    hint_text="Ex: bonus, festas empresariais, brindes, etc...",
                                    prefix_text="R$ ",
                                    color = ft.Colors.ON_SURFACE_VARIANT,
                                    text_size=15,
                                    width = 300,
                                    border_radius=10,
                                    filled=True,
                                    fill_color=ft.Colors.WHITE70,
                                    content_padding=ft.padding.all(15),
                                    input_filter = ft.InputFilter(
                                        allow = True,
                                        regex_string = r"^[0-9,.]*$",
                                        replacement_string = ""
                                    ),
                                    on_blur = lambda e: Fix_value(e, e.control),
                                    on_focus = TextField_on_focus
                                )
                            ],
                            alignment = ft.MainAxisAlignment.CENTER,
                            spacing=20
                        ),
                        
                        
                        ft.Row(
                            controls=[
                                third_party_service_cost := ft.TextField(
                                    value = '0.0',
                                    label="Custo total de serviços terceirizados:",
                                    hint_text="Ex: Seguradoras, Serviços de aplicativo, etc...",
                                    prefix_text="R$ ",
                                    color = ft.Colors.ON_SURFACE_VARIANT,
                                    text_size=15,
                                    width = 300,
                                    border_radius=10,
                                    filled=True,
                                    fill_color=ft.Colors.WHITE70,
                                    content_padding=ft.padding.all(15),
                                    input_filter = ft.InputFilter(
                                        allow = True,
                                        regex_string = r"^[0-9,.]*$",
                                        replacement_string = ""
                                    ),
                                    on_blur = lambda e: Fix_value(e, e.control),
                                    on_focus = TextField_on_focus
                                ),

                                maintenance_cost := ft.TextField(
                                    value = '0.0',
                                    label="Custo total com manutenção e custos operacionais:",
                                    hint_text="Ex: combustível, troca/manutenção equipamento, etc...",
                                    prefix_text="R$ ",
                                    color = ft.Colors.ON_SURFACE_VARIANT,
                                    text_size=15,
                                    width = 300,
                                    border_radius=10,
                                    filled=True,
                                    fill_color=ft.Colors.WHITE70,
                                    content_padding=ft.padding.all(15),
                                    input_filter = ft.InputFilter(
                                        allow = True,
                                        regex_string = r"^[0-9,.]*$",
                                        replacement_string = ""
                                    ),
                                    on_blur = lambda e: Fix_value(e, e.control),
                                    on_focus = TextField_on_focus
                                )
                            ],
                            alignment = ft.MainAxisAlignment.CENTER,
                            spacing=20
                        ),

                        
                        ft.Row(
                            controls=[
                                ft.Container(ft.Divider(thickness=1, color=ft.Colors.GREY_400), width=350),
                                ft.Text("Faturamento da empresa", size=16, weight=ft.FontWeight.BOLD, color=ft.Colors.GREY_700),
                                ft.Container(ft.Divider(thickness=1, color=ft.Colors.GREY_400), width=350)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=15
                        ),
                        
                        
                        ft.Row(
                            controls=[
                                value_of_each_product:= ft.TextField(
                                    value = '0.0',
                                    label="Valor de cada produto/serviço:",
                                    prefix_text="R$ ",
                                    color = ft.Colors.ON_SURFACE_VARIANT,
                                    text_size=15,
                                    width = 300,
                                    border_radius=10,
                                    filled=True,
                                    fill_color=ft.Colors.WHITE70,
                                    content_padding=ft.padding.all(15),
                                    input_filter = ft.InputFilter(
                                        allow = True,
                                        regex_string = r"^[0-9,.]*$",
                                        replacement_string = ""
                                    ),
                                    on_blur = lambda e: Fix_value(e, e.control),
                                    on_focus = TextField_on_focus
                                ),

                                sales_amount := ft.TextField(
                                    value = '0',
                                    label="Quantidade de vendas de cada produto/serviço:",
                                    color = ft.Colors.ON_SURFACE_VARIANT,
                                    text_size=15,
                                    width = 300,
                                    border_radius=10,
                                    filled=True,
                                    fill_color=ft.Colors.WHITE70,
                                    content_padding=ft.padding.all(15),
                                    input_filter = ft.InputFilter(
                                        allow = True,
                                        regex_string = r"^[0-9]*$",
                                        replacement_string = ""
                                    ),
                                    on_blur = Sales_amount,
                                    on_focus = TextField_on_focus
                                )
                            ],
                            alignment = ft.MainAxisAlignment.CENTER,
                            spacing=20
                        ),
                        
                        
                        ft.Row(
                            controls=[
                                ft.Container(ft.Divider(thickness=1, color=ft.Colors.GREY_400), width=920)
                            ],
                            alignment=ft.MainAxisAlignment.CENTER,
                            vertical_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=15
                        ),
                        
                        
                        ft.Column(
                            controls = [
                                ft.Row(
                                    controls=[
                                        Remove_Enterprise_Button := ft.ElevatedButton(
                                            text="Remover empresas",
                                            tooltip="Remove todos os cadastros de empresas feitos até o momento",
                                            bgcolor="#E53935",
                                            color=ft.Colors.WHITE,
                                            width=200,
                                            height=50,
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                                padding=ft.padding.symmetric(vertical=15, horizontal=30)
                                            ),
                                            on_click = remove_all_enterprises,
                                            disabled=True
                                        ),
                                        
                                        
                                        Add_Enterprise_Button := ft.ElevatedButton(
                                            text="Adicionar Empresa",
                                            tooltip="Adicione a empresa com os dados preenchidos acima",
                                            bgcolor="#9E9E9E",
                                            color=ft.Colors.WHITE,
                                            width=200,
                                            height=50,
                                            style=ft.ButtonStyle(
                                                shape=ft.RoundedRectangleBorder(radius=10),
                                                padding=ft.padding.symmetric(vertical=15, horizontal=30)
                                            ),
                                            on_click = Add_Enterprise,
                                            disabled=True
                                        )
                                    ],
                                    alignment = ft.MainAxisAlignment.CENTER,
                                    spacing=20
                                ),
                                
                                Calculate_Button := ft.ElevatedButton(
                                    text="Calcular Lucros",
                                    tooltip="Clique no botão para calcular o lucro das empresas cadastradas e verificar quem ganhou",
                                    bgcolor="#9E9E9E",
                                    color=ft.Colors.WHITE,
                                    width=200,
                                    height=50,
                                    on_click = Go_to_Results_Page,
                                    style=ft.ButtonStyle(
                                        shape=ft.RoundedRectangleBorder(radius=10),
                                        padding=ft.padding.symmetric(vertical=15, horizontal=30)
                                    ),
                                    disabled=True
                                )
                            ],
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                            #expand=True
                        )
                    ],
                    spacing = 20,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER
                ),
                #expand = True
            )
        ],
        #horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        scroll = ft.ScrollMode.AUTO,
        spacing = 60,
        expand=True
    )


    update_layout()


ft.app(main, assets_dir="assets", use_color_emoji = True)
