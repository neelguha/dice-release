# DICE: Data Integration, Cleaning, and Extraction Benchmark

Knowledge graphs (KGs) are a core component of applications ranging from search to personal assistants. However, learning representations for KG entities is a challenging problem, with implications for a wide range of knowledge graph construction and reasoning tasks.

We introduce the Data Integration, Cleaning, and Extraction (DICE) Benchmark: a collection of resources for developing and studying knowledge graph representations in multi-task settings. DICE consists of 12 tasks over 3 KG datasets, spanning a range of task types (regression, classification, retrieval).

This repository contains: 

- Scripts for downloading the DICE datasets 
- Supporting code for loading datasets and evaluating task performance 
- Example notebooks with baseline results for each of the DICE tasks


To download the datasets, simply run: 

```
python download_data.py
```

For more information about DICE, refer to https://neelguha.github.io/dice/index.html