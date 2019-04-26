scalaVersion := "2.10.5"
mainClass := Some("SimpleApp")

libraryDependencies += "org.apache.spark" % "spark-core_2.10" % "2.1.0"

resolvers += "Cloudera Repository" at "http://repository.cloudera.com/artifactory/cloudera-repos/"

resolvers += "Spark Packages Repo" at "http://dl.bintray.com/spark-packages/maven"
libraryDependencies += "neo4j-contrib" % "neo4j-spark-connector" % "2.1.0-M4"

libraryDependencies += "org.apache.spark" %% "spark-sql" % "2.1.0"


