import requests


def fb_api_test(metric, version):
    print "metric : %s " %(metric)
    url = "https://graph.facebook.com/v" + version + "/234877673256809/insights?period=day&since=1532518210&until=1533814211&access_token=EAAHcoJgTk8gBAK2fvnGvwnske3i72zMsYEZCzeCVKVoMyfuC8lIRvvfT5GmZCn4iwDIKNNnnLZAqeNt5ZC4wlg4yNFw5TsJ6fgWGp5xBqTsEwlfYvSUtbq4uKZA59HA5NytLb9wKZAcZBAegG7g2Ek6ATKquCIFeqj99STXIfT7dQZDZD&metric=[\"" + metric + "\"]"
    r = requests.get(url)
    print r.url
    print r.text
    return r


def getMetrics(filePath):
    f = open(filePath)
    outFile = open("/Local/Users/rvatsa/fb_test/output.tsv","w")
    line = f.readline()
    while line:
        print line.strip()
        response = fb_api_test(line.strip(), "2.12")
        response2 = fb_api_test(line.strip(), "3.1")
        outFile.write("metric :" + line + "\t2.12 : " + response.text + "\t3.1 " + response2.text + "\n")
        line = f.readline()

    outFile.close()


#fb_api_test("page_impressions", "2.12")
getMetrics("/Local/Users/rvatsa/fb_test/metic_parameters")
