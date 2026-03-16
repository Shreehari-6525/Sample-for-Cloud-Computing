# # star pattern 

# #   * * * * * 
# #   * * * * 
# #   * * * 
# #   * *
# #   *

value = 5
i = 0
print("\n============ STAR PATTERNS ===========\n\n")

while value >= i:
    print(" * " * value)
    value -= 1


# #   *
# #   * *
# #   * * *
# #   * * * *
# #   * * * * *
value = 5

while i <= value:
    print(" * " * i)
    i += 1



#   * * * * *
#    * * * *
#     * * *
#      * *
#       *
value = 5

i = 0

while i < value:
    
    print(" " * i,"* " * (value - i))
    i += 1

#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
value = 5

i = 1

while i <= value:
    spaces = value - i

    print(" " * spaces,"* " * i)
    i += 1
    

# #       *
# #      * *
# #     * * *
# #    * * * *
# #   * * * * *
# #    * * * *
# #     * * *
# #      * *
# #       *
value = 5

i = 1

while i <= value:
    spaces = value - i

    print(" " * spaces,"* " * i)
    i += 1

i = value - 1
while i >= 1:
    spaces = value - i
    print(" " * spaces,"* " * i)
    i -= 1
