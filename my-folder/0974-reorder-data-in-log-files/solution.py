class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digi_logs = []
        for log in logs:
            if log[-1] in ['0','1','2','3','4','5','6','7','8','9']:
                digi_logs.append(log)
            else:
                letter_logs.append(log)
        # print(digi_logs, letter_logs)
        letter_logs.sort(key = lambda letter: (letter.split()[1:],letter.split()[0]))
        return letter_logs + digi_logs
