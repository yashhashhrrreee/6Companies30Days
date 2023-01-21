

class Solution: 
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        res = []
        def getdetail(el):
            val = el.split(",")
            return {"name": val[0], "time": int(val[1]), "amount": int(val[2]), "city": val[3]}
        
        mapper = dict()

        def is_valid(trans, translist):
            if trans["amount"] > 1000:
                return False
            for transv in translist:
                if trans["city"] != transv["city"] and abs(trans["time"] - transv["time"]) <= 60:
                    return False
            return True

        for transaction in transactions:
            trans = getdetail(transaction)
            mapper[trans["name"]] = mapper.get(trans["name"], []) + [trans]
        
        print("mapper is ", mapper)

        for transaction in transactions:
            trans = getdetail(transaction)

            if not is_valid(trans, mapper[trans["name"]]):
                res.append(transaction)

        return res
