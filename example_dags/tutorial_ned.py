import textwrap
from datetime import datetime, timedelta
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

with DAG(
    "Ned_tutorial",
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"]
    },
    description="A simple tutorial DAG",
    schedule=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["example"]
) as dag:
    
    t1 = BashOperator(
        task_id="print_date",
        bash_command="date",
    )

    t2 = BashOperator(
        task_id="sleep",
        depends_on_past=False,
        bash_command="sleep 5",
        retries=3,
    )

    t1.doc_md = textwrap.dedent(
        """
        Task 1 documentation string test
        """
    )

    dag.doc_md = __doc__
    dag.doc_md = """
        This is a documentation placed anywhere
    """

    t3 = BashOperator(
        task_id="templated",
        depends_on_past=False,
        bash_command="echo 999",
    )

    t1 >> t2 >> t3
