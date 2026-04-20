from jinja2 import Template
from datetime import datetime
import uuid

XML_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<p:FatturaElettronica versione="FPR12" xmlns:p="http://ivaservizi.agenziaentrate.gov.it/docs/xsd/fatture/v1.2">
  <FatturaElettronicaHeader>
    <DatiTrasmissione><IdTrasmittente><IdPaese>IT</IdPaese><IdCodice>06881890823</IdCodice></IdTrasmittente>
    <ProgressivoInvio>{{ progressivo_invio }}</ProgressivoInvio><FormatoTrasmissione>FPR12</FormatoTrasmissione>
    <CodiceDestinatario>{{ codice_destinatario }}</CodiceDestinatario></DatiTrasmissione>
    <CedentePrestatore><DatiAnagrafici><IdFiscaleIVA><IdPaese>IT</IdPaese><IdCodice>06881890823</IdCodice></IdFiscaleIVA>
    <CodiceFiscale>DSLVCN97H17G273A</CodiceFiscale><Anagrafica><Denominazione>VELIX SRLS</Denominazione></Anagrafica>
    <RegimeFiscale>RF01</RegimeFiscale></DatiAnagrafici>
    <Sede><Indirizzo>{{ indirizzo_sede }}</Indirizzo><CAP>{{ cap_sede }}</CAP><Comune>{{ comune_sede }}</Comune><Provincia>{{ provincia_sede }}</Provincia><Nazione>IT</Nazione></Sede></CedentePrestatore>
    <CessionarioCommittente><DatiAnagrafici>{% if piva_cliente %}<IdFiscaleIVA><IdPaese>IT</IdPaese><IdCodice>{{ piva_cliente }}</IdCodice></IdFiscaleIVA>{% else %}<CodiceFiscale>{{ cf_cliente }}</CodiceFiscale>{% endif %}
    <Anagrafica><Denominazione>{{ nome_cliente }}</Denominazione></Anagrafica></DatiAnagrafici>
    <Sede><Indirizzo>{{ indirizzo_cliente }}</Indirizzo><CAP>{{ cap_cliente }}</CAP><Comune>{{ comune_cliente }}</Comune><Provincia>{{ provincia_cliente }}</Provincia><Nazione>IT</Nazione></Sede></CessionarioCommittente>
  </FatturaElettronicaHeader>
  <FatturaElettronicaBody>
    <DatiGenerali><DatiGeneraliDocumento><TipoDocumento>TD01</TipoDocumento><Divisa>EUR</Divisa><Data>{{ data_fattura }}</Data><Numero>{{ numero_fattura }}</Numero><Causale>{{ causale }}</Causale></DatiGeneraliDocumento></DatiGenerali>
    <DatiBeniServizi><DettaglioLinee><NumeroLinea>1</NumeroLinea><Descrizione>{{ descrizione }}</Descrizione><Quantita>1.00</Quantita><PrezzoUnitario>{{ imponibile }}</PrezzoUnitario><PrezzoTotale>{{ imponibile }}</PrezzoTotale><AliquotaIVA>22.00</AliquotaIVA></DettaglioLinee>
    <DatiRiepilogo><AliquotaIVA>22.00</AliquotaIVA><ImponibileImporto>{{ imponibile }}</ImponibileImporto><Imposta>{{ imposta }}</Imposta><EsigibilitaIVA>I</EsigibilitaIVA></DatiRiepilogo></DatiBeniServizi>
  </FatturaElettronicaBody>
</p:FatturaElettronica>"""

def generate_sdi_invoice(order_data: dict, invoice_type: str = "recurring") -> str:
    imponibile = round(order_data["monthly_price"] / 1.22, 2) if invoice_type == "recurring" else round(order_data["activation_price"] / 1.22, 2)
    imposta = round(imponibile * 0.22, 2)
    data = {
        "progressivo_invio": f"{datetime.now().year}{uuid.uuid4().hex[:6].upper()}",
        "codice_destinatario": "0000000", "pec_destinatario": "",
        "indirizzo_sede": "Via Sede Legale 1", "cap_sede": "74100", "comune_sede": "TARANTO", "provincia_sede": "TA",
        "piva_cliente": order_data.get("piva_cliente", ""), "cf_cliente": order_data.get("cf_cliente", ""),
        "nome_cliente": order_data["nome_cliente"],
        "indirizzo_cliente": order_data.get("indirizzo", ""), "cap_cliente": order_data.get("cap", ""), "comune_cliente": order_data.get("comune", ""), "provincia_cliente": order_data.get("provincia", ""),
        "data_fattura": datetime.now().strftime("%Y-%m-%d"),
        "numero_fattura": f"VEL/{datetime.now().year}/{uuid.uuid4().hex[:6].upper()}",
        "causale": "Attivazione servizio" if invoice_type == "activation" else f"Canone mensile {datetime.now().strftime('%B %Y')}",
        "descrizione": "Servizio di connettività FTTH 2.5Gbps - Velix Srls AS206658",
        "imponibile": f"{imponibile:.2f}", "imposta": f"{imposta:.2f}"
    }
    return Template(XML_TEMPLATE).render(**data)
