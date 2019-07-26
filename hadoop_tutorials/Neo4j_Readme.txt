1.creation of a node
create (bumra:player{role:"bowler",type:"rh"}) return bumra

create (kohli:player{role:"batsman",type:"rh"}) return kohli

2.Setting a property
match p=(a:player) where a.role="batsman" set a.name="kohli"

match p=(a:player) where a.role="bowler" set a.name="bumra"

3. matching based on a property condition
match p = (a:player) where a.role="bowler" return p

match p=(a:player) where a.type="rh"

4. creation of a relationship
MATCH (a:player), (b:team) WHERE a.type = "rh" AND b.name = "India" 
CREATE (a)-[r: MEMBER_OF]->(b) 
RETURN a,b 

5. updation of a relationship using a merge
match (a:player), (b:team) where b.name="India" merge (a)-[:MEMBER_OF]->(b) return a,b

match (a:player), (b:team) where b.name="India" merge (a)-[:MEMBER_OF]->(b) return count(a),count(b)

6. getting seto f nodes based on a particular relationship with a node
match  (a)-[:MEMBER_OF]->(:team{name:"India"}) return a

7. getting set of nodes based on a particular relationship and also its own particular property values
match p=(a:player) where a.type="rh" and (a)-[:MEMBER_OF]->(:team{name:"India"}) return p

match p=(a:player) where a.role="bowler" and (a)-[:MEMBER_OF]->(:team{name:"India"}) return p

match p=(a:player) where a.role="batsman" and (a)-[:MEMBER_OF]->(:team{name:"India"}) return p
