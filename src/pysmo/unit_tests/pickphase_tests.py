import unittest
import sys, os, matplotlib
from pysmo.aimbat.qualctrl import getOptions, getDataOpts, sortSeis, getAxes, PickPhaseMenuMore
from pysmo.aimbat.pickphase import PickPhaseMenu


# ############################################################################### #
#                                     VIEWS                                       #
# ############################################################################### #

class pickphaseView(unittest.TestCase):

    def test__save_headers_filterParams(self):
    	sys.argv[1:] = ['20120124.00520523.bhz.pkl']
    	gsac, opts = getDataOpts()
    	axs = getAxes(opts)
    	setattr(opts,'labelqual',True)
    	ppm = PickPhaseMenu(gsac, opts, axs)

    	# click the save button
    	click_save_event = matplotlib.backend_bases.MouseEvent('button_press_event', ppm.axpp.figure.canvas, 63, 481)
    	ppm.save(click_save_event)

    	#ppm.save_headers_filterParams(self, event):

# ############################################################################### #
#                                     VIEWS                                       #
# ############################################################################### #