async function realizarTeste(disp) {

    const response = await axios.get('http://localhost:8000/teste');

    const devices = response.data;

    const device = document.getElementById(`d${disp + 1}`);

    const listTeste = ["GERTEC", "SEFAZ", "LINUX", "SUPER HASH", "LED ON", "LED OFF", "TOKEN", "NVRAM", "USB", "MSP"];

    const list = device.querySelector('ul');

    let i = 0;

    let li = ""

    Object.values(devices[disp]).forEach((entry) => {

        const key = listTeste[i];

        const val = entry;

        const listItem = document.createElement('li');

        const isBool = typeof val === 'boolean' ? true : false;

        if (isBool) {

            if (val === true) {
                
                li +=`<li><img src="assets/positivo.png"> ${key}</li>`

            } else {

                li += `<li><img src="assets/negativo.png"> ${key}</li>`

            }

        } else {

            li += `<li>${key}: ${val.toString()}</li>`;

        }

        i++;

    });

    li += '<br>';

    li += '<li><button type="button" style="background-color : red" onclick="location.reload()">Cancelar</button><button>Salvar</button></li>';

    list.innerHTML = li;

}