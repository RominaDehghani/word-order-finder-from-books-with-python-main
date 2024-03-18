import string

def Word_Order_Frequency_One_Book(Book, Word_Order, File_Output):
    
    #Reading the first book
    Book = open (Book, "r", encoding="utf-8-sig")
    content = Book.read().lower()
    Book.close()
    
    #Removing punctuation from file_1
    remove_num = "".join([i for i in content if not i.isdigit()])
    words = remove_num.split()
    table = str.maketrans("", "", string.punctuation)
    stripped = [w.translate(table) for w in words]
    assembled = " ".join(stripped)
    
    #Removing extra spaces and remaining punctuation from file_1
    remove_s = assembled.replace("  ", " ")
    remove_s = remove_s.replace("“", "")
    remove_s = remove_s.replace("”", "")
    remove_s = remove_s.replace("’", "")
    remove_s = remove_s.replace("—", "")
    
    #Splitting the text of file_1 into a list
    text_words = remove_s.split()
    #print(text_words)
    
    #Displaying the words that must be removed from the text of two files as a list
    stop_words= ['able', 'about', 'above', 'abroad', 'according', 'accordingly',
            'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against',
            'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 'almost', 'alone',
            'along', 'alongside', 'already', 'also', 'although', 'always', 'am',
            'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any',
            'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways',
            'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are',
            'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 'associated',
            'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards',
            'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been',
            'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below',
            'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both',
            'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant',
            'caption', 'cause', 'causes', 'certain', 'certainly', 'changes',
            'clearly', 'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning',
            'consequently', 'consider', 'considering', 'contain', 'containing',
            'contains', 'corresponding', 'could', 'couldnt', 'course', 'cs',
            'currently', 'dare', 'darent', 'definitely', 'described', 'despite',
            'did', 'didnt', 'different', 'directly', 'do', 'does', 'doesnt',
            'doing', 'done', 'dont', 'down', 'downwards', 'during', 'each', 'edu',
            'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end',
            'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even',
            'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything',
            'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far',
            'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed',
            'following', 'follows', 'for', 'forever', 'former', 'formerly',
            'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore',
            'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going',
            'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half',
            'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he',
            'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter',
            'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes',
            'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit',
            'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im',
            'immediate', 'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate',
            'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead',
            'into', 'inward', 'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its',
            'itself', 'ive', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known',
            'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
            'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'likewise',
            'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made',
            'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'maynt', 'me',
            'mean', 'meantime', 'meanwhile', 'merely', 'might', 'mightnt', 'mine',
            'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs',
            'much', 'must', 'mustnt', 'my', 'myself', 'name', 'namely', 'nd',
            'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 'neither',
            'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine',
            'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone',
            'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding',
            'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh',
            'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'ones', 'only',
            'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought',
            'oughtnt', 'our', 'ours', 'ourselves', 'out', 'outside', 'over',
            'overall', 'own', 'particular', 'particularly', 'past', 'per',
            'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably',
            'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather',
            'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding',
            'regardless', 'regards', 'relatively', 'respectively', 'right',
            'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second',
            'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems',
            'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously',
            'seven', 'several', 'shall', 'shant', 'she', 'shed', 'shell', 'shes',
            'should', 'shouldnt', 'since', 'six', 'so', 'some', 'somebody', 'someday',
            'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat',
            'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying',
            'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking',
            'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that',
            'thatll', 'thats', 'thats', 'thatve', 'the', 'their', 'theirs', 'them',
            'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby',
            'thered', 'therefore', 'therein', 'therell', 'therere', 'theres',
            'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd', 'theyll',
            'theyre', 'theyve', 'thing', 'things', 'think', 'third', 'thirty',
            'this', 'thorough', 'thoroughly', 'those', 'though', 'three',
            'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together',
            'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try',
            'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing',
            'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up',
            'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
            'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz',
            'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome',
            'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what',
            'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever',
            'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres',
            'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while',
            'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl',
            'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing', 'wish',
            'with', 'within', 'without', 'wonder', 'wont', 'would', 'wouldnt',
            'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre', 'yours',
            'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows', 'i', 'whens',
            'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'i', 'www',
            'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt',
            'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen',
            'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give',
            'hasnt', 'herse', 'himse', 'interest', 'itse', 'mill', 'move', 'myse',
            'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten',
            'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance',
            'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah',
            'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent',
            'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol',
            'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 'gave',
            'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately',
            'importance', 'important', 'index', 'information', 'invention', 'itd',
            'keys', 'kg', 'km', 'largely', 'lets', 'line', 'll', 'means', 'mg',
            'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted',
            'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages',
            'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present',
            'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran',
            'readily', 'ref', 'refs', 'related', 'research', 'resulted',
            'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes',
            'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
            'similar', 'similarly', 'slightly', 'somethan', 'specifically',
            'state', 'states', 'stop', 'strongly', 'substantially', 'successfully',
            'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto',
            'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
            'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols',
            'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
            'world', 'youd', 'youre']
    
    
    
    #Using list comprehension to perform task(removing stop_words from file_1)
    result_text = [i for i in text_words if i not in stop_words]
    #print(result_text)
    
    #From the first book (single words)
    if Word_Order == 1: 
        
        #Initializing dictionary    
        d=dict()
        #Counting number of times each word comes up in list of words(in dictionary)
        for element in result_text:  
            d[element] = d.get(element, 0) + 1
        #print(d)
        
        
        #Sorting the number of words repeated in the text to write the results in descending order
        word_freq = sorted(d.items(), key = lambda t: t[1], reverse = True)[:100]
        #for i in word_freq:
            #print(i[0],i[1])
        
        
        
        #Displaying results in a text file
        f = open(File_Output, "a+")
        f.write("|   WORD        |   WORD        |\n")
        f.write("|   ORDER       |   ORDER       |\n")
        f.write("|   SEQUENCE    |   FREQUENCY   |\n")
        f.write("---------------------------------\n")
        for i in word_freq:
            f.write("      " + str(i[0]) + "             " +str(i[1]) + "\n")
        f.close()
        
        

    #From the first book (double words)
    elif Word_Order == 2:
        
        
        double_result = list(map(' '.join, zip(result_text[:-1],result_text[1:])))
        #print(double_result)
        
        #Initializing dictionary    
        d1=dict()
        #Counting number of times each word comes up in list of words(in dictionary)
        for element1 in double_result:  
            d1[element1] = d1.get(element1, 0) + 1
        #print(d1)
        
        #Sorting the number of words repeated in the text to write the results in descending order
        word_freq1 = sorted(d1.items(), key = lambda t: t[1], reverse = True)[:100]
        #for i in word_freq1:
            #print(i[0],i[1])
        
        
        #Displaying results in a text file
        f1 = open(File_Output, "a+")
        f1.write("|   WORD        |   WORD        |\n")
        f1.write("|   ORDER       |   ORDER       |\n")
        f1.write("|   SEQUENCE    |   FREQUENCY   |\n")
        f1.write("---------------------------------\n")
        for i in word_freq1:
            f1.write("  " + str(i[0]) + "             " +str(i[1]) + "\n")
        f1.close()
        
    else:
        print("Invalid number for WORD_ORDER.")
     
Word_Order_Frequency_One_Book("book_1.txt", 2, "result_1.txt")



def Word_Order_Frequency_Two_Books(Book_1, Book_2, Word_Order, File_Output):
    #Reading the first book
    Book_1 = open (Book_1, "r", encoding="utf-8-sig")
    content = Book_1.read().lower()
    Book_1.close()
    
    #Reading the second book
    Book_2 = open (Book_2, "r", encoding="utf-8-sig")
    content2 = Book_2.read().lower()
    Book_2.close()
    
    #Removing punctuation from file_1
    remove_num = "".join([i for i in content if not i.isdigit()])
    words = remove_num.split()
    table = str.maketrans("", "", string.punctuation)
    stripped = [w.translate(table) for w in words]
    assembled = " ".join(stripped)
    
    #Removing punctuation from file_2
    remove_num2 = "".join([i for i in content2 if not i.isdigit()])
    words2 = remove_num2.split()
    table2 = str.maketrans("", "", string.punctuation)
    stripped2 = [w.translate(table2) for w in words2]
    assembled2 = " ".join(stripped2)
    
    #Removing extra spaces and remaining punctuation from file_1
    remove_s = assembled.replace("  ", " ")
    remove_s = remove_s.replace("“", "")
    remove_s = remove_s.replace("”", "")
    remove_s = remove_s.replace("’", "")
    remove_s = remove_s.replace("—", "")

    #Removing extra spaces and remaining punctuation from file_2
    remove_s2 = assembled2.replace("  ", " ")
    remove_s2 = remove_s2.replace("“", "")
    remove_s2 = remove_s2.replace("”", "")
    remove_s2 = remove_s2.replace("’", "")
    remove_s2 = remove_s2.replace("—", "")
    
    #Splitting the text of file_1 into a list
    text_words = remove_s.split()
    #print(text_words)

    #Splitting the text of file_2 into a list
    text_words2 = remove_s2.split()
    #print(text_words2)
    
    #Displaying the words that must be removed from the text of two files as a list
    stop_words= ['able', 'about', 'above', 'abroad', 'according', 'accordingly',
            'across', 'actually', 'adj', 'after', 'afterwards', 'again', 'against',
            'ago', 'ahead', 'aint', 'all', 'allow', 'allows', 'almost', 'alone',
            'along', 'alongside', 'already', 'also', 'although', 'always', 'am',
            'amid', 'amidst', 'among', 'amongst', 'an', 'and', 'another', 'any',
            'anybody', 'anyhow', 'anyone', 'anything', 'anyway', 'anyways',
            'anywhere', 'apart', 'appear', 'appreciate', 'appropriate', 'are',
            'arent', 'around', 'as', 'as', 'aside', 'ask', 'asking', 'associated',
            'at', 'available', 'away', 'awfully', 'back', 'backward', 'backwards',
            'be', 'became', 'because', 'become', 'becomes', 'becoming', 'been',
            'before', 'beforehand', 'begin', 'behind', 'being', 'believe', 'below',
            'beside', 'besides', 'best', 'better', 'between', 'beyond', 'both',
            'brief', 'but', 'by', 'came', 'can', 'cannot', 'cant', 'cant',
            'caption', 'cause', 'causes', 'certain', 'certainly', 'changes',
            'clearly', 'cmon', 'co', 'co', 'com', 'come', 'comes', 'concerning',
            'consequently', 'consider', 'considering', 'contain', 'containing',
            'contains', 'corresponding', 'could', 'couldnt', 'course', 'cs',
            'currently', 'dare', 'darent', 'definitely', 'described', 'despite',
            'did', 'didnt', 'different', 'directly', 'do', 'does', 'doesnt',
            'doing', 'done', 'dont', 'down', 'downwards', 'during', 'each', 'edu',
            'eg', 'eight', 'eighty', 'either', 'else', 'elsewhere', 'end',
            'ending', 'enough', 'entirely', 'especially', 'et', 'etc', 'even',
            'ever', 'evermore', 'every', 'everybody', 'everyone', 'everything',
            'everywhere', 'ex', 'exactly', 'example', 'except', 'fairly', 'far',
            'farther', 'few', 'fewer', 'fifth', 'first', 'five', 'followed',
            'following', 'follows', 'for', 'forever', 'former', 'formerly',
            'forth', 'forward', 'found', 'four', 'from', 'further', 'furthermore',
            'get', 'gets', 'getting', 'given', 'gives', 'go', 'goes', 'going',
            'gone', 'got', 'gotten', 'greetings', 'had', 'hadnt', 'half',
            'happens', 'hardly', 'has', 'hasnt', 'have', 'havent', 'having', 'he',
            'hed', 'hell', 'hello', 'help', 'hence', 'her', 'here', 'hereafter',
            'hereby', 'herein', 'heres', 'hereupon', 'hers', 'herself', 'hes',
            'hi', 'him', 'himself', 'his', 'hither', 'hopefully', 'how', 'howbeit',
            'however', 'hundred', 'id', 'ie', 'if', 'ignored', 'ill', 'im',
            'immediate', 'in', 'inasmuch', 'inc', 'inc', 'indeed', 'indicate',
            'indicated', 'indicates', 'inner', 'inside', 'insofar', 'instead',
            'into', 'inward', 'is', 'isnt', 'it', 'itd', 'itll', 'its', 'its',
            'itself', 'ive', 'just', 'k', 'keep', 'keeps', 'kept', 'know', 'known',
            'knows', 'last', 'lately', 'later', 'latter', 'latterly', 'least',
            'less', 'lest', 'let', 'lets', 'like', 'liked', 'likely', 'likewise',
            'little', 'look', 'looking', 'looks', 'low', 'lower', 'ltd', 'made',
            'mainly', 'make', 'makes', 'many', 'may', 'maybe', 'maynt', 'me',
            'mean', 'meantime', 'meanwhile', 'merely', 'might', 'mightnt', 'mine',
            'minus', 'miss', 'more', 'moreover', 'most', 'mostly', 'mr', 'mrs',
            'much', 'must', 'mustnt', 'my', 'myself', 'name', 'namely', 'nd',
            'near', 'nearly', 'necessary', 'need', 'neednt', 'needs', 'neither',
            'never', 'neverf', 'neverless', 'nevertheless', 'new', 'next', 'nine',
            'ninety', 'no', 'nobody', 'non', 'none', 'nonetheless', 'noone',
            'noone', 'nor', 'normally', 'not', 'nothing', 'notwithstanding',
            'novel', 'now', 'nowhere', 'obviously', 'of', 'off', 'often', 'oh',
            'ok', 'okay', 'old', 'on', 'once', 'one', 'ones', 'ones', 'only',
            'onto', 'opposite', 'or', 'other', 'others', 'otherwise', 'ought',
            'oughtnt', 'our', 'ours', 'ourselves', 'out', 'outside', 'over',
            'overall', 'own', 'particular', 'particularly', 'past', 'per',
            'perhaps', 'placed', 'please', 'plus', 'possible', 'presumably',
            'probably', 'provided', 'provides', 'que', 'quite', 'qv', 'rather',
            'rd', 're', 'really', 'reasonably', 'recent', 'recently', 'regarding',
            'regardless', 'regards', 'relatively', 'respectively', 'right',
            'round', 'said', 'same', 'saw', 'say', 'saying', 'says', 'second',
            'secondly', 'see', 'seeing', 'seem', 'seemed', 'seeming', 'seems',
            'seen', 'self', 'selves', 'sensible', 'sent', 'serious', 'seriously',
            'seven', 'several', 'shall', 'shant', 'she', 'shed', 'shell', 'shes',
            'should', 'shouldnt', 'since', 'six', 'so', 'some', 'somebody', 'someday',
            'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhat',
            'somewhere', 'soon', 'sorry', 'specified', 'specify', 'specifying',
            'still', 'sub', 'such', 'sup', 'sure', 'take', 'taken', 'taking',
            'tell', 'tends', 'th', 'than', 'thank', 'thanks', 'thanx', 'that',
            'thatll', 'thats', 'thats', 'thatve', 'the', 'their', 'theirs', 'them',
            'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby',
            'thered', 'therefore', 'therein', 'therell', 'therere', 'theres',
            'theres', 'thereupon', 'thereve', 'these', 'they', 'theyd', 'theyll',
            'theyre', 'theyve', 'thing', 'things', 'think', 'third', 'thirty',
            'this', 'thorough', 'thoroughly', 'those', 'though', 'three',
            'through', 'throughout', 'thru', 'thus', 'till', 'to', 'together',
            'too', 'took', 'toward', 'towards', 'tried', 'tries', 'truly', 'try',
            'trying', 'ts', 'twice', 'two', 'un', 'under', 'underneath', 'undoing',
            'unfortunately', 'unless', 'unlike', 'unlikely', 'until', 'unto', 'up',
            'upon', 'upwards', 'us', 'use', 'used', 'useful', 'uses', 'using',
            'usually', 'v', 'value', 'various', 'versus', 'very', 'via', 'viz',
            'vs', 'want', 'wants', 'was', 'wasnt', 'way', 'we', 'wed', 'welcome',
            'well', 'well', 'went', 'were', 'were', 'werent', 'weve', 'what',
            'whatever', 'whatll', 'whats', 'whatve', 'when', 'whence', 'whenever',
            'where', 'whereafter', 'whereas', 'whereby', 'wherein', 'wheres',
            'whereupon', 'wherever', 'whether', 'which', 'whichever', 'while',
            'whilst', 'whither', 'who', 'whod', 'whoever', 'whole', 'wholl',
            'whom', 'whomever', 'whos', 'whose', 'why', 'will', 'willing', 'wish',
            'with', 'within', 'without', 'wonder', 'wont', 'would', 'wouldnt',
            'yes', 'yet', 'you', 'youd', 'youll', 'your', 'youre', 'yours',
            'yourself', 'yourselves', 'youve', 'zero', 'a', 'hows', 'i', 'whens',
            'whys', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o',
            'p', 'q', 'r', 's', 't', 'u', 'uucp', 'w', 'x', 'y', 'z', 'i', 'www',
            'amount', 'bill', 'bottom', 'call', 'computer', 'con', 'couldnt',
            'cry', 'de', 'describe', 'detail', 'due', 'eleven', 'empty', 'fifteen',
            'fifty', 'fill', 'find', 'fire', 'forty', 'front', 'full', 'give',
            'hasnt', 'herse', 'himse', 'interest', 'itse', 'mill', 'move', 'myse',
            'part', 'put', 'show', 'side', 'sincere', 'sixty', 'system', 'ten',
            'thick', 'thin', 'top', 'twelve', 'twenty', 'abst', 'accordance',
            'act', 'added', 'adopted', 'affected', 'affecting', 'affects', 'ah',
            'announce', 'anymore', 'apparently', 'approximately', 'aren', 'arent',
            'arise', 'auth', 'beginning', 'beginnings', 'begins', 'biol',
            'briefly', 'ca', 'date', 'ed', 'effect', 'etal', 'ff', 'fix', 'gave',
            'giving', 'heres', 'hes', 'hid', 'home', 'id', 'im', 'immediately',
            'importance', 'important', 'index', 'information', 'invention', 'itd',
            'keys', 'kg', 'km', 'largely', 'lets', 'line', 'll', 'means', 'mg',
            'million', 'ml', 'mug', 'na', 'nay', 'necessarily', 'nos', 'noted',
            'obtain', 'obtained', 'omitted', 'ord', 'owing', 'page', 'pages',
            'poorly', 'possibly', 'potentially', 'pp', 'predominantly', 'present',
            'previously', 'primarily', 'promptly', 'proud', 'quickly', 'ran',
            'readily', 'ref', 'refs', 'related', 'research', 'resulted',
            'resulting', 'results', 'run', 'sec', 'section', 'shed', 'shes',
            'showed', 'shown', 'showns', 'shows', 'significant', 'significantly',
            'similar', 'similarly', 'slightly', 'somethan', 'specifically',
            'state', 'states', 'stop', 'strongly', 'substantially', 'successfully',
            'sufficiently', 'suggest', 'thered', 'thereof', 'therere', 'thereto',
            'theyd', 'theyre', 'thou', 'thoughh', 'thousand', 'throug', 'til',
            'tip', 'ts', 'ups', 'usefully', 'usefulness', 've', 'vol', 'vols',
            'wed', 'whats', 'wheres', 'whim', 'whod', 'whos', 'widely', 'words',
            'world', 'youd', 'youre']



    #Using list comprehension to perform task(removing stop_words from file_1)
    result_text = [i for i in text_words if i not in stop_words]
    #print(result_text) 

    #Using list comprehension to perform task(removing stop_words from file_2)
    result_text2 = [i for i in text_words2 if i not in stop_words]
    #print(result_text2)
    
    #Adding the words from the first_list to the second_list
    result_text2.extend(result_text)
    #print(result_text2)
    
    
    #From the first and second books (single words)
    if Word_Order == 1:
        
        #Initializing dictionary    
        d2=dict()
        #Counting number of times each word comes up in list of words(in dictionary)
        for element2 in result_text2:  
            d2[element2] = d2.get(element2, 0) + 1
        #print(d2)
        
        #Sorting the number of words repeated in the text to write the results in descending order
        word_freq2 = sorted(d2.items(), key = lambda t: t[1], reverse = True)[:100]
        #for i in word_freq2:
            #print(i[0],i[1])
            
        
        #Displaying results in a text file    
        f2 = open(File_Output, "a+")
        f2.write("|   WORD        |   BOOK 1      |   BOOK 2      |   WORD        |\n")
        f2.write("|   ORDER       |   ORDER       |   ORDER       |   ORDER       |\n")
        f2.write("|   SEQUENCE    |   FREQUENCY   |   FREQUENC    |   FREQUENCY   |\n")
        f2.write("-----------------------------------------------------------------\n")
        for i in word_freq2:
            f2.write("  " + str(i[0]) +
                     "                                                      "+ str(i[1]) + "\n")
            
        f2.close()
    
 
    #From the first and second books (double words)
    elif Word_Order == 2:
        
        double_result2 = list(map(' '.join, zip(result_text2[:-1],result_text2[1:])))
        #print(double_result2)
        
        #Initializing dictionary    
        d22=dict()
        #Counting number of times each word comes up in list of words(in dictionary)
        for element22 in double_result2:  
            d22[element22] = d22.get(element22, 0) + 1
        #print(d22)
        
        #Sorting the number of words repeated in the text to write the results in descending order
        word_freq22 = sorted(d22.items(), key = lambda t: t[1], reverse = True)[:100]
        #for i in word_freq22:
            #print(i[0],i[1])
            
        
        #Displaying results in a text file
        f22 = open(File_Output, "a+")
        f22.write("|   WORD        |   BOOK 1      |   BOOK 2      |   WORD        |\n")
        f22.write("|   ORDER       |   ORDER       |   ORDER       |   ORDER       |\n")
        f22.write("|   SEQUENCE    |   FREQUENCY   |   FREQUENC    |   FREQUENCY   |\n")
        f22.write("-----------------------------------------------------------------\n")
        for i in word_freq22:
            f22.write("  " + str(i[0]) +
                      "                                                     " + str(i[1]) + "\n")
            
        f22.close()
        
    else:
        print("Invalid number for WORD_ORDER.")
        
Word_Order_Frequency_Two_Books("book_1.txt", "book_2.txt", 2, "result_2.txt")






