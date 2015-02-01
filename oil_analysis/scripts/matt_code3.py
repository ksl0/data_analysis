import requests
c =  requests.post("http://cogcc.state.co.us/cogis/IncidentSearch2.asp",
    data='itype=insp&operator_name_number=name',
    headers={
        "Content-Type": "application/x-www-form-urlencoded",
    },
    cookies={},
)

print c.text
