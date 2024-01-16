# practice-airflow

Start a server and see existing DAGs. Note that this is not for production.
```
airflow standalone
```
Then we can access Airflow through `localhost:8080`


Airflow's home directory is `~/airflow` by default. We can create dags folder inside it.
```
mkdir -p ${AIRFLOW_HOME}/dags
```

To create a pipeline, a DAG file has to be inside the folder `~airflow/dags/` we have created. However, let's keep DAG files in `project_dags/` to keep the project organized, and copy them to `~airflow/dags` once we want to test those pipelines in Airflow.
```
cp -a example_dags/. ${AIRFLOW_HOME}/dags/
```

You should now be able to see your DAG in Airflow's UI.

Unpause DAG and manually trigger it through UI, or terminal:
```
airflow unpause <your_dag_id>
airflow dags trigger <your_dag_id>
```
Your dag_id is defined in your dag file

