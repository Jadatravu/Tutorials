package spark.simple_app
/* SimpleApp.scala */
import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.SparkConf
import org.neo4j.spark._

object SimpleApp {
  def main(args: Array[String]) {
    val logFile = "README.md" // Should be some file on your system
    val conf = new SparkConf().setAppName("Simple Application")
    conf.set("spark.neo4j.bolt.url","bolt://xx.xx.xx.xx:7687")
    conf.set("spark.neo4j.bolt.password","xxxx")
    val sc = new SparkContext(conf)
    val neo = Neo4j(sc)
    var match_str="MATCH (people:Person)  WHERE people.born = 1978 RETURN people.name LIMIT 10"
    val df = neo.cypher(match_str).loadDataFrame
    df.show()
    
    sc.stop()
  }
}
