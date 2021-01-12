# Added white space at the end of ASCII art so that the mirror version looks good

rock = '''
    _______  
---'   ____) 
      (_____)
      (_____)
      (____) 
---.__(___)  
'''

paper = '''
    _______       
---'   ____)____  
          ______) 
          _______)
         _______) 
---.__________)   
'''

scissors = '''
    _______       
---'   ____)____  
          ______) 
       __________)
      (____)      
---.__(___)       
'''

def mirror(text:str)->str:
  result = []

  for line in text.split('\n'):
    line_text = ""
    for char in line[::-1]:
      if char == "(":
        line_text += ")"
      elif char == ")":
        line_text += "("
      else:
        line_text += char
    result.append(line_text)
  return "\n".join(result)

def print_result(p1:str, p2:str)->None:
  p1 = p1.split("\n")
  p2 = mirror(p2).split("\n")

  print(f"\n{'You':<18}  {'Computer':>18}")
  for idx in range(len(p1)):
    print(f"{p1[idx]:<18}  {p2[idx]:>18}")
