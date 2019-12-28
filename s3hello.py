import boto3
import pandas as pd

def hello():
    location = '/tmp/nba_2017_endorsement_full_stats.csv'
    resource = boto3.resource("s3")
    resource.meta.client.download_file('testntest', 'nba_2017_endorsement_full_stats.csv',
    location)
    return location

if __name__ == "__main__":
    my_location = hello()
    df = pd.read_csv(my_location)
    print(f"I download a file and the descr stats are: {df.describe()}")
    