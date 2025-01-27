def input_name():
  return  input("Enter your name:")

def process_data(name):
  print(f"Hello,{name}!")

name=input_name()
process_data(name)

p=int(input("enter your mark for physics:") )
m=int(input("enter your mark for maths:") )
c=int(input("enter your mark for chemisry:") )

def average(p,c,m):
  return (p+c+m)/3
print(f"your average mark:",round(average(p,c,m),2))

report_card = f"""
 Report Card
------------
Name: {name}
Physics Marks: {p}
Chemistry Marks: {c}
Mathematics Marks: {m}
Average Marks: {average:.2f}
"""

file_name = f"{name}_report_card.txt"

# Write the report card to the file
with open(file_name, "w") as file:
    file.write(report_card_content)

# Inform the user that the report card has been generated
print(f"\n{name}, your report card has been generated as {file_name}.")