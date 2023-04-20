class StringUtility:
    def __init__(self, string):
        self.s = string

    def __str__(self):
        """
        returns the instance variable as a string 
        arg: (self)
        return: [str]
        """
        return f"{self.s}"
    
    def vowels(self):
        """
        counts the number of vowels in a word and returns the value
        args: (self) [str]
        return: [int] or "many" [str] if the value is greater than 5
        """
        self.str = str(self)
        self.vowels = self.str.lower()
        count = 0
        vowels = ["a", "e", "i", "o", "u"]
        for ch in self.vowels:
            if ch in vowels:
                count += 1
            else:
                pass
        
        if count < 5: 
            return f"{str(count)}"
        elif count >= 5:
            return f"many"
        
    
    def bothEnds(self):
        """
        splices together the first two letters and last two letters of a word 
        args: self [str]
        return: [str]
        """
        self.bothEnds = str(self)      
        if len(self.bothEnds) <= 2:
            return f""
        else:
            return f"{self.bothEnds[0]}{self.bothEnds[1]}{self.bothEnds[-2]}{self.bothEnds[-1]}"
        
    def fixStart(self):
        """
        replaces all other instances of the first character with an astetisk 
        args: self [str]
        return: match [str] first letter, asterisksadded [str] rest of the word with asterisks added
        """
        self.fixStart = str(self)

        if str(self) == "":
            return f"{self.fixStart}"
        
        elif len(self.fixStart) <= 1:
            return f"{self.fixStart}"

        else:
            match = self.fixStart[0]
            asterisk = "*"
            newword = []
        
            for ch in (self.fixStart):
                if ch == match:
                    newword += asterisk
                else:
                    newword += ch
            
            asterisksadded = "".join(newword)

            return f"{match}{asterisksadded[1:]}"
                

    def asciiSum(self): 
        """
        adds up the ascii values for each input 
        args: self [str]
        return: [int]
        """
        self.asciiSum = str(self)
        result = 0
        for ch in self.asciiSum:
            result += ord(ch)
        
        return result


    def cipher(self):
        self.caesar_cipher = str(self)
        result = ""
        shift = len(self.caesar_cipher)
        for ch in self.caesar_cipher:
            if ch.isalpha():
                start = ord('A') if ch.isupper() else ord('a')
                new_pos = (ord(ch) - start + shift) % 26
                ch = chr(start + new_pos)
            result += ch
        return result

