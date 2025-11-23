class Enterprise:
    def __init__(
            self, 
            Name: str,
            cost_employees: str,
            Business_rental_cost: str,
            product_production_cost: str,
            warehouse_cost: str,
            marketing_cost: str,
            creation_production_cost: str,
            tax_cost: str,
            overtime_cost: str,
            bonus_cost: str,
            tools_cost: str,
            maintenance_cost: str,
            third_party_service_cost: str,
            value_of_each_product: str,
            sales_amount: str
        ) -> None:
        
        # +------------------ Variables Initialization ------------------+
        self.Name = Name.strip()
        self.cost_employees = float(cost_employees)
        self.Business_rental_cost = float(Business_rental_cost)
        self.product_production_cost = float(product_production_cost)
        self.warehouse_cost = float(warehouse_cost)
        self.marketing_cost = float(marketing_cost)
        self.creation_production_cost = float(creation_production_cost)
        self.tax_cost = float(tax_cost)
        self.overtime_cost = float(overtime_cost)
        self.bonus_cost = float(bonus_cost)
        self.tools_cost = float(tools_cost)
        self.maintenance_cost = float(maintenance_cost)
        self.third_party_service_cost = float(third_party_service_cost)
        self.value_of_each_product = float(value_of_each_product)
        self.sales_amount = float(sales_amount)
        # +--------------------------------------------------------------+
        
        # Calculations
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