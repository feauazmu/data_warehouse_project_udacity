# Project: Data Modeling with Postgres.

In this repository you can find the code for the project: *Data Warehouse* of [udacity's nanodegree in data engineering](https://www.udacity.com/course/data-engineer-nanodegree--nd027).

The introduction to the project states the following:

>*A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.*

## Project Description

The idea of the project is to create an ETL pipeline to transfer data from a set of JSON files located in a S3 bucket, stage them in Redshift, and then transform the data in a collection of tables following a [*star schema*](https://en.wikipedia.org/wiki/Star_schema). At the end of the process there will be 1 fact table and 4 dimension tables.

![Schema](https://raw.githubusercontent.com/feauazmu/data_warehouse_project_udacity/main/static/schema.png)

## Motivation

The analysts working in the company will be able to do their work more efficiently and can continue to make insights into the use of the platform. 

## Requirements

The scripts for the creation (and deletion) of the tables and the ETL process are written in `Python`. 

The code used to create the Redshift cluster, the associated roles and the configuration file can be found in the Jupyter Notebook `iac.ipynb`.  To run this document you need to have an `.env` file with the AWS Access Key ID as `AWS_KEY` and the AWS Secret Access Key as `AWS_SECRET` associated to a role with sufficient permissions.

## Running the project

Functions used in the creation of the tables can be found in `create_tables.py`.  To connect to the database and create the tables described above it is necessary to run this script.

```bash
python create_tables.py
```

Then you can fill in the data by running the script `etl.py`

```bash
python etl.py
```