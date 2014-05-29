HyperPython
===========

A brief and practical introduction to the solution of hyperbolic conservation laws.
This set of IPython notebooks was originally prepared for a 1-day tutorial that I
taught in Gyor, Hungary in May 2014 as part of the 
[Workshop on Design, Simulation, Optimization and Control of Green Vehicles and Transportation](http://jkk.sze.hu/en_GB/program).

The easiest way to run these is to create a free account on [SageMathCloud](cloud.sagemath.org).  Then create a new project, click "new file", type https://github.com/ketch/HyperPython.git into the box and hit enter.  That's it!

To run the notebooks on your own computer, you'll need:

- Python >=2.7
- IPython >=1.2.0
- Numpy
- Matplotlib
- Clawpack >=5.1

The last four can all be installed using [pip](http://pip.readthedocs.org/en/latest/installing.html):

    pip install ipython
    pip install numpy
    pip install matplotlib
    pip install clawpack

To start the course, do

    git clone https://github.com/ketch/HyperPython.git
    cd HyperPython
    ipython notebook
    
and click on Lesson 0.

The design of the notebooks and their organization was inspired by [Lorena Barba](http://lorenabarba.com/)'s excellent
[AeroPython course](https://github.com/barbagroup/AeroPython).

If you spot any errors or would like to make improvements, pull requests are welcome!

Content provided under a Creative Commons Attribution license, CC-BY 4.0; code under MIT License.

(c)2014 David I. Ketcheson
