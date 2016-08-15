import requests
import json
from pymarc import JSONReader

def get_record(r):
    rjson =r.json()
    marc = rjson['marc']
    marc['fields'] = [{k:v} for k,v in zip(marc['fields'][0::2],
                                           marc['fields'][1::2])]
    for field in marc['fields']:
        k = list(field.keys())[0]
        try:
            field[k]['subfields'] = [{k:v} for k,v in zip(field[k]['subfields'][0::2], 
                                                          field[k]['subfields'][1::2])]
        except TypeError:
            pass
    
    jmarc = JSONReader(json.dumps(marc))
    for record in jmarc:
        return record


if __name__ == '__main__':
    r = requests.get('http://govtest.sandbox.kohalibrary.com/api/work/12345')
    record = get_record(r)
    print(record.leader)