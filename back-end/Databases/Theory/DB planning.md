***
[[Databases in general]]
### Special values:
#### Questions to ask yourself:
1. *==Why do i need storage?==(remember what Mr.Plawell said about describing/opening/explaining the statements)*
2. *==What do I have?==* 
3. *==What tables do I need?==*
4. *==What columns do I need?==*
5. *==What keys do I need?==*
6. *==What relations do I need?==*
### To know:

#### Questions to ask yourself:
1. *==Why do I need storage?==* - "I need storage, because my users on a website can filter, sort and choose specific clothes by various parameters"

2. *==What do I have?==* - existing database?(can fix existing problems instead of re-architecting them)

3. *==What tables do I need?==* - each table should contain single entity

4. ==*What columns do I need?*== - define columns as exactly as possible. All aspects of data is though about(==not just first name, but maybe last name, too?)==, what datatype, what size 

5. ==*What keys do I need?*== - one identifier should lead to one row, to one employee

6. *==What relations do I need?==* - what tables should know about each other? What common info? 


i need storage, so my customers can filter orders, contain various clothing types with several parameters, like: type, size, brand, price, gender, description. They can see the detailed info about the things, add it into the cart and next buy it, these orders should be tracked. also i have to provide authorization 

![[Pasted image 20240824204954.png]]