
### Midterm Exam
- First section is MCQ
	- 20 to 30 questions
- Second part is written theory questions
	- Eg. use cases with opinions about that case. How can we re-design the case based on what was learned in the lectures.
	- Eg. Power management based on last lecture, if we have a project and use case, what would you recommend to improve the design based on your understanding of power management.
	- 5 to 6 questions
	- Will be conducted online, not on paper. Class voted.
### IoT Connectivity
- Cellphones for example have network cards that lets it connect to the network infrastructure wirelessly.
- Some devices are not designed to be moved such as fixed cameras that have wireless connectivity, while other devices move around like phones.
- We have hosts such as smart phones, computers, cameras, etc.
- We have base stations called routers which are connected using wires. They are connected to the service provider via fiber optics or w/e.
	- They will send packets over the network.
	- Will connect to cell towers down the line.
- Wireless links 
- Characterizes of wireless links
	- In x axis we have types of range
	- Y axis shows data rate, meaning type of networks and protocols used to send wireless signals.
		- IEEE put together the rules for these networks.
		- Wi-Fi is an example of communication channel that uses the indoor protocols.
	- 5G has a larger data rate so more capacity to send/receive data
		- All EV's are using 5G
- Ad hoc mode
	- In case of emergencies if there is no base station, nodes will be active that allow certain computers to communicate with each other on a specific channel
- Wireless Link
	- Data can be transferred in a secure medium
	- Decreased signal strength the farther it gets from source
	- Interference from other sources
		- Eg. not recommended setting up a router next to a microwave incase signals of similar frequencies overlap.
	- Multipath propagation
- 802.11 - Basic protocol, an indoor wireless protocol
	- Has range of 10 to 30m and is ideal for indoor use
	- Have two modes, passive and active
		- Passive is where in the middle we have a host and two access points. There are two broadcast base stations (BBS) that send beacon frames from access points
			- Every access point sends information saying that I'm w/e access point, I'm available
			- It's like a control frames, saying I'm access point 1 with said address, I'm access point 2 etc. Can't communicate with all access points at once, so based on signal strength, etc. the host will decide which access point to communicate with. Once connection is established, selected access point will start sending data frames.
		- Active scanning
	- 2+ nodes transmitting data at the same time can collide and interfere so this protocol is single access. 
- 801.11 multiple access
	- Avoids collisions between 2+ nodes transmitting at the same time.
	- Does not detect collissions
		- Because of power consumption
	- 802.11 CSMA senses before transmitting to ensure no collision takes place with ongoing transmissions by another node.
	- 