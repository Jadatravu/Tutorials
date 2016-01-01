import java.io.IOException;
import java.util.Iterator;

import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.MapReduceBase;
import org.apache.hadoop.mapred.OutputCollector;
import org.apache.hadoop.mapred.Reducer;
import org.apache.hadoop.mapred.Reporter;


public class WACReducer extends MapReduceBase implements Reducer<Text, IntWritable, Text, DoubleWritable>{
	@Override
	public void reduce(Text key/* h*/, Iterator<IntWritable> values/* [1,1,1,1,1]*/,
			OutputCollector<Text, DoubleWritable> output, Reporter r)
			throws IOException {
		int count = 0;
		int sum = 0;
		double average = 0.0;
		while( values.hasNext()){
			IntWritable i = values.next();
			sum= sum + i.get();	
			count = count +1;
		}
		average = (double)sum/(double)count;
		output.collect(key, new DoubleWritable(average));	
	}
}
