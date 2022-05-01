
def arithmetic_arranger(problems):
  if len(problems)>5: return "Error: Too many problems."
  for problem in problems:
    for p in problem:
        item = p.split(' ')
        if item[0].isdecimal() and item[2].isdecimal():
            if item[1] == '+' or item[1] == '-':
                if len(item[0]) < 5 and len(item[2]) < 5:
                    firstOP.append(item[0])
                    operators.append(item[1])
                    secondOP.append(item[2])
                    if item[1] == "+": results.append(str(int(item[0]) + int(item[2])))
                    else: results.append(str(int(item[0]) - int(item[2])))
                    spacer = " " * 3
                    line1, line2, dashes, line3 = "", "", "", ""
                    for index in range(len(firstOP)):
                        result = results[index]
                        width = max(len(firstOP[index]), len(secondOP[index]))
                        line1 += spacer + " " + " " + firstOP[index].rjust(width)
                        line2 += spacer + operators[index] + " " + secondOP[index].rjust(width)
                        dashes += spacer + "-" * (width + 2)
                        line3 += spacer + " " * (2 - len(result) + width) + result
                    output = line1 + "\n" + line2 + "\n" + dashes
                else: return "Error: Numbers cannot be more than four digits."
            else: return "Error: Operator must be '+' or '-'."
        else: return "Error: Numbers must only contain digits." 
    firstOP.clear()
    secondOP.clear()
    results.clear()
    operators.clear() 
    return output 



# [['3801 - 2', '123 + 49']],
#         '  3801      123\n'
#         '-    2    +  49\n'
#         '------    -----',
#         'Expected different output when calling "arithmetic_arranger()" with ["3801 - 2", "123 + 49"]',

firstOP = list()
secondOP = list()
results = list()
operators = list()
ejemplo = [['3801 - 2', '123 + 49']]

print(arithmetic_arranger(ejemplo))