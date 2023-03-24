def q_soer(a, low, high):
    if low < high:
        pivotpos = partition(a, low, high)
        q_sort(a,low,pivotpos-1)
        q_sort(a,pivotpos+1, high)
def partition(a,low,high):
    pivotvalue = 
down = high
done = False
while not done:
    while up