class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = 0
        record = []
        number = 0
        for op in range(len(operations)):
            if operations[op] == "+":
                for i in range(len(record)):
                    number += int(record[i])
                record.append(str(number))
            elif operations[op] == "D":
                record.append((int(operations[op - 1]))* 2)
            elif operations[op] == "C":
                record.remove(record[op - 1])
            else: # all integer string cases
                record.append(operations[op])
        for i in range(len(record)):
            x += int(record[i])
        return x