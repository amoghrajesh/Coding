def calculate(ram, total_tlb, overcommit_ratio, total_swap):
    return (ram-total_tlb)*overcommit_ratio/100 + total_swap


print(calculate(2, 0.00023841857910155263, 300, 8))