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
