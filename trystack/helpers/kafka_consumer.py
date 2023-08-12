from kafka import KafkaConsumer

def consumer():
  consumer = KafkaConsumer('my-topic',
                         group_id='my-group',
                         bootstrap_server=['localhost:9092'])

  for message in consumer:
      print("%s:%d:%d: key=%s value=%s" % (
            message.topic,
            message.partition,
            message.offset,
            message.key,
            message.value
      ))

  KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)
  KafkaConsumer(value_deserializer=lambda m: json.load(m.decode('ascii')))
  KafkaConsumer(value_deserializer=msgpack.unpackb)
  KafkaConsumer(consumer_timeout_ms=1000)