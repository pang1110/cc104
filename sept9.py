#def displayrange (lower, upper) :
 #   """Outputs the numbers from lower to upper."""
  #  while lower <= upper:
   #     print(lower)
    #    lower = lower + 1
     #   upper = upper - 1
      # displayrange (lower + 1, upper)


def displayrange (lower, upper) :
    """Outputs the numbers from lower to upper."""
    if lower <= upper:
        print(lower)
    displayrange(lower + 1, upper)




