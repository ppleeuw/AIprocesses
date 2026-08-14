"""
Project 02 — Control Flow & Conditionals
Difficulty 2/10

Trace which branch executes and how many iterations run.
"""


def classify(score):
    """Only ONE branch in an if/elif/else chain ever executes."""
    if score >= 90:
        return "A"
    elif score >= 80:          # checked only if the first was False
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


print(classify(15))            # predict: ?  (none of the >=90/80/70 are True)


# --- Truthiness -----------------------------------------------------------
# Falsy values: False, None, 0, 0.0, "", [], {}, set()
# Everything else is truthy.
status = ""                    # empty string -> falsy
default = "guest"
# 'or' returns the FIRST truthy operand, or the last if all are falsy.
result = status or default     # -> "guest"
print(result)                  # predict: ?

# Short-circuit: 'and' stops at the first falsy operand.
print(0 and "never reached")   # predict: ?  (0 is falsy, right side not evaluated)


# --- for loops and range --------------------------------------------------
total = 0
# range(1, 6) yields 1,2,3,4,5  (the 6 is EXCLUSIVE)
for i in range(1, 6):
    total += i                # 1+2+3+4+5 = 15
print(total)                  # predict: ?


# --- while, break, continue, and loop-else --------------------------------
n = 5
while n > 0:
    n -= 1                    # decrement happens BEFORE the checks below
    if n == 2:
        continue              # skip the rest of this iteration
    print(n)                  # prints 4,3,1,0  (skips 2)
    if n == 0:
        break                 # exit the loop immediately
else:
    # This else runs ONLY if the loop ended naturally (no break).
    print("ran to completion")


# --- for...else -----------------------------------------------------------
for item in [1, 2, 3]:
    if item == 2:
        break                 # break -> the else below does NOT run
    print(item)
else:
    print("loop completed without break")  # predict: does this print?

print("done")                 # predict: ?
