import pyodbc


def getData(pageSize=10, pageNumber=1):
    response = {
        "items" : []
    }
    server = '103.113.247.15'
    database = 'vconnectnewdata'
    username = 'vcdata'
    password = 'vcdata'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()
    print(pageSize, pageNumber)
    tsql = "SELECT email, phone, state, city, website, establishyear, lattiude, longitude, category, service, " \
           "workinghours, ratingcount, verifiedstatus FROM dbo.Businessmaster, dbo.Businesscategory " \
           "where businesscategory.businessid = businessmaster.contentid order by businessmaster.contentid OFFSET " \
           + str((pageSize*(pageNumber-1))) + " ROWS FETCH NEXT " + str(pageSize) + " ROWS ONLY"
    with cursor.execute(tsql):
        row = cursor.fetchone()
        while row:
            response["items"].append({"name": "unknown" , "email": str(row[0]), "phone": str(row[1]),
                                      "stateCity": str(row[2]) + "/" + str(row[3]), "lga": "unknown",
                                      "website": str(row[4]), "companySize": "unknown",
                                      "ey": str(row[5]), "lat": str(row[6]), "long": str(row[7]),
                                      "category": str(row[8]), "service": str(row[9]), "workingHours": str(row[10]),
                                      "ratingScore": str(row[11]), "verifiedStatus": str(row[12])})
            response["has_next"] = True
            row = cursor.fetchone()
    return response
