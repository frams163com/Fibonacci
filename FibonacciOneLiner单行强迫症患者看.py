from math import *
GoldenRatio=(sqrt(5)+1)/2

m=int(raw_input())
for i in range(m):
  N=int(raw_input())
  print int(log((sqrt(5)*(2 + N) + sqrt(-4 + 5*(2 + N)**2))/2.)/log(GoldenRatio)+1e-15)-3 if int(log((sqrt(5)*(2 + N) + sqrt(4 + 5*(2 + N)**2))/2.)/log(GoldenRatio)+1e-15)%2 else int(log((sqrt(5)*(2 + N) + sqrt(4 + 5*(2 + N)**2))/2.)/log(GoldenRatio)+1e-15)-3
  
