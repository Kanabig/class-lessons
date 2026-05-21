import calculator
import convert_unit

calculator.add(1, 2)
calculator.sub(1, 2)
calculator.mul(1, 2)
calculator.div(1, 2)
calculator.rst(1, 2)
calculator.prt(1, 2)

calculator.div(1, 0)


length_mm = int(input("길이(mm): "))
result = convert_unit.convertUnit(length_mm)
convert_unit.printLength(result)
