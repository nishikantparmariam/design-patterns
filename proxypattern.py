import time


class IBookParser:

    def getNumberOfPages(self):
        raise NotImplemented


class BookParser:

    def __init__(self, bookString):
        time.sleep(2)

    def getNumberOfPages(self):
        return 9


class ProxyBookParser(IBookParser):

    def __init__(self, bookString):
        self.bookString = bookString
        self.bookParser = None

    def getNumberOfPages(self):
        
        if not self.bookParser:
            self.bookParser = BookParser(self.bookString)

        return self.bookParser.getNumberOfPages()


######################################################


def main():

    startTime = time.time()    
    parser1 = ProxyBookParser("abc")    
    print('Initialize proxy - ', time.time() - startTime)

    startTime = time.time() 
    parser2 = BookParser("def")
    print('Initialize book parser - ', time.time() - startTime)

    startTime = time.time() 
    print(parser1.getNumberOfPages())
    print('Call number of pages on proxy - ', time.time() - startTime)

    startTime = time.time() 
    print(parser2.getNumberOfPages())
    print('Call number of pages on proxy - ', time.time() - startTime)

main()