#Creating json for DataSource:
echo ['{"AwsAccountId":"'$1'","DSourceId":"'$2'"}',`aws quicksight describe-data-source --aws-account-id $1 --data-source-id $2`,`aws quicksight describe-data-source-permissions --aws-account-id $1 --data-source-id $2`]|jq '{"AwsAccountId":.[0].AwsAccountId,"DataSourceId":.[1].DataSource.DataSourceId,"Name":.[1].DataSource.Name,"Type":.[1].DataSource.Type,"DataSourceParameters":.[1].DataSource.DataSourceParameters,"Permissions":.[2].Permissions,"SslProperties":.[1].DataSource.SslProperties}'>$3/DataSource/create-datasource-$2.json

echo "DSourceId=$2">>$3/Ids.txt