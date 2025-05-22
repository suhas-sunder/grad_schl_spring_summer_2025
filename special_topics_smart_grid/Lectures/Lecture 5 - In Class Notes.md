### Correlation Algorithms ~ Cosine Filters
- When we use the full cycle DFT or any algorithm, we use two filters. One estimates the real part. The other one estimates the imaginary part.
- Since real and imaginary are at a phases shift of 90 degrees, we technically don't need to calculate both. Can calculate the real part then just shift it to get both real and imaginary.
- So, when we design orthogonal filters, we can just use one. Which one to use? Whichever is better. How do we know which is better? We look at the frequency response.
- So, using this method of shifting by 90 degrees means there is a lag, because 90 > 60Hz. So our sampling window becomes 90 deg instead of 60. So we're adding a quarter window to the entire thing, compared to what we did before. So overall it takes one and a quarter cycle to provide the results.
- The top filter is better for removing higher frequencies. Bottom filter is better for Decaying DC (probably because we don't want those  additional high frequencies removed). Which one we choose depends on the condition.

### Least Error Square ~ Non-recursive Algorithm
- Very general and other correlation algorithms are derived from this one.
- Let's supposed you have a set of data where x is your independent variable and y is your dependent variable.
	- eg. independent can be temperature and dependent variable can be the quality of something base don the temperature like pressure. 
	- You get a bunch of points based on this set of data and you need to find a relationship between the two variables.
		- To find the relationship you find the average of all points, so it could be a linear line (y=ax + b) or a curve (y = ax^2 + bx + c) or w/e. This averaging method is called least error square.
		- This is nothing but data fitting. Trying to fit the data to a relationship.
- In our case we have voltage and current signal which is sample data in a window. Eg. a sine wave with one 60hz sample at 720 Hz sample rate with 12 samples.
	- Using that sample data, we can model the sample waveform. Then we can figure out the real and imaginary of the filter.
	- We are defining our model. 
- In a best fit line the sum of the residuals is 0. A residual is the distance from a point to the ideal line modeling the graph. A residual can be positive (point is above line) or negative (point is blow line).
- Sum of squares is a square formed by the residual which is summed up. As the line moves around, the squares (a representation of the square error), the squares change. The further you get from the data, those squares get larger. So we adjust the line until the squares are the smallest (error is the least).
	- There is a formal way of doing this which doesn't involve manual trial and error.
- A is known because we have t. m is known because we have m results. Rest we don't know. 
	- We want to minimize the error square with respect to the unknowns. To do this we differentiate error with respect to x and set it equal to 0.
	- Left pseudo inverse is for -1L matrix power. Used when you have more data points than unknowns.
		- Right pseudo inverse is when you have less data points than unknowns but we won't be covering this in the course.
	- 

