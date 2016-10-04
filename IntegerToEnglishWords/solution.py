class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return "Zero"
            
        s = []
        triplet = 0
        mappings = ["", "Thousand", "Million", "Billion", "Trillion"]
        while num/(1000**triplet):
            part = (num/(1000**triplet))%1000
            res = self.convert(part)
            if res:
                s = res + [mappings[triplet]] + s
            triplet += 1
        return " ".join(x for x in s if x)
    
    def convert(self, num):
        digs = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        twenties = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        hundred = "Hundred"
        
        res = []
        if num >= 100:
            res.append(digs[num/100])
            res.append(hundred)
            num %= 100
        
        if num > 0 and num < 10:
            return res + [digs[num]]
        elif num >= 10 and num <= 19:
            return res + [twenties[num - 10]]
        elif num >= 20:
            return res + [tens[num/10], digs[num%10]] 
        else:
            return res
            