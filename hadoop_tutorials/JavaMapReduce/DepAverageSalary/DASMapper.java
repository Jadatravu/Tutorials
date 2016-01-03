import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.Mapper;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reporter;


public class DASMapper extends MapReduceBase implements Mapper<LongWritable, Text, Text, IntWritable>{

	@Override
	public void map(LongWritable key, Text value,
			OutputCollector<Text, IntWritable> output, Reporter r)
			throws IOException {
		// TODO Auto-generated method stub
		String val = value.toString();
		String Sal;
		for (String retval: val.split(" ")){
	         Sal = retval;
	      }
		String  salArr[] = val.split(" ");
		if ( (salArr.length < 3 )){
			return;
		}
		if( (salArr.length > 3)){
			return;
		}		
		int sal = Integer.parseInt(salArr[ salArr.length -1]);		
		
		output.collect(new Text(salArr[0]), new IntWritable(sal));		
	}

}
