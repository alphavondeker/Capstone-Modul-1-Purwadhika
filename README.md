# README for Capstone Project: Dagang Besi Application

## Introduction

The **Dagang Besi Application** is a Python-based inventory and sales management system for a galvanized pipe shop. This application enables users to manage a catalog of products, update inventory, and facilitate customer purchases with a simple terminal interface.

---

## Features

### 1. **Product Catalog**
- View a complete list of galvanized pipes.
- Search for pipes by various attributes:
  - Diameter
  - Thickness
  - Length
  - Type
  - Code

### 2. **Inventory Management**
- Add new pipe products to the catalog.
- Update the stock of existing products:
  - Increase or decrease stock.
  - Change product prices.
- Delete products from the catalog.

### 3. **Sales Management**
- Customers can:
  - Browse available products.
  - Add products to the shopping cart.
  - See a detailed summary of purchases, including:
    - Total price.
    - Total weight.
- Automatically deduct purchased quantities from inventory.

### 4. **User-Friendly Interface**
- Tabular display of data using the `tabulate` library.
- Clear instructions and input validation.

---

## How to Use

### Prerequisites
- Python 3.x installed on your system.
- Install the required library:
  ```bash
  pip install tabulate
