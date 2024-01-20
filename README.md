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
airflow unpause [YOUR_DAG_ID]
airflow dags trigger [YOUR_DAG_ID]
```
Your dag_id is defined in your dag file

### Using Cloud Composer

#### Setup Cloud Composer Environment
Cloud Composer is a managed Apache Airflow provided by Google. There are multiple options to setup, including: <br>
(1) gcloud CLI: https://cloud.google.com/composer/docs/composer-2/run-apache-airflow-dag <br>
(2) Use Terraform: https://github.com/nedspnt/terraform-with-gcp

#### Upload Dags
```
gcloud composer environments storage dags import \
  --environment [ENVIRONMENT_NAME] \
  --location [YOUR_REGION] \
  --source [LOCAL_PATH_TO_DAG_FILE]
```

#### Trigger Dags
```
gcloud composer environments run [ENVIRONMENT_NAME] \
  --location [YOUR_REGION] trigger_dag -- [DAG_ID]
```