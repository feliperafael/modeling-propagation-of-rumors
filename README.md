# modeling-propagation-of-rumors
this repository proposes analysis of a model for propagating rumors

Consider the spread of a rumor through a company of 1500 employees, all working in the same building. Assume that the spread of the rumor is similar to the spread of a disease contagious, in which the number of people who listen to the rumor of each day is proportional to the product of the number who heard the rumor earlier and the number who did not hear the rumor. This is given by:

> $ r_{n+1} = r_{n} + kr_{n}(1500-r_{n}) $

where k is a parameter that depends on how fast the rumor spreads and n is the number of days. Assume
k = 0.0012 and suppose that four people initially heard the rumor. How long will every 1500 employees will have heard the rumor? Again consider disclosure of a rumor, but now assume a company with 5500 funcialists. Considering the model presented above, construct a model for the company with the rumor growth rates k = (0.25, 0.025, 0.0025, 0.00025) to determine the number of people who heard the rumor after 1 week. Based on the simulation of the previous model, build a proposal on how to control the growth rate of rumor.
