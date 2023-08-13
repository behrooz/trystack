from kafka import KafkaConsumer

def consumer():
  consumer = KafkaConsumer('my-topic',
                         group_id='my-group',
                         bootstrap_servers=['192.168.2.20:9092'])
    
  for message in consumer:
      print("key=%s value=%s" % (
            # message.topic,
            # message.partition,
            # message.offset,
            message.key,
            message.value
      ))

#   KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)
#   KafkaConsumer(value_deserializer=lambda m: json.load(m.decode('ascii')))
#   KafkaConsumer(value_deserializer=msgpack.unpackb)
#   KafkaConsumer(consumer_timeout_ms=1000)

#   consumer.subscribe(pattern='^awesome.*')

#   # Use multiple consumers in parallel w/ 0.9 kafka brokers
#   # typically you would run each on a different server / process / CPU
#   consumer1 = KafkaConsumer('my-topic',
#                           group_id='my-group',
#                           bootstrap_servers='my.server.com')