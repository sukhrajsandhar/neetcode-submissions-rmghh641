class Solution:
    def calPoints(self, operations: List[str]) -> int:
        x = 0
        record = []
        number = 0
        for op in range(len(operations)):
            if operations[op] == "+":
                val = int(record[-1]) + int(record[-2])
                record.append(str(val))
            elif operations[op] == "D":
                record.append(str(int(record[-1]) * 2))
            elif operations[op] == "C":
                record.pop()
            else: # all integer string cases
                record.append(operations[op])
        for i in range(len(record)):
            x += int(record[i])
        return x