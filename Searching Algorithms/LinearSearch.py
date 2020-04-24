
class Search:
    """ True : If searching objet found in list it will return True 
        False : If Searching object not found in list it will return False
    """
    def __init__(self,list,search_for):
        self.list = list 
        self.search_for = search_for

    def __len__(self):
        return len(self.list)

    def linear_search(self):
        """
        In this type of search, a sequential search is made over all items one by one. Every Item is checked. 
        If a match is found then that particular item is returned,
        otherwise the search continue till the end of the 
        data-strucutre
        """
        search_at = 0
        search_res = False
        # match the value with each data point
        while search_at < len(self.list) and search_res is False:
            if self.list[search_at] == self.search_for:
                search_res = True
            else:
                search_at = search_at + 1
            
        print(f'{search_res}')


l = [4,534,646,3,6,6,33,6,34,643,32,4,43,6]
result = Search(l,5)
result.linear_search()

        