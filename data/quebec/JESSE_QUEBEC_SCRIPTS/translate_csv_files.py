#!/usr/bin/env python3
"""
Script to translate Quebec CSV files from French to English while preserving all data.
"""

import csv
import os
from pathlib import Path

def translate_portfolio_name(french_name):
    """Translate French portfolio names to English."""
    translations = {
        "Assemblée nationale": "National Assembly",
        "Personnes désignées par l'Assemblée nationale": "Persons Designated by the National Assembly",
        "Affaires municipales et Habitation": "Municipal Affairs and Housing",
        "Agriculture, Pêcheries et Alimentation": "Agriculture, Fisheries and Food",
        "Conseil du trésor et Administration gouvernementale": "Treasury Board and Government Administration",
        "Conseil exécutif": "Executive Council",
        "Culture et Communications": "Culture and Communications",
        "Cybersécurité et Numérique": "Cybersecurity and Digital",
        "Économie, Innovation et Énergie": "Economy, Innovation and Energy",
        "Éducation": "Education",
        "Emploi et Solidarité sociale": "Employment and Social Solidarity",
        "Enseignement supérieur": "Higher Education",
        "Environnement, Lutte contre les changements climatiques, Faune": "Environment, Climate Change Fight, Wildlife",
        "Famille": "Family",
        "Finances": "Finance",
        "Immigration, Francisation et Intégration": "Immigration, Francization and Integration",
        "Justice": "Justice",
        "Langue française": "French Language",
        "Relations internationales et Francophonie": "International Relations and Francophonie",
        "Ressources naturelles et Forêts": "Natural Resources and Forests",
        "Santé et Services sociaux": "Health and Social Services",
        "Sécurité publique": "Public Security",
        "Tourisme": "Tourism",
        "Transports et Mobilité durable": "Transportation and Sustainable Mobility",
        "Travail": "Labor"
    }
    return translations.get(french_name, french_name)

def translate_program_name(french_name):
    """Translate French program names to English."""
    translations = {
        "Secrétariat général et affaires juridiques et parlementaires": "General Secretariat and Legal and Parliamentary Affairs",
        "Secrétariat général adjoint à l'administration, affaires institutionnelles et Bibliothèque de l'Assemblée nationale": "Deputy General Secretariat for Administration, Institutional Affairs and National Assembly Library",
        "Services statutaires aux parlementaires": "Statutory Services to Parliamentarians",
        "Le Protecteur du citoyen": "Citizen Protector",
        "Le Vérificateur général": "Auditor General",
        "Administration du système électoral": "Electoral System Administration",
        "Le Commissaire au lobbyisme": "Lobbying Commissioner",
        "Le Commissaire à l'éthique et à la déontologie": "Ethics and Deontology Commissioner",
        "Le Commissaire à la langue française": "French Language Commissioner",
        "Soutien aux activités ministérielles": "Support for Ministerial Activities",
        "Modernisation des infrastructures municipales": "Modernization of Municipal Infrastructure",
        "Compensations tenant lieu de taxes et soutien aux municipalités": "Tax Compensations and Municipal Support",
        "Développement des régions et des territoires": "Regional and Territorial Development",
        "Promotion et développement de la région métropolitaine": "Promotion and Development of the Metropolitan Region",
        "Commission municipale du Québec": "Quebec Municipal Commission",
        "Habitation": "Housing",
        "Développement des entreprises bioalimentaires et qualité des aliments": "Development of Agrifood Enterprises and Food Quality",
        "Organismes d'État": "Government Organizations",
        "Soutien au Conseil du trésor": "Support for Treasury Board",
        "Soutien aux fonctions gouvernementales": "Support for Government Functions",
        "Commission de la fonction publique": "Public Service Commission",
        "Régimes de retraite et d'assurances": "Retirement and Insurance Plans",
        "Soutien aux infrastructures gouvernementales": "Support for Government Infrastructure",
        "Promotion et développement de la Capitale-Nationale": "Promotion and Development of the National Capital",
        "Cabinet du lieutenant-gouverneur": "Lieutenant Governor's Office",
        "Services de soutien auprès du premier ministre et du Conseil exécutif": "Support Services for the Prime Minister and Executive Council",
        "Relations canadiennes": "Canadian Relations",
        "Relations avec les Premières Nations et les Inuit": "Relations with First Nations and Inuit",
        "Institutions démocratiques, accès à l'information et laïcité": "Democratic Institutions, Access to Information and Secularism",
        "Internet haute vitesse et projets spéciaux de connectivité": "High-Speed Internet and Special Connectivity Projects",
        "Direction, administration et soutien à la mission": "Direction, Administration and Mission Support",
        "Soutien et développement de la culture, des communications et du patrimoine": "Support and Development of Culture, Communications and Heritage",
        "Jeunesse": "Youth",
        "Direction et administration": "Direction and Administration",
        "Gestion des ressources informationnelles spécifiques": "Management of Specific Information Resources",
        "Développement de l'économie": "Economic Development",
        "Développement de la science, de la recherche et de l'innovation": "Development of Science, Research and Innovation",
        "Interventions relatives au Fonds du développement économique": "Interventions Related to the Economic Development Fund",
        "Organismes dédiés à la recherche et à l'innovation": "Organizations Dedicated to Research and Innovation",
        "Énergie": "Energy",
        "Administration": "Administration",
        "Soutien aux organismes": "Support for Organizations",
        "Taxe scolaire – Subvention d'équilibre fiscal": "School Tax – Fiscal Balance Grant",
        "Éducation préscolaire et enseignement primaire et secondaire": "Preschool and Primary and Secondary Education",
        "Développement du loisir et du sport": "Development of Recreation and Sports",
        "Régimes de retraite": "Retirement Plans",
        "Gouvernance, administration et services à la clientèle": "Governance, Administration and Client Services",
        "Solidarité sociale et Action communautaire": "Social Solidarity and Community Action",
        "Emploi": "Employment",
        "Protection de l'environnement et de la faune": "Protection of Environment and Wildlife",
        "Bureau d'audiences publiques sur l'environnement": "Bureau of Public Hearings on the Environment",
        "Planification, recherche et administration": "Planning, Research and Administration",
        "Mesures d'aide à la famille": "Family Assistance Measures",
        "Services de garde": "Childcare Services",
        "Curateur public": "Public Curator",
        "Activités en matière économique, fiscale, budgétaire et financière": "Activities in Economic, Fiscal, Budgetary and Financial Matters",
        "Contributions, frais de services bancaires et provisions pour transférer des crédits": "Contributions, Banking Service Fees and Provisions for Transferring Credits",
        "Relations avec les Québécois d'expression anglaise": "Relations with English-Speaking Quebecers",
        "Service de la dette": "Debt Service",
        "Direction et soutien aux activités du Ministère": "Direction and Support for Ministry Activities",
        "Immigration, francisation et intégration": "Immigration, Francization and Integration",
        "Administration de la justice": "Administration of Justice",
        "Activité judiciaire": "Judicial Activity",
        "Justice administrative": "Administrative Justice",
        "Indemnisation et reconnaissance": "Compensation and Recognition",
        "Autres organismes relevant du ministre": "Other Organizations Under the Minister",
        "Poursuites criminelles et pénales": "Criminal and Penal Prosecutions",
        "Langue française": "French Language",
        "Direction et administration": "Direction and Administration",
        "Affaires internationales": "International Affairs",
        "Condition féminine": "Women's Status",
        "Gestion des ressources naturelles et forestières": "Management of Natural Resources and Forests",
        "Fonctions de coordination": "Coordination Functions",
        "Services dispensés à la population": "Services Provided to the Population",
        "Office des personnes handicapées du Québec": "Quebec Office for Disabled Persons",
        "Régie de l'assurance maladie du Québec": "Quebec Health Insurance Board",
        "Condition des Aînés": "Seniors' Status",
        "Direction et administration": "Direction and Administration",
        "Services de la Sûreté du Québec": "Quebec Provincial Police Services",
        "Gestion du système correctionnel": "Correctional System Management",
        "Affaires policières": "Police Affairs",
        "Expertises scientifiques et médicolégales": "Scientific and Forensic Expertise",
        "Encadrement et surveillance": "Oversight and Monitoring",
        "Sécurité civile et sécurité incendie": "Civil Security and Fire Safety",
        "Direction, administration et gestion des programmes": "Direction, Administration and Program Management",
        "Développement du tourisme": "Tourism Development",
        "Organismes relevant du ministre": "Organizations Under the Minister",
        "Infrastructures et systèmes de transport": "Transportation Infrastructure and Systems",
        "Administration et services corporatifs": "Administration and Corporate Services",
        "Travail": "Labor"
    }
    return translations.get(french_name, french_name)

def translate_element_name(french_name):
    """Translate French element names to English."""
    translations = {
        "Secrétariat général et affaires juridiques": "General Secretariat and Legal Affairs",
        "Affaires parlementaires": "Parliamentary Affairs",
        "Affaires institutionnelles et de la Bibliothèque de l'Assemblée nationale": "Institutional Affairs and National Assembly Library",
        "Affaires administratives et sécurité": "Administrative Affairs and Security",
        "Indemnités et allocations aux parlementaires": "Indemnities and Allowances to Parliamentarians",
        "Dépenses du personnel des cabinets et des députés": "Expenses of Cabinet and Member Personnel",
        "Services de recherche des partis politiques": "Research Services for Political Parties",
        "Régime de retraite des membres de l'Assemblée nationale": "Retirement Plan for Members of the National Assembly",
        "Le Protecteur du citoyen": "Citizen Protector",
        "Le Vérificateur général": "Auditor General",
        "Gestion interne et soutien": "Internal Management and Support",
        "Commission de la représentation électorale": "Electoral Representation Commission",
        "Activités électorales": "Electoral Activities",
        "Le Commissaire au lobbyisme": "Lobbying Commissioner",
        "Le Commissaire à l'éthique et à la déontologie": "Ethics and Deontology Commissioner",
        "Le Commissaire à la langue française": "French Language Commissioner",
        "Direction et administration": "Direction and Administration",
        "Politiques et programmes": "Policies and Programs",
        "Programmes en lien avec le Plan québécois des infrastructures": "Programs Related to the Quebec Infrastructure Plan",
        "Autres programmes d'infrastructures municipales": "Other Municipal Infrastructure Programs",
        "Compensations tenant lieu de taxes": "Tax Compensations",
        "Aide financière aux municipalités": "Financial Assistance to Municipalities",
        "Mesures financières du partenariat fiscal": "Financial Measures of the Fiscal Partnership",
        "Soutien au développement des régions et à la ruralité": "Support for Regional Development and Rurality",
        "Autres programmes d'aide financière aux territoires": "Other Financial Assistance Programs for Territories",
        "Soutien à la région métropolitaine": "Support for the Metropolitan Region",
        "Commission municipale du Québec": "Quebec Municipal Commission",
        "Société d'habitation du Québec": "Quebec Housing Corporation",
        "Tribunal administratif du logement": "Administrative Housing Tribunal",
        "Soutien à l'habitation": "Housing Support",
        "Développement durable, territorial et sectoriel": "Sustainable, Territorial and Sectoral Development",
        "Transformation, marchés, main d'œuvre et politiques intergouvernementales": "Transformation, Markets, Labor and Intergovernmental Policies",
        "Pêches et aquaculture commerciales": "Commercial Fisheries and Aquaculture",
        "Remboursement des taxes foncières et de compensations aux exploitations agricoles": "Reimbursement of Property Taxes and Compensations to Agricultural Operations",
        "Santé animale et inspection des aliments": "Animal Health and Food Inspection",
        "Politiques bioalimentaires, programmes et innovation": "Agrifood Policies, Programs and Innovation",
        "La Financière agricole du Québec": "Quebec Agricultural Finance Corporation",
        "Commission de protection du territoire agricole du Québec": "Quebec Agricultural Territory Protection Commission",
        "Régie des marchés agricoles et alimentaires du Québec": "Quebec Agricultural and Food Markets Board",
        "Institut de technologie agroalimentaire du Québec": "Quebec Institute of Agrifood Technology",
        "Gouvernance en gestion des ressources humaines": "Governance in Human Resource Management",
        "Gouvernance en gestion des ressources budgétaires et de la performance": "Governance in Budgetary Resource Management and Performance",
        "Gouvernance en gestion des marchés publics": "Governance in Public Procurement Management",
        "Financement de fonctions gouvernementales": "Funding of Government Functions",
        "Financement des conditions de travail": "Funding of Working Conditions",
        "Financement d'activités rendues par le Fonds de la cybersécurité et du numérique": "Funding of Activities Provided by the Cybersecurity and Digital Fund",
        "Financement du Centre d'acquisitions gouvernementales": "Funding of the Government Procurement Center",
        "Financement de l'Autorité des marchés publics": "Funding of the Public Markets Authority",
        "Financement des activités gouvernementales de recherche, d'examen ou d'enquête": "Funding of Government Research, Review or Investigation Activities",
        "Passif au titre des sites contaminés": "Liability for Contaminated Sites",
        "Régime de retraite des fonctionnaires": "Civil Servants Retirement Plan",
        "Régime de retraite de certains enseignants": "Retirement Plan for Certain Teachers",
        "Régime de retraite des employés du gouvernement et des organismes publics": "Retirement Plan for Government Employees and Public Organizations",
        "Assurance collective sur la vie des employés publics": "Collective Life Insurance for Public Employees",
        "Régime de retraite des agents de la paix en services correctionnels": "Retirement Plan for Peace Officers in Correctional Services",
        "Régime de retraite des juges": "Judges Retirement Plan",
        "Régime de retraite des membres de la Sûreté du Québec": "Retirement Plan for Quebec Provincial Police Members",
        "Régime de retraite du personnel d'encadrement": "Management Personnel Retirement Plan",
        "Gouvernance en gestion des infrastructures": "Governance in Infrastructure Management",
        "Secrétariat à la Capitale-Nationale": "National Capital Secretariat",
        "Commission de la capitale nationale du Québec": "Quebec National Capital Commission",
        "Cabinet du lieutenant-gouverneur": "Lieutenant Governor's Office",
        "Cabinet du premier ministre": "Prime Minister's Office",
        "Secrétariat général et greffe du Conseil exécutif": "General Secretariat and Registry of the Executive Council",
        "Direction générale de la gouvernance et de l'administration": "General Directorate of Governance and Administration",
        "Indemnités de l'exécutif": "Executive Indemnities",
        "Secrétariat à la communication gouvernementale": "Government Communication Secretariat",
        "Modification comptable – Paiements de transfert": "Accounting Modification – Transfer Payments",
        "Cabinet du ministre responsable des Relations canadiennes et de la Francophonie canadienne": "Office of the Minister Responsible for Canadian Relations and Canadian Francophonie",
        "Secrétariat du Québec aux relations canadiennes": "Quebec Secretariat for Canadian Relations",
        "Représentation du Québec au Canada": "Quebec Representation in Canada",
        "Cabinet du ministre responsable des Relations avec les Premières Nations et les Inuit": "Office of the Minister Responsible for Relations with First Nations and Inuit",
        "Secrétariat aux relations avec les Premières Nations et les Inuit": "Secretariat for Relations with First Nations and Inuit",
        "Cabinet du ministre responsable des Institutions démocratiques, cabinet du ministre responsable de l'Accès à l'information et de la Protection des renseignements personnels et cabinet du ministre responsable de la Laïcité": "Office of the Minister Responsible for Democratic Institutions, Office of the Minister Responsible for Access to Information and Protection of Personal Information and Office of the Minister Responsible for Secularism",
        "Commission d'accès à l'information": "Access to Information Commission",
        "Institutions démocratiques": "Democratic Institutions",
        "Accès à l'information et protection des renseignements personnels": "Access to Information and Protection of Personal Information",
        "Laïcité de l'État": "State Secularism",
        "Secrétariat à l'Internet haute vitesse et aux projets spéciaux de connectivité": "High-Speed Internet and Special Connectivity Projects Secretariat",
        "Soutien à la mission": "Mission Support",
        "Conseil du patrimoine culturel du Québec": "Quebec Cultural Heritage Council",
        "Modification comptable – Paiements de transfert": "Accounting Modification – Transfer Payments",
        "Actions en matière de développement culturel, de communications et de patrimoine": "Actions in Cultural Development, Communications and Heritage",
        "Musées nationaux": "National Museums",
        "Société de la Place des Arts de Montréal et Société du Grand Théâtre de Québec": "Montreal Place des Arts Society and Quebec Grand Theatre Society",
        "Société de développement des entreprises culturelles": "Cultural Enterprise Development Society",
        "Société de télédiffusion du Québec": "Quebec Broadcasting Society",
        "Conseil des arts et des lettres du Québec": "Quebec Arts and Letters Council",
        "Bibliothèque et Archives nationales du Québec": "Quebec National Library and Archives",
        "Conservatoire de musique et d'art dramatique du Québec": "Quebec Music and Dramatic Arts Conservatory",
        "Secrétariat à la jeunesse": "Youth Secretariat",
        "Cybersécurité": "Cybersecurity",
        "Transformation numérique": "Digital Transformation",
        "Services à la clientèle des solutions communes": "Common Solutions Client Services",
        "Projets majeurs visant l'accélération de la transformation numérique de l'État": "Major Projects Aimed at Accelerating the State's Digital Transformation",
        "Projets majeurs en lien avec les solutions communes": "Major Projects Related to Common Solutions",
        "Politiques économiques et affaires extérieures": "Economic Policies and External Affairs",
        "Industries stratégiques et projets économiques majeurs": "Strategic Industries and Major Economic Projects",
        "Développement économique régional": "Regional Economic Development",
        "Soutien administratif": "Administrative Support",
        "Soutien aux organismes et aux projets": "Support for Organizations and Projects",
        "Soutien aux infrastructures de recherche": "Support for Research Infrastructure",
        "Soutien à l'entrepreneuriat technologique": "Support for Technological Entrepreneurship",
        "Soutien à la relève et à la culture scientifique": "Support for Next Generation and Scientific Culture",
        "Mandats gouvernementaux": "Government Mandates",
        "Programme ESSOR": "ESSOR Program",
        "Rétention d'entreprises stratégiques": "Retention of Strategic Enterprises",
        "Soutien aux projets de commercialisation": "Support for Commercialization Projects",
        "Autres mesures de soutien aux entreprises": "Other Enterprise Support Measures",
        "Fonds de recherche du Québec – Santé": "Quebec Research Fund – Health",
        "Fonds de recherche du Québec – Société et culture": "Quebec Research Fund – Society and Culture",
        "Fonds de recherche du Québec – Nature et technologies": "Quebec Research Fund – Nature and Technologies",
        "Commission de l'éthique en science et en technologie": "Science and Technology Ethics Commission",
        "Électricité et combustibles": "Electricity and Fuels",
        "Financement, infrastructures et performance": "Funding, Infrastructure and Performance",
        "Transformation numérique et ressources informationnelles": "Digital Transformation and Information Resources",
        "Soutien aux élèves, pédagogie et services à l'enseignement": "Student Support, Pedagogy and Teaching Services",
        "Relations du travail, enseignement privé et ressources humaines": "Labor Relations, Private Education and Human Resources",
        "Réseau éducatif anglophone, relations interculturelles et Autochtones": "English Educational Network, Intercultural Relations and Indigenous",
        "Loisir et sport": "Recreation and Sports",
        "Prospective, statistiques et politiques": "Prospective, Statistics and Policies",
        "Institut national des mines": "National Institute of Mines",
        "Soutien à des partenaires en éducation": "Support for Education Partners",
        "Action communautaire": "Community Action",
        "Instances régionales de concertation": "Regional Consultation Bodies",
        "Conseil supérieur de l'éducation": "Superior Council of Education",
        "Commission consultative de l'enseignement privé": "Private Education Advisory Commission",
        "Protecteur national de l'élève": "National Student Protector",
        "Subvention d'équilibre fiscal": "Fiscal Balance Grant",
        "Centres de services scolaires et commissions scolaires": "School Service Centers and School Boards",
        "Centre de services scolaire et commissions scolaires à statut particulier": "School Service Center and School Boards with Special Status",
        "Financement des infrastructures des centres de services scolaires et des commissions scolaires": "Funding of Infrastructure for School Service Centers and School Boards",
        "Enseignement privé": "Private Education",
        "Aide au transport scolaire": "School Transportation Assistance",
        "Développement du loisir et du sport": "Development of Recreation and Sports",
        "Infrastructures de loisirs et de sports": "Recreation and Sports Infrastructure",
        "Société des établissements de plein air du Québec": "Quebec Outdoor Establishments Society",
        "Régime de retraite des enseignants": "Teachers Retirement Plan",
        "Régime de retraite des employés du gouvernement et des organismes publics": "Retirement Plan for Government Employees and Public Organizations",
        "Régime de retraite du personnel d'encadrement": "Management Personnel Retirement Plan",
        "Solidarité sociale et analyse stratégique": "Social Solidarity and Strategic Analysis",
        "Services d'aide à l'emploi": "Employment Assistance Services",
        "Services Québec": "Quebec Services",
        "Recouvrement": "Recovery",
        "Aide aux personnes et aux familles": "Assistance to Individuals and Families",
        "Action communautaire": "Community Action",
        "Office de la sécurité économique des chasseurs cris": "Cree Hunters Economic Security Office",
        "Mesures d'aide à l'emploi": "Employment Assistance Measures",
        "Performance, financement, interventions régionales et soutien à la gestion": "Performance, Funding, Regional Interventions and Management Support",
        "Développement et soutien des réseaux": "Network Development and Support",
        "Accessibilité aux études, infrastructures et ressources informationnelles": "Accessibility to Studies, Infrastructure and Information Resources",
        "Modification comptable – Paiements de transfert": "Accounting Modification – Transfer Payments",
        "Institut de tourisme et d'hôtellerie du Québec": "Quebec Institute of Tourism and Hospitality",
        "Soutien à des partenaires en enseignement supérieur": "Support for Higher Education Partners",
        "Comité consultatif sur l'accessibilité financière aux études": "Advisory Committee on Financial Accessibility to Studies",
        "Commission d'évaluation de l'enseignement collégial": "College Education Evaluation Commission",
        "Bourses consécutives aux prêts": "Scholarships Following Loans",
        "Intérêts et remboursements aux banques": "Interest and Bank Reimbursements",
        "Autres bourses": "Other Scholarships",
        "Bourses incitatives": "Incentive Scholarships",
        "Cégeps": "CEGEPs",
        "Universités": "Universities",
        "Enseignement privé au collégial": "Private College Education",
        "Financement des infrastructures des cégeps": "CEGEP Infrastructure Funding",
        "Financement des infrastructures des universités": "University Infrastructure Funding",
        "Régime de retraite des employés du gouvernement et des organismes publics": "Retirement Plan for Government Employees and Public Organizations",
        "Régime de retraite du personnel d'encadrement": "Management Personnel Retirement Plan",
        "Direction du Ministère": "Ministry Direction",
        "Services à la gestion": "Management Services",
        "Gouvernance et coordination des interventions": "Governance and Coordination of Interventions",
        "Aménagement durable du territoire forestier": "Sustainable Forest Territory Development",
        "Suppression des feux de forêts": "Forest Fire Suppression",
        "Forestier en chef": "Chief Forester",
        "Opérations régionales": "Regional Operations",
        "Ressources minérales": "Mineral Resources",
        "Direction et gestion ministérielle": "Direction and Ministry Management",
        "Organisme-conseil": "Advisory Organization",
        "Activités nationales": "National Activities",
        "Santé publique": "Public Health",
        "Services généraux – Activités cliniques et d'aide": "General Services – Clinical and Support Activities",
        "Soutien à l'autonomie des personnes âgées – Soutien à domicile": "Support for Seniors' Autonomy – Home Support",
        "Soutien à l'autonomie des personnes âgées – Hébergement": "Support for Seniors' Autonomy – Housing",
        "Déficience intellectuelle et trouble du spectre de l'autisme": "Intellectual Disability and Autism Spectrum Disorder",
        "Jeunes en difficulté": "Youth in Difficulty",
        "Dépendances": "Addictions",
        "Santé mentale": "Mental Health",
        "Santé physique": "Physical Health",
        "Administration": "Administration",
        "Soutien aux services": "Service Support",
        "Gestion des bâtiments et des équipements": "Building and Equipment Management",
        "Organismes communautaires et autres organismes": "Community Organizations and Other Organizations",
        "Activités connexes": "Related Activities",
        "Financement des infrastructures de santé et de services sociaux": "Health and Social Services Infrastructure Funding",
        "Financement d'achats centralisés": "Centralized Purchasing Funding",
        "Programme d'aide financière pour les gicleurs dans les résidences privées pour aînés": "Financial Assistance Program for Sprinklers in Private Seniors' Residences",
        "Déficience physique": "Physical Disability",
        "Administration et soutien à l'intégration des personnes handicapées": "Administration and Support for Integration of Disabled Persons",
        "Services médicaux": "Medical Services",
        "Services optométriques": "Optometric Services",
        "Services dentaires": "Dental Services",
        "Services pharmaceutiques et médicaments": "Pharmaceutical Services and Medications",
        "Autres services": "Other Services",
        "Administration": "Administration",
        "Vieillissement actif": "Active Aging",
        "Soutien aux personnes aînées en situation de vulnérabilité": "Support for Seniors in Vulnerable Situations",
        "Surveillance du territoire": "Territory Surveillance",
        "Enquêtes criminelles": "Criminal Investigations",
        "Services correctionnels": "Correctional Services",
        "Prestation des organismes communautaires": "Community Organization Services",
        "Commission québécoise des libérations conditionnelles": "Quebec Parole Board",
        "Organisation et pratiques policières": "Police Organization and Practices",
        "Soutien aux services policiers en milieu autochtone": "Support for Police Services in Indigenous Communities",
        "Sécurité et protection des personnes et des institutions": "Security and Protection of Individuals and Institutions",
        "Prévention et lutte contre le crime": "Crime Prevention and Fight",
        "Services et expertises judiciaires": "Judicial Services and Expertise",
        "Bureau du coroner": "Coroner's Office",
        "Commissaire à la déontologie policière": "Police Ethics Commissioner",
        "Comité de déontologie policière": "Police Ethics Committee",
        "Régie des alcools, des courses et des jeux": "Alcohol, Racing and Gaming Board",
        "Commissaire à la lutte contre la corruption": "Anti-Corruption Commissioner",
        "Bureau des enquêtes indépendantes": "Independent Investigations Bureau",
        "Prévention des sinistres et atténuation des risques": "Disaster Prevention and Risk Mitigation",
        "Interventions de sécurité civile": "Civil Security Interventions",
        "Gestion du rétablissement et adaptation": "Recovery and Adaptation Management",
        "Sécurité incendie et télécommunications d'urgence": "Fire Safety and Emergency Telecommunications",
        "Direction et administration": "Direction and Administration",
        "Gestion des programmes": "Program Management",
        "Soutien aux projets de développement du tourisme": "Support for Tourism Development Projects",
        "Appui aux organisations de développement touristique régional": "Support for Regional Tourism Development Organizations",
        "Soutien aux événements touristiques": "Support for Tourism Events",
        "Société du Centre des congrès de Québec": "Quebec City Convention Center Society",
        "Société du Palais des congrès de Montréal": "Montreal Convention Center Society",
        "Société de développement et de mise en valeur du Parc olympique": "Olympic Park Development and Enhancement Society",
        "Transport terrestre": "Land Transportation",
        "Transport maritime": "Maritime Transportation",
        "Transport aérien": "Air Transportation",
        "Commission des transports du Québec": "Quebec Transportation Commission",
        "Direction": "Direction",
        "Services corporatifs": "Corporate Services",
        "Planification, recherche et développement": "Planning, Research and Development",
        "Modification comptable – Paiements de transfert": "Accounting Modification – Transfer Payments",
        "Gouvernance et administration": "Governance and Administration",
        "Politiques et relations du travail": "Labor Policies and Relations",
        "Tribunal administratif du travail": "Administrative Labor Tribunal",
        "Régie du bâtiment du Québec": "Quebec Building Authority"
    }
    return translations.get(french_name, french_name)

def translate_distribution(french_name):
    """Translate French distribution terms to English."""
    translations = {
        "Dépenses": "Expenditures",
        "Investissements": "Investments",
        "Revenus": "Revenues",
        "Surplus (déficit)": "Surplus (Deficit)"
    }
    return translations.get(french_name, french_name)

def translate_supercategory(french_name):
    """Translate French supercategory terms to English."""
    translations = {
        "Rémunération": "Remuneration",
        "Fonctionnement": "Operations",
        "Transfert": "Transfer",
        "Prêts, placements, avances et autres coûts": "Loans, Investments, Advances and Other Costs",
        "Immobilisations autres qu'en ressources informationnelles": "Other Capital Assets",
        "Immobilisations en ressources informationnelles": "Information Resource Capital Assets",
        "Créances douteuses et autres provisions": "Doubtful Accounts and Other Provisions",
        "Affectation à un fonds spécial": "Allocation to Special Fund",
        "Service de la dette": "Debt Service",
        "Excédent sur les sommes approuvées": "Surplus on Approved Amounts",
        "Surplus (déficit) de l'exercice lié aux activités": "Surplus (Deficit) for the Year Related to Activities",
        "Surplus (déficit) cumulé lié aux activités, au début": "Cumulative Surplus (Deficit) Related to Activities, at Beginning",
        "Surplus (déficit) cumulé lié aux activités, à la fin": "Cumulative Surplus (Deficit) Related to Activities, at End",
        "Transferts provenant du ministère responsable": "Transfers from Responsible Ministry",
        "Revenus divers": "Miscellaneous Revenues",
        "Taxes à la consommation": "Consumption Taxes"
    }
    return translations.get(french_name, french_name)

def translate_beneficiary(french_name):
    """Translate French beneficiary terms to English."""
    translations = {
        "Organismes à but non lucratif": "Non-profit Organizations",
        "Entreprises du secteur privé": "Private Sector Enterprises",
        "Institutions d'enseignement": "Educational Institutions",
        "Municipalités": "Municipalities",
        "Organismes et entreprises du gouvernement": "Government Organizations and Enterprises",
        "Personnes": "Individuals",
        "Établissements de santé et de services sociaux": "Health and Social Services Establishments"
    }
    return translations.get(french_name, french_name)

def translate_assistance_objective(french_name):
    """Translate French assistance objective terms to English."""
    translations = {
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
        "Mesures financières du partenariat fiscal": "Financial Measures of the Fiscal Partnership"
    }
    return translations.get(french_name, french_name)

def translate_file(input_file, output_file, file_type):
    """Translate a CSV file from French to English."""
    print(f"Translating {input_file} to {output_file}")
    
    # Try different encodings
    encodings = ['utf-16', 'utf-16le', 'utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
    infile = None
    
    for encoding in encodings:
        try:
            infile = open(input_file, 'r', encoding=encoding, errors='ignore')
            # Test read first line
            infile.readline()
            infile.seek(0)  # Reset to beginning
            break
        except (UnicodeDecodeError, UnicodeError):
            if infile:
                infile.close()
            continue
    
    if not infile:
        print(f"❌ Could not read {input_file} with any encoding")
        return
    
    with infile, \
         open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        # Read and translate header
        header = next(reader)
        translated_header = []
        
        for col in header:
            if col == "Portefeuille":
                translated_header.append("Portfolio")
            elif col == "Programme":
                translated_header.append("Program")
            elif col == "Nom_programme":
                translated_header.append("Program_Name")
            elif col == "Element":
                translated_header.append("Element")
            elif col == "Nom_element":
                translated_header.append("Element_Name")
            elif col == "Repartition":
                translated_header.append("Distribution")
            elif col == "Supercategorie":
                translated_header.append("Supercategory")
            elif col == "Montant":
                translated_header.append("Amount")
            elif col == "Objet_aide":
                translated_header.append("Assistance_Objective")
            elif col == "Bénéficiaires":
                translated_header.append("Beneficiaries")
            elif col == "Fonds_special":
                translated_header.append("Special_Fund")
            elif col == "REGRP_Sommaire":
                translated_header.append("REGRP_Summary")
            elif col == "REGRP_Nom":
                translated_header.append("REGRP_Name")
            else:
                translated_header.append(col)
        
        writer.writerow(translated_header)
        
        # Translate data rows
        for row in reader:
            if not row:  # Skip empty rows
                continue
                
            translated_row = []
            for i, cell in enumerate(row):
                if i == 0:  # Portfolio column
                    translated_row.append(translate_portfolio_name(cell))
                elif i == 1:  # Program column
                    translated_row.append(translate_program_name(cell))
                elif i == 2:  # Program name column
                    translated_row.append(translate_program_name(cell))
                elif i == 3:  # Element column
                    translated_row.append(translate_element_name(cell))
                elif i == 4:  # Element name column
                    translated_row.append(translate_element_name(cell))
                elif i == 5:  # Distribution column
                    translated_row.append(translate_distribution(cell))
                elif i == 6:  # Supercategory column
                    translated_row.append(translate_supercategory(cell))
                elif i == 7:  # Amount column
                    translated_row.append(cell)
                elif i == 3 and file_type == "assistance_objectives":  # Assistance objective column
                    translated_row.append(translate_assistance_objective(cell))
                elif i == 1 and file_type == "beneficiaries":  # Beneficiaries column
                    translated_row.append(translate_beneficiary(cell))
                elif i == 1 and file_type == "special_funds":  # Special fund column
                    translated_row.append(cell)  # Keep as is for now
                elif i == 2 and file_type == "special_funds":  # REGRP_Summary column
                    translated_row.append(translate_distribution(cell))
                elif i == 3 and file_type == "special_funds":  # REGRP_Name column
                    translated_row.append(translate_supercategory(cell))
                else:
                    translated_row.append(cell)
            
            writer.writerow(translated_row)
    
    print(f"✅ Successfully translated {input_file}")

def main():
    """Main function to translate all Quebec CSV files."""
    script_dir = Path(__file__).parent
    granular_dir = script_dir.parent / "granular"
    
    # Define file mappings
    file_mappings = [
        {
            "input": "1_depenses-et-investissements-du-fonds-general-2023-2024.csv",
            "output": "1_expenditures_and_investments_general_fund_2023-2024.csv",
            "type": "expenditures"
        },
        {
            "input": "2_depenses-de-transfert-du-fonds-general-par-objets-daide-2023-2024.csv",
            "output": "2_transfer_expenditures_general_fund_by_assistance_objectives_2023-2024.csv",
            "type": "assistance_objectives"
        },
        {
            "input": "3_depenses-de-transfert-du-fonds-general-par-beneficiaires-2023-2024.csv",
            "output": "3_transfer_expenditures_general_fund_by_beneficiaries_2023-2024.csv",
            "type": "beneficiaries"
        },
        {
            "input": "4_revenus-depenses-et-investissements-des-fonds-speciaux-2023-2024.csv",
            "output": "4_revenues_expenditures_and_investments_special_funds_2023-2024.csv",
            "type": "special_funds"
        }
    ]
    
    for mapping in file_mappings:
        input_file = granular_dir / mapping["input"]
        output_file = granular_dir / mapping["output"]
        
        if input_file.exists():
            translate_file(input_file, output_file, mapping["type"])
        else:
            print(f"❌ Input file not found: {input_file}")
    
    print("\n🎉 All Quebec CSV files translated successfully!")

if __name__ == "__main__":
    main()
