from phonenumbers import parse; from requests import get; from os import system


RAPID_API_KEY = '1234-ABC-DEFG'


def lookup(pre, num):
    url = 'https://scout.p.rapidapi.com/v1/numbers/search'
    key = {
        'x-rapidapi-key': RAPID_API_KEY,
        'x-rapidapi-host': 'scout.p.rapidapi.com'
        }
    query = {'dialcode': f'+{pre}{num}'}


    try:
        r = get(url, headers=key, params=query)

        if r.status_code == 200:
            r = r.json()
    
            company = r['operating_company_name']
            ctype = f"{r['operating_company_type']}, {r['line_type']}"
            ported = f"{r['ported']}, {r['ported_date']}"


            dial_code = f"{r['dialcode_e164']}, invalid: {r['dialcode_invalid']}"
            lrn = r['location_routing_number']


            timezone = r['timezone']
            country = f"{r['country']}, {r['country_short']}"
            state = r['administrative_area_level_1']


            county = r['administrative_area_level_2']
            locality = r['locality']
            postal = r['postal_code']

            print(f'''         │─(query@{num}):
         │
         │─ company  -> {company}
         │─ routing  -> {lrn}
         │─ dialcode -> {dial_code}
         │─  ported  -> {ported}
         │─    type  -> {ctype}
         │         
         │─(query@{num}):
         │
         │─ timezone  -> {timezone}
         │─  country  -> {country}
         │─    state  -> {state}
         │─   county  -> {county}
         │─     area  -> {locality}, {postal}
         │
         │─(query@{num}):''')

            input(f'      ┌──(usr@infidelity)-[enter#]\n      └─$│ '); main()
    except Exception as e:
        print(f'         │─(query@{num}): "{e}"')
        input(f'      ┌──(usr@infidelity)-[enter#]\n      └─$│ '); main()


def main():
    system('cls && mode con cols=57 lines=32 && title infidelity - phone-search')

    print(f''' 
      ────────────────────────
    ────────────────────────────
      ┬┌┐┌┌─┐┬┌┬┐┌─┐┬  ┬┌┬┐┬ ┬ : PHONE-SEARCH
      ││││├┤ │ ││├┤ │  │ │ └┬┘ : SCOUT.TEL API
      ┴┘└┘└  ┴─┴┘└─┘┴─┘┴ ┴  ┴  : E.164 FORMAT
    ──────────────────────────── 
      ────────────────────────''')
    
    arg = input(f'      ┌──(usr@infidelity)-[phone#]\n      └─$│ ')

    try:
        pre = parse(arg).country_code
        num = parse(arg).national_number

        lookup(pre, num)
    except:
        print(f'         │─(query@{arg}): invalid format, use E.164')
        input(f'      ┌──(usr@infidelity)-[enter#]\n      └─$│ '); main()


main()
