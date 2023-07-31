import serial

def enviar_comando_hexadecimal(comando_hex, port, baudrates):
    respostas = {}
    for baudrate in baudrates:
        try:
            with serial.Serial(port, baudrate=baudrate, timeout=1) as ser:
                comando_bytes = bytes.fromhex(comando_hex)
                ser.write(comando_bytes)
                resposta_bytes = ser.read(10)
                resposta_hex = resposta_bytes.hex().upper()
                respostas[baudrate] = resposta_hex
        except serial.SerialException:
            respostas[baudrate] = None
            continue

    return respostas

if __name__ == "__main__":
    comando = "024745544C4F47C203"
    porta = "COM7"
    baudrates = [300, 1200, 2400, 4800, 9600, 14400, 19200, 38400, 57600, 115200]

    respostas_por_baud = enviar_comando_hexadecimal(comando, porta, baudrates)

    for baudrate, resposta in respostas_por_baud.items():
        if resposta is not None:
            print(f"Resposta em {baudrate} bps: {resposta}")
        else:
            print(f"Sem resposta em {baudrate} bps.")