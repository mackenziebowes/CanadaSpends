#!/usr/bin/env python3
"""
Script to populate Quebec sankey.json with revenue and expenditure data from CSV.
"""

import json
import csv
import os
from pathlib import Path

def parse_csv_data(csv_file_path):
    """Parse the Quebec CSV data and extract revenue and expenditure information."""
    revenues = []
    expenditures = []
    
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            regrp_summary = row['REGRP_Summary']
            regrp_name = row['REGRP_Name']
            amount = float(row['Amount'])
            
            # Convert from raw number to billions
            amount_billions = amount / 1_000_000_000
            
            if regrp_summary == 'Revenues':
                revenues.append({
                    'name': regrp_name,
                    'amount': amount_billions
                })
            elif regrp_summary == 'Expenditures':
                expenditures.append({
                    'name': regrp_name,
                    'amount': amount_billions
                })
    
    return revenues, expenditures

def create_sankey_data(revenues, expenditures):
    """Create the sankey.json structure with revenue and expenditure data."""
    
    # Calculate totals
    total_revenue = sum(item['amount'] for item in revenues)
    total_expenditure = sum(item['amount'] for item in expenditures)
    total_amount = max(total_revenue, total_expenditure)
    
    # Create sankey structure
    sankey_data = {
        "total": total_amount,
        "spending": total_expenditure,
        "revenue": total_revenue,
        "spending_data": {
            "name": "Spending",
            "children": expenditures
        },
        "revenue_data": {
            "name": "Revenue",
            "children": revenues
        }
    }
    
    return sankey_data

def main():
    """Main function to process CSV and update sankey.json."""
    
    # Paths
    script_dir = Path(__file__).parent
    quebec_dir = script_dir.parent
    csv_file = quebec_dir / "open_data_vol1_statistics_23-24.csv"
    sankey_file = quebec_dir / "sankey.json"
    
    print(f"Reading CSV data from: {csv_file}")
    print(f"Updating sankey.json at: {sankey_file}")
    
    # Check if files exist
    if not csv_file.exists():
        print(f"Error: CSV file not found at {csv_file}")
        return
    
    if not sankey_file.exists():
        print(f"Error: sankey.json file not found at {sankey_file}")
        return
    
    try:
        # Parse CSV data
        revenues, expenditures = parse_csv_data(csv_file)
        
        print(f"Found {len(revenues)} revenue categories:")
        for revenue in revenues:
            print(f"  - {revenue['name']}: ${revenue['amount']:.1f}B")
        
        print(f"\nFound {len(expenditures)} expenditure categories:")
        for expenditure in expenditures:
            print(f"  - {expenditure['name']}: ${expenditure['amount']:.1f}B")
        
        # Create sankey data
        sankey_data = create_sankey_data(revenues, expenditures)
        
        print(f"\nSankey totals:")
        print(f"  - Total Revenue: ${sankey_data['revenue']:.1f}B")
        print(f"  - Total Spending: ${sankey_data['spending']:.1f}B")
        print(f"  - Chart Total: ${sankey_data['total']:.1f}B")
        
        # Write to sankey.json
        with open(sankey_file, 'w', encoding='utf-8') as file:
            json.dump(sankey_data, file, indent=2, ensure_ascii=False)
        
        print(f"\n✅ Successfully updated {sankey_file}")
        
    except Exception as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    main()
