***
#### Special values:
1. #deployment - process of delivering the application from developing to production 
#### To know:

- Kinds of #deployment:
	1. `Blue/Green` - involves two running environments, where all the traffic is handled by "Blue" one and "Green" is responsible for implementing new features and technologies. When "Green" is fully developed and tested, we change the live traffic flow to "Green" by `router` or `load balancer`
	
	2. `Canary` - involves narrowed environment where new releases are send to small amount of users, separated from entire service
	
	3. `Rolling` - new version of an application is slowly enrolled in by updating existing instances, that approach reduces downtimes and possible impact of errors   
	
	4. `A/B testing` - two environments who splits the traffic of users, and allow to track the engagement of new features 
	
	5. `Shadow` - launching updated application without sending traffic to it. Two application are running simultaneously
	
	6. `Recreate` - shut the fuck up existing application and launch new one