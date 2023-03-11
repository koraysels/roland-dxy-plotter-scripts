#!/usr/bin/env python
from chiplotle3.tools.plottertools import instantiate_plotters
import sys
import time

def plot_hpgl_file(file):
    '''Send an HPGL file to the plotter found connected to the computer.'''
    plotter = instantiate_plotters( )[0]

    ## comment this if you do not want to reset position to bottom left. 
    plotter.set_origin_bottom_left() 

    plotter.write_file(file)
    ## call flush( ) to wait till all data is written before exiting...
    plotter._serial_port.flush( )


if __name__ == '__main__':
    print("Argument List:", str(sys.argv))
    # if len(sys.argv) < 2:
    #     print 'Must give HPGL file to plot.\nExample: $ plot_hpgl_file.py myfile.hpgl'
    #     sys.exit(2)
    file = sys.argv[1]
    print('starting print of file: ' , file)
    plot_hpgl_file(file)
