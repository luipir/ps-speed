# -*- coding: utf-8 -*-

"""
/***************************************************************************
Name                : PS Time Series Viewer
Description         : Computation and visualization of time series of speed for 
                    Permanent Scatterers derived from satellite interferometry
Date                : Jul 25, 2012 
copyright           : (C) 2012 by Giuseppe Sucameli (Faunalia)
email               : brush.tyler@gmail.com

 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

def name():
	return "PS Time Series Viewer"

def description():
	return "Computation and visualization of time series of speed for Permanent Scatterers derived from satellite interferometry"

def author():
	return "Giuseppe Sucameli (Faunalia)"

def authorName():
	return author()

def email():
	return "sucameli@faunalia.it"

def icon():
	return "icons/logo.png"

def version():
	return "0.1.3"

def qgisMinimumVersion():
	return "1.5"

def classFactory(iface):
	from .pstimeseries_plugin import PSTimeSeries_Plugin
	return PSTimeSeries_Plugin(iface)

