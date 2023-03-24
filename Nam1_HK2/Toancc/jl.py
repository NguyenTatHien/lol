from pylab import plot, show
hcm_rain = [13.8, 4.1, 10.5, 50.4, 218.4, 311.7, 293.7, 269.8, 327.1, 266.7, 116.5, 48.3]
months = range(1, 13)
plot(months, hcm_rain, marker = 'o')
show()