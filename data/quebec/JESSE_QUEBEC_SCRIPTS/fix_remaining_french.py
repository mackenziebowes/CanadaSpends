#!/usr/bin/env python3
"""
Script to fix remaining French terms in Quebec CSV files.
"""

import csv
import os
from pathlib import Path

def translate_remaining_french(text):
    """Translate remaining French terms to English."""
    translations = {
        # Program names
        "Secrétariat général adjoint à l'administration, affaires institutionnelles et Bibliothèque de l'Assemblée nationale": "Deputy General Secretariat for Administration, Institutional Affairs and National Assembly Library",
        
        # Assistance objectives
        "Autres": "Other",
        "Financement des partis politiques": "Political Party Funding",
        "Remboursement des dépenses électorales": "Electoral Expense Reimbursement",
        "Fonds pour l'eau potable et le traitement des eaux usées": "Fund for Drinking Water and Wastewater Treatment",
        "Fonds pour l'infrastructure municipale d'eau": "Municipal Water Infrastructure Fund",
        "Infrastructures municipales en milieu nordique": "Municipal Infrastructure in Northern Environment",
        "Parachèvement des programmes en infrastructures municipales": "Completion of Municipal Infrastructure Programs",
        "Programme d'aide financière pour les bâtiments municipaux": "Financial Assistance Program for Municipal Buildings",
        "Programmes de la taxe sur l'essence et de la contribution du Québec": "Gas Tax and Quebec Contribution Programs",
        "Programmes des Fonds Chantiers Canada-Québec": "Canada-Quebec Construction Fund Programs",
        "Programmes d'infrastructures Québec-Municipalités": "Quebec-Municipalities Infrastructure Programs",
        "Programmes visant à atténuer l'impact des changements climatiques et des inondations": "Programs to Mitigate the Impact of Climate Change and Flooding",
        "Aide aux municipalités reconstituées": "Assistance to Reconstituted Municipalities",
        "Compensation tenant lieu de taxes sur les immeubles des réseaux de la santé et des services sociaux ainsi que de l'éducation": "Tax Compensation on Health and Social Services Network Buildings and Education",
        "Compensation tenant lieu de taxes sur les immeubles gouvernementaux et des organisations internationales": "Tax Compensation on Government Buildings and International Organizations",
        "Mesures financières du partenariat fiscal": "Financial Measures of the Fiscal Partnership",
        
        # Beneficiaries
        "Organismes à but non lucratif": "Non-profit Organizations",
        "Entreprises du secteur privé": "Private Sector Enterprises",
        "Institutions d'enseignement": "Educational Institutions",
        "Municipalités": "Municipalities",
        "Établissements de santé et de services sociaux": "Health and Social Services Establishments",
        "Personnes": "Individuals",
        "Organismes et entreprises du gouvernement": "Government Organizations and Enterprises",
        
        # Special funds and financial terms
        "Fonds régions et ruralité": "Regional and Rural Fund",
        "Fonds de la région de la Capitale-Nationale": "National Capital Region Fund",
        "Fonds Avenir Mécénat Culture": "Culture Patronage Future Fund",
        "Fonds du patrimoine culturel québécois": "Quebec Cultural Heritage Fund",
        "Fonds de la cybersécurité et du numérique": "Cybersecurity and Digital Fund",
        "Capital ressources naturelles et énergie": "Natural Resources and Energy Capital",
        "Fonds des ressources naturelles": "Natural Resources Fund",
        "Fonds du développement économique": "Economic Development Fund",
        "Fonds pour la croissance des entreprises québécoises": "Fund for Growth of Quebec Enterprises",
        "Fonds relatif à l'administration fiscale": "Tax Administration Fund",
        "Fonds de l'économie et de l'innovation": "Economy and Innovation Fund",
        "Fonds de solidarité des travailleurs du Québec": "Quebec Workers Solidarity Fund",
        "Fonds de développement de la métropole": "Metropolitan Development Fund",
        "Fonds de développement des territoires": "Territorial Development Fund",
        "Fonds de développement des collectivités": "Community Development Fund",
        "Fonds de développement du tourisme": "Tourism Development Fund",
        "Fonds de développement de la culture et des communications": "Culture and Communications Development Fund",
        "Fonds de développement de l'éducation": "Education Development Fund",
        "Fonds de développement de la santé et des services sociaux": "Health and Social Services Development Fund",
        "Fonds de développement de la sécurité publique": "Public Security Development Fund",
        "Fonds de développement des transports": "Transportation Development Fund",
        "Fonds de développement du travail": "Labor Development Fund",
        
        # Financial terms
        "Revenus": "Revenues",
        "Dépenses": "Expenditures",
        "Surplus (déficit)": "Surplus (Deficit)",
        "Transferts provenant du ministère responsable": "Transfers from Responsible Ministry",
        "Transferts provenant des autres entités du périmètre comptable du gouvernement du Québec": "Transfers from Other Entities in Quebec Government Accounting Perimeter",
        "Revenus divers": "Miscellaneous Revenues",
        "Transfert": "Transfer",
        "Excédent sur les sommes approuvées": "Surplus on Approved Amounts",
        "Surplus (déficit) de l'exercice lié aux activités": "Surplus (Deficit) for the Year Related to Activities",
        "Surplus (déficit) cumulé lié aux activités, au début": "Cumulative Surplus (Deficit) Related to Activities, at Beginning",
        "Surplus (déficit) cumulé lié aux activités, à la fin": "Cumulative Surplus (Deficit) Related to Activities, at End",
        "Taxes à la consommation": "Consumption Taxes",
        "Impôt sur le revenu et les biens": "Income and Property Tax",
        "Rémunération": "Remuneration",
        "Fonctionnement": "Operations",
        
        # Portfolio names (all caps versions)
        "AFFAIRES MUNICIPALES ET HABITATION": "Municipal Affairs and Housing",
        "CONSEIL DU TRÉSOR ET ADMINISTRATION GOUVERNEMENTALE": "Treasury Board and Government Administration",
        "CULTURE ET COMMUNICATIONS": "Culture and Communications",
        "CYBERSÉCURITÉ ET NUMÉRIQUE": "Cybersecurity and Digital",
        "ÉCONOMIE, INNOVATION ET ÉNERGIE": "Economy, Innovation and Energy",
        "ÉDUCATION": "Education",
        "EMPLOI ET SOLIDARITÉ SOCIALE": "Employment and Social Solidarity",
        "ENSEIGNEMENT SUPÉRIEUR": "Higher Education",
        "ENVIRONNEMENT, LUTTE CONTRE LES CHANGEMENTS CLIMATIQUES, FAUNE": "Environment, Climate Change Fight, Wildlife",
        "FAMILLE": "Family",
        "FINANCES": "Finance",
        "IMMIGRATION, FRANCISATION ET INTÉGRATION": "Immigration, Francization and Integration",
        "JUSTICE": "Justice",
        "LANGUE FRANÇAISE": "French Language",
        "RELATIONS INTERNATIONALES ET FRANCOPHONIE": "International Relations and Francophonie",
        "RESSOURCES NATURELLES ET FORÊTS": "Natural Resources and Forests",
        "SANTÉ ET SERVICES SOCIAUX": "Health and Social Services",
        "SÉCURITÉ PUBLIQUE": "Public Security",
        "TOURISME": "Tourism",
        "TRANSPORTS ET MOBILITÉ DURABLE": "Transportation and Sustainable Mobility",
        "TRAVAIL": "Labor"
    }
    
    return translations.get(text, text)

def fix_csv_file(input_file, output_file):
    """Fix French terms in a CSV file."""
    print(f"Fixing French terms in {input_file}")
    
    with open(input_file, 'r', encoding='utf-8') as infile, \
         open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Process header
        header = next(reader)
        writer.writerow(header)
        
        # Process data rows
        row_count = 0
        for row in reader:
            if not row:  # Skip empty rows
                continue
                
            # Translate each cell
            translated_row = []
            for cell in row:
                translated_cell = translate_remaining_french(cell)
                translated_row.append(translated_cell)
            
            writer.writerow(translated_row)
            row_count += 1
    
    print(f"✅ Successfully fixed {input_file} ({row_count} rows)")

def main():
    """Main function to fix all Quebec CSV files."""
    script_dir = Path(__file__).parent
    granular_dir = script_dir.parent / "granular"
    
    # Define file mappings
    file_mappings = [
        "1_expenditures_and_investments_general_fund_2023-2024.csv",
        "2_transfer_expenditures_general_fund_by_assistance_objectives_2023-2024.csv",
        "3_transfer_expenditures_general_fund_by_beneficiaries_2023-2024.csv",
        "4_revenues_expenditures_and_investments_special_funds_2023-2024.csv"
    ]
    
    for filename in file_mappings:
        input_file = granular_dir / filename
        output_file = granular_dir / filename.replace('.csv', '_fixed.csv')
        
        if input_file.exists():
            fix_csv_file(input_file, output_file)
        else:
            print(f"❌ Input file not found: {input_file}")
    
    print("\n🎉 All Quebec CSV files fixed successfully!")
    print("Fixed files have '_fixed' suffix. Replace originals if satisfied with results.")

if __name__ == "__main__":
    main()
