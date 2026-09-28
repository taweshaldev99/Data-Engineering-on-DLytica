from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers="localhost:9092")

for i in range(10):
    key = f"user-{i % 3}"
    value = f"order number:  {i}"
    producer.send(
        "demo.topic",
        key=key.encode(),  #Kafka wants bytes on the wire
        value=value.encode(),
    ) 

    print(f"send key ={key}: value]='{value}'")

producer.flush()  #deliver everything before we exit
print("Done--------- 10 Messages sent")