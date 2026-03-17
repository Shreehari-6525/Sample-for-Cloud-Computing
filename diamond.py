
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
