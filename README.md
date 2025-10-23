# snooker-billing-system

A billing management system for snooker clubs

## Overview

This project provides a simple yet effective billing system for managing snooker club operations. It allows you to track customers, record billing entries for table usage, and generate billing reports.

## Features

### 1. Customer Management
- Create new customers with unique IDs, names, and phone numbers
- Store customer information for billing purposes
- Prevent duplicate customer registrations

### 2. Billing Entry Management
- Record billing entries for each customer
- Track table number, hours played, and hourly rates
- Automatic calculation of total charges
- Generate unique bill IDs for each transaction

### 3. Bill Display & Reporting
- Display all billing entries in a formatted report
- Show customer details, table usage, and charges
- Calculate and display total revenue

## Files

- **billing_system.py**: Main Python script containing the `SnookerBillingSystem` class with all functionality

## Usage

### Running the System

```python
python billing_system.py
```

### Example Code

```python
from billing_system import SnookerBillingSystem

# Initialize the billing system
billing_system = SnookerBillingSystem()

# Create customers
billing_system.create_customer("C001", "Rajesh Kumar", "9876543210")
billing_system.create_customer("C002", "Amit Singh", "9876543211")

# Add billing entries
billing_system.add_billing_entry("C001", "Table 1", 2.5, 100)  # 2.5 hours at ₹100/hour
billing_system.add_billing_entry("C002", "Table 2", 1.0, 100)  # 1 hour at ₹100/hour

# Display all bills
billing_system.display_all_bills()
```

## Class Methods

### `create_customer(customer_id, name, phone)`
Creates a new customer in the system.
- **Parameters:**
  - `customer_id`: Unique identifier for the customer
  - `name`: Customer's name
  - `phone`: Customer's phone number
- **Returns:** `True` if successful, `False` if customer already exists

### `add_billing_entry(customer_id, table_number, hours, rate_per_hour)`
Records a new billing entry for a customer.
- **Parameters:**
  - `customer_id`: ID of the customer
  - `table_number`: Table number used
  - `hours`: Number of hours played (can be decimal)
  - `rate_per_hour`: Hourly rate in rupees
- **Returns:** `True` if successful, `False` if customer not found

### `display_all_bills()`
Displays all billing entries with customer details and calculates total revenue.

## Future Enhancements

- Add database integration for persistent storage
- Implement payment tracking and outstanding balance management
- Add date/time stamps for billing entries
- Generate PDF invoices
- Add user authentication for staff members
- Implement search and filter functionality

## Requirements

- Python 3.x

## License

This project is open source and available for modification and distribution.
