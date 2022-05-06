import pandas as pd
count = 0
clients_list = []
bills_data = pd.read_excel('./media/bills.xlsx')
client_org = pd.DataFrame(bills_data, columns=['client_org'])
number = pd.DataFrame(bills_data, columns=['№'])
summary = pd.DataFrame(bills_data, columns=['sum'])
date = pd.DataFrame(bills_data, columns=['date'])
result_summary = (summary
       .groupby("sum")
       .apply(lambda x: x.drop(columns="sum").to_dict("records"))
       .to_dict())
for s in result_summary.keys():
    count += s



client_org_data = pd.read_excel('./media/client_org.xlsx')
organization_data = pd.read_excel('./media/client_org.xlsx', sheet_name='organization')
client = pd.DataFrame(client_org_data, columns=['name'])
organization = pd.DataFrame(organization_data, columns=['client_name', 'name'])
result_name = (client
       .groupby("name")
       .apply(lambda x: x.drop(columns="name").to_dict("records"))
       .to_dict())
for c in result_name.keys():
     clients_list.append(c)
