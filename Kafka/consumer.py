from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "demo-topic",
    bootstrap_servers="localhost:9092",
    group_id="class-group",
    auto_offset_reset="earliest",  # earliest bho bhane agadi dekhi kei data auxa

)

print("Waiting for messages .........(CTRL + C to STOP)")

for msg in consumer:
    print(
        f"partition={msg.partition} offset= {msg.offset}"
        f"key={msg.key.decode() if msg.key else None} value= {msg.value.decode()}"
    )

