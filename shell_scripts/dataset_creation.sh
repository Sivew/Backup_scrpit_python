#Creating json for DataSet:
echo ['{"AwsAccountId":"'$1'", "DataSetId": "'$2'"}',`aws quicksight describe-data-set --aws-account-id $1 --data-set-id $2`,`aws quicksight describe-data-set-permissions --aws-account-id $1 --data-set-id $2`]|jq '{"AwsAccountId":.[0].AwsAccountId,"DataSetId":(.[1].DataSet.DataSetId),"Name":(.[1].DataSet.Name),"PhysicalTableMap":.[1].DataSet.PhysicalTableMap,"LogicalTableMap":.[1].DataSet.LogicalTableMap,"ImportMode":.[1].DataSet.ImportMode,"ColumnGroups":.[1].DataSet.ColumnGroups,"FieldFolders":.[1].DataSet.FieldFolders,"Permissions":.[2].Permissions,"RowLevelPermissionDataSet":.[1].DataSet.RowLevelPermissionDataSet,"RowLevelPermissionTagConfiguration":.[1].DataSet.RowLevelPermissionTagConfiguration,"ColumnLevelPermissionRules":.[1].DataSet.ColumnLevelPermissionRules,"Tags":.[1].DataSet.Tags,"DataSetUsageConfiguration":.[1].DataSet.DataSetUsageConfiguration}'>$3/DataSet/create-dataset-$2.json

echo "DSetId=$2">>$3/Ids.txt