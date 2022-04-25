tax_rate = 0.2      #tax rate = 20%
gr_inc = int(input('gross income = '))
num_dep = int(input('number of dependents = '))
std_ded = 10000
dep_ded = 3000

#taxable income = gross income - std deduction - (dep deduction*no. of dep)

tax_inc = gr_inc - std_ded - (dep_ded*num_dep)

#tax = taxable income*tax rate\
tax = tax_inc*tax_rate

print(tax_inc)
print(tax)
