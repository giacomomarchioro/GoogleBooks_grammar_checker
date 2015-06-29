# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:44:28 2015
This is a simple way to check if sentence is correct or not checking the number
of results in google books for the sentence. Use check function to and type the sentence
as an argument or calling the function from the python shell.

@author: giacomo
"""
from bs4 import BeautifulSoup
import urllib2
def check(raw_query=''):
    """ (str) -> str, int
    Return number of results and original phrase.
    """
    if raw_query=='':
        raw_query=raw_input("Write sentence:")
    query= raw_query.replace(" ","+")
    url="""https://www.google.com/search?q=%%22%s%%22&btnG=Search+Books&tbm=bks&tbo=1""" %(query)
    #avoid HTTP Error 403: Forbidden
    req = urllib2.Request(url, headers={'User-agent' : "Topolino"}) 
    html_code = urllib2.urlopen( req )
    soupHandler = BeautifulSoup(html_code)
    a=soupHandler.find(id="resultStats")
    resultStats=[int(s) for s in str(a).replace(".","").split() if s.isdigit()][0]
    return raw_query,resultStats,

def compare_two_sentences(sentence_a='',sentence_b=''):
    """()->print
    Compare the results for two sentences.
    """
    if sentence_a=='':
        sentence_a=raw_input("Write first sentence:")
    if sentence_b=='':
        sentence_b=raw_input("Write second sentence:")
    result_a=check(sentence_a)
    result_b=check(sentence_b)
    print "-------------------------------"
    print "------------RESULTS----------"
    print "-------------------------------"
    print " \"%s\" :has %s results" %(result_a[0],result_a[1])
    print " \"%s\" :has %s results" %(result_b[0],result_b[1])
    
if __main__== "__main__":
    compare_two_sentences('if I were you','if I was you')
