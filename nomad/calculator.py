#계산기 만들기
text = 'go'
while text == 'go' or text == "Go" :
  text=input('Enter "go", then you can start this calculator : ')
  a = int(input("Number a = "))
  b = int(input("Number b = "))
  op = str(input("Operator?(+,-,x,/,power, negation, remainder) "))
  def pl(a, b):
    return int(a + b)
  def min(a, b):
    return int(a - b)
  def tms(a, b):
    return int(a * b)
  def div(a, b):
    return int(a / b)
  def ngt(a, b):
    return int(-a)
  def po(a, b):
    return int(a ** b)
  def rmd(a, b):
    return int(a % b)

  if op == "+" :
    print(pl(a, b))
  elif op == "-" :
    print(min(a,b))
  elif op == "x" :
    print(tms(a,b))
  elif op == "/" :
    result_div = div(a, b)
    print(result_div)
  elif op == "negation" :
    result_neg = ngt(a, b)
    print(result_neg)
  elif op == "power" :
    result_po = po(a, b)
    print(result_po)
  elif op == "remainder" :
    result_rmd = rmd(a, b)
    print(result_rmd)
  else :
    print("Error : it's not an Operator")

