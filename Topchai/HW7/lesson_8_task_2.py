"""
There are two character strings of lowercase and uppercase Latin letters and numbers.
Develop a program that builds and prints in alphabetical order the set of letters that
are in both arrays and the set of letters of the first and second arrays separately.
"""

"""
1234abcdABCD
5678efghEFGH
"""

first_str = set(input("Enter first string: "))
second_str = set(input("Enter second string: "))

marged = first_str.union(second_str)

print(f"""
{"-"*120}
{sorted(marged)}
{"-"*120}
{sorted(first_str)}
{"-"*120}
{sorted(second_str)}
{"-"*120}
""")