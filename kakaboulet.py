# Available variables:
#  - env: environment on which the action is triggered
#  - model: model of the record on which the action is triggered; is a void recordset
#  - record: record on which the action is triggered; may be void
#  - records: recordset of all records on which the action is triggered in multi-mode; may be void
#  - time, datetime, dateutil, timezone: useful Python libraries
#  - float_compare: utility function to compare floats based on specific precision
#  - log: log(message, level='info'): logging function to record debug information in ir.logging table
#  - _logger: _logger.info(message): logger to emit messages in server logs
#  - UserError: exception class for raising user-facing warning messages
#  - Command: x2many commands namespace
# To return an action, assign: action = {...}

#DEEL1 INTRO
if record.id:
  OB = env['x_offerte_builder'].search([('id','=',record.id)])
  AC = OB['x_studio_audit_categorie']
  html =  "<h1><div style='text-align: right;'>" +  str(OB['x_studio_partner_id']['display_name']) + "</div></h1>"
  html +=  "<b><div style='text-align: right;'>" +  str(OB['x_studio_date']) + "</div></b>"
  html += str(AC['x_studio_inleiding'])

  
  html += "<div style='page-break-before: always; page-break-after: always;'>"
  html += "</div>"
  
  
#DEEL2 Producten lijst
  html += "<div style='width:50%;float:left;'><h2>Producten wel aanwezig</h2><hr><br />" 
  for i in OB['x_studio_one2many_field_933_1hjukhcev']:      
    if i['x_studio_opnemen_in_rapport'] == 0:
      html += "<h4>" + str(i['x_studio_audit_check']['x_name']) + "</h4>"
      html += "<h4>" + str(i['x_studio_audit_check']['x_studio_toelichting_klant']) + "</h4></tr>"
#      html += str(AC['x_studio_boodschap_bij_product'])  + i['x_studio_nieuw_product']['display_name']
  html += "</div>"
  html += "<div style='width:50%;float:right;'><h2>Producten niet aanwezig</h2><hr><br />"
  for i in OB['x_studio_one2many_field_933_1hjukhcev']:
    if i['x_studio_opnemen_in_rapport'] == 1:
      html += "<h4>" + str(i['x_studio_audit_check']['x_name']) + "</h4>"
      html += "<h4>" + str(i['x_studio_audit_check']['x_studio_toelichting_klant']) + "</h4>"
#      html += str(AC['x_studio_boodschap_bij_product'])  + i['x_studio_nieuw_product']['display_name']
  html += "</div>"  
  html += "<div style='clear: both;'></div>"
  html += "<div style='width: 100%;'>"
  html += "</div>"
  html += "<hr>" 
  html += "<div style='page-break-before: always; page-break-after: always;'>"
  html += "</div>"
  
  
  #DEEL 3 Tekening
  html += "<div style='text-align: center;'>"
  html += "<img src='https://odoo.serso.be/web/image/107907?filename=hacker.png&unique=ea1ba7c2c481669d93e27011c1bfe5527200092f' style='width: 50%; margin-bottom: 20px;'>"
  for i in OB['x_studio_one2many_field_933_1hjukhcev']:
    if i['x_studio_opnemen_in_rapport'] == 1 and i['x_studio_audit_check']['x_studio_audit_groep']['x_name'] == 'Hacker':
      html += "<h4 style='text-align: center;'>" + str(i['x_studio_audit_check']['x_name']) + "</h4>"
  html += "</div>"

# Inline CSS-stijlen
  table_style = "width: 100%; border-collapse: collapse !important; border: none !important; margin: 0 !important; padding: 0 !important;"
  cell_style = "display: table-cell; width: 50%; padding: 5px; border: none !important; margin: 0 !important;"
# Tabel 1
  html += "<div style='float: left; width: 33.33%; box-sizing: border-box;'>"
  html += "<img src='https://odoo.serso.be/web/image/107911?filename=client.png&unique=cbdd120bdb24d8a28d3203de8693edf930194792' style='width: 100%;'>"
  for i in OB['x_studio_one2many_field_933_1hjukhcev']:
    if i['x_studio_opnemen_in_rapport'] == 1 and i['x_studio_audit_check']['x_studio_audit_groep']['x_name'] == 'Client':
      html += "<h4 style='text-align: center;'>" + str(i['x_studio_audit_check']['x_name']) + "</h4>"
  html += "</div>"

  # Tabel 2
  html += "<div style='float: left; width: 33.33%; box-sizing: border-box;'>"
  html += "<img src='https://odoo.serso.be/web/image/107910?filename=User.png&unique=c947018fc49ffb18b5683986d583556947a7a646' style='width: 100%;'>"
  for i in OB['x_studio_one2many_field_933_1hjukhcev']:
    if i['x_studio_opnemen_in_rapport'] == 1 and i['x_studio_audit_check']['x_studio_audit_groep']['x_name'] == 'User':
      html += "<h4 style='text-align: center;'>" + str(i['x_studio_audit_check']['x_name']) + "</h4>"
  html += "</div>"

# Tabel 3
  html += "<div style='float: left; width: 33.33%; box-sizing: border-box;'>"
  html += "<img src='https://odoo.serso.be/web/image/107908?filename=email.png&unique=c8544d8635f6b0dcc5868037b6fde93c578626fa' style='width: 100%;'>"
  for i in OB['x_studio_one2many_field_933_1hjukhcev']:
    if i['x_studio_opnemen_in_rapport'] == 1 and i['x_studio_audit_check']['x_studio_audit_groep']['x_name'] == 'Email':
      html += "<h4 style='text-align: center;'>" + str(i['x_studio_audit_check']['x_name']) + "</h4>"
  html += "</div><br><br>"
  html += "<div style='float: left; width: 100%; box-sizing: border-box;'><br></div>"
# Tabel 4
  html += "<div style='float: left; width: 33.33%; box-sizing: border-box;'>"
  html += "<img src='https://odoo.serso.be/web/image/107958?filename=cloet.jpg&unique=8b38856301eb9e8508ef85667d29f013767be1f1' style='width: 100%;'>"
  for i in OB['x_studio_one2many_field_933_1hjukhcev']:
    if i['x_studio_opnemen_in_rapport'] == 1 and i['x_studio_audit_check']['x_studio_audit_groep']['x_name'] == 'Cloud':
      html += "<h4 style='text-align: center;'>" + str(i['x_studio_audit_check']['x_name']) + "</h4>"
  html += "</div>"

# Tabel 5
  html += "<div style='float: left; width: 33.33%; box-sizing: border-box;'>"
  html += "<img src='https://odoo.serso.be/web/image/107912?filename=network.png&unique=0f1be10748f2146f270257dc6aa7c6b88e260932' style='width: 100%;'>"
  for i in OB['x_studio_one2many_field_933_1hjukhcev']:
    if i['x_studio_opnemen_in_rapport'] == 1 and i['x_studio_audit_check']['x_studio_audit_groep']['x_name'] == 'Network':
      html += "<h4 style='text-align: center;'>" + str(i['x_studio_audit_check']['x_name']) + "</h4>"
  html += "</div>"

# Tabel 6
  html += "<div style='float: left; width: 33.33%; box-sizing: border-box;'>"
  html += "<img src='https://odoo.serso.be/web/image/107909?filename=infrastructure.png&unique=2ccd65f9e765af0ca719d5e8f99d4f4f342424cb' style='width: 100%;'>"
  for i in OB['x_studio_one2many_field_933_1hjukhcev']:
    if i['x_studio_opnemen_in_rapport'] == 1 and i['x_studio_audit_check']['x_studio_audit_groep']['x_name'] == 'Infrastructure':
      html += "<h4 style='text-align: center;'>" + str(i['x_studio_audit_check']['x_name']) + "</h4>"
  html += "</div>"

  html += "<div style='page-break-before: always; page-break-after: always;'>"
  html += "</div>"

# Sluit de tabelrij
  html += "<h1>Ons Advies</h1>"
  html += "<div>Ons advies is om de volgende oplossingen spoedig en doordacht aan te pakken, om op die manier een verbeterd beveiligingsniveau te bereiken en de algehele cyberweerbaarheid van het systeem te versterken.</div><br>"
  html += "<div>Om een robuuste en uitgebreide beveiligingsinfrastructuur te waarborgen, adviseren wij het implementeren en actief beheren van een geïntegreerd beveiligingsprogramma. Dit omvat onder meer het invoeren van Multi-Factor Authenticatie (MFA) voor verbeterde toegangscontrole, het regelmatig uitvoeren van penetratietests en het versterken van Active Directory-beveiliging, zoals het beheren van lokale beheerderswachtwoorden met behulp van LAPS.</div><br>"
  html += "<div>Voor de bescherming van gevoelige gegevens en naleving van privacyvereisten, is het essentieel om BitLocker-versleuteling op Windows-systemen te implementeren. Het periodiek uitvoeren van back-ups met betrouwbare oplossingen en het gebruik van geavanceerde antivirussoftware met Endpoint Detection and Response (EDR) en Patch Management draagt bij aan een proactieve beveiligingsbenadering.</div><br>"
  html += "<div>Bovendien is het cruciaal om een sterke gebruikersbewustzijnsprogramma te implementeren, waarbij werknemers getraind worden over cybersecurity en bewust gemaakt worden van potentiële bedreigingen. Het regelmatig evalueren en aanpassen van beveiligingsmaatregelen, gecombineerd met proactieve monitoring en het implementeren van webfiltering en antispam-oplossingen, draagt bij aan een algehele veerkrachtige beveiligingshouding.</div><br>"
  html += "<div>Het gebruik van Honeypots voor het detecteren van aanvallen en regelmatige beveiligingsbeoordelingen dragen verder bij aan een effectieve beveiligingsstrategie. Tot slot adviseren wij om incidentresponsplannen te herzien en te testen, zodat organisaties snel en doeltreffend kunnen handelen bij onvoorziene gebeurtenissen. Door deze maatregelen geïntegreerd toe te passen, kunnen organisaties een hoog beveiligingsniveau handhaven en zich beter beschermen tegen steeds geavanceerdere cyberbedreigingen.</div><br>"
  html += "<div style='float: left; width: 100%; box-sizing: border-box;'>"
  html += "<hr>" 
  html += str(AC['x_studio_slot'])
  OB['x_studio_rapport'] = html
  html += "</div>"