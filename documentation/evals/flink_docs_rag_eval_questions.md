# Flink Docs RAG Eval Questions (Baseline Set)

Use these questions as a lightweight retrieval/answer-quality regression set for the docs RAG.

1. Which configuration options control checkpoint interval and timeout in Flink?
2. How do checkpoints differ from savepoints, and when should each be used?
3. What settings are recommended when checkpointing is slow under backpressure?
4. Which state backend choices are available, and what are the tradeoffs between them?
5. How do I configure RocksDB state backend tuning for large state workloads?
6. What are the key differences between event time and processing time in Flink?
7. How do watermarks work, and how can I generate them in the DataStream API?
8. What causes backpressure in Flink jobs, and how can I diagnose it?
9. How do I run Flink on Kubernetes, and what deployment modes are supported?
10. What are the required steps to enable high availability in a Flink cluster?
11. How do I configure memory for JobManager and TaskManager processes?
12. How do I submit a SQL job and inspect the query plan in Flink SQL?
13. How do temporal joins work in Flink SQL, and what are common constraints?
14. Which options are available for Kafka connectors in DataStream and Table API?
15. How do exactly-once guarantees work for connectors and checkpointing together?
16. How can I debug classloading issues in Flink deployments?
17. Which metrics and observability options are available for production Flink jobs?
18. How do I use SQL Gateway, and what endpoints or modes does it expose?
19. What changed between Flink 1.x and 2.x for relevant APIs or configuration behavior?
20. How do I troubleshoot task failure recovery and restart behavior in Flink?
