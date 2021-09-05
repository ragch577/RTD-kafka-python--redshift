# RTD-kafka-python--redshift


-  Geeting the real-time for every 30 seconds
   https://www.rtd-denver.com/business-center/open-data/gtfs-developer-guide#gtfs-realtime-feeds
   
   - Format Documentation
     - The GTFS-realtime specification is detailed at
       https://developers.google.com/transit/gtfs-realtime/
     
     - The Protocol Buffer format is detailed at
      https://github.com/protocolbuffers/protobuf
      
  - Amazon DynamoDB
    - Hosted, scalable database service by Amazon with the data stored in Amazons cloud, 
      https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html
      
      
      
- Install MSK cluster, Make a note on security groups.
- EC2 instances, create a key pairs
            File format in pem. 
            Launch instance, choose a free tier. 
            Use a powershell to connect EC2
- Get the kafka binaries from the files.
  https://kafka.apache.org/downloads
- untar Kafka_2.13-2.8.0.tgz
- Install java on EC2.
- Create a toipc on EC2 instance as, https://docs.aws.amazon.com/msk/latest/developerguide/create-topic.html
- Create a topics using the following command, 
 
  Topic name in this example is "AWSKafkaTutorialTopic"
  
  bin/kafka-topics.sh --create --zookeeper "ZookeeperConnectString" --replication-factor 3 --partitions 1 --topic AWSKafkaTutorialTopic
  
- The ZookeeperConnectStrig looks like this, z-1.mskcsv.******.c4.kafka.eu-north-1.amazonaws.com:2181 (Find on MSK)
- Create a Postgres DB on aws
- Use this scheme to create two tables,

CREATE TABLE msksc.cust_dat (

id int NOT NULL,

timestamp int NOT NULL,

longitutde NOT NULL,

country VARCHAR (50) NOT NULL
);


CREATE TABLE msksc.cust_dat (

username VARCHAR(50) NOT NULL,

sub_no int NOT NULL,

city VARCHAR (50) NOT NULL,

country VARCHAR (50) NOT NULL
);

- Copy the python files to EC2 instance.
- Run the code producer and consumer codes on two different terminals,
- python3 Consumer.py
- python3 Consumer_30.py
- python3 producer_gtfs.py

- Extra infromation, please edit inbounds on EC2 and RDS to allow traffic.
- Sometimes need editing routes and network gateways too.

     
      
      
