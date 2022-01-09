# Write program to generate equated monthly instalments (EMI)(intrest 5%/Month) of 3 year and 5 year of amount 161258/-
a=161258

month3=a/36

month5=a/60

emi3=month3+(0.05 * month3)

emi5=month5+(0.05 * month5)

print("EMI for 3 years with intrest 5%",emi3)

print("EMI for 5 years with intrest 5%",emi5)