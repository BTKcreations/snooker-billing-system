class SnookerBillingSystem:
    def __init__(self):
        self.customers = {}
        self.bills = []
        self.bill_id_counter = 1

    def create_customer(self, customer_id, name, phone):
        """Create a new customer"""
        if customer_id in self.customers:
            print(f"Customer {customer_id} already exists!")
            return False
        
        self.customers[customer_id] = {
            'name': name,
            'phone': phone
        }
        print(f"Customer {name} created successfully!")
        return True

    def add_billing_entry(self, customer_id, table_number, hours, rate_per_hour):
        """Add a new billing entry for a customer"""
        if customer_id not in self.customers:
            print(f"Customer {customer_id} not found!")
            return False
        
        total_amount = hours * rate_per_hour
        bill = {
            'bill_id': self.bill_id_counter,
            'customer_id': customer_id,
            'customer_name': self.customers[customer_id]['name'],
            'table_number': table_number,
            'hours': hours,
            'rate_per_hour': rate_per_hour,
            'total_amount': total_amount
        }
        
        self.bills.append(bill)
        self.bill_id_counter += 1
        print(f"Bill #{bill['bill_id']} created for {bill['customer_name']} - Total: ₹{total_amount}")
        return True

    def display_all_bills(self):
        """Display all billing entries"""
        if not self.bills:
            print("No bills found!")
            return
        
        print("\n" + "="*80)
        print("SNOOKER BILLING SYSTEM - ALL BILLS")
        print("="*80)
        
        for bill in self.bills:
            print(f"\nBill ID: {bill['bill_id']}")
            print(f"Customer: {bill['customer_name']} (ID: {bill['customer_id']})")
            print(f"Table Number: {bill['table_number']}")
            print(f"Hours Played: {bill['hours']}")
            print(f"Rate per Hour: ₹{bill['rate_per_hour']}")
            print(f"Total Amount: ₹{bill['total_amount']}")
            print("-" * 40)
        
        total_revenue = sum(bill['total_amount'] for bill in self.bills)
        print(f"\nTotal Revenue: ₹{total_revenue}")
        print("="*80)


if __name__ == "__main__":
    # Example usage
    billing_system = SnookerBillingSystem()
    
    # Create customers
    billing_system.create_customer("C001", "Rajesh Kumar", "9876543210")
    billing_system.create_customer("C002", "Amit Singh", "9876543211")
    billing_system.create_customer("C003", "Priya Sharma", "9876543212")
    
    # Add billing entries
    billing_system.add_billing_entry("C001", "Table 1", 2.5, 100)
    billing_system.add_billing_entry("C002", "Table 2", 1.0, 100)
    billing_system.add_billing_entry("C003", "Table 3", 3.0, 100)
    billing_system.add_billing_entry("C001", "Table 1", 1.5, 100)
    
    # Display all bills
    billing_system.display_all_bills()
