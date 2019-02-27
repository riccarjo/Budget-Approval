# PSMA 7124 Budget Activity

# Users

u_orourke = 0
u_rand = 0
u_romney = 0
u_cortez = 0
u_sanders = 0



# Original Master Budget

# Revenues

m_income = 12000
m_sales = 9000
m_corporation = 1750
m_fees = 5000

m_revenues = m_income + m_sales + m_corporation + m_fees

# Expenses

m_gov = 450
m_agri = 20
m_banking = 65
m_children = 1150
m_community = 840
m_corrections = 1000
m_education = 12000
m_environment = 275
m_health = 1525
m_human = 6000
m_labor = 170
m_law = 580
m_military = 95
m_transportation = 1800
m_treasury = 2200
m_pension = 2100
m_misc = 1

m_expenses = m_gov + m_agri + m_banking + m_children + m_community + m_corrections + m_education + m_environment + m_health + m_human + m_labor + m_law + m_military + m_transportation + m_treasury + m_pension + m_misc

# Approved Budget

print("Please enter your estimated budget revenues: ")
print("\nRevenues")


a_income = int(input("\nIncome tax: "))

change_income = 100 * (a_income - m_income) / m_income

if change_income > 0:
    print("The new Income Tax is", change_income, "percent higher than the Master budget.")
    print("\nGovernor O'Rourke receives 2 points")
    print("Senator Cortez receives 3 points.")
    print("Senator Sanders receives 5 points.")
    u_orourke += 2
    u_cortez += 3
    u_sanders += 5
else:
    print("The new Income Tax is", abs(change_income),"percent lower than the Master budget.")
    print("\nSenator Rand receives 6 points.")
    print("Senator Romney receives 3 points.")
    u_rand += 6
    u_romney += 3
    



a_sales = int(input("\nSales tax: "))

change_sales = 100 * (a_sales - m_sales) / m_sales

if change_sales > 0:
    print("The new Sales Tax is", change_sales, "percent higher than the Master budget.")
    print("\nGovernor O'Rourke receives 2 points")
    print("Senator Cortez receives 3 points.")
    print("Senator Sanders receives 2 points.")
    u_orourke += 2
    u_cortez += 3
    u_sanders += 2
else:
    print("The new Sales Tax is", abs(change_sales),"percent lower than the Master budget.")
    print("\nSenator Rand receives 2 points.")
    print("Senator Romney receives 2 points.")
    u_rand += 2
    u_romney += 2



a_corporation = int(input("\nCorporation tax: "))

change_corporation = 100 * (a_corporation - m_corporation) / m_corporation

if change_corporation > 0:
    print("The new Corporate Tax is", change_corporation, "percent higher than the Master budget.")
    print("\nGovernor O'Rourke receives 4 points")
    print("Senator Cortez receives 6 points.")
    print("Senator Sanders receives 5 points.")
    u_orourke += 4
    u_cortez += 6
    u_sanders += 5
else:
    print("The new Corporate Tax is", abs(change_corporation),"percent lower than the Master budget.")
    print("\nSenator Rand receives 2 points.")
    print("Senator Romney receives 5 points.")
    u_rand += 2
    u_romney += 5

a_fees = int(input("\nFee income: "))

change_fees = 100 * (a_fees - m_fees) / m_fees

if change_fees > 0:
    print("The new Fees and Other Tax is", change_fees, "percent higher than the Master budget.")
    print("\nGovernor O'Rourke receives 3 points")
    print("Senator Cortez receives 2 points.")
    print("Senator Sanders receives 2 points.")
    u_orourke += 3
    u_cortez += 2
    u_sanders += 2
else:
    print("The new Fees and Other Tax is", abs(change_fees),"percent lower than the Master budget.")
    print("\nSenator Rand receives 3 points.")
    print("Senator Romney receives 3 points.")
    u_rand += 3
    u_romney += 3

print("\n\nSo far:")
print("\nGovernor O'Rourke has", u_orourke,"points.")
print("Senator Rand has", u_rand,"points.")
print("Senator Romney has", u_romney,"points.")
print("Senator Cortez has", u_cortez,"points.")
print("Senator Sanders has", u_sanders,"points.") 

# Expenses
print("\n\nPlease enter your approved budget expenditures: ")
print("\nExpenses")

a_gov = int(input("\nGovernment and Interdepartmental spending: "))

change_gov = 100 * (a_gov - m_gov) / m_gov

if change_gov > 0:
    print("The new budgeted expenditures for Interdepartmental spending are", change_gov, "percent higher than the Master budget.")
    print("No one receives any points.")
    print("Wow.  Way to make things worse!")
else:
    print("The new budgeted expenditures for Interdepartmental spending are", abs(change_gov),"percent lower than the Master budget.")
    print("\nGovernor O'Rourke receives 2 points.")
    print("Senator Rand receives 3 points.")
    print("Senator Romney receives 4 points.")
    print("Senator Cortez receives 1 point.")
    print("Senator Sanders receives 1 point.")
    u_orourke += 2
    u_rand += 3
    u_romney += 4
    u_cortez += 1
    u_sanders += 1

a_agri = int(input("\nAgricultural spending: "))

change_agri = 100 * (a_agri - m_agri) / m_agri

if change_agri > 0:
    print("The new budgeted expenditures for Agriculture are", change_agri, "percent higher than the Master budget.")
    print("Senator Cortez receives 1 points.")
    print("Senator Sanders receives 1 points.")
    u_cortez += 1
    u_sanders += 1
else:
    print("The new budgeted expenditures for Agriculture are", abs(change_agri),"percent lower than the Master budget.")
    print("\nGovernor O'Rourke receives 2 points.")
    print("Senator Rand receives 2 points.")
    print("Senator Romney receives 2 points.")
    u_orourke += 2
    u_rand += 2
    u_romney += 2

    
a_banking = int(input("\nBanking and Insurance spending: "))

change_banking = 100 * (a_banking - m_banking) / m_banking

if change_banking > 0:
    print("The new budgeted expenditures for Banking and Insurance are", change_banking, "percent higher than the Master budget.")
    print("\nGovernor O'Rourke receives 3 points.")
    print("Senator Cortez receives 4 point.s")
    print("Senator Sanders receives 3 points.")
    u_orourke += 3
    u_cortez += 4
    u_sanders += 3
else:
    print("The new budgeted expenditures for Banking and Insurance are", abs(change_banking),"percent lower than the Master budget.")
    print("\nSenator Rand receives 2 points.")
    print("Senator Romney receives 1 points.")
    u_rand += 2
    u_romney += 1


a_children = int(input("\nChildren and Family spending: "))

change_children = 100 * (a_children - m_children) / m_children

if change_children > 0:
    print("The new budgeted expenditures for Children and Family spending are", change_children, "percent higher than the Master budget.")
    print("\nGovernor O'Rourke receives 5 points.")
    print("Senator Cortez receives 5 points.")
    print("Senator Sanders receives 3 points.")
    u_orourke += 5
    u_cortez += 5
    u_sanders += 3
else:
    print("The new budgeted expenditures for Children and Family spending are", abs(change_children),"percent lower than the Master budget.")
    print("\nSenator Rand receives 2 points.")
    print("Senator Romney receives 2 points.")
    u_rand += 2
    u_romney += 2
    
a_community = int(input("\nCommunity Affairs spending: "))

change_community = 100 * (a_community - m_community) / m_community

if change_community > 0:
    print("The new budgeted expenditures for Community Affairs spending are", change_community, "percent higher than the Master budget.")
    print("\nSenator Cortez receives 3 points.")
    print("Senator Sanders receives 3 points.")
    u_cortez += 3
    u_sanders += 3
else:
    print("The new budgeted expenditures for Community Affairs spending are", abs(change_community),"percent lower than the Master budget.")
    print("\nGovernor O'Rourke receives 2 points.")
    print("Senator Rand receives 3 points.")
    print("Senator Romney receives 3 points.")
    u_orourke += 2
    u_rand += 3
    u_romney += 3
    
a_corrections = int(input("\nCorrections spending: "))

change_corrections = 100 * (a_corrections - m_corrections) / m_corrections

if change_corrections > 0:
    print("The new budgeted expenditures for Corrections spending are", change_corrections, "percent higher than the Master budget.")
    print("\nNo one receives any points.")
else:
    print("The new budgeted expenditures for Corrections are", abs(change_corrections),"percent lower than the Master budget.")
    print("\nGovernor O'Rourke receives 2 points.")
    print("Senator Rand receives 2 points.")
    print("Senator Romney receives 2 points.")
    print("Senator Cortez receives 1 point.")
    print("Senator Sanders receives 2 point.")
    u_orourke +=2
    u_rand += 2
    u_romney += 2
    u_cortez += 1
    u_sanders += 2
    
a_education = int(input("\nEducation spending: "))

change_education = 100 * (a_education - m_education) / m_education

if change_education > 0:
    print("The new budgeted expenditures for Education spending are", change_education, "percent higher than the Master budget.")
    print("\nSenator Cortez receives 5 points.")
    print("Senator Sanders receives 3 points.")
    u_cortez += 5
    u_sanders += 3
else:
    print("The new budgeted expenditures for Education spending are", abs(change_education),"percent lower than the Master budget.")
    print("\nGovernor O'Rourke receives 2 points.")
    print("Senator Rand receives 1 point.")
    print("Senator Romney receives 2 points.")
    u_orourke += 2
    u_rand += 1
    u_romney += 2
    
a_environment = int(input("\nEnvironmental Protection spending: "))

change_environment = 100 * (a_environment - m_environment) / m_environment

if change_environment > 0:
    print("The new budgeted expenditures for Environmental Protection spending are", change_environment, "percent higher than the Master budget.")
    print("\nGovernor O'Rourke receives 5 points.")
    print("Senator Cortez receives 4 points.")
    print("Senator Sanders receives 4 points.")
    u_orourke += 5
    u_cortez += 4
    u_sanders += 4
else:
    print("The new budgeted expenditures for Environmental Protection spending are", abs(change_environment),"percent lower than the Master budget.")
    print("\nSenator Rand receives 2 points.")
    print("Senator Romney receives 3 points.")
    u_rand += 2
    u_romney += 3
    
a_health = int(input("\nHealth spending: "))

change_health = 100 * (a_health - m_health) / m_health

if change_health > 0:
    print("The new budgeted expenditures for Health spending are", change_health, "percent higher than the Master budget.")
    print("\nGovernor O'Rourke receives 5 points.")
    print("Senator Cortez receives 4 points.")
    print("Senator Sanders receives 5 points.")
    print("Senator Romney receives 3 points.")
    u_orourke += 5
    u_cortez += 4
    u_sanders += 5
    u_romney += 3
else:
    print("The new budgeted expenditures for Health spending are", abs(change_children),"percent lower than the Master budget.")
    print("\nSenator Rand receives 2 points.")
    u_rand += 2
    
a_human = int(input("\nHuman Services spending: "))

change_human = 100 * (a_human - m_human) / m_human

if change_human > 0:
    print("The new budgeted expenditures for Human Services spending are", change_human, "percent higher than the Master budget.")
    print("\nGovernor O'Rourke receives 5 points.")
    print("Senator Cortez receives 5 points.")
    print("Senator Sanders receives 4 points.")
    u_orourke += 5
    u_cortez += 5
    u_sanders += 4
else:
    print("The new budgeted expenditures for Human Services spending are", abs(change_human),"percent lower than the Master budget.")
    print("\nSenator Rand receives 2 points.")
    print("Senator Romney receives 3 points.")
    u_rand += 2
    u_romney += 3
    
a_labor = int(input("\nLabor and Workforce spending: "))

change_labor = 100 * (a_labor - m_labor) / m_labor

if change_labor > 0:
    print("The new budgeted expenditures for Labor and Workforce spending are", change_labor, "percent higher than the Master budget.")
    print("\nSenator Cortez receives 4 points.")
    print("Senator Sanders receives 3 points.")
    u_cortez += 4
    u_sanders += 3
else:
    print("The new budgeted expenditures for Labor and Workforce spending are", abs(change_labor),"percent lower than the Master budget.")
    print("\nGovernor O'Rourke receives 2 points.")
    print("Senator Rand receives 3 points.")
    print("Senator Romney receives 4 points.")
    u_orourke += 2
    u_rand += 3
    u_romney += 4
    
a_law = int(input("\nLaw and Public Safety spending: "))

change_law = 100 * (a_law - m_law) / m_law

if change_law > 0:
    print("The new budgeted expenditures for Law and Public Safety spending are", change_law, "percent higher than the Master budget.")
    print("\nSenator Cortez receives 3 points.")
    print("Senator Sanders receives 1 points.")
    print("Senator Rand receives 5 points.")
    print("Senator Romney receives 6 points.")
    u_cortez += 3
    u_sanders += 1
    u_rand += 5
    u_romney += 6
else:
    print("The new budgeted expenditures for Law and Public Safety spending are", abs(change_law),"percent lower than the Master budget.")
    print("\nSenator O'Rourke receives 1 point.")
    u_orourke += 1
    
a_military = int(input("\nMilitary and Veteran Affairs spending: "))

change_military = 100 * (a_military - m_military) / m_military

if change_military > 0:
    print("The new budgeted expenditures for Military and Veteran spending are", change_military, "percent higher than the Master budget.")
    print("\nSenator Rand receives 5 points.")
    print("Senator Romney receives 6 points.")
    print("Senator Cortez receives 1 points.")
    print("Senator Sanders receives 2 points.")
    u_rand += 5
    u_romney += 6
    u_cortez += 1
    u_sanders += 2
else:
    print("The new budgeted expenditures for Military and Veteran spending are", abs(change_military),"percent lower than the Master budget.")
    print("\nGovernor O'Rourke receives 2 points.")
    u_orourke += 2
    
    
a_transportation = int(input("\nTransportation spending: "))

change_transportation = 100 * (a_transportation - m_transportation) / m_transportation

if change_transportation > 0:
    print("The new budgeted expenditures for Transportation spending are", change_transportation, "percent higher than the Master budget.")
    print("\nGovernor O'Rourke receives 5 points.")
    print("Senator Cortez receives 2 points.")
    print("Senator Sanders receives 5 points.")
    u_orourke += 5
    u_cortez += 2
    u_sanders += 5
else:
    print("The new budgeted expenditures for Transportation spending are", abs(change_transportation),"percent lower than the Master budget.")
    print("\nSenator Rand receives 3 points.")
    print("Senator Romney receives 2 points.")
    u_rand += 3
    u_romney += 2
    

a_treasury = int(input("\nTreasury spending: "))

change_treasury = 100 * (a_treasury - m_treasury) / m_treasury

if change_treasury > 0:
    print("The new budgeted expenditures for Treasury spending are", change_treasury, "percent higher than the Master budget.")
    print("\nSenator Cortez receives 1 points.")
    print("Senator Sanders receives 2 points.")
    u_cortez += 1
    u_sanders += 2
else:
    print("The new budgeted expenditures for Treasury spending are", abs(change_environment),"percent lower than the Master budget.")
    print("\nGovernor O'Rourke receives 2 points.")
    print("Senator Rand receives 3 points.")
    print("Senator Romney receives 1 points.")
    u_orourke += 2
    u_rand += 3
    u_romney += 1
    

a_pension = int(input("\nPensions spending: "))

change_pension = 100 * (a_pension - m_pension) / m_pension

if change_environment > 0:
    print("The new budgeted expenditures for Pension spending are", change_pension, "percent higher than the Master budget.")
    print("\nSenator Rand receives 5 points.")
    print("Senator Cortez receives 1 points.")
    print("Senator Sanders receives 2 points.")
    u_rand += 5
    u_cortez += 1
    u_sanders += 2
else:
    print("The new budgeted expenditures for Pension spending are", abs(change_pension),"percent lower than the Master budget.")
    print("\nGovernor O'Rourke receives 2 points.")
    print("Senator Romney receives 1 points.")
    u_orourke += 2
    u_romney += 1
    

a_misc = int(input("\nMiscellaneous spending: "))

change_misc = 100 * (a_misc - m_misc) / m_misc

if change_misc > 0:
    print("The new budgeted expenditures for Miscellaneous spending are", change_misc, "percent higher than the Master budget.")
    print("\nSenator Cortez receives 1 points.")
    print("Senator Sanders receives 2 points.")
    u_cortez += 1
    u_sanders += 2
else:
    print("The new budgeted expenditures for Miscellaneous spending are", abs(change_misc),"percent lower than the Master budget.")
    print("\nGovernor O'Rourke receives 2 points.")
    print("Senator Rand receives 2 points.")
    print("Senator Romney receives 2 points.")
    u_orourke += 2
    u_rand += 2
    u_romney += 2
    


print("\n\nThe results are in!")
print("\nGovernor O'Rourke has", u_orourke,"points.")
print("Senator Rand has", u_rand,"points.")
print("Senator Romney has", u_romney,"points.")
print("Senator Cortez has", u_cortez,"points.")
print("Senator Sanders has", u_sanders,"points.") 

data = {
    "Governor O Rourke": u_orourke,
    "Senator Rand": u_rand,
    "Senator Romney": u_romney,
    "Senator Cortez": u_cortez,
    "Senator Sanders": u_sanders
}

winner = max(data, key=data.get)

print("And the winner is: ")
print(winner,"!!!")
print("\n\nCongratulations,", winner, "!")




input("\n\nPress any key to exit")


