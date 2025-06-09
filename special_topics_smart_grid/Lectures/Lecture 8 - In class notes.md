
### Numerical Relay
- Signal Conditioning
	- 120V is brought into control room, which is where the IED is. This 120V will be given to a transformer which brings it down to 5V or 10V, which will then be sampled. 
	- The first part is scaling and isolation. need ot isolate from power system because it is very harsh in terms of transient interference, etc. Must have antialiasing filters to do the sampling.
- Data Acquisition
	- It will then be converted to digital numbers. Analog to digital. This is done every time a new sample comes in. We are continuously sampling voltage and current.
- Block Diagram
	- Ct: current transformer 
	- Vt: voltage transformer
	- Before Ct, vt, there is isolation and scaling. Once voltage and current is obtained then main transformer will bring down the current to either 1 ampere 5 ampere (during normal condition. During fault it might be 10 or 20 times more). This is the first step, stepping down from main CTs and PTs.
	- Auxiliary CT and PT brings down the voltage/current during faults.
	- Then high frequency components and noise are filtered using antialiasing. Otherwise we will have errors in our calculations.
	- Ratings vary from 1 volt ampere to 24 volt ampere, depending on the size of the circuit being monitored.
	- The IED's are magnetically coupled meaning they are electrically isolated. 
- Filter Implementations
	- Op-amps require their own power source
	- Op amp circuits can't be put on chips. 
	- With switched-capacitor filters, its the same as the op amp filters but put on a chip. You can put C and L on a chip but not R, so they used a capacitor that switches on and off to behave like a resistor. 
- Data Acquisition
	- Once data is passed through antia alising filter, then analog signals can be converted to digital signals to analyze the data.
	- Need a buffer in-between switch capacitor filters, a buffer is required to correct the input signal or something.
	- Sample and hold the signal.
	- Depending on how many A to D converters you use, you might need multiplexers.



![[Pasted image 20250602111539.png]]
This is how the signal should respond after we adjust the filter and apply it to the input signal. This is not the filter being adjusted in real time. So the above signal is after we adjust the filter to 55Hz and pass the signal through.