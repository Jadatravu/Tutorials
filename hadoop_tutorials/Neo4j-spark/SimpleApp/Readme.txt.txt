1. Update Neo4j server url and passwd details
2. Update the cypher query as well.
3. Compile and build jar using "sbt package command" 
4. Run the application
spark2-submit --master yarn  --jars /path/to/neo4j-spark-connector-2.1.0-M4.jar --class "spark.simple_app.SimpleApp" ./target/scala-2.10/simpleapp_2.10-0.1-SNAPSHOT.jar