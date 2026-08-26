# Список транзакций, полученных от платежного шлюза  
raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10", "SUCCESS:0", "SUCCESS:250", "ERROR:200"]  
# Реализация фильтрации в одну строку с помощью List Comprehension 


clean_transactions = [
    int(transaction.split(":")[1]) 
    for transaction in raw_transactions 
    if transaction.startswith("SUCCESS") 
    and int(transaction.split(":")[1]) > 0
]


print("Очищенные транзакции:", clean_transactions)