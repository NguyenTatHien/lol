from matplotlib_venn import venn2
import matplotlib.pyplot as plt
from sympy import FiniteSet
def draw_venn(sets):
    venn2(subsets=sets)
    plt.show()

s1 = FiniteSet(1, 3, 5, 7, 9, 11, 13, 15, 17, 19)
s2 = FiniteSet(2, 3, 5, 7, 11, 13, 17, 19)
draw_venn([s1, s2])
s3 = [s1, s2]
print(s3)

def draw_venn(sets):
    venn2(subsets=sets, set_labels=('Tap S1', 'Tap S2'))
    plt.show()

draw_venn([s1, s2])