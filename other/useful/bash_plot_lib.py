#!/usr/bin/env python3

# sudo pip3 install bashplotlib
# bashplotlib is a python package and command line tool for making basic plots in the terminal. 
# It’s a quick way to visualize data when you don’t have a GUI.

import numpy as np
from bashplotlib.histogram import plot_hist

arr = np.random.normal(size=10000, loc=0, scale=1)

plot_hist(arr, bincount=50)

#* 647|                         oo                        
#* 613|                        ooooo                      
#* 579|                       oooooo                      
#* 545|                      ooooooo o                    
#* 511|                     oooooooooo                    
#* 477|                     ooooooooooo                   
#* 443|                     ooooooooooo                   
#* 409|                     oooooooooooo                  
#* 375|                    ooooooooooooo                  
#* 341|                   ooooooooooooooo                 
#* 307|                   ooooooooooooooo                 
#* 273|                   oooooooooooooooo                
#* 239|                  ooooooooooooooooo                
#* 205|                 oooooooooooooooooo                
#* 171|                 ooooooooooooooooooo               
#* 137|                ooooooooooooooooooooo              
#* 103|               ooooooooooooooooooooooo             
#*  69|             oooooooooooooooooooooooooo            
#*  35|             ooooooooooooooooooooooooooo           
#*   1| o  ooooooooooooooooooooooooooooooooooooooooooooo o
#*     --------------------------------------------------