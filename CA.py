import xml.etree.ElementTree as ET
from xml.dom import minidom


name = input('Введите полный нейм БС:')
MRBTS = int(input('Введите MRBTS БС:'))
Cells1800 = input('Введите перечень Сот 1800 (через запятую):')
Cells2600 = input('Введите перечень Сот 2600 (через запятую):')
Cells900 = input('Введите перечень Сот 900 (через запятую):')


if len(Cells1800) > 0:
    Cells1800 = tuple(int(x) for x in Cells1800.split(","))
if len(Cells2600) > 0:
    Cells2600 = tuple(int(x) for x in Cells2600.split(","))
if len(Cells900) > 0:
    Cells900 = tuple(int(x) for x in Cells900.split(","))


CAREL = {'class': "CAREL"}

strDistName1 = f'PLMN-PLMN/MRBTS-{MRBTS}LNBTS-{MRBTS}LNCEL-{Cells1800}/CAREL-1'
strDistName2 = f'PLMN-PLMN/MRBTS-{MRBTS}LNBTS-{MRBTS}LNCEL-{Cells2600}/CAREL-1'


def main():
    new = ET.Element('raml', version='2.0', xmlns='raml20.xsd')
    cm_data = ET.SubElement(new, 'cmData', xmlns="", type='plan', scope='changes', name=name)
    header = ET.SubElement(cm_data, 'header')
    log = ET.SubElement(header, 'log', dateTime='29.09.2021', action="created", appInfo="PlanExporter")
    log.text = 'InternalValues are used'
    x = 0           # LTE 1800
    x1 = 0          # LTE 2600
    x2 = 0          # LTE 900
    n_carel = 1

    # 1800 <> 2600

    if len(Cells1800) > 0 and len(Cells2600) > 0:
        while x < len(Cells1800):
            while x1 < len(Cells2600):

                scell_prio = '2'
                if int(Cells2600[x1]) - int(Cells1800[x]) == 40:
                    scell_prio = '1'

                managed_object = ET.SubElement(cm_data, 'managedObject', CAREL, version="xL20B_2003_002", distName=
                                               f'PLMN-PLMN/MRBTS-{MRBTS}/LNBTS-{MRBTS}/LNCEL-{Cells1800[x]}'
                                               f'/CAREL-{n_carel}', operation="create")
                defaults = ET.SubElement(managed_object, 'defaults', name="System")
                p1 = ET.SubElement(managed_object, 'p', name="lcrId")
                p1.text = str(Cells2600[x1])
                p1 = ET.SubElement(managed_object, 'p', name="lnBtsId")
                p1.text = str(MRBTS)
                p1 = ET.SubElement(managed_object, 'p', name="maxNumOfSuppMimoLayer")
                p1.text = '2'
                p1 = ET.SubElement(managed_object, 'p', name="pcellSwapAllowed")
                p1.text = '1'
                p1 = ET.SubElement(managed_object, 'p', name="scellPrio")
                p1.text = scell_prio
                x1 += 1
                n_carel += 1
            n_carel = 1
            x1 = 0
            x += 1
        x = 0
        x1 = 0

        while x < len(Cells2600):
            while x1 < len(Cells1800):

                scell_prio = '2'
                if int(Cells2600[x1]) - int(Cells1800[x]) == 40:
                    scell_prio = '1'

                managed_object = ET.SubElement(cm_data, 'managedObject', CAREL, version="xL20B_2003_002", distName=
                                               f'PLMN-PLMN/MRBTS-{MRBTS}/LNBTS-{MRBTS}/LNCEL-{Cells2600[x]}'
                                               f'/CAREL-{n_carel}', ooperation="create")
                defaults = ET.SubElement(managed_object, 'defaults', name="System")
                p1 = ET.SubElement(managed_object, 'p', name="lcrId")
                p1.text = str(Cells1800[x1])
                p1 = ET.SubElement(managed_object, 'p', name="lnBtsId")
                p1.text = str(MRBTS)
                p1 = ET.SubElement(managed_object, 'p', name="maxNumOfSuppMimoLayer")
                p1.text = '2'
                p1 = ET.SubElement(managed_object, 'p', name="pcellSwapAllowed")
                p1.text = '1'
                p1 = ET.SubElement(managed_object, 'p', name="scellPrio")
                p1.text = scell_prio
                x1 += 1
                n_carel += 1
            n_carel = 1
            x1 = 0
            x += 1

    # LTE 900 <> 1800

    if len(Cells900) > 0 and len(Cells1800) > 0:

        x = 0   # LTE 1800 обнуление счётчика
        x1 = 0  # LTE 2600 обнуление счётчика
        x2 = 0  # LTE 900 обнуление счётчика
        n_carel = 1

        while x2 < len(Cells900):
            while x < len(Cells1800):

                scell_prio = '2'
                if int(Cells900[x2]) - int(Cells1800[x]) == 50:
                    scell_prio = '1'

                managed_object = ET.SubElement(cm_data, 'managedObject', CAREL, version="xL20B_2003_002", distName=
                                               f'PLMN-PLMN/MRBTS-{MRBTS}/LNBTS-{MRBTS}/LNCEL-{Cells900[x2]}/CAREL-'
                                               f'{n_carel}', operation="create")
                defaults = ET.SubElement(managed_object, 'defaults', name="System")
                p1 = ET.SubElement(managed_object, 'p', name="lcrId")
                p1.text = str(Cells1800[x])
                p1 = ET.SubElement(managed_object, 'p', name="lnBtsId")
                p1.text = str(MRBTS)
                p1 = ET.SubElement(managed_object, 'p', name="maxNumOfSuppMimoLayer")
                p1.text = '2'
                p1 = ET.SubElement(managed_object, 'p', name="pcellSwapAllowed")
                p1.text = '1'
                p1 = ET.SubElement(managed_object, 'p', name="scellPrio")
                p1.text = scell_prio
                x += 1
                n_carel += 1
            n_carel = 1
            x = 0
            x2 += 1

        x = 0
        x2 = 0

        while x < len(Cells1800):
            while x2 < len(Cells900):

                scell_prio = '2'
                if int(Cells900[x2]) - int(Cells1800[x]) == 50:
                    scell_prio = '1'

                managed_object = ET.SubElement(cm_data, 'managedObject', CAREL, version="xL20B_2003_002", distName=
                                               f'PLMN-PLMN/MRBTS-{MRBTS}/LNBTS-{MRBTS}/LNCEL-{Cells1800[x]}/CAREL-'
                                               f'{n_carel}', operation="create")
                defaults = ET.SubElement(managed_object, 'defaults', name="System")
                p1 = ET.SubElement(managed_object, 'p', name="lcrId")
                p1.text = str(Cells900[x2])
                p1 = ET.SubElement(managed_object, 'p', name="lnBtsId")
                p1.text = str(MRBTS)
                p1 = ET.SubElement(managed_object, 'p', name="maxNumOfSuppMimoLayer")
                p1.text = '2'
                p1 = ET.SubElement(managed_object, 'p', name="pcellSwapAllowed")
                p1.text = '1'
                p1 = ET.SubElement(managed_object, 'p', name="scellPrio")
                p1.text = scell_prio
                x2 += 1
                n_carel += 1
            n_carel = 1
            x2 = 0
            x += 1

    managed_object = ET.SubElement(cm_data, 'managedObject', version="xL20B_2003_002", distName=f'PLMN-PLMN/MRBTS-'
                                   f'{MRBTS}/LNBTS-{MRBTS}/CADPR-0', id="41429697", operation="create")
    defaults = ET.SubElement(managed_object, 'defaults', name="System")
    p1 = ET.SubElement(managed_object, 'p', name='a3Offset')
    p1.text = '-3'
    p1 = ET.SubElement(managed_object, 'p', name='a3TimeToTrigger')
    p1.text = '320'
    p1 = ET.SubElement(managed_object, 'p', name='a3TriggerQuantity')
    p1.text = '0'
    p1 = ET.SubElement(managed_object, 'p', name='a6Offset')
    p1.text = '3'
    p1 = ET.SubElement(managed_object, 'p', name='a6ReportInterval')
    p1.text = '640'
    p1 = ET.SubElement(managed_object, 'p', name='a6TimeToTrigger')
    p1.text = '8'
    p1 = ET.SubElement(managed_object, 'p', name='enableA3Event')
    p1.text = '1'
    p1 = ET.SubElement(managed_object, 'p', name='enableA6Event')
    p1.text = '1'
    p1 = ET.SubElement(managed_object, 'p', name='enableFreqPrioSwap')
    p1.text = '0'
    p1 = ET.SubElement(managed_object, 'p', name='hysA3Offset')
    p1.text = '2'
    p1 = ET.SubElement(managed_object, 'p', name='hysA6Offset')
    p1.text = '0'
    p1 = ET.SubElement(managed_object, 'p', name='maxNumMimoLayerFdd')
    p1.text = '10'
    p1 = ET.SubElement(managed_object, 'p', name='maxNumMimoLayerTdd')
    p1.text = '10'
    p1 = ET.SubElement(managed_object, 'p', name='maxNumScellSwaps')
    p1.text = '0'
    p1 = ET.SubElement(managed_object, 'p', name='sFreqPrio')
    p1.text = '1'
    p1 = ET.SubElement(managed_object, 'p', name='scellMeasThreshRsrp')
    p1.text = '-110'
    p1 = ET.SubElement(managed_object, 'p', name='scellMeasThreshRsrq')
    p1.text = '-120'
    p1 = ET.SubElement(managed_object, 'p', name='scellPdcchOlLa')
    p1.text = '2'

    save_xml('test.xml', new)


def save_xml(NSNTEST, xml_code):
    xml_string = ET.tostring(xml_code).decode(errors='ignore')  # до этого было просто .decode()

    xml_prettyxml = minidom.parseString(xml_string).toprettyxml()

    xmlname1 = 'C://Python/Carrier Aggregation NSN/CA_'
    xmlname2 = name
    xmlname3 = '.xml'
    fullnamexml = xmlname1+xmlname2+xmlname3

    with open(fullnamexml, 'w') as xml_file:
        xml_file.write(xml_prettyxml)


if __name__ == '__main__':
    main()
