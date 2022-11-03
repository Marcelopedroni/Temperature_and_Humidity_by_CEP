import requests
import json

# https://viacep.com.br/ws/13035500/json
# https://apiprevmet3.inmet.gov.br/estacao/proxima/<geocode>


def main():
    cep = input("Informe o seu CEP: ")
    geo = str(getGeo(cep))
    getInmetData(cep, geo)    


def getGeo(cep):
    url = "https://viacep.com.br/ws/{}/json".format(str(cep).strip().replace('-',''))
    response = requests.request("GET", url)
    fields = json.loads(response.text)
    geocode = fields['ibge']
    return (geocode)


def getInmetData(cep, geo):
    inmet_url  = "https://apiprevmet3.inmet.gov.br/estacao/proxima/" + str(geo)
    inmet_response = requests.request("GET", inmet_url)
    inmet_fields = json.loads(inmet_response.text)
    for field in inmet_fields:
        if field[1]:
            temp_inst = inmet_fields['dados']['TEM_INS']
            umid_inst = inmet_fields['dados']['UMD_INS']
    printMetrics(cep,temp_inst, umid_inst)


def printMetrics(cep, temp_inst, umid_inst):
    print("Para o CEP: {} temos:\nTemperatura Instantanea: {} C\nUmidade Instantanea: {}%".format(cep,temp_inst,umid_inst))

if __name__ == "__main__":
    main()