# Let $W'_i$ be the necessary weight to ensure there is just enough of any chemical $C_i$ after the $N$ days of production. Thus we have equations

# \begin{align}
# (\frac{p}{100})^{N} * W'_A &= W_A &
# (\frac{p}{100})^{N} * W'_G &= W_G
# \end{align}
# and we know 
# $W_G \leq W_A$
# therefore 
# \begin{align}
#  (\frac{p}{100})^{N} * W'_G \leq  (\frac{p}{100})^{N} * W'_A
# \end{align}
# \begin{align}
#  W'_G \leq  W'_A \text{(since p is positive)}
# \end{align}
# After $k$ days, $W'_G$ will be reduced to $(\frac{p}{100})^{k} * W'_G $ and $W'_A$ will be reduced to $(\frac{p}{100})^{k} * W'_A$. Thus, the amount of each chemical lost 
# \begin{align}
# L_G &= W'_G - (\frac{p}{100})^{k} * W'_G
# &
# L_A &= W'_A - (\frac{p}{100})^{k} * W'_A
# \end{align}
# simplifying for visibility, we have with $(0 < c \leq 1)$
# \begin{align}
# L_G &= W'_G - c * W'_G
# &
# L_A &= W'_A - c * W'_A 
# \end{align}
# \begin{align}
# L_G &= W'_G (1 - c)
# &
# L_A &= W'_A (1 - c) 
# \end{align}
# Now we can easily see that the loss of each chemical $L_G$ and $L_A$ are proportional to their initial weights. Where $(0 \leq d < 1)$
# \begin{align}
# L_G &= W'_G * d
# &
# L_A &= W'_A * d 
# \end{align}
# Thus, the loss of $C_A$ in the alternate solution 