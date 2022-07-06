import os
from numpy import sqrt
import random
import matplotlib.pyplot as plt
  
nazwa_pierwszego_pliku = input('prosze wpisac sciezke do pierwszego pliku: ')
nazwa_drugiego_pliku =  input('prosze wpisac sciezke do drugiego pliku: ')
rozmiar_pierwszego_pliku=os.path.getsize(nazwa_pierwszego_pliku)
rozmiar_drugiego_pliku=os.path.getsize(nazwa_drugiego_pliku)
print(str(rozmiar_pierwszego_pliku)+ 'to jest drugi plik :' + str(rozmiar_drugiego_pliku))
snrindB_range = range(0, 10)
itr = len(snrindB_range)
N = 100000
ber = [None]*itr
ber1 = [None]*itr
tx_symbol = 0
noise = 0 
ch_coeff = 0
rx_symbol = 0 
det_symbol = 0
for n in range (0, itr):
    snrindB = snrindB_range[n]   
    snr=10.0**(snrindB/10.0)
    noise_std = 1/sqrt(2*snr)
    noise_mean = 0
    no_errors = 0
    for m in range (0, N):
      tx_symbol = 2*random.randint(0,1)-1
      noise = random.gauss(noise_mean, noise_std)
      rx_symbol = tx_symbol + noise
      det_symbol = 2 * (rx_symbol >= 0) - 1
      no_errors += 1*(tx_symbol != det_symbol)  
      ber[n] = no_errors / N
      print ("SNR in dB:", snrindB)
      print ("Numbder of errors:", no_errors)
      print ("Error probability:", ber[n] )
    plt.plot(snrindB_range, ber, 'o-',label='practical')
    plt.axis([0, 10, 0, 0.1])
    plt.xlabel('snr(dB)')
    plt.ylabel('BER')
    plt.grid(True)
    plt.title('BPSK Modulation')
    plt.legend()
    plt.show()