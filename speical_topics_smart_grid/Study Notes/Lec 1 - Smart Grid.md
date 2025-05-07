**Smart Grid
- **Built over time, not all at once. It's evolutionary. 
	- If you go to a substation you'll find technology from 1950 to 2025.

- **How is it defined? ![[Pasted image 20250507070320.png]]
	- It is an advanced electrical grid. It's an intelligent system which uses digital communication and advanced technologies, which is the end goal (ambition) to mange the system much more efficiently and reliable way (fundamentals don't change. just the technologies used to make it more efficient). Some parts of it exist, but some don't.  
	- The goal is to better sense, monitor, and control/respond in real time, what is already being managed (frequency and voltage mgmt) going back to the fundamentals.
	- It has become a data driven energy network in a way including data analytics etc.

- **What are the core components of a smart grid? (This is the end goal. Not happening everywhere but things are moving in this direction.) ![[Pasted image 20250507070413.png]]
	- Smart meters are installed in homes and business to monitor and record usage in real time.
		- Utility companies have no idea what's going on until the meter reading comes in. It is now done in real time.
	- Sensors and controls detect faults and enable automation. This means it will self diagnose the problems and figure out solutions for it.
	- Communication infrastructure. The system is huge so communication is crucial. There are strict requirements in terms of communication, latency, etc.
	- Control centers use data to balance supply and demand.

- **What are the functionalities and benefits?![[Pasted image 20250507070438.png]]
	- Responsiveness: The smart grid will be able to respond very quickly to any fluctuations in the system. Outages, changes in voltage, etc. The goal is to act proactively in real time. The traditional system lacks real-time data which makes it very difficult to be proactive.
	- Two way communication between utility and consumer to optimize the energy distribution. 
	- Eg. the utility company might provide incentives to consumers for using less energy which is communicated through some smart monitoring system. This way the company can distribute that saved power elsewhere.
	- Supports integration of renewable sources like solar wind etc.

- Traditional Power Grids![[Pasted image 20250507070641.png]]

- **Smart grid is a modern approach![[Pasted image 20250507070736.png]]
	- Smart grid will be decentralized and generation will happen throughout the system. Generation could even happen at peoples houses via solar etc. which feeds back into the system.

- **Traditional grid vs smart grid![[Pasted image 20250507070800.png]]
	- Centralized meaning large systems. If a large system goes down, big portions of the grid are affected.
	- Distributed meaning smaller systems that are more flexible and easier to manage/reliable.

- **Challenges for the current power systems![[Pasted image 20250507070840.png]]
	- Aging grid infracture, increased demand strains, extreme weather and cyberattacks.
	- Not enough power in the grid available in some areas due to the advancement in technologies. Eg. Too many Ev's can make it difficult to charge some in specific areas.

- **Climate change and decarbonization is also another incentive to switch to smart grid
	- Power sector is one of the largest greenhouse gas emitters. They need to decarbonize but there are challenges. Can't be switched overnight.
	- Global goals demand cleaner energy and lower emissions. Canada has a goal of being carbon neutral by around 2035 or something close. For that to happen, smart grid is crucial.

- **Enabling energy transition ![[Pasted image 20250507070858.png]]
	- Smart monitoring and data is all there right now. Consumers are switching to smart monitoring. It is not being utilized fully because we don't have the ideal smart grid yet.
	- In control centers people/operators have set rules for what needs to be done to adjust voltage, load, and routing. The goal with smart grid is to automate all of this. 

- **Real-time monitoring and automation

- **Self healing capabilities ![[Pasted image 20250507071008.png]]
	- Smart grid concept was originally started by protection and automation people. It has been around for a long while, it just got labelled as smart grid for political reasons.
	- If one line is lost, rerouting will be done automatically very quickly. Right now it is done manually by operators who are highly skilled and know how to manage the changes.

- **Consumer participation![[Pasted image 20250507071100.png]]
	- Summer time, everyone turns on their AC and so on so power generators tend to hit their peak. The voltage level (reactive power) goes down as a result since the demand/load is higher so generation is not sufficient. 
	- Consumers want lower cost and reliable power.
	- Automated processes reduce cost for utilities because there can be less manual adjustments, thus less extremely skilled workers need to be paid for work that can be automated more reliably.
	- The operator needs to know how much power is being fed into the system in order to realize the benefits and compensate the end user accordingly.

- **What is AMI & key benefits (one technology)![[Pasted image 20250507071925.png]] ![[Pasted image 20250507072056.png]]
	- Almost every part of the world has some form of AMI, advanced metering infrastructure.
	- This is basically measuring your power at various intervals at businesses, homes etc. Then it communicates this information back at the control center, so that they know exactly how much power is being consumed in the area.
	- The two way communication part is not being used much even though it has the capability. This is the end goal so that we can monitor the load being used on the system and enabling two way communication to benefit both consumers and utility companies.
	- Automatically shifts consumer behavior and detects electricity theft and illegal activities. Eg. marijuana grow-ups when energy consumption goes up suddenly in some area.

- **Consumer empowerment thought AIM ![[Pasted image 20250507072135.png]]
	- Informs energy saving behavior so that users can decide when and how they want to consume power as it becomes more/less available.

- **Role of sensors in smart grid (another technology)![[Pasted image 20250507072519.png]]
	- Aids in the control of voltage and frequency.
	- Detects vibrations in the line, voltage, current, temperature, etc.
	- End goal is to have everything sensed in the power system.
	- Enable predictive maintenance well in advance. Eg. predicting maintenance required a year in advance.
		- Predicting motor maintenance could have sensors for temperature, vibrations, motion, etc. to predict what will go wrong with the generator.
		- For transformers there are infrared sensors that can measure hotspots. Image processing techniques could be used by smart monitoring systems to predict outcomes in advance.
	- Old sensors didn't really provide data. It measured and took action.

- **Understand phasor measurement units PMUS (another technology)![[Pasted image 20250507072609.png]] ![[Pasted image 20250507072849.png]]
	- Measure voltage and phasors to time synchronize using GPS systems. Back in the day time signals were synchronized using fiber optics, but now we can use GPS systems for it.
	- In the old system we only know the voltage magnitudes, but in this system we know the phase angle and voltages. This allows dynamics in real time for situational awareness.
	- Wide area monitoring is possible and quick response to disturbances.

- **SCADA is supervisory control and data acquisition. (another technology)![[Pasted image 20250507072911.png]] ![[Pasted image 20250507073008.png]] ![[Pasted image 20250507073102.png]]
	- Some of it is in place but not in full capability. Eg. opening and closing distribution lines by opening and closing switches but it doesn't happen automatically.
	- RTUs are remote terminal units which are being replaced by PMUs in the newer systems.
	- Some of the smart metering data is starting to go to SCADA as well.
	- Integrates AMI, PMU, DER for smart opererations. Eg. even electic vehiacle charging data is being sent to the system, to determine what level of charging each ev charging station can have. So cars will charge faster or slower depending on how many cars are drawing power in a certain area.

- **Distributed energy resources (DER) ![[Pasted image 20250507073121.png]]
	- Wind turbines, solar panels, micro grids. 
	- All of these will be integrated in smart grid.

- **Demand response technologies. ![[Pasted image 20250507073121.png]]![[Pasted image 20250507073138.png]]
	- Empowers the consumer to change their electricity usage depending on the demands on the system. eg. if consumers can see the real time price they can adjust their behavior to shift energy consuming activities to times where costs are less which automatically stabilizes the grid.

- **Communication Networks ![[Pasted image 20250507073154.png]]
	- At one point utilities had more fiberoptic lines than telephone companies.
	- IEC618w/e uses IP-based protocols. At one point every system will have IP for optimal communication.

- **Data management and analytics ![[Pasted image 20250507073219.png]]
	- Big data and data analytic techniques
	- Load forecasting
	- Forecasting power generation from wind turbines and solar (by predicting weather conditions etc.)
	- Bits and pieces are already in the system. Just needs to be utilized.

- **Energy storage systems ![[Pasted image 20250507073245.png]]
	- Battery storage is crucial for when not enough power is generated from solar, wind etc.

- **Cybersecurity ![[Pasted image 20250507073300.png]]
	- Control systems can be hacked.
	- Computer systems controlling smart grid can be hacked.

- **Issues ![[Pasted image 20250507073353.png]] ![[Pasted image 20250507073408.png]] ![[Pasted image 20250507073425.png]] ![[Pasted image 20250507073438.png]] ![[Pasted image 20250507073501.png]] ![[Pasted image 20250507073517.png]]
	- Can't shut the power system off, but it needs to be improved. So it would need to happen in stages.
	- Implementation costs are very high.
	- Technology has to be developed and must be proven via trial bases. That can take years to go from proof of concept to deployment stage. Then you have to start with the important substation, meters, and communication system upgrades before moving to other areas. 
	- New technologies need to be able to work with existing technologies.
	- Initially you have to invest a lot of money but it can be recovered over a long time.
	- Interoperability issues.
		- One tech uses one standard but another uses another standard. Then its difficult to make them operate together. There is no common standard so two systems may not be able to communicate together though they do the same thing. This makes it very challenging to implement new technologies.
		- There is a big push towards coming up with a universal standard for interoperability.
		- Risk of vendor lock in is when your stuck with a particular manufacturer because their devices communicated with only other devices made by them. So another vendors device would not be compatible.
	- Consumer awareness and participation
		- When smart meters first came about people were against them because they thought costs would go high and they wouldn't have benefits. 

- **Smart cities ![[Pasted image 20250507073537.png]]
	- Smart gird is a part of these cities that have been developed in certain areas.
	- Can only be created if we have a smart grid. 
	- Made to improve urbal life. eg. smart street lights.

- **Rural electrification ![[Pasted image 20250507073551.png]]
	- Micro grids are being setup for these rural areas because there might only be one line going there etc. So when one line goes out power goes out to that area. So a micro grid using wind, solar etc can power the area and can also be integrated into the smart grid for overall power distribution.

- **Power plant monitoring ![[Pasted image 20250507073609.png]]
	- person doesn't need to be at a power plant. Can be controlled remotely, enhancing safety, making maintenance predictable, etc.
	- Ancillary service (service that provides power back to the grid) where EV's can supply power back to the grid rather than charge. (vehiacle to grid technology.)

- Integration with renewables ![[Pasted image 20250507073700.png]]

- **Case Study US smart grid pilot project ![[Pasted image 20250507073714.png]] ![[Pasted image 20250507073729.png]]
	- Pilot projects are going on throughtou the world.
		- Eg. ontario funds various projects as proof of concept which can be expanded
		- Trying to show it results in efficiency and all benefits smartgrid can bring

- **Blockchain in Energy Trading (Another tech in smart grid area) ![[Pasted image 20250507073752.png]]
	- More for energy trading so that energy trading platforms can be created.
	- Reduces transition costs and intermediaries

- **5G and Real-Time control ![[Pasted image 20250507073807.png]]
	- Improves communication speeds

- **Global trends and dev ![[Pasted image 20250507073823.png]]
	- There needs to be more international cooperation on smart grid standards.
	- There needs to be more r and d
	- More (everything else on list)

- **Smart Grid and Sustainable Development Goals (SDGs) ![[Pasted image 20250507073841.png]]
	- Codes for goals setup by UN which contributes to the development of Smart Grid