#!/usr/bin/python3

#improrting confluence module from atlassian-python-api
#from datetime import date
from re import template
from atlassian import Confluence
from json import loads, dumps
from ast import literal_eval
from os import getcwd

#from incidents_count import incident_count


#Authentication using PATs (Personal Access Token)
confluence = Confluence(
    url='https://confluence.nexgen.neustar.biz/',
    token='')



#updating the DOC page 
page_id=479440497

query_output = confluence.get_page_by_id(page_id, expand='body.storage', status=None, version=None) #expand='storage', 
#converting json object to python dictionary
query_output_json = dumps(query_output)              #takes a dictionary as input and returns a string as output.
query_output_dict = loads(query_output_json)         #takes a string as input and returns a dictionary as output.

#getting the DOC page HTML template
html_template = query_output['body']['storage']['value']     # literal_eval()changing the string output to dictionary 

#getting the working directory of script 

template_file = getcwd() + '\DOC_html_template.html'

#replacing the Magnet Infrastructure string in the template
with open(template_file, 'w') as TF:
    for line in html_template: 
        TF.writelines(line)

with open(template_file, 'r') as TF:
    lines = TF.readlines()


#html_template = html_template.replace("Magnet Infrastructure 2 1 1", "Magnet Infrastructure")

#update the confluence page 
status = confluence.update_page(
    parent_id=None,
    page_id=479440497,
    title="TEST COPY - DOC PAGE",
    body=html_template,
)

print(status)


'''
title='TEST COPY - DOC PAGE'
space=''
page_id = '479440497'
#print( confluence.get_page_by_title( space, title) )
print( confluence.get_page_by_id(self, page_id, expand=None, status=None, version=None))
'''