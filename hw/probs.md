# LT1 Homework: Probabilities


The following tasks come from the book *Statistical Machine Translation* available here: http://www.statmt.org/book

## Task 1
If we flip a coin 10 times, we might get the outcome `HTTHTHTHTT` (where `H` is heads, and `T` is tails).

1. Estimate a distribution by maximum likelihood estimation for this event. Estimating a distribution in this case would mean reporting probabilty of two disjoint events; first p(observing a heads) and second p(observing a tails). (3 points)
2. We want to test the quality of the estimation. We flip the coin five times and get `HHTTH`. What is the probability of this outcome according to 
  1. the estimated distribution, and (1 point)
  2. the uniform distribution or said another way assume that the coin is unbiased? (1 point)
3. What is the entropy of a coin toss where the coin has a head on each side (fake coin)? (2 points)

## Task 2
1. Show that p(y|x) = p(y), if X and Y are independent.  Explain each of your steps. (3 points)
2. What is the difference between entropy and cross entropy? (2 points)
