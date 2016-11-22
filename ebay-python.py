import datetime, sys, os
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

ebayappid = os.environ['APPID']
print ebayappid

try:
    api = Connection(appid=ebayappid, config_file=None)
    response = api.execute('findItemsAdvanced', {'keywords': 'legos'})

    assert(response.reply.ack == 'Success')
    assert(type(response.reply.timestamp) == datetime.datetime)
    assert(type(response.reply.searchResult.item) == list)

    item = response.reply.searchResult.item[0]
    assert(type(item.listingInfo.endTime) == datetime.datetime)
    assert(type(response.dict()) == dict)

except ConnectionError as e:
    print(e)
    print(e.response.dict())
