
def parseEngineFile(filepath):
    headerpassed = False

    data = {
        'motor name':None,
        'motor diameter':None,
        'motor length':None,
        'motor delay': None,
        'propellant weight': None,
        'total weight': None,
        'manufacturer': None,
        'thrust data': {'time':[],'thrust':[]}
    }

    with open(filepath) as enginefile:
        while True:
            line = enginefile.readline()
            if not line:
                break
            if ~headerpassed:
                if line[0].isalpha():
                    headerpassed = True
                    name, diam, length, delay, prop_weight, total_weight, manufacturer = parseHeader(line)
                    data['motor name'] = name
                    data['motor diameter'] = diam
                    data['motor length'] = length
                    data['motor delay'] = delay
                    data['propellant weight'] = prop_weight
                    data['total weight'] = total_weight
                    data['manufacturer'] = manufacturer

            else:
                line = enginefile.readline()
                time, thrust = parseDataLine(line)
                data['thrust data']['time'].append(time)
                data['thrust data']['thrust'].append(thrust)
    enginefile.close()
    return data

def parseDataLine(line):
    # first float is the time
    # second is the thrust (N)
    contents = line.split()
    time = float(contents[0])
    thrust = float(contents[1])
    return time, thrust

def parseHeader(header):
    # the content of the header is as follows:
    # 1. Motor Name
    # 2. Motor Diameter
    # 3. Motor Length
    # 4. Motor Delay
    # 5. Propellant Weight
    # 6. Total Weight
    # 7. Manufacturer

    # parse by spaces
    headercontents = header.split()
    motor_name = headercontents[0]
    motor_diameter = headercontents[1]
    motor_length = headercontents[2]
    motor_delay = headercontents[3]
    propellant_weight = headercontents[4]
    total_weight = headercontents[5]
    manufacturer = headercontents[6]

    return motor_name, motor_diameter, motor_length, motor_delay, propellant_weight, total_weight, manufacturer


if __name__ == '__main__':
    from os import path # for relative path import
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "resources", "Cesaroni_9955M1450-P.eng"))
    print(parseEngineFile(filepath))
