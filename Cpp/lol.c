void BubbleSort(int a[], int n)
{
    for(int i = 0; i < n-1; i++)
    {
        for(int j = n-1; j > 1; j--)
        {
            if(a[j] < a[j-1])
            {
                Swap(a[j], a[j-1]);
            }
        }
    }
}