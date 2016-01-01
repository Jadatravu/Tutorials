import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.FileInputFormat;
import org.apache.hadoop.mapred.FileOutputFormat;
import org.apache.hadoop.mapred.JobClient;
import org.apache.hadoop.mapred.JobConf;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;


public class WAverageCount extends Configured implements Tool{

	@Override
	public int run(String[] args) throws Exception {
		if (args.length < 2){
			System.out.println("invalid paramaeters\n");
			return -1;
		}
		JobConf conf = new JobConf(WAverageCount.class);
		conf.setJobName("Word Average count");
		
		FileInputFormat.setInputPaths(conf, new Path(args[0]));
	    FileOutputFormat.setOutputPath(conf, new Path(args[1]));
	    conf.setMapperClass(WACMapper.class);
	    conf.setReducerClass(WACReducer.class);

	    conf.setMapOutputKeyClass(Text.class);
	    conf.setMapOutputValueClass(IntWritable.class);

	    conf.setOutputKeyClass(Text.class);
	    //conf.setOutputValueClass(IntWritable.class);
	    conf.setOutputValueClass(DoubleWritable.class);
	    
	    JobClient.runJob(conf); /* Initiates job to the JobTracker */
	    return 0;
		
	}
	public static void main(String[] args){
		Tool tool = new WAverageCount();
		int e;
		try {
			e = ToolRunner.run(tool, args);
			System.exit(e);
		} catch (Exception e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		
	}

}
