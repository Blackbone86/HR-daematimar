r_0_str = input("What's the basic reproduction rate (R_0)? ")
# Convert input to float
# Calculate the expected number of cases after 3 rounds of transmission originating
# from kitten Zero
r_0_float = float(r_0_str)
total_cases = 1 + r_0_float + r_0_float**2 + r_0_float**3
print("Total cases after 3 rounds of transmission:", round(total_cases))