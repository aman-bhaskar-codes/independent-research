# Reproducibility Guidelines

All experiments must be reproducible from the code and configuration stored in this repository.

1. **Environment**: Specify environment details in the experiment record (e.g., Python version, OS).
2. **Configuration**: Use configuration files or command-line arguments to specify parameters. Record these exactly in the experiment record.
3. **Seeds**: Set random seeds where applicable and record them.
4. **Data**: Do not commit large datasets. Use external storage and document the retrieval process (e.g., manifests, URLs, checksums) in the experiment record or project documentation.
5. **Traceability**: All claims in publications must be traceable to a specific experiment record and code commit.
