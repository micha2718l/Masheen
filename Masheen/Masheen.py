class Masheen():
    validCommands = '+-><[].,'
    
    def __init__(self, prog):
        self.dataProg = [0]*10
        self.dataCode = [di for di in prog if di in self.validCommands]
        self.maxStep = 1000
        self.pointData = 0
        self.pointCode = 0
        self.pointJumps = []
        self.outs = []
        #print(self.dataCode)
    def run(self):
        if len(self.dataCode)==0:
            return
        for i in range(self.maxStep):
            #print(f'iter {i}, code {self.dataCode[self.pointCode]}')
            if self.dataCode[self.pointCode] == '+':
                self.dataProg[self.pointData] += 1
            elif self.dataCode[self.pointCode] == '-':
                self.dataProg[self.pointData] -= 1
            elif self.dataCode[self.pointCode] == '>':
                self.pointData += 1
            elif self.dataCode[self.pointCode] == '<':
                self.pointData -= 1
            elif self.dataCode[self.pointCode] == '[':
                self.pointJumps.append(self.pointCode)
            elif self.dataCode[self.pointCode] == ']':
                if len(self.pointJumps) == 0:
                    self.pointJumps.append(0)
                if self.dataProg[self.pointData] != 0:
                    self.pointCode = self.pointJumps[-1]
                else:
                    del self.pointJumps[-1]
            elif self.dataCode[self.pointCode] == '.':
                self.outs.append(self.dataProg[self.pointData])
                
            self.pointCode +=1
            #print(self.dataProg)
            #print(f'pointData {self.pointData} \npointCode {self.pointCode}')
            if self.pointCode >= len(self.dataCode):
                break

if __name__ == '__main__':            
    c = '+>++<-'
    c = '++++[><-]'

    hello = '++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++.'
    m = Masheen(hello)

    m.run()

    print(''.join([chr(mi) for mi in m.outs]))